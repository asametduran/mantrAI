from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
import google.generativeai as genai

app = Flask(__name__)
CORS(app, origins=['http://localhost:5174', 'http://127.0.0.1:5174'])

# Gemini API anahtarınızı buraya ekleyin
genai.configure(api_key="AIzaSyA-Qd1FLbqvV7i7iEmPCE2qp84TypePBGA")

@app.route('/')
def index():
    return jsonify({
        "message": "HealthyLife AI Backend",
        "status": "running",
        "endpoints": ["/api/analyze_image_only"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/test', methods=['GET', 'POST'])
def test_endpoint():
    print("Test endpoint called!")
    return jsonify({"message": "Test endpoint working", "method": request.method})

@app.route('/api/analyze_image_only', methods=['POST', 'OPTIONS'])
def analyze_image_only():
    print(f"Request method: {request.method}")
    print(f"Request headers: {dict(request.headers)}")
    print(f"Request files: {request.files}")
    
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        print("Analyzing image...")
        
        if 'image' not in request.files:
            print("No image file in request")
            return jsonify({"error": "No image file provided"}), 400
        
        image_file = request.files['image']
        print(f"Image file: {image_file.filename}")
        
        if image_file.filename == '':
            print("Empty filename")
            return jsonify({"error": "No image selected"}), 400
        
        # Resmi PIL Image olarak yükle
        try:
            image = Image.open(image_file.stream)
            print(f"Image loaded successfully: {image.size}")
        except Exception as e:
            print(f"Error loading image: {e}")
            return jsonify({"error": f"Invalid image file: {str(e)}"}), 400
        
        # Gemini modeli oluştur
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            print("Gemini model created successfully")
        except Exception as e:
            print(f"Error creating Gemini model: {e}")
            return jsonify({"error": f"AI model error: {str(e)}"}), 500
        
        # Analiz için prompt
        prompt = """
        Bu ürün etiketini analiz et ve MUTLAKA aşağıdaki HTML formatını kullan. 
        
        ÖNEMLİ: Hiç markdown işareti kullanma (*, **, #, vb.). Sadece HTML etiketleri kullan!
        
        Yanıtın şu HTML formatında olmalı:
        
        <div class="product-analysis">
        <h3>🍽️ ÜRÜN ANALİZ RAPORU</h3>
        
        <div class="section">
        <h4>1. Ürün Adı ve Türü:</h4>
        <p>Burada ürün adını ve türünü yaz</p>
        </div>
        
        <div class="section">
        <h4>2. Ana Bileşenler:</h4>
        <ul>
        <li>Bileşen 1</li>
        <li>Bileşen 2</li>
        <li>Bileşen 3</li>
        </ul>
        </div>
        
        <div class="section">
        <h4>3. Beslenme Değerleri (100g başına):</h4>
        <ul>
        <li>Kalori: XXX kcal</li>
        <li>Protein: XXX g</li>
        <li>Karbonhidrat: XXX g</li>
        <li>Yağ: XXX g</li>
        </ul>
        </div>
        
        <div class="section">
        <h4>4. Sağlık Değerlendirmesi:</h4>
        <p>Sağlık açısından değerlendirmeyi buraya yaz</p>
        </div>
        
        <div class="section">
        <h4>5. Sağlıklı Yaşam Puanı: X/10</h4>
        <p>Puan açıklamasını buraya yaz</p>
        </div>
        
        <div class="section">
        <h4>6. Alternatif Öneriler:</h4>
        <ul>
        <li>Alternatif 1</li>
        <li>Alternatif 2</li>
        <li>Alternatif 3</li>
        </ul>
        </div>
        
        <div class="section">
        <p><strong>💡 Tavsiye:</strong> Genel tavsiyeni buraya yaz</p>
        </div>
        </div>
        
        TEKRAR EDİYORUM: Sadece HTML kullan, hiç markdown işareti kullanma!
        """
        
        # Resmi analiz et
        try:
            print("Sending to Gemini...")
            response = model.generate_content([prompt, image])
            analysis = response.text
            print("Analysis received from Gemini")
            
            return jsonify({
                "analysis": analysis,
                "confidence_score": 0.85,
                "status": "success"
            })
        except Exception as e:
            print(f"Error with Gemini analysis: {e}")
            return jsonify({"error": f"AI analysis failed: {str(e)}"}), 500
    
    except Exception as e:
        print(f"General error: {e}")
        return jsonify({
            "error": f"Analiz sırasında hata oluştu: {str(e)}",
            "status": "error"
        }), 500

if __name__ == '__main__':
    print("🚀 HealthyLife AI Backend başlatılıyor...")
    print("📍 Sunucu adresi: http://localhost:5002")
    print("🔗 Frontend bağlantısı hazır")
    app.run(host='0.0.0.0', port=5002, debug=True)
