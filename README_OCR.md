# Consumer Product Filter with OCR Support 📷🔍

**Evrensel Ürün Uygunluk Kontrol Sistemi - Gemini AI + Görsel OCR Destekli**

Bu proje, kullanıcıların özel gereksinimlerine göre ürün uygunluğunu kontrol eden AI destekli bir web uygulamasıdır. **Yeni özellik**: Artık ürün etiket fotoğraflarını yükleyerek otomatik içerik analizi yapabilirsiniz!

## 🆕 Yeni Özellikler (v3.0)

### 📷 Görsel Etiket Analizi (OCR)
- **Fotoğraf Yükleme**: Ürün etiket fotoğraflarını doğrudan yükleyin
- **Otomatik OCR**: Gemini AI görselden yazıları otomatik okur
- **İçerik Çıkarma**: İçindekiler, besin değerleri ve allergen uyarıları
- **Multimodal AI**: Görsel + metin analizi bir arada

### 🎯 Çift Mod Desteği
- **📝 Metin Modu**: Manuel içerik girişi (eski yöntem)
- **📷 Görsel Modu**: Fotoğraf yükleme ile otomatik analiz (yeni!)

## 🌟 Ana Özellikler

### 🤖 AI Destekli Analiz
- **Google Gemini 1.5 Flash** ile güçlendirilmiş
- Doğal dil işleme ve görsel analiz
- Çoklu gereksinim desteği (18 farklı kategori)
- Akıllı alternatif öneriler

### 🏷️ Evrensel Ürün Desteği
- **Gıda**: Glütensiz, laktozsiz, vegan, helal, allerjen kontrolü
- **Kozmetik**: Cruelty-free, parfümsüz, hipoalerjenik
- **Giyim**: Polyester içermez, organik pamuk, etik üretim
- **Genel**: Çevre dostu, organik, sürdürülebilir

### 📊 Detaylı Değerlendirme
- **Uygunluk Skoru**: 0-100 arası değerlendirme
- **Neden Analizi**: Uygun/uygun değil gerekçeleri
- **Alternatif Öneriler**: Benzer uygun ürün önerileri
- **Gereksinim Eşleştirme**: Hangi kriterlerin karşılandığı

## 🚀 Nasıl Çalışır?

### 📷 Görsel Modu (Önerilen)
1. **Gereksinimlerinizi girin**: \"Glütensiz, vegan, helal ürün arıyorum\"
2. **Ürün kategorisini belirtin**: \"Gıda\"
3. **Ürün adını girin**: \"Organik Protein Tozu\"
4. **Etiket fotoğrafını yükleyin**: Ürün ambalajının fotoğrafı
5. **AI analizi alın**: Otomatik OCR + uygunluk kontrolü

### 📝 Metin Modu (Klasik)
1. **Gereksinimlerinizi girin**: Özel ihtiyaçlarınız
2. **Ürün bilgilerini doldurun**: Kategori, ad, içerik listesi
3. **AI analizi alın**: Uygunluk kontrolü ve öneriler

## 🛠️ Teknik Özellikler

### Backend API
- **Framework**: Flask 3.0
- **AI Model**: Google Gemini 1.5 Flash
- **Görsel İşleme**: Pillow (PIL)
- **OCR**: Gemini Vision API
- **CORS**: Tüm origin'lere açık

### Frontend
- **Framework**: React 18 + Vite
- **Styling**: Tailwind CSS
- **UI Components**: Custom responsive design
- **File Upload**: Drag & drop görsel yükleme
- **Mode Toggle**: Metin/Görsel mod değiştirici

### API Endpoints

#### 🆕 Görsel Destekli Endpoint
```http
POST /api/complete_workflow_with_image
Content-Type: multipart/form-data

Form Fields:
- user_requirements: string (gereksinimler)
- product_category: string (kategori)
- product_name: string (ürün adı)
- product_tags: string (etiketler)
- product_image: file (görsel dosya)
```

#### 📝 Metin Tabanlı Endpoint
```http
POST /api/complete_workflow
Content-Type: application/json

{
  \"user_requirements\": \"Glütensiz, vegan ürün\",
  \"product_category\": \"Gıda\",
  \"product_name\": \"Protein Tozu\",
  \"product_ingredients\": \"Bezelye proteini, pirinç proteini\",
  \"product_tags\": \"Organik, Vegan\"
}
```

