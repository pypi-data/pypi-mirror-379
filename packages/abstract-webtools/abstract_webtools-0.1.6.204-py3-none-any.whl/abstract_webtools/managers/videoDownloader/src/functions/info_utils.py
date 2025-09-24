from ..imports import *
from .utils import *
class infoRegistry(metaclass=SingletonMeta):
    """Singleton for managing video + info registry directories."""

    def __init__(self, video_directory=None, envPath=None, info_directory=None,temp_directory=None,data_directory=None,**kwargs):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.videoDirectory = get_video_directory(video_directory=video_directory, envPath=envPath)
            self.infoRegistryDirectory = get_info_directory(directory=info_directory, envPath=envPath)
            self.tempDirectory = get_info_directory(directory=temp_directory, envPath=envPath)
            self.dataDirectory = get_info_directory(directory=data_directory, envPath=envPath)
            self.registry_path = os.path.join(self.infoRegistryDirectory, "registry.json")
            self._load_registry()

    def _load_registry(self):
        registry = {"by_url": {}, "by_id": {},"by_path": {}}
        if os.path.isfile(self.registry_path):
            with open(self.registry_path, "r", encoding="utf-8") as f:
                self.registry = registry
                json_data = json.load(f)
                self.registry.update(json_data)
                self.registry["by_path"] = json_data.get('video_path') or json_data.get('file_path',{})
        else:
            self.registry = registry

    def _save_registry(self):
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(self.registry, f, indent=2)

    def _get_cache_path(self, video_id=None,url=None,video_path=None):
        video_id = self._get_video_id(url=url,video_id=video_id,video_path=video_path)
        return os.path.join(self.infoRegistryDirectory, f"{video_id}.json")

    def _get_video_id(self,url=None,video_id=None,video_path=None):
        if video_path and not video_id:
            video_id = self.registry["by_path"].get(video_path)
        if url and not video_id:
            video_id = self.registry["by_url"].get(url)
        return video_id
    def _fetch_get_id(self,url=None,filepath=None):
        
        cache_path = self._get_cache_path(url=url,filepath=filepath)
        if cache_path and not os.path.isfile(cache_path):
            if filepath and os.path.isfile(filepath):
                info = make_video_info(filepath)
            else:
                ydl_opts = {"quiet": True, "skip_download": True}
                info = _get_video_info(url,ydl_opts=ydl_opts)
                video_id = info.get("id") or hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
            cache_path = self._get_cache_path(video_id)
        safe_dump_to_file(data=info,file_path=cache_path)
        return video_id,cache_path
    def _save_to_info_path(self,data,url=None,video_id=None, video_path=None):
        if video_path and os.path.isfile(video_path):
            if not video_id and not video_path:
                video_id = data.get("id")
            if not video_id and video_path:
                video_id = data.get("id") or hashlib.sha1(video_path.encode("utf-8")).hexdigest()[:12]
        if url:
            if not video_id and not url:
                video_id = data.get("id")
            if not video_id and url:
                video_id = data.get("id") or hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
        if video_id:
            cache_path = self._get_cache_path(video_id=video_id,video_path=video_path)
            if data.get('info_path') == None:
                data['info_path'] = cache_path
            if data.get('info_dir') == None:
                data['info_dir'] = os.path.dirname(cache_path)
            safe_dump_to_file(data=data,file_path=cache_path)
            return video_id,cache_path
    def _get_cached_info(self,url=None,video_id=None):
        cache_path = self._get_cache_path(url=url,video_id=video_id)
        if os.path.isfile(cache_path):
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
    def _add_url_top_registry(self, url=None, video_id=None, video_path=None):
        """
        Ensure the registry always links url, id, and video_path together.
        Merges into existing entry if one already exists.
        """
        # Resolve or assign video_id
        if url:
            video_id = video_id or self._get_video_id(url=url,video_path=video_path)
            self.registry["by_url"][url] = video_id

        if video_path and os.path.isfile(video_path):
            video_id = video_id or generate_video_id(video_path)
            self.registry["by_path"][video_path] = video_id

        # Merge with existing record if available
        existing = self.registry["by_id"].get(video_id, {})
        existing.update({
            "url": url or existing.get("url"),
            "timestamp": time.time(),
            "video_path": video_path or existing.get("video_path"),
        })
        self.registry["by_id"][video_id] = existing

        self._save_registry()
        return video_id
    def get_video_info(self, url=None, video_id=None, force_refresh=False,
                       download=False, video_path=None):
        """
        Fetch video info either from a local file (video_path) or via URL.
        Keeps registry synced with url, id, and path.
        """
        # Case 1: File-based info
        if video_path and os.path.isfile(video_path):
            video_id = video_id or generate_video_id(video_path)
            info = make_video_info(video_path)
            self._save_to_info_path(info, url=url, video_id=video_id)
            self._add_url_top_registry(url=url, video_id=video_id, video_path=video_path)
            return info

        # Case 2: URL-based info
        url = get_corrected_url(url=url)
        video_id = video_id or self._get_video_id(url=url, video_path=video_path)

        # Look up cached
        if video_id:
            cache_path = self._get_cache_path(video_id)
            if os.path.isfile(cache_path) and not force_refresh:
                info = self._get_cached_info(url=url, video_id=video_id)
                self._add_url_top_registry(url=url, video_id=video_id, video_path=video_path)
                return info

        # Otherwise, fetch fresh from yt_dlp
        video_id, cache_path = self._fetch_get_id(url=url)
        self._add_url_top_registry(url=url, video_id=video_id, video_path=video_path)
        return self._get_cached_info(url=url, video_id=video_id)

                        



        return self._get_cached_info(url=url,video_id=video_id)
    def edit_info(self,data,url=None,video_id=None, force_refresh=False,download=False):
        video_info = self.get_video_info(url=url, video_id=video_id, force_refresh=force_refresh,download=download)
        video_info.update(data)
        self._save_to_info_path(data=video_info,url=url,video_id=video_id)
        return video_info
    def list_cached_videos(self):
        """Return all cached entries (url, id, metadata)."""
        results = []
        for vid, meta in self.registry["by_id"].items():
            results.append({"video_id": vid, "url": meta["url"], "timestamp": meta["timestamp"]})
        return results
