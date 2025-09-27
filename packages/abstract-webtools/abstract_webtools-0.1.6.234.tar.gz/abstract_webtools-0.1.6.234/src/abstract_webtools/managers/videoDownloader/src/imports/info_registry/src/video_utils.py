from ..imports import *
_LOCK = threading.RLock()
from .video_paths import *

def generate_video_id(path: str, max_length: int = 50) -> str:
    # 1. Take basename (no extension)
    file_parts = get_file_parts(path)
    base= file_parts.get("filename")
    if base == 'video':
        base = file_parts.get("dirbase")
    # 2. Normalize Unicode → ASCII
    base = unicodedata.normalize('NFKD', base).encode('ascii', 'ignore').decode('ascii')
    # 3. Lower-case
    base = base.lower()
    # 4. Replace non-alphanumeric with hyphens
    base = re.sub(r'[^a-z0-9]+', '-', base).strip('-')
    # 5. Collapse duplicates
    base = re.sub(r'-{2,}', '-', base)
    # 6. Optionally truncate & hash for uniqueness
    if len(base) > max_length:
        h = hashlib.sha1(base.encode()).hexdigest()[:8]
        base = base[: max_length - len(h) - 1].rstrip('-') + '-' + h
    return base
def _get_video_info(url=None,file_path=None, ydl_opts=None,output_filename=None, cookies_path=None):
    from yt_dlp import YoutubeDL
    
    
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    if cookies_path and os.path.exists(cookies_path):
        ydl_opts['cookiefile'] = cookies_path

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as e:
        print(f"Failed to extract video info: {e}")
        return None




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
