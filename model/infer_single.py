from PIL import Image
from model_loader import load_blip_model

def generate_caption(image_path):
    processor, model, device = load_blip_model()
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
