# HealthyLife AI - Akıllı Ürün Analiz Sistemi

Bu proje, kullanıcıların ürün etiketlerini fotoğraflayarak **AI destekli sağlık analizi** yapabilen modern bir web uygulamasıdır. Google Gemini AI teknolojisi ile ürünlerin beslenme değerlerini analiz eder ve sağlıklı yaşam için öneriler sunar.

## 🚀 Özellikler

- **📸 Görsel Analiz**: Ürün etiketlerini fotoğraflayarak otomatik analiz
- **🤖 AI Destekli**: Google Gemini 1.5 Flash modeli ile güçlü analiz
- **🍽️ Detaylı Raporlama**: HTML formatında düzenli ve okunabilir analiz raporları
- **⚡ Anlık Sonuçlar**: Gerçek zamanlı ürün değerlendirmesi
- **💊 Sağlık Puanlama**: 1-10 arası sağlıklı yaşam uygunluk puanı
- **🔄 Alternatif Öneriler**: Daha sağlıklı ürün alternatifleri
- **🎨 Modern Tasarım**: Glassmorphism efektli responsive arayüz
- **🌐 Türkçe Destek**: Tam Türkçe analiz ve raporlama

## 📁 Proje Yapısı

```
mantrAI/
├── consumer_product_filter_api/          # Flask Backend
│   ├── simple_backend.py                 # Ana backend sunucu
│   ├── requirements.txt                  # Python bağımlılıkları
│   ├── venv/                            # Python sanal ortamı
│   └── src/                             # Kaynak dosyalar
│       ├── database/                    # SQLite veritabanı
│       ├── models/                      # Veritabanı modelleri
│       ├── routes/                      # API endpoint'leri
│       └── static/                      # Statik dosyalar
├── consumer_product_filter_frontend/    # React Frontend
│   ├── src/
│   │   ├── App.jsx                      # Ana React bileşeni (Yeniden tasarlandı)
│   │   ├── App.css                      # Modern CSS stilleri (Yeni)
│   │   ├── main.jsx                     # React giriş noktası
│   │   └── components/ui/               # shadcn/ui bileşenleri
│   ├── package.json                     # Node.js bağımlılıkları
│   └── vite.config.js                   # Vite yapılandırması
├── README.md                            # Bu dosya
├── KULLANIM_KILAVUZU.md                # Detaylı kullanım kılavuzu
├── README_OCR.md                        # OCR özellik dokümantasyonu
├── README_SMART_ANALYSIS.md            # AI analiz dokümantasyonu
└── todo.md                              # Proje görevleri
```

## 🛠️ Kurulum

### Gereksinimler

