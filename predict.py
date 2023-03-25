from flask import Flask, request
from PIL import Image

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # 이미지 파일 추출
    image_file = request.files['image']
    image = Image.open(image_file)

    # 이미지 처리 코드 작성
    resized_image = image.resize((224, 224))
    # ...

    return 'Image uploaded', 200

if __name__ == '__main__':
    app.run()