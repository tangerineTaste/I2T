import sys
from model.infer_single import generate_caption

if __name__ == "__main__":
    img_path = sys.argv[1] if len(sys.argv) > 1 else "images/sample.jpg"
    caption = generate_caption(img_path)
    print(f"🖼️ 이미지: {img_path}")
    print(f"🗣️  생성된 대사: {caption}")