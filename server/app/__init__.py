import os
import traceback

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(test_config)
    app.config['UPLOAD_FOLDER'] = 'uploads'

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
                file = request.files['file']
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return jsonify({'message': 'File uploaded successfully'})
            except Exception as e:
                return jsonify({'message': str(e)})

    return app