## 📦 Kurulum ve Çalıştırma

### Backend Kurulumu
```bash
cd consumer_product_filter_api
pip install -r requirements.txt
python src/main.py
```

### Frontend Kurulumu
```bash
cd consumer_product_filter_frontend
npm install
npm run dev
```

### Gerekli Bağımlılıklar
```txt
# Backend
Flask==3.0.0
Flask-CORS==4.0.0
google-generativeai==0.8.5
requests==2.32.4
Pillow==10.4.0

# Frontend
React 18+
Tailwind CSS
Vite
```

## 🌐 Canlı Demo

- **Web Sitesi**: https://rmvezwts.manus.space
- **Backend API**: https://8xhpiqclm90n.manus.space

## 🎯 Kullanım Senaryoları

### 🥗 Gıda Ürünleri
- Allerjen kontrolü (glüten, laktoz, fındık)
- Diyet uygunluğu (vegan, vejetaryen)
- Dini gereksinimler (helal, kosher)
- Sağlık kriterleri (düşük tuz, şeker)

### 💄 Kozmetik Ürünleri
- Hayvan testleri (cruelty-free)
- Parfüm hassasiyeti (fragrance-free)
- Cilt uygunluğu (hipoalerjenik)
- Doğal içerik tercihi

### 👕 Giyim Ürünleri
- Malzeme hassasiyeti (polyester, yün)
- Etik üretim kriterleri
- Organik malzeme tercihi
- Sürdürülebilirlik

## 🔧 API Yanıt Formatı

```json
{
  \"success\": true,
  \"workflow_result\": {
    \"parsed_requirements\": {
      \"gluten_free\": true,
      \"vegan\": true,
      \"halal\": true
    },
    \"extracted_ingredients\": \"Organik bezelye proteini %80, organik pirinç proteini %15, doğal vanilya aroması %5\",
    \"product_evaluation\": {
      \"product_name\": \"Organik Protein Tozu\",
      \"category\": \"Gıda\",
      \"status\": \"✅ uygun\",
      \"reason\": \"Ürün vegan, glütensiz ve helal sertifikalı\",
      \"score\": 95,
      \"alternatives\": []
    },
    \"final_response\": \"Harika! Bu ürün sizin için mükemmel uygun...\"
  }
}
```

## 🔒 Güvenlik ve Gizlilik

- **HTTPS**: Tüm iletişim şifrelenmiş
- **API Güvenliği**: Gemini API anahtarı backend'de korunuyor
- **Veri Saklama**: Kullanıcı verileri saklanmıyor
- **Görsel İşleme**: Yüklenen görseller geçici olarak işleniyor

## 🚀 Performans

- **Yanıt Süresi**: 3-8 saniye (görsel analizi dahil)
- **Desteklenen Formatlar**: PNG, JPG, JPEG
- **Maksimum Görsel Boyutu**: 1024px (otomatik optimize)
- **Eş Zamanlı İstek**: Sınırsız

## 🎨 Özellik Karşılaştırması

| Özellik | Metin Modu | Görsel Modu |
|---------|------------|-------------|
| Hız | ⚡ Hızlı (2-3s) | 🔄 Orta (5-8s) |
| Doğruluk | 📝 Manuel girişe bağlı | 🎯 OCR doğruluğu |
| Kullanım | 💻 Masaüstü uygun | 📱 Mobil uygun |
| Allergen Tespiti | ✅ Manuel | ✅ Otomatik |
| Besin Değerleri | ❌ Desteklenmez | ✅ Otomatik |

## 🔮 Gelecek Özellikler

- [ ] Çoklu dil desteği (İngilizce, Almanca)
- [ ] Barkod tarama desteği
- [ ] Ürün veritabanı entegrasyonu
- [ ] Kullanıcı profili ve geçmiş
- [ ] Mobil uygulama (React Native)
- [ ] Batch işleme (çoklu ürün analizi)

## 📞 Destek

Herhangi bir sorun veya öneriniz için:
- GitHub Issues açabilirsiniz
- API dokümantasyonunu kontrol edin
- Demo sitesini test edin

## 📄 Lisans

Bu proje MIT lisansı altında yayınlanmıştır.

---

**Consumer Product Filter v3.0** - Gemini AI + OCR ile güçlendirilmiş evrensel ürün uygunluk kontrol sistemi 🚀

