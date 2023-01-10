import logging
import os
import traceback

import cv2

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename, send_file
from core.image_editor import ImageEditor

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(test_config)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Handle cors
    CORS(app)

    @app.errorhandler(500)
    def internal_error(exception):
        print(traceback.format_exc())

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'Welcome to the API'})

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            try:
                # Save the file
                logger.info('Received file: %s', request.files['file'].filename)
                file = request.files['file']
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Turn to a cartoon
                logger.info('Turning to a cartoon')
                editor = ImageEditor.from_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cartoon_pic = editor.as_cartoon(k=8, remove_background=True)
                cartoon_pic_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cartoon_' + filename)
                cv2.imwrite(cartoon_pic_path, cartoon_pic)

                # Return the cartoon image as multipart
                return send_file(cartoon_pic_path, mimetype='image/png', environ=request.environ)
            except Exception as e:
                return jsonify({'message': str(e)})

    return app
