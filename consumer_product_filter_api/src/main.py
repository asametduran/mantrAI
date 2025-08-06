import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, jsonify
from flask_cors import CORS
from src.routes.image_only_analysis import image_analysis_bp
from src.routes.product_filter import product_filter_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# CORS desteği ekle
CORS(app)

app.register_blueprint(image_analysis_bp, url_prefix='/api')
app.register_blueprint(product_filter_bp, url_prefix='/api')

@app.route('/')
def index():
    return jsonify({
        "message": "Consumer Product Filter API with Smart Image Analysis",
        "version": "4.0.0",
        "description": "Sadece fotoğraf yükleyerek otomatik ürün analizi - Gemini AI destekli",
        "endpoints": {
            "analyze_image_only": "/api/analyze_image_only",
            "health_image": "/api/health_image",
            "parse_user_input": "/api/parse_user_input",
            "evaluate_product": "/api/evaluate_product",
            "final_response": "/api/final_response",
            "complete_workflow": "/api/complete_workflow"
        },
        "features": ["smart_image_analysis", "auto_detection", "multimodal_ai", "drag_drop_upload", "text_analysis", "product_filtering"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "product-filter-api"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
