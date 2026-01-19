from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.multimodal import router
from pathlib import Path
from fastapi.responses import FileResponse

app = FastAPI(title="Multimodal AI Demo")

BASE_DIR = Path(__file__).resolve().parent

# 1️⃣ Include API routes FIRST
app.include_router(router)

# 2️⃣ Mount static files LAST
app.mount(
    "/",
    StaticFiles(directory=BASE_DIR / "static", html=True),
    name="static"
)

# 3️⃣ (Optional but recommended) Explicit root
@app.get("/")
def root():
    return FileResponse(BASE_DIR / "static" / "index.html")

