from ..imports import *
from .video_paths import *
from .video_utils import *
from .video_utils import _LOCK,_get_video_info,ensure_standard_paths,_sha12,_atomic_write,_yt_dlp_info

class infoRegistry(metaclass=SingletonMeta):
    """Thread-safe registry with all video assets stored under ~/videos/<video_id>/."""

    def __init__(self, video_root=None, **kwargs):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.video_root = get_video_root(video_root)
            self.registry_path = os.path.join(self.video_root, "registry.json")
            self._load_registry()

    def _load_registry(self):
        with _LOCK:
            self.registry = {"by_url": {}, "by_id": {}, "by_path": {}}
            if os.path.isfile(self.registry_path):
                try:
                    with open(self.registry_path, "r", encoding="utf-8") as f:
                        j = json.load(f)
                    self.registry["by_url"].update(j.get("by_url", {}))
                    self.registry["by_id"].update(j.get("by_id", {}))
                    self.registry["by_path"].update(j.get("by_path", {}))
                except Exception:
                    pass

    def _save_registry(self):
        with _LOCK:
            _atomic_write(self.registry_path, self.registry)

    def _read_cached_info(self, video_id: str) -> dict | None:
        cache = os.path.join(self.video_root, video_id, "info.json")
        if os.path.isfile(cache):
            try:
                with open(cache, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def _write_cached_info(self, video_id: str, info: dict) -> str:
        dirbase = os.path.join(self.video_root, video_id)
        os.makedirs(dirbase, exist_ok=True)
        cache = os.path.join(dirbase, "info.json")
        _atomic_write(cache, info)
        return cache

    def _resolve_video_id(self, url: str | None, video_path: str | None, hint_id: str | None) -> str | None:
        if hint_id:
            return hint_id
        if video_path and video_path in self.registry["by_path"]:
            return self.registry["by_path"][video_path]
        if url and url in self.registry["by_url"]:
            return self.registry["by_url"][url]
        return None

    def _link(self, video_id: str, url: str | None, video_path: str | None):
        with _LOCK:
            if url:
                self.registry["by_url"][url] = video_id
            if video_path:
                self.registry["by_path"][video_path] = video_id
            rec = self.registry["by_id"].get(video_id, {})
            if url:
                rec["url"] = url
            if video_path:
                rec["video_path"] = video_path
            rec["timestamp"] = time.time()
            self.registry["by_id"][video_id] = rec
            self._save_registry()

    def get_video_info(self, url: str | None = None, video_id: str | None = None,
                       force_refresh: bool = False, download: bool = False,
                       video_path: str | None = None) -> dict | None:
        if video_path and os.path.isfile(video_path):
            vid = video_id or generate_video_id(video_path)
            info = make_video_info(video_path)
            cache = self._write_cached_info(vid, info)
            self._link(vid, url, os.path.abspath(video_path))
            info["info_path"] = cache
            info["video_id"] = vid
            return ensure_standard_paths(info, self.video_root)

        if not url and not video_id:
            raise ValueError("Either url or video_id or video_path must be provided")

        vid = self._resolve_video_id(url, video_path, video_id)

        if vid and not force_refresh:
            cached = self._read_cached_info(vid)
            if cached:
                self._link(vid, url, cached.get("file_path"))
                cached["info_path"] = os.path.join(self.video_root, vid, "info.json")
                cached["video_id"] = vid
                return ensure_standard_paths(cached, self.video_root)

        if url:
            info = _yt_dlp_info(url)
            if info:
                vid = info.get("id") or _sha12(url)
                cache = self._write_cached_info(vid, info)
                self._link(vid, url, None)
                info["info_path"] = cache
                info["video_id"] = vid
                return ensure_standard_paths(info, self.video_root)

        return None

    def edit_info(self, data: dict, url: str | None = None,
                  video_id: str | None = None, video_path: str | None = None):
        cur = self.get_video_info(url=url, video_id=video_id, video_path=video_path, force_refresh=False)
        if not cur:
            raise RuntimeError("No existing info to edit")
        cur.update(data or {})
        vid = cur.get("video_id") or video_id or (url and _sha12(url)) or generate_video_id(video_path or "video")
        cur = ensure_standard_paths(cur, self.video_root)
        cache = self._write_cached_info(vid, cur)
        self._link(vid, url, cur.get("file_path") or video_path)
        cur["info_path"] = cache
        cur["video_id"] = vid
        return cur

    def list_cached_videos(self):
        with _LOCK:
            out = []
            for vid, meta in self.registry["by_id"].items():
                out.append({
                    "video_id": vid,
                    "url": meta.get("url"),
                    "video_path": meta.get("video_path"),
                    "timestamp": meta.get("timestamp"),
                })
            return out
