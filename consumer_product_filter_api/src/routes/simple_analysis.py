from flask import Blueprint, request, jsonify
import requests
import json

simple_analysis_bp = Blueprint('simple_analysis', __name__)

@simple_analysis_bp.route('/analyze_image_only', methods=['POST'])
def analyze_image_only():
    """Sadece görsel yükleyerek otomatik analiz - Basit versiyon"""
    try:
        # Görsel dosyasını al
        if 'product_image' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Görsel dosyası bulunamadı'
            }), 400
        
        image_file = request.files['product_image']
        if image_file.filename == '':
            return jsonify({
                'success': False,
                'error': 'Görsel dosyası seçilmedi'
            }), 400
        
        # Basit mock analiz sonucu
        analysis_result = {
            "product_name": "Ürün Etiketi Tespit Edildi",
            "category": "Gıda",
            "extracted_ingredients": "Bu bir demo versiyondur. Gerçek analiz için yerel sunucuyu kullanın.",
            "allergens": ["Demo Allergen"],
            "nutrition_facts": "Demo besin değerleri - Gerçek analiz için yerel sunucuyu kullanın",
            "special_conditions": ["Demo"],
            "ai_recommendation": "Bu, Consumer Product Filter'ın demo versiyonudur. Gerçek görsel analizi için projeyi yerel olarak çalıştırın. Yerel sunucuda Gemini AI ile tam analiz yapılmaktadır."
        }
        
        return jsonify({
            'success': True,
            'analysis_result': analysis_result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Genel hata: {str(e)}'
        }), 500

@simple_analysis_bp.route('/health_image', methods=['GET'])
def health_image():
    """Görsel analiz servisi sağlık kontrolü"""
    return jsonify({
        'status': 'healthy',
        'service': 'simple_image_analysis',
        'version': '1.0.0',
        'note': 'Demo version - For real analysis, run locally'
    })