- Python 3.11+
- Node.js 20+
- Google Gemini API anahtarı ([Google AI Studio](https://makersuite.google.com/app/apikey)'dan alın)

### 📦 Backend Kurulumu

1. **Backend dizinine gidin:**
```bash
cd consumer_product_filter_api
```

2. **Sanal ortamı aktifleştirin:**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Gemini API anahtarınızı güncelleyin:**
`simple_backend.py` dosyasında:
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```

5. **Backend sunucuyu başlatın:**
```bash
python simple_backend.py
```

Backend http://localhost:5002 adresinde çalışacaktır.

### 🎨 Frontend Kurulumu

1. **Frontend dizinine gidin:**
```bash
cd consumer_product_filter_frontend
```

2. **Bağımlılıkları yükleyin:**
```bash
npm install
```

3. **Geliştirme sunucusunu başlatın:**
```bash
npm run dev
```

Frontend http://localhost:5174 adresinde çalışacaktır.

## 🔗 API Endpoints

### Ana Analiz Endpoint'i

- `POST /api/analyze_image_only` - Ürün etiket resmini analiz eder

### Yardımcı Endpoint'ler

- `GET /` - Backend durum bilgisi
- `GET /health` - Sağlık kontrolü
- `POST /api/test` - Test endpoint'i

### 📝 API Kullanım Örneği

```javascript
const formData = new FormData();
formData.append('image', imageFile);

const response = await fetch('http://localhost:5002/api/analyze_image_only', {
  method: 'POST',
  body: formData
});

const result = await response.json();
console.log(result.analysis); // HTML formatında analiz raporu
```

## 🎯 Kullanım

1. **Web arayüzünü açın:** http://localhost:5174
2. **Ürün fotoğrafı yükleyin:** "Resim Seç" butonuna tıklayın
3. **Analiz başlatın:** "Analizi Başlat" butonuna tıklayın
4. **Sonuçları görüntüleyin:** AI'nin detaylı analiz raporunu inceleyin

## 📊 Analiz Raporu İçeriği

AI analizi şu bilgileri içerir:

1. **🏷️ Ürün Adı ve Türü**
2. **🧪 Ana Bileşenler Listesi**
3. **📈 Beslenme Değerleri** (100g başına)
4. **❤️ Sağlık Değerlendirmesi**
5. **⭐ Sağlıklı Yaşam Puanı** (1-10 arası)
6. **💡 Alternatif Öneriler**
7. **🔍 Genel Tavsiyeler**

## 🛡️ Teknik Detaylar

### Backend Teknolojileri
- **Flask**: Web framework
- **Google Gemini 1.5 Flash**: AI görsel analiz
- **Flask-CORS**: Cross-origin istekleri
- **PIL (Pillow)**: Görsel işleme
- **SQLite**: Veri saklama

### Frontend Teknolojileri
- **React 18**: UI framework
- **Vite**: Build tool ve dev server
- **Modern CSS**: Glassmorphism tasarım
- **Responsive Design**: Mobil uyumlu arayüz

### 🤖 AI Workflow

1. **Görsel Yükleme**: Kullanıcı ürün etiket fotoğrafını yükler
2. **Görsel İşleme**: PIL ile görsel doğrulanır ve işlenir
3. **AI Analizi**: Gemini API ile görsel analiz edilir
4. **HTML Formatı**: Sonuçlar düzenli HTML formatında döndürülür
5. **Kullanıcı Arayüzü**: Modern tasarımla sonuçlar gösterilir

## 🎨 Tasarım Özellikleri

- **Glassmorphism Efekt**: Modern cam görünümü
- **Gradient Arka Planlar**: Dinamik renk geçişleri
- **Responsive Grid**: Mobil ve masaüstü uyumlu
- **Hover Animasyonlar**: Etkileşimli kullanıcı deneyimi
- **Türkçe UI**: Tam Türkçe arayüz metinleri

## 🔧 Yapılandırma

### CORS Ayarları
Backend şu origin'lerden gelen istekleri kabul eder:
- http://localhost:5174
- http://127.0.0.1:5174

### Sunucu Portları
- **Backend**: 5002
- **Frontend**: 5174

## 📱 Desteklenen Dosya Formatları

- **JPEG** (.jpg, .jpeg)
- **PNG** (.png)
- **WebP** (.webp)
- **BMP** (.bmp)

## 🐛 Sorun Giderme

### Backend Sorunları
```bash
# Python bulunamıyor hatası
venv\Scripts\activate
python --version

# Paket eksik hatası
pip install -r requirements.txt

# Port kullanımda hatası
taskkill /f /im python.exe
```

### Frontend Sorunları
```bash
# Bağımlılık hatası
rm -rf node_modules package-lock.json
npm install

# Port kullanımda hatası
# Yeni terminal açın veya farklı port kullanın
npm run dev -- --port 5175
```

## 🌟 Öne Çıkan Özellikler

- ✅ **Gerçek AI Analizi**: Mock değil, gerçek Gemini AI
- ✅ **HTML Formatı**: Düzenli ve okunabilir raporlar
- ✅ **Modern Tasarım**: Glassmorphism ve animasyonlar
- ✅ **Türkçe Destek**: Tam yerelleştirme
- ✅ **Responsive**: Tüm cihazlarda çalışır
- ✅ **Hızlı**: Optimized performans

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik: XYZ'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📞 Destek

Herhangi bir sorun yaşarsanız, lütfen GitHub Issues sayfasında bir issue oluşturun.

---

**HealthyLife AI** - Sağlıklı yaşam için akıllı tercihler! 🌱

## Kurulum

### Gereksinimler

- Python 3.11+
- Node.js 20+
- Google Gemini API anahtarı

### Backend Kurulumu

1. Backend dizinine gidin:
```bash
cd consumer_product_filter_api
```

2. Sanal ortamı aktifleştirin:
```bash
source venv/bin/activate
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. Gemini API anahtarınızı `src/routes/product_filter.py` dosyasında güncelleyin:
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```

5. Flask uygulamasını başlatın:
```bash
python src/main.py
```

Backend http://localhost:5001 adresinde çalışacaktır.

### Frontend Kurulumu

1. Frontend dizinine gidin:
```bash
cd consumer_product_filter_frontend
```

2. Bağımlılıkları yükleyin:
```bash
npm install
```

3. Geliştirme sunucusunu başlatın:
```bash
npm run dev -- --host
```

Frontend http://localhost:5173 adresinde çalışacaktır.

## API Endpoints

### Ürün Filtreleme API'leri

- `POST /api/parse_user_input` - Kullanıcı gereksinimlerini JSON formatına dönüştürür
- `POST /api/evaluate_product` - Ürünün kullanıcı gereksinimlerine uygunluğunu değerlendirir
- `POST /api/final_response` - Ürün değerlendirme sonucunu kullanıcıya anlaşılır şekilde sunar
- `POST /api/complete_workflow` - Tüm workflow'u tek seferde çalıştırır

### Örnek API Kullanımı

```javascript
// Tüm workflow'u çalıştırma
const response = await fetch('http://localhost:5001/api/complete_workflow', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    user_requirements: "Ben veganım, hayvanlar üzerinde test yapılmış ürünleri kullanmam, parfüme hassasım",
    product_category: "Kozmetik",
    product_name: "Mat Ruj",
    product_ingredients: "Paraben, koku verici, bitkisel yağlar",
    product_tags: "cruelty_tested, vegan değil"
  }),
});

