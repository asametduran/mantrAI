from flask import Blueprint, jsonify, request
import google.generativeai as genai
import json
import re
import os

product_filter_bp = Blueprint('product_filter', __name__)

# Gemini API yapılandırması
genai.configure(api_key="AIzaSyA-Qd1FLbqvV7i7iEmPCE2qp84TypePBGA")

def call_gemini_api(prompt, max_tokens=500):
    """Gemini API'sini çağıran yardımcı fonksiyon"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=0.3,
            )
        )
        return response.text.strip()
    except Exception as e:
        return f"API Hatası: {str(e)}"

def extract_json_from_response(response_text):
    """Yanıttan JSON'u çıkaran yardımcı fonksiyon"""
    try:
        # JSON bloğunu bul
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)
        else:
            return {"error": "JSON bulunamadı"}
    except json.JSONDecodeError:
        return {"error": "Geçersiz JSON formatı"}

@product_filter_bp.route('/parse_user_input', methods=['POST'])
def parse_user_input():
    """Kullanıcı gereksinimlerini JSON formatına dönüştürür"""
    try:
        data = request.json
        user_requirements = data.get('user_requirements', '')
        
        prompt = f"""
        Kullanıcı kendi özel gereksinimlerini açıklayacak.
        Görevin, bu bilgileri standart bir JSON formatına dönüştürmek.
        Eğer belirtilmemişse false yap.

        Kullanıcı açıklaması: "{user_requirements}"

        JSON şeması:
        {{
            "gluten_free": false,
            "lactose_free": false,
            "nut_allergy": false,
            "soy_free": false,
            "vegan": false,
            "vegetarian": false,
            "halal": false,
            "kosher": false,
            "no_polyester": false,
            "no_wool": false,
            "latex_free": false,
            "cruelty_free": false,
            "fragrance_free": false,
            "organic_only": false,
            "eco_friendly": false,
            "low_salt": false,
            "low_sugar": false,
            "hypoallergenic": false
        }}
        
        Sadece JSON formatında yanıt ver, başka açıklama ekleme.
        """
        
        response = call_gemini_api(prompt)
        parsed_requirements = extract_json_from_response(response)
        
        return jsonify({
            "success": True,
            "parsed_requirements": parsed_requirements,
            "original_input": user_requirements
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@product_filter_bp.route('/evaluate_product', methods=['POST'])
def evaluate_product():
    """Ürünün kullanıcı gereksinimlerine uygunluğunu değerlendirir"""
    try:
        data = request.json
        user_constraints = data.get('user_constraints', {})
        product_category = data.get('product_category', '')
        product_name = data.get('product_name', '')
        product_ingredients = data.get('product_ingredients', '')
        product_tags = data.get('product_tags', '')
        
        prompt = f"""
        Aşağıdaki kullanıcı kısıtlamalarına göre ürünü değerlendir.
        Ürün gıda, giyim, kozmetik veya başka bir kategoriye ait olabilir. 
        Kullanıcının hassasiyetlerini dikkate alarak uygunluk durumunu belirle.
        Eğer ürün ❌ uygun değilse, neden olmadığını açıkla ve alternatif öneriler ver.

        Kullanıcı Gereksinimleri:
        {json.dumps(user_constraints, ensure_ascii=False, indent=2)}

        Ürün Bilgisi:
        {{
            "category": "{product_category}",
            "name": "{product_name}",
            "ingredients_or_materials": "{product_ingredients}",
            "tags": "{product_tags}"
        }}

        Beklenen JSON çıktısı:
        {{
            "product_name": "...",
            "category": "...",
            "status": "✅ uygun" veya "❌ uygun değil",
            "reason": "...",
            "score": 0-100,
            "alternatives": ["...", "..."]
        }}
        
        Sadece JSON formatında yanıt ver, başka açıklama ekleme.
        """
        
        response = call_gemini_api(prompt)
        product_evaluation = extract_json_from_response(response)
        
        return jsonify({
            "success": True,
            "evaluation": product_evaluation
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@product_filter_bp.route('/final_response', methods=['POST'])
def final_response():
    """Ürün değerlendirme sonucunu kullanıcıya anlaşılır şekilde sunar"""
    try:
        data = request.json
        evaluation = data.get('evaluation', {})
        
        prompt = f"""
        Aşağıdaki değerlendirmeyi kullanıcıya sade ve net bir şekilde aktar.
        Eğer ürün uygunsuzsa, alternatif önerileri öne çıkar. 
        Mümkünse kullanıcıyı cesaretlendirici bir dil kullan.
        Türkçe yanıt ver.

        Değerlendirme:
        {json.dumps(evaluation, ensure_ascii=False, indent=2)}
        """
        
        response = call_gemini_api(prompt, max_tokens=800)
        
        return jsonify({
            "success": True,
            "final_response": response,
            "evaluation_data": evaluation
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@product_filter_bp.route('/complete_workflow', methods=['POST'])
def complete_workflow():
    """Tüm workflow'u tek seferde çalıştırır"""
    try:
        data = request.json
        user_requirements = data.get('user_requirements', '')
        product_category = data.get('product_category', '')
        product_name = data.get('product_name', '')
        product_ingredients = data.get('product_ingredients', '')
        product_tags = data.get('product_tags', '')
        
        # 1. Kullanıcı gereksinimlerini parse et
        parse_prompt = f"""
        Kullanıcı kendi özel gereksinimlerini açıklayacak.
        Görevin, bu bilgileri standart bir JSON formatına dönüştürmek.
        Eğer belirtilmemişse false yap.

        Kullanıcı açıklaması: "{user_requirements}"

        JSON şeması:
        {{
            "gluten_free": false,
            "lactose_free": false,
            "nut_allergy": false,
            "soy_free": false,
            "vegan": false,
            "vegetarian": false,
            "halal": false,
            "kosher": false,
            "no_polyester": false,
            "no_wool": false,
            "latex_free": false,
            "cruelty_free": false,
            "fragrance_free": false,
            "organic_only": false,
            "eco_friendly": false,
            "low_salt": false,
            "low_sugar": false,
            "hypoallergenic": false
        }}
        
        Sadece JSON formatında yanıt ver.
        """
        
        parse_response = call_gemini_api(parse_prompt)
        parsed_requirements = extract_json_from_response(parse_response)
        
        # 2. Ürün uygunluğunu değerlendir
        evaluate_prompt = f"""
        Aşağıdaki kullanıcı kısıtlamalarına göre ürünü değerlendir.
        Ürün gıda, giyim, kozmetik veya başka bir kategoriye ait olabilir. 
        Kullanıcının hassasiyetlerini dikkate alarak uygunluk durumunu belirle.
        Eğer ürün ❌ uygun değilse, neden olmadığını açıkla ve alternatif öneriler ver.

        Kullanıcı Gereksinimleri:
        {json.dumps(parsed_requirements, ensure_ascii=False, indent=2)}

        Ürün Bilgisi:
        {{
            "category": "{product_category}",
            "name": "{product_name}",
            "ingredients_or_materials": "{product_ingredients}",
            "tags": "{product_tags}"
        }}

        Beklenen JSON çıktısı:
        {{
            "product_name": "...",
            "category": "...",
            "status": "✅ uygun" veya "❌ uygun değil",
            "reason": "...",
            "score": 0-100,
            "alternatives": ["...", "..."]
        }}
        
        Sadece JSON formatında yanıt ver.
        """
        
        evaluate_response = call_gemini_api(evaluate_prompt)
        product_evaluation = extract_json_from_response(evaluate_response)
        
        # 3. Final response oluştur
        final_prompt = f"""
        Aşağıdaki değerlendirmeyi kullanıcıya sade ve net bir şekilde aktar.
        Eğer ürün uygunsuzsa, alternatif önerileri öne çıkar. 
        Mümkünse kullanıcıyı cesaretlendirici bir dil kullan.
        Türkçe yanıt ver.

        Değerlendirme:
        {json.dumps(product_evaluation, ensure_ascii=False, indent=2)}
        """
        
        final_response_text = call_gemini_api(final_prompt, max_tokens=800)
        
        return jsonify({
            "success": True,
            "workflow_result": {
                "parsed_requirements": parsed_requirements,
                "product_evaluation": product_evaluation,
                "final_response": final_response_text
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

