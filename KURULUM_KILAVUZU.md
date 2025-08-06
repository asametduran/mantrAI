# 🚀 MantrAI Consumer Product Filter - Kurulum Kılavuzu

Bu dokuman, projeyi GitHub'dan zip olarak indirdikten sonra sıfırdan nasıl kuracağınızı ve çalıştıracağınızı gösterir.

## 📋 Gereksinimler

Kuruluma başlamadan önce aşağıdaki yazılımların bilgisayarınızda yüklü olduğundan emin olun:

- **Python 3.11+** (https://python.org/downloads/)
- **Node.js 20+** (https://nodejs.org/downloads/)
- **Git** (isteğe bağlı, https://git-scm.com/)
- **Google Gemini API Anahtarı** (https://makersuite.google.com/app/apikey)

## 📁 Proje Yapısı

```
mantrAI-master/
├── consumer_product_filter_api/     # Backend (Flask API)
│   ├── src/
│   │   ├── main.py                 # Ana Flask uygulaması
│   │   └── routes/
│   │       └── product_filter.py  # API endpoints
│   ├── requirements.txt            # Python bağımlılıkları
│   └── venv/                       # Python sanal ortamı (oluşturulacak)
└── consumer_product_filter_frontend/ # Frontend (React + Vite)
    ├── src/
    ├── package.json                # Node.js bağımlılıkları
    └── node_modules/               # Node.js paketleri (oluşturulacak)
```

## 🔧 Backend Kurulumu (Flask API)

### 1. Backend Dizinine Geçin

Windows PowerShell'de:
```powershell
cd "path\to\your\mantrAI-master\consumer_product_filter_api"
```

### 2. Python Sanal Ortamı Oluşturun

```powershell
python -m venv venv
```

### 3. Sanal Ortamı Aktifleştirin

**Windows:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/Mac (eğer sistem Linux/Mac'te oluşturulmuşsa):**
```bash
source venv/bin/activate
```

Başarılı olursa terminal prompt'unuzda `(venv)` görünecektir.

### 4. Python Bağımlılıklarını Yükleyin

```powershell
pip install -r requirements.txt
```

### 5. Gemini API Anahtarınızı Yapılandırın

`src/routes/product_filter.py` dosyasını açın ve aşağıdaki satırı bulun:
```python
genai.configure(api_key="AIzaSyA-Qd1FLbqvV7i7iEmPCE2qp84TypePBGA")
```

Bu satırdaki API anahtarını kendi Gemini API anahtarınızla değiştirin:
```python
genai.configure(api_key="BURAYA_KENDI_API_ANAHTARINIZI_YAZIN")
```

### 6. Backend'i Çalıştırın

```powershell
python src\main.py
```

Başarılı olursa şu mesajı göreceksiniz:
```
* Running on http://127.0.0.1:5002
* Running on http://10.x.x.x:5002
```

Backend artık **http://localhost:5002** adresinde çalışıyor! 🎉

## 🌐 Frontend Kurulumu (React + Vite)

### 1. Yeni Bir Terminal/PowerShell Penceresi Açın

Backend'i çalışır durumda bırakarak, yeni bir terminal açın.

### 2. Frontend Dizinine Geçin

```powershell
cd "path\to\your\mantrAI-master\consumer_product_filter_frontend"
```

### 3. Node.js Bağımlılıklarını Yükleyin

```powershell
npm install --legacy-peer-deps
```

> **Not:** `--legacy-peer-deps` parametresi bazı paket uyumsuzluklarını çözmek için gereklidir.

### 4. Frontend Geliştirme Sunucusunu Başlatın

```powershell
npm run dev -- --host
```

Başarılı olursa şu mesajı göreceksiniz:
```
VITE v6.x.x ready in xxxms

➜  Local:   http://localhost:5173/
➜  Network: http://10.x.x.x:5173/
```

Frontend artık **http://localhost:5173** adresinde çalışıyor! 🎉

## 🔗 API Endpoints

Backend başarıyla çalıştığında aşağıdaki endpoints kullanılabilir olacak:

- `POST http://localhost:5002/api/parse_user_input` - Kullanıcı gereksinimlerini JSON'a çevirir
- `POST http://localhost:5002/api/evaluate_product` - Ürün uygunluğunu değerlendirir
- `POST http://localhost:5002/api/final_response` - Son yanıtı formatlar
- `POST http://localhost:5002/api/complete_workflow` - Tüm işlemi tek seferde yapar

## ✅ Test Etme

### 1. Frontend Testi
Tarayıcınızda http://localhost:5173 adresini açın. React uygulaması yüklenmelidir.

### 2. Backend Testi
Tarayıcınızda http://localhost:5002 adresini açın. JSON formatında API bilgilerini görmelisiniz.

### 3. API Testi (Postman veya curl ile)
```bash
curl -X POST http://localhost:5002/api/complete_workflow \
  -H "Content-Type: application/json" \
  -d '{
    "user_requirements": "Vegan, gluten-free",
    "product_category": "Gıda",
    "product_name": "Organik Kurabiye",
    "product_ingredients": "Pirinç unu, hindistancevizi yağı, agave şurubu",
    "product_tags": "vegan, organik, glutensiz"
  }'
```

## 🛠️ Sorun Giderme

### Backend Sorunları

**Problem:** `ModuleNotFoundError: No module named 'flask'`
**Çözüm:** Sanal ortamın aktif olduğundan emin olun ve `pip install -r requirements.txt` komutunu tekrar çalıştırın.

**Problem:** `API Hatası: Invalid API key`
**Çözüm:** Gemini API anahtarınızın doğru olduğundan ve aktif olduğundan emin olun.

**Problem:** `ImportError: No module named 'google.generativeai'`
**Çözüm:** `pip install google-generativeai` komutunu çalıştırın.

### Frontend Sorunları

**Problem:** `npm ERR! ERESOLVE unable to resolve dependency tree`
**Çözüm:** `npm install --legacy-peer-deps` komutunu kullanın.

**Problem:** `'vite' is not recognized`
**Çözüm:** `node_modules` klasörünü silin ve `npm install --legacy-peer-deps` komutunu tekrar çalıştırın.

**Problem:** Port 5173 zaten kullanımda
**Çözüm:** `npm run dev -- --host --port 3000` komutuyla farklı bir port kullanın.

## 🔧 Geliştirme Ortamı

### Backend Geliştirme
- Flask debug modu aktiftir, kod değişiklikleri otomatik olarak uygulanır
- Loglara terminal üzerinden erişebilirsiniz

### Frontend Geliştirme  
- Vite hot reload aktiftir, değişiklikler anında tarayıcıda görünür
- React DevTools kullanabilirsiniz

## 📝 Önemli Notlar

1. **API Anahtarı Güvenliği:** Gerçek projelerde API anahtarını environment variable olarak saklayın.
2. **CORS:** Backend, frontend'den gelen istekleri kabul edecek şekilde yapılandırılmıştır.
3. **Port Ayarları:** Backend 5002, Frontend 5173 portunu kullanır.
4. **Debug Modu:** Geliştirme amaçlı debug modu aktiftir, production'da kapatın.

## 🚀 Production'a Hazırlık

### Backend için:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5002 src.main:app
```

### Frontend için:
```bash
npm run build
```

## 📞 Destek

Herhangi bir sorunla karşılaştığınızda:
1. Terminal çıktılarını kontrol edin
2. API anahtarınızın geçerli olduğundan emin olun
3. Port çakışmaları olup olmadığını kontrol edin
4. Sanal ortamın aktif olduğundan emin olun

---

**Happy Coding!** 🎉🚀