const data = await response.json();
console.log(data.workflow_result);
```

## Kullanım

1. Web arayüzünde özel gereksinimlerinizi girin
2. Ürün kategorisini belirtin (Gıda, Giyim, Kozmetik, Elektronik vb.)
3. Kontrol etmek istediğiniz ürünün adını girin
4. Ürünün içerik/malzeme listesini girin
5. Ürün etiketlerini girin (opsiyonel)
6. "Ürünü Kontrol Et" butonuna tıklayın
7. AI analiz sonuçlarını ve alternatif önerileri görüntüleyin

## Desteklenen Gereksinimler

### Gıda Ürünleri
- **Alerjiler**: Glütensiz, laktozsuz, fındık alerjisi, soya alerjisi
- **Diyet**: Vegan, vejetaryen, düşük tuzlu, düşük şekerli
- **Dini/Etik**: Helal, koşer
- **Kalite**: Organik, katkısız

### Giyim Ürünleri
- **Malzeme**: Polyester içermez, yün içermez, pamuk
- **Üretim**: Organik, sürdürülebilir, etik üretim
- **Sertifika**: GOTS, OEKO-TEX

### Kozmetik Ürünleri
- **Test**: Cruelty-free (hayvan testleri yapılmamış)
- **İçerik**: Parfümsüz, paraben içermez, hipoalerjenik
- **Malzeme**: Latex içermez, doğal içerikli
- **Sertifika**: Organik, vegan

### Elektronik Ürünleri
- **Çevre**: Çevre dostu, geri dönüştürülebilir
- **Sertifika**: Energy Star, RoHS uyumlu
- **Üretim**: Etik üretim, adil ticaret

## Teknik Detaylar

### Backend Teknolojileri
- **Flask**: Web framework
- **Google Gemini API**: AI analiz için
- **Flask-CORS**: Cross-origin istekleri için
- **SQLAlchemy**: Veritabanı ORM

### Frontend Teknolojileri
- **React**: UI framework
- **Tailwind CSS**: Styling
- **shadcn/ui**: UI bileşenleri
- **Lucide React**: İkonlar
- **Vite**: Build tool

### AI Workflow

1. **Parse User Input**: Kullanıcının doğal dil gereksinimlerini 18 farklı kategoride yapılandırılmış JSON formatına dönüştürür
2. **Evaluate Product**: Ürün bilgilerini kategori bağımsız şekilde kullanıcı gereksinimlerine göre değerlendirir
3. **Final Response**: Sonuçları kullanıcıya anlaşılır şekilde sunar ve alternatif öneriler verir

## Örnek Kullanım Senaryoları

### Senaryo 1: Gıda Ürünü
```
Gereksinimler: "Çölyak hastasıyım, glütensiz ürün arıyorum"
Kategori: "Gıda"
Ürün: "Tam Buğday Ekmeği"
Sonuç: ❌ Uygun değil - Glüten içeriyor
```

### Senaryo 2: Kozmetik Ürünü
```
Gereksinimler: "Vegan yaşıyorum, hayvan testleri yapılmış ürün kullanmam"
Kategori: "Kozmetik"
Ürün: "Organik Ruj"
Sonuç: ✅ Uygun - Cruelty-free ve vegan
```

### Senaryo 3: Giyim Ürünü
```
Gereksinimler: "Polyester alerjim var, doğal kumaş istiyorum"
Kategori: "Giyim"
Ürün: "Pamuklu T-shirt"
Sonuç: ✅ Uygun - %100 pamuk
```

## Geliştirme

### Yeni Gereksinim Türü Ekleme

1. `product_filter.py` dosyasındaki JSON şemasına yeni alanı ekleyin
2. Prompt'larda yeni gereksinim türünü belirtin
3. Frontend'de gerekirse yeni UI bileşenleri ekleyin

### API Endpoint Ekleme

1. `src/routes/` dizininde yeni route dosyası oluşturun
2. `main.py` dosyasında blueprint'i kaydedin
3. Frontend'de yeni endpoint'i kullanın

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## Destek

Herhangi bir sorun yaşarsanız, lütfen GitHub Issues sayfasında bir issue oluşturun.

