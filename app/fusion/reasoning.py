from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import json
# =====================================================
# Environment & OpenAI
# =====================================================

load_dotenv(dotenv_path=Path(".env"))

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found")

client = OpenAI(api_key=api_key)

def multimodal_reasoning(results: dict) -> str:
    prompt = f"""
You are an expert multimodal AI analyst.

Analyze the following multimodal outputs and provide a unified explanation.
Be concise, explicit, and reason across modalities.
explain each modality by separate and isplay each conclusion in no more than 3 sentences.

Multimodal Results:
{json.dumps(results, indent=2)}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text
