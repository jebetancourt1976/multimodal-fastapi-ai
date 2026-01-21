import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def analyze(image_file):
    image = Image.open(image_file.file)
    inputs = processor(
        text=["person", "office", "outdoor", "computer"],
        images=image,
        return_tensors="pt",
        padding=True
    )
    outputs = model(**inputs)
    probs = outputs.logits_per_image.softmax(dim=1)
    return {
        "scene_probabilities": probs.detach().numpy().tolist()
    }
