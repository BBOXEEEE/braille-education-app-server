import os
from flask import jsonify, request
from werkzeug.utils import secure_filename
from ultralytics import YOLO

from . import object_detection
from ..constants.domain import Domain
from ..text_to_braille.text_to_braille import textToBraille

@object_detection.route("/", methods=['POST'])
def detect_object():
    '''
    테스트용 Object Detection API
    모델 학습이 완료되기 전까지 pre-trined 모델을 이용하여 Object Detection을 수행
    '''
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    filename = secure_filename(file.filename)
    save_path = os.path.join(os.path.dirname(__file__), 'data')
    file.save(os.path.join(save_path, filename))

    try:
        '''
        Load the model and prediction
        '''
        model = YOLO('yolov8n.pt')
        img_path = os.path.join(save_path, filename)
        results = model.predict(source=img_path)

        '''
        Post-Processing

        1. Get the class and confidence score
        2. Sort the result by confidence score in descending order
        3. Select the top 3 classes without duplication
        4. Mapping the class id to the class name
        5. Translation Text to Braille
        6. Convert the result to the JSON format
        7. Return the result
        '''

        # 1. Get the class and confidence score
        ids = results[0].boxes.cls
        scores = results[0].boxes.conf

        results = set()
        for id, score in zip(ids, scores):
            results.add((int(id.item()), score.item()))

        # 2. Sort the result by confidence score in descending order
        results = sorted(results, key=lambda x: x[1], reverse=True)
        
        # 3. Select the top 3 classes without duplication
        top3 = []
        cnt = 0
        for id, _ in results:
            if cnt < 3 and id not in top3:
                top3.append(id)
                cnt += 1

        # 4. Mapping the class id to the class name
        categories = [Domain().get_category(id) for id in top3]

        # 5. Translation Text to Braille
        braille_list = [textToBraille(category) for category in categories]

        # 6. Convert the result to the JSON format
        ret = [{'word': category, 'braille': braille} for category, braille in zip(categories, braille_list)]

        # 7. Return the result
        return jsonify(ret), 200
    finally:
        os.remove(os.path.join(save_path, filename))

