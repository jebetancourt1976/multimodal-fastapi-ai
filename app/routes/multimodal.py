from fastapi import APIRouter, UploadFile, File, Form
from app.models import text_model, image_model, audio_model, video_model
from app.fusion.reasoning import multimodal_reasoning

router = APIRouter(prefix="/api")

@router.post("/analyze")
async def analyze(
    text: str = Form(None),
    image: UploadFile = File(None),
    audio: UploadFile = File(None),
    video: UploadFile = File(None)
):
    # 🔍 DEBUG LOG (TEMPORARY)
    print("VIDEO RECEIVED:", video.filename if video else "NO VIDEO")
    results = {}

    if text:
        results["text"] = text_model.analyze(text)

    if image:
        results["image"] = image_model.analyze(image)

    if audio:
        results["audio"] = audio_model.analyze(audio)

    if video:
        results["video"] = video_model.analyze(video)

    reasoning = multimodal_reasoning(results)

    return {
        "modal_outputs": results,
        "final_reasoning": reasoning
    }
    print("FINAL API RESPONSE:", {
        "modal_outputs": results,
        "final_reasoning": multimodal_reasoning(results)
    })