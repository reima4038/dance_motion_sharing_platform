from typing import Any
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to the Dance Skill-up Platform API"}


@app.post("/upload_video", status_code=202)
def upload_video(file: UploadFile = File(...)) -> dict[str, Any]:
    """
    Accepts a video file, simulates processing, and returns a task ID.
    In a real implementation, this would save the file and start
    an async background task for pose estimation.
    """
    # In a real app, we would save the file and process it.
    # For the PoC architecture, we just simulate acceptance.
    video_id = "some_unique_video_id_123"
    return {
        "message": "Video upload received. Processing has started.",
        "video_id": video_id,
        "filename": file.filename,
        "content_type": file.content_type,
    }


@app.get("/videos/{video_id}")
def get_video_status(video_id: str) -> dict[str, Any]:
    """
    Returns the status and data for a given video ID.
    In a real implementation, this would check the status of the
    pose estimation task.
    """
    # For the PoC architecture, we return mock data.
    # This structure matches the domain model.
    return {
        "video_id": video_id,
        "status": "completed",
        "video_url": f"/static/videos/{video_id}.mp4",
        "pose_data_url": f"/static/posedata/{video_id}.json",
    }
