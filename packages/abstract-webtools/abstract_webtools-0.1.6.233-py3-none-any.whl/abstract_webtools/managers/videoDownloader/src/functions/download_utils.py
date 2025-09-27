from ..imports import *
from .image_utils import *

def get_corrected_url(url):
    try:
        url_mgr = urlManager(url=url)
        return url_mgr.url
    except Exception as e:
        logger.info(f"{e}")
    return url
class VideoDownloader:
    def __init__(self, url, download_directory=None, user_agent=None,
                 video_extention="mp4", download_video=True,
                 output_filename=None, ydl_opts=None,
                 registry=None, force_refresh=False):

        self.url = get_corrected_url(url=url)
        self.video_urls = self.url if isinstance(self.url, list) else [self.url]

        self.registry = registry or infoRegistry()
        self.ydl_opts = ydl_opts or {}
        self.get_download = download_video
        self.user_agent = user_agent
        self.video_extention = video_extention
        self.download_directory = get_video_root(download_directory)
        self.output_filename = output_filename
        self.force_refresh = force_refresh

        self.monitoring = True
        self.pause_event = threading.Event()

        # Start immediately
        self._start()

    # ---------- threading ----------
    def _start(self):
        self.download_thread = threading.Thread(
            target=self._download_entrypoint, name="video-download", daemon=True
        )
        self.monitor_thread = threading.Thread(
            target=self._monitor, name="video-monitor", daemon=True
        )

        self.download_thread.start()
        self.monitor_thread.start()
        self.download_thread.join()

    def stop(self):
        self.monitoring = False
        self.pause_event.set()

    # ---------- monitor ----------
    def _monitor(self, interval=30, max_minutes=15):
        start = time.time()
        while self.monitoring:
            logger.info("Monitoring...")
            if time.time() - start > max_minutes * 60:
                logger.info("Monitor: timeout reached, stopping.")
                break
            self.pause_event.wait(interval)
        logger.info("Monitor: exited.")

    # ---------- yt-dlp options ----------
    def _build_ydl_opts(self, outtmpl, extractor_client=None, force_itag18=False):
        fmt = "bestvideo+bestaudio/best"
        if self.video_extention and self.video_extention != "mp4":
            fmt = f"bestvideo[ext={self.video_extention}]+bestaudio[ext=m4a]/best[ext={self.video_extention}]"
        if force_itag18:
            fmt = "18"

        opts = {
            "quiet": True,
            "noprogress": True,
            "external_downloader": "ffmpeg",
            "outtmpl": outtmpl,
            "format": fmt,
            "merge_output_format": "mp4",
            "concurrent_fragment_downloads": 3,
            "ratelimit": 0,
            "retries": 5,
            "fragment_retries": 5,
            "ignoreerrors": False,
        }

        if extractor_client:
            opts.setdefault("extractor_args", {})
            opts["extractor_args"].setdefault("youtube", {})
            opts["extractor_args"]["youtube"]["player_client"] = [extractor_client]

        if self.user_agent:
            opts["http_headers"] = {"User-Agent": self.user_agent}

        # allow shallow override
        for k, v in self.ydl_opts.items():
            if k == "extractor_args":
                base = opts.setdefault("extractor_args", {})
                for ek, ev in v.items():
                    if isinstance(ev, dict) and isinstance(base.get(ek), dict):
                        base[ek].update(ev)
                    else:
                        base[ek] = ev
            else:
                opts[k] = v

        return opts

    # ---------- entrypoint ----------
    def _download_entrypoint(self):
        try:
            for url in self.video_urls:
                self._download_single(url)
        finally:
            self.stop()

    # ---------- main logic ----------
    def _download_single(self, video_url: str):
        logger.info(f"[VideoDownloader] Processing: {video_url}")

        # 1. Check registry
        info = self.registry.get_video_info(url=video_url, force_refresh=self.force_refresh)
        if info and info.get("video_path") and os.path.isfile(info["video_path"]):
            logger.info(f"[VideoDownloader] Already cached: {info['video_path']}")
            return info

        try:
            # 2. Download fresh
            outtmpl = os.path.join(self.download_directory, "%(id)s.%(ext)s")
            with yt_dlp.YoutubeDL(self._build_ydl_opts(outtmpl)) as ydl:
                raw_info = ydl.extract_info(video_url, download=self.get_download)

            # 3. Assign video_id + folder
            video_id = raw_info.get("id") or generate_video_id(raw_info.get("title") or "video")
            dirbase = os.path.join(self.download_directory, video_id)
            os.makedirs(dirbase, exist_ok=True)

            temp_path = ydl.prepare_filename(raw_info)
            _, ext = os.path.splitext(temp_path)
            final_path = os.path.join(dirbase, f"video{ext or '.mp4'}")
            if temp_path != final_path and os.path.isfile(temp_path):
                shutil.move(temp_path, final_path)

            # 4. Save minimal JSON-safe info through registry
            minimal_info = {
                "id": raw_info.get("id"),
                "title": raw_info.get("title"),
                "ext": raw_info.get("ext", "mp4"),
                "duration": raw_info.get("duration"),
                "upload_date": raw_info.get("upload_date"),
                "video_id": video_id,
                "video_path": final_path,
                "file_path": final_path,
            }
            self.registry.edit_info(minimal_info, url=video_url, video_id=video_id, video_path=final_path)

            # 5. Always return the registry version (single source of truth)
            info = self.registry.get_video_info(video_id=video_id)
            logger.info(f"[VideoDownloader] Stored in registry at {info['video_path']}")
            return info

        except Exception as e:
            logger.error(f"[VideoDownloader] Download failed: {e}")
            return None
