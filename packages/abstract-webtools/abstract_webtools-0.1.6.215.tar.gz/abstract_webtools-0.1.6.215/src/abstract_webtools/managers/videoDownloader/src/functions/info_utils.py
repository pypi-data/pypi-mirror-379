from ..imports import *
from .utils import *
from .utils import _get_video_info
import os, json, time, hashlib, subprocess, unicodedata, re, threading
from datetime import datetime
from abstract_utilities import safe_dump_to_file  # assumes exists

_LOCK = threading.RLock()
def _ensure_standard_paths(info: dict, registry_dir: str,download_directory) -> dict:
    """
    Given a video info dict, populate standard paths for consistency.
    Does not check existence — just defines where things *will* live.
    """
    vid = info.get("video_id") or info.get("id")
    if not vid:
        return info

    dirbase = os.path.join(download_directory, vid)
    os.makedirs(dirbase, exist_ok=True)

    # Always enforce these
    standard = {
        "file_path": info.get("file_path") or os.path.join(dirbase, "video.mp4"),
        "info_path": info.get("info_path") or os.path.join(dirbase, "info.json"),
        "audio_path": os.path.join(dirbase, "audio.wav"),
        "whisper_path": os.path.join(dirbase, "whisper.json"),
        "srt_path": os.path.join(dirbase, "captions.srt"),
        "metadata_path": os.path.join(dirbase, "metadata.json"),
        "thumbnails_dir": os.path.join(dirbase, "thumbnails"),
        "thumbnails_path": os.path.join(dirbase, "thumbnails.json")
    }
    os.makedirs(standard["thumbnails_dir"], exist_ok=True)

    info.update(standard)
    return info
def _sha12(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]

def _atomic_write(path: str, data: dict):
    tmp = f"{path}.tmp"
    safe_dump_to_file(data, tmp)
    os.replace(tmp, path)

def _normalize_ascii(s: str) -> str:
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')

def generate_video_id(path_or_title: str, max_length: int = 50) -> str:
    base = os.path.splitext(os.path.basename(path_or_title))[0]
    if base == 'video':
        base = os.path.basename(os.path.dirname(path_or_title)) or base
    base = _normalize_ascii(base.lower())
    base = re.sub(r'[^a-z0-9]+', '-', base).strip('-')
    base = re.sub(r'-{2,}', '-', base)
    if len(base) > max_length:
        h = _sha12(base)
        base = f"{base[:max_length - len(h) - 1].rstrip('-')}-{h}"
    return base or _sha12(path_or_title)

def make_video_info(filepath: str) -> dict:
    import json as _json
    import subprocess as _sub
    cmd = [
        "ffprobe","-v","quiet","-print_format","json",
        "-show_format","-show_streams", filepath
    ]
    probe = _sub.check_output(cmd)
    data = _json.loads(probe)
    info = {
        "id": generate_video_id(filepath),
        "title": os.path.splitext(os.path.basename(filepath))[0],
        "upload_date": datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y%m%d"),
        "duration": float(data["format"].get("duration", 0.0)),
        "streams": data.get("streams", []),
        "format": data.get("format", {}),
        "file_path": os.path.abspath(filepath),
    }
    return info

def _yt_dlp_info(url: str, ydl_opts: dict | None = None) -> dict | None:
    from yt_dlp import YoutubeDL
    opts = {'quiet': True, 'skip_download': True}
    if ydl_opts:
        opts.update(ydl_opts)
    try:
        with YoutubeDL(opts) as ydl:
            return ydl.extract_info(url, download=False)
    except Exception:
        return None

def get_info_directory(directory=None, envPath=None):
    # replace with your own util if you have it already
    d = directory or os.path.expanduser("~/.video_info_cache")
    os.makedirs(d, exist_ok=True)
    return d

class infoRegistry(metaclass=SingletonMeta):
    """Thread-safe registry with consistent paths for each video."""

    def __init__(self, video_directory=None, envPath=None, info_directory=None,
                 temp_directory=None, data_directory=None,download_directory=None, **kwargs):
        if not hasattr(self, 'initialized',):
            self.initialized = True
            self.infoRegistryDirectory = get_info_directory(directory=info_directory, envPath=envPath)
            self.registry_path = os.path.join(self.infoRegistryDirectory, "registry.json")
            self.download_directory = get_download_directory(download_directory)
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

    def _get_cache_path(self, video_id: str) -> str:
        return os.path.join(self.infoRegistryDirectory, f"{video_id}.json")

    def _read_cached_info(self, video_id: str) -> dict | None:
        cache = self._get_cache_path(video_id)
        if os.path.isfile(cache):
            try:
                with open(cache, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def _write_cached_info(self, video_id: str, info: dict) -> str:
        cache = self._get_cache_path(video_id)
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
            return _ensure_standard_paths(info, self.infoRegistryDirectory,self.download_directory)

        if not url and not video_id:
            raise ValueError("Either url or video_id or video_path must be provided")

        vid = self._resolve_video_id(url, video_path, video_id)

        if vid and not force_refresh:
            cached = self._read_cached_info(vid)
            if cached:
                self._link(vid, url, cached.get("file_path"))
                cached["info_path"] = self._get_cache_path(vid)
                cached["video_id"] = vid
                return _ensure_standard_paths(cached, self.infoRegistryDirectory,self.download_directory)

        if url:
            info = _yt_dlp_info(url)
            if info:
                vid = info.get("id") or _sha12(url)
                cache = self._write_cached_info(vid, info)
                self._link(vid, url, None)
                info["info_path"] = cache
                info["video_id"] = vid
                return _ensure_standard_paths(info, self.infoRegistryDirectory,self.download_directory)

        return None

    def edit_info(self, data: dict, url: str | None = None, video_id: str | None = None, video_path: str | None = None):
        cur = self.get_video_info(url=url, video_id=video_id, video_path=video_path, force_refresh=False)
        if not cur:
            raise RuntimeError("No existing info to edit")
        cur.update(data or {})
        vid = cur.get("video_id") or video_id or (url and _sha12(url)) or generate_video_id(video_path or "video")
        cur = _ensure_standard_paths(cur, self.infoRegistryDirectory, self.download_directory)  # ✅ fixed
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
