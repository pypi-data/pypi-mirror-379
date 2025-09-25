from ..imports import *
def make_video_info(filepath):
    # base ffprobe
    cmd = ["ffprobe","-v","quiet","-print_format","json",
           "-show_format","-show_streams",filepath]
    probe = subprocess.check_output(cmd)
    data = json.loads(probe)

    # derive fields
    info = {
        "id": os.path.basename(filepath).split('.')[0],
        "title": os.path.splitext(os.path.basename(filepath))[0],
        "upload_date": datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y%m%d"),
        "duration": float(data["format"]["duration"]),
        "streams": data["streams"],
        "format": data["format"],
        "video_path": filepath

    }
    return info

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
