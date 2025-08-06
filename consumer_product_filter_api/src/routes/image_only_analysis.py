from flask import Blueprint, request, jsonify
import google.generativeai as genai
from PIL import Image
import io
import base64
import time

# Gemini API anahtarını ayarla
genai.configure(api_key="AIzaSyA-Qd1FLbqvV7i7iEmPCE2qp84TypePBGA")

image_analysis_bp = Blueprint('image_analysis', __name__)

# Rate limiting için son istek zamanı
last_request_time = 0

def optimize_image(image_file):
    """Görseli optimize et (boyut ve format)"""
    try:
        image = Image.open(image_file)
        
        # RGBA'yı RGB'ye çevir (PNG transparency için)
        if image.mode == 'RGBA':
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[-1])
            image = background
        elif image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Boyutu optimize et (max 1024px)
        max_size = 1024
        if max(image.size) > max_size:
            ratio = max_size / max(image.size)
            new_size = tuple(int(dim * ratio) for dim in image.size)
            image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        return image
    except Exception as e:
        raise Exception(f"Görsel optimizasyonu hatası: {str(e)}")

@image_analysis_bp.route('/analyze_image_only', methods=['POST'])
def analyze_image_only():
    """Sadece görsel yükleyerek otomatik analiz"""
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
        
        # Görseli optimize et
        try:
            optimized_image = optimize_image(image_file)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Görsel işleme hatası: {str(e)}'
            }), 400
        
        # Görseli base64'e çevir
        img_byte_arr = io.BytesIO()
        optimized_image.save(img_byte_arr, format='JPEG', quality=85)
        img_byte_arr.seek(0)
        
        # Gemini model oluştur
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # AI prompt - Türkçe ve kapsamlı
        prompt = """
Bu ürün etiket fotoğrafını analiz et ve aşağıdaki bilgileri çıkar:

1. ÜRÜN BİLGİSİ:
   - Ürün adı
   - Ürün kategorisi (gıda, kozmetik, giyim, vs.)

2. İÇERİK LİSTESİ:
   - Tüm içerikleri/malzemeleri listele
   - İçindekiler listesini tam olarak oku

3. ALLERGEN TESPİTİ:
   - Glüten, laktoz, yumurta, fındık, soya, balık vb. allergenler
   - Allergen uyarılarını tespit et

4. BESİN DEĞERLERİ:
   - Kalori, yağ, karbonhidrat, protein, tuz değerleri
   - 100g başına besin değerleri

5. ÖZEL DURUMLAR:
   - Vegan, vegetaryen, helal, kosher sertifikaları
   - Organik, glütensiz, laktozsiz etiketleri
   - Cruelty-free, parfümsüz gibi özellikler

6. AI ÖNERİSİ:
   - Bu ürünün genel değerlendirmesi
   - Dikkat edilmesi gereken noktalar
   - Kimler için uygun/uygun değil

Sonucu JSON formatında ver:
{
  "product_name": "ürün adı",
  "category": "kategori",
  "extracted_ingredients": "içerikler listesi",
  "allergens": ["allergen1", "allergen2"],
  "nutrition_facts": "besin değerleri",
  "special_conditions": ["vegan", "glütensiz"],
  "ai_recommendation": "AI önerisi ve değerlendirme"
}

Eğer bazı bilgiler net değilse "Tespit edilemedi" yaz.
Türkçe yanıt ver.
"""
        
        # Gemini'ye görsel ve prompt gönder
        try:
            response = model.generate_content([prompt, optimized_image])
            ai_response = response.text
            
            # JSON parse etmeye çalış
            import json
            import re
            
            # JSON kısmını bul
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                try:
                    analysis_result = json.loads(json_str)
                except:
                    # JSON parse edilemezse, ham metni kullan
                    analysis_result = {
                        "product_name": "Tespit edilemedi",
                        "category": "Tespit edilemedi", 
                        "extracted_ingredients": ai_response,
                        "allergens": [],
                        "nutrition_facts": "Tespit edilemedi",
                        "special_conditions": [],
                        "ai_recommendation": "Görsel analiz tamamlandı, ancak yapılandırılmış veri çıkarılamadı."
                    }
            else:
                # JSON bulunamazsa ham metni kullan
                analysis_result = {
                    "product_name": "Tespit edilemedi",
                    "category": "Tespit edilemedi",
                    "extracted_ingredients": ai_response,
                    "allergens": [],
                    "nutrition_facts": "Tespit edilemedi", 
                    "special_conditions": [],
                    "ai_recommendation": "Görsel analiz tamamlandı."
                }
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'AI analiz hatası: {str(e)}'
            }), 500
        
        return jsonify({
            'success': True,
            'analysis_result': analysis_result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Genel hata: {str(e)}'
        }), 500

@image_analysis_bp.route('/health_image', methods=['GET'])
def health_image():
    """Görsel analiz servisi sağlık kontrolü"""
    return jsonify({
        'status': 'healthy',
        'service': 'image_analysis',
        'version': '1.0.0'
    })
