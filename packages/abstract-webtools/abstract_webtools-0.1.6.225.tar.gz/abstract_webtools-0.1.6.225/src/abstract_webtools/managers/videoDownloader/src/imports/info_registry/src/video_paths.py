from typing import Any
import os
from abstract_security import get_env_value

VIDEO_ENV_KEY = "DATA_DIRECTORY"
# Full schema
VIDEO_SCHEMA = {
    "video": "video.mp4",
    "info": "info.json",
    "audio": "audio.wav",
    "whisper": "whisper.json",
    "captions": "captions.srt",
    "metadata": "metadata.json",
    "thumbnail": "thumb.jpg",
    "thumbnails_index": "thumbnails.json",
    "total_info": "total_info.json",

    "aggregated_dir": {
        "aggregated_json": "aggregated.json",
        "aggregated_metadata": "aggregated_metadata.json",
        "best_clip": "best_clip.txt",
        "hashtags": "hashtags.txt",
    },

    "thumbnails_dir": {
        "frames": "{video_id}_frame_{i}.jpg",  # pattern
    }
}


def expand_schema(video_id: str, folder: str, schema: dict[str, Any]) -> dict[str, Any]:
    """
    Expand VIDEO_SCHEMA into concrete paths (recursively).
    - Replaces {video_id} placeholder with the actual ID.
    - Leaves {i} in place for thumbnail frames (user expands at runtime).
    """
    result = {}
    for key, rel in schema.items():
        if isinstance(rel, dict):
            subfolder = os.path.join(folder, key.replace("_dir", ""))
            os.makedirs(subfolder, exist_ok=True)
            result[key] = expand_schema(video_id, subfolder, rel)
        elif isinstance(rel, str):
            rel = rel.format(video_id=video_id, i="{i}")
            path = os.path.join(folder, rel)
            if key.endswith("_dir"):
                os.makedirs(path, exist_ok=True)
            result[key] = path
    return result


def ensure_standard_paths(info: dict, video_root: str) -> dict:
    """
    Ensure standard paths exist inside <video_root>/<video_id>/ and
    attach canonical paths to `info`.
    """
    vid = info.get("video_id") or info.get("id")
    if not vid:
        return info

    dirbase = os.path.join(video_root, vid)
    os.makedirs(dirbase, exist_ok=True)

    schema_paths = expand_schema(vid, dirbase, VIDEO_SCHEMA)

    # flatten for convenience (keep nested under "schema_paths" too)
    def flatten(d, parent_key="", sep="_"):
        flat = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                flat.update(flatten(v, new_key, sep))
            else:
                flat[new_key] = v
        return flat

    flat_paths = flatten(schema_paths)

    for k, v in flat_paths.items():
        if not info.get(k):
            info[k] = v

    info["schema_paths"] = schema_paths
    return info
def get_video_env(key=None, envPath=None):
    """Pull video directory from env file or environment variables."""
    key = key or VIDEO_ENV_KEY
    return get_env_value(key=key, path=envPath)

def get_video_root(video_root=None):
    """Fallback root directory if no env override is found."""
    home = os.path.expanduser("~")
    candidates = [
        video_root,
        os.path.join(home, "Videos"),
        os.path.join(home, "videos"),
        os.path.join(home, "Downloads"),
        os.path.join(home, "downloads"),
        home,
    ]
    for directory in candidates:
        if directory and os.path.isdir(directory):
            return directory
    return home  # last resort

def get_video_directory(key=None, envPath=None):
    """Assure that a valid video directory exists and return its path."""
    video_directory = get_video_env(key=key, envPath=envPath)
    if not video_directory:
        video_directory = get_video_root()

    os.makedirs(video_directory, exist_ok=True)
    return video_directory

def get_video_folder(video_id, envPath=None):
    """Return the canonical per-video folder and ensure subdirs exist."""
    root = get_video_directory(envPath=envPath)
    dir_path = os.path.join(root, video_id)
    os.makedirs(dir_path, exist_ok=True)

    # Ensure schema directories exist
    for key, rel in VIDEO_SCHEMA.items():
        if rel.endswith("/") or "dir" in key:
            os.makedirs(os.path.join(dir_path, rel), exist_ok=True)

    return dir_path

def get_video_paths(video_id, envPath=None):
    """Return dict of canonical paths for this video_id."""
    folder = get_video_folder(video_id, envPath=envPath)
    return {key: os.path.join(folder, rel) for key, rel in VIDEO_SCHEMA.items()}
