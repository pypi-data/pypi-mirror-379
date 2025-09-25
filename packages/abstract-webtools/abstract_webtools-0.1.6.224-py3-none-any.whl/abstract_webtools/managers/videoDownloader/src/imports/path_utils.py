import os

# Single root for all videos
VIDEO_ROOT = os.path.expanduser("~/videos")

# Schema: subfolders created *inside each video folder*
VIDEO_SCHEMA = {
    "info_path": "info.json",
    "file_path": "video.mp4",
    "audio_path": "audio.wav",
    "whisper_path": "whisper.json",
    "srt_path": "captions.srt",
    "metadata_path": "metadata.json",
    "thumbnails_dir": "thumbnails",
    "thumbnails_path": "thumbnails/thumbnails.json",
    "aggregated_dir": "aggregated",
    "total_info_path": "total_info.json",
    "total_data_path": "total_data.json",
    "total_aggregated_path": "aggregated/total_aggregated.json",
}

def get_video_root(envKey="VIDEO_DATA_DIRECTORY", envPath=None):
    """Get or create the global video root directory."""
    video_directory = (
        get_env_value(key=envKey, path=envPath)
        or VIDEO_ROOT
    )
    os.makedirs(video_directory, exist_ok=True)
    return video_directory

def get_video_folder(video_id, envPath=None):
    """Return the canonical per-video folder and ensure subdirs exist."""
    root = get_video_root(envPath=envPath)
    dir_path = os.path.join(root, video_id)
    os.makedirs(dir_path, exist_ok=True)

    # Ensure standard subfolders exist
    for key, rel in VIDEO_SCHEMA.items():
        if rel.endswith("/"):  # directory
            os.makedirs(os.path.join(dir_path, rel), exist_ok=True)
        elif "dir" in key:  # explicit dir keys
            os.makedirs(os.path.join(dir_path, rel), exist_ok=True)

    return dir_path

def get_video_paths(video_id, envPath=None):
    """Return dict of canonical paths for this video_id."""
    folder = get_video_folder(video_id, envPath=envPath)
    return {key: os.path.join(folder, rel) for key, rel in VIDEO_SCHEMA.items()}
