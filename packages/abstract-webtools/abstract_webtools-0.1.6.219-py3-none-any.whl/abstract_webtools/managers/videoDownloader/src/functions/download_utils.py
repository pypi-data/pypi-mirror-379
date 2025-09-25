from .functions import *
from ..imports import *
from .info_utils import infoRegistry
import threading,os,re,yt_dlp,urllib.request,m3u8_To_MP4,subprocess
from abstract_utilities import get_logFile,safe_dump_to_file

from m3u8 import M3U8  # Install: pip install m3u8
from urllib.parse import urljoin
from yt_dlp.postprocessor.ffmpeg import FFmpegFixupPostProcessor
from abstract_math import divide_it,add_it,multiply_it,subtract_it
from abstract_pandas import *
import os, shutil, threading, time, yt_dlp
from abstract_utilities import safe_dump_to_file
from .info_utils import infoRegistry, generate_video_id  # from above
from ..imports import logger  # assuming you have a logger

def get_download_directory(download_directory):
    d = download_directory or os.path.expanduser("~/Downloads/videos")
    os.makedirs(d, exist_ok=True)
    return d

def get_corrected_url(url: str | list):
    if isinstance(url, list):
        return url
    return url.strip()

class VideoDownloader:
    def __init__(self, url, download_directory=None, user_agent=None,
                 video_extention="mp4", download_video=True,
                 get_info=False, output_filename=None,
                 ydl_opts=None, registry=None, force_refresh=False):

        self.monitoring = True
        self.pause_event = threading.Event()

        self.url = get_corrected_url(url=url)
        self.video_urls = self.url if isinstance(self.url, list) else [self.url]

        self.registry = registry or infoRegistry()
        self.ydl_opts = ydl_opts or {}
        self.get_download = download_video
        self.get_info = get_info
        self.user_agent = user_agent
        self.video_extention = video_extention
        self.download_directory = get_download_directory(download_directory)
        self.output_filename = output_filename
        self.force_refresh = force_refresh
        self.info = {}

        # start immediately (same behavior as before)
        self._start()

    # ---------- threading ----------

    def _start(self):
        self.download_thread = threading.Thread(target=self._download_entrypoint, name="video-download")
        self.download_thread.daemon = True

        self.monitor_thread = threading.Thread(target=self._monitor, name="video-monitor")
        self.monitor_thread.daemon = True

        self.download_thread.start()
        self.monitor_thread.start()

        # Only join the download (monitor is daemon and will exit)
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
            "merge_output_format": "mp4",  # ensure mp4 merge when needed
            "concurrent_fragment_downloads": 3,
            "ratelimit": 0,
            "retries": 5,
            "fragment_retries": 5,
            "ignoreerrors": False,
        }

        if extractor_client:
            # critical for SABR/NSIG issues
            opts.setdefault("extractor_args", {})
            opts["extractor_args"].setdefault("youtube", {})
            opts["extractor_args"]["youtube"]["player_client"] = [extractor_client]

        if self.user_agent:
            opts["http_headers"] = {"User-Agent": self.user_agent}

        # allow caller to override
        if self.ydl_opts:
            # shallow merge to not lose extractor_args
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

    # ---------- main download ----------

    def _download_entrypoint(self):
        try:
            info = self._download()
            if info:
                self.info = info
        finally:
            # Always stop the monitor
            self.stop()

    def _download(self):
        for video_url in self.video_urls:
            logger.info(f"[VideoDownloader] Processing: {video_url}")

            # --- Registry shortcut
            cached = self.registry.get_video_info(video_url, force_refresh=self.force_refresh)
            if cached and cached.get("file_path") and os.path.isfile(cached["file_path"]):
                logger.info(f"[VideoDownloader] Found cached file: {cached['file_path']}")
                return cached

            tmp_outtmpl = os.path.join(self.download_directory, "%(id)s.%(ext)s")

            try:
                with yt_dlp.YoutubeDL(self._build_ydl_opts(tmp_outtmpl)) as ydl:
                    info = ydl.extract_info(video_url, download=self.get_download)
                    video_id = info.get("id") or generate_video_id(info.get("title") or "video")
                    dirbase = self.download_directory
                    if self.download_directory and os.path.isdir(self.download_directory) and not os.path.basename(self.download_directory) == video_id:
                        # --- Canonical base directory
                        dirbase = os.path.join(self.download_directory, video_id)
                    os.makedirs(dirbase, exist_ok=True)
                    
                    # --- Final video file
                    temp_path = ydl.prepare_filename(info)
                    _, ext = os.path.splitext(temp_path)
                    final_path = os.path.join(dirbase, f"video{ext or '.mp4'}")

                    if temp_path != final_path and os.path.isfile(temp_path):
                        shutil.move(temp_path, final_path)

                    # --- Core info
                    info["file_path"] = final_path
                    info["video_id"] = video_id
                    info_path = os.path.join(dirbase, "info.json")
                    safe_dump_to_file(info, info_path)
                    info["info_path"] = info_path

                    # --- Add placeholders for extras
                    info.update({
                        "audio_path": os.path.join(dirbase, "audio.wav"),
                        "whisper_path": os.path.join(dirbase, "whisper.json"),
                        "srt_path": os.path.join(dirbase, "captions.srt"),
                        "metadata_path": os.path.join(dirbase, "metadata.json"),
                        "thumbnails_dir": os.path.join(dirbase, "thumbnails"),
                    })
                    os.makedirs(info["thumbnails_dir"], exist_ok=True)

                    # --- Update registry
                    self.registry.edit_info(
                        data={"file_path": final_path, "info_path": info_path, **info},
                        url=video_url,
                        video_id=video_id
                    )

                    logger.info(f"[VideoDownloader] Downloaded and stored at {final_path}")
                    return info

            except Exception as e:
                logger.error(f"[VideoDownloader] Download failed: {e}")
                return None

