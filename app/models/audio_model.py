import whisper
import tempfile

model = whisper.load_model("base")

def analyze(audio_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return {
        "transcript": result["text"]
    }
