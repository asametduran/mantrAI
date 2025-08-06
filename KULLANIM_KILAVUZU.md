# Kullanım Kılavuzu - Evrensel Ürün Uygunluk Kontrol Sistemi

Bu kılavuz, Evrensel Ürün Uygunluk Kontrol Sistemi'nin nasıl kullanılacağını adım adım açıklar. Sistem **her türlü ürün** için (gıda, giyim, kozmetik, elektronik vb.) kullanılabilir.

## Hızlı Başlangıç

### 1. Sistemi Başlatma

#### Backend'i Başlatma
```bash
cd consumer_product_filter_api
source venv/bin/activate
python src/main.py
```

#### Frontend'i Başlatma
```bash
cd consumer_product_filter_frontend
npm run dev -- --host
```

### 2. Web Arayüzüne Erişim

Tarayıcınızda `http://localhost:5173` adresine gidin.

## Adım Adım Kullanım

### Adım 1: Özel Gereksinimlerinizi Girin

"Özel Gereksinimleriniz" alanına ihtiyaçlarınızı doğal dilde yazın.

**Gıda için örnek girişler:**
- "Glütensiz ve vegan ürün arıyorum"
- "Helal sertifikalı, düşük tuzlu ürün istiyorum"
- "Laktozsiz, organik ve katkısız ürün gerekiyor"
- "Fındık alerjim var, soya içermesin"

**Kozmetik için örnek girişler:**
- "Hayvan testleri yapılmamış, vegan ürün istiyorum"
- "Parfümsüz, hipoalerjenik ürün arıyorum"
- "Paraben içermeyen, doğal ürün gerekiyor"

**Giyim için örnek girişler:**
- "Polyester alerjim var, doğal kumaş istiyorum"
- "Organik pamuk, etik üretim ürünü arıyorum"
- "Yün içermeyen, vegan giyim ürünü"

### Adım 2: Ürün Kategorisini Belirtin

Kontrol etmek istediğiniz ürünün kategorisini girin.

**Desteklenen kategoriler:**
- **Gıda**: Yiyecek, içecek, gıda takviyeleri
- **Giyim**: Kıyafet, ayakkabı, aksesuar
- **Kozmetik**: Makyaj, cilt bakımı, parfüm
- **Elektronik**: Telefon, bilgisayar, ev aletleri
- **Ev Ürünleri**: Temizlik, mobilya, dekorasyon
- **Sağlık**: İlaç, medikal ürünler
- **Oyuncak**: Çocuk oyuncakları, eğitici materyaller

### Adım 3: Ürün Adını Girin

Kontrol etmek istediğiniz ürünün tam adını yazın.

**Örnekler:**
- "Organik Vegan Protein Tozu"
- "Cruelty-Free Mat Ruj"
- "Pamuklu Organik T-shirt"
- "Glütensiz Tam Buğday Ekmeği"

### Adım 4: İçerik/Malzeme Listesini Girin

Ürünün etiketinde yazan içerik veya malzeme listesini tam olarak yazın.

**Gıda örneği:**
```
Organik bezelye proteini, organik pirinç proteini, 
doğal vanilya aroması, stevia, tuz
```

**Kozmetik örneği:**
```
Aqua, glycerin, shea butter, vitamin E, 
doğal parfüm, preservative-free
```

**Giyim örneği:**
```
%100 organik pamuk, doğal boyalar, 
GOTS sertifikalı
```

### Adım 5: Ürün Etiketlerini Girin (Opsiyonel)

Ürün üzerinde bulunan sertifika ve etiketleri yazın.

**Örnekler:**
- "Organik, Vegan, Helal Sertifikalı, Glütensiz"
- "Cruelty-Free, Paraben-Free, Hypoallergenic"
- "GOTS, OEKO-TEX, Fair Trade"
- "Energy Star, RoHS Compliant"

### Adım 6: Kontrolü Başlatın

"Ürünü Kontrol Et" butonuna tıklayın ve AI analizinin tamamlanmasını bekleyin.

## Sonuçları Anlama

### Uygunluk Durumu

- **✅ Uygun**: Ürün gereksinimlerinize uygun
- **❌ Uygun Değil**: Ürün gereksinimlerinizi karşılamıyor

### Uygunluk Skoru

0-100 arası bir skor ile ürünün ne kadar uygun olduğunu gösterir:
- **80-100**: Çok uygun
- **60-79**: Uygun
- **40-59**: Kısmen uygun
- **0-39**: Uygun değil

### AI Önerisi

Sistem, ürünün durumuna göre:
- Ürünü kullanabileceğinizi onaylar
- Dikkat edilmesi gereken noktaları belirtir
- Alternatif ürün önerileri sunar

### Algılanan Gereksinimler

Sisteminizin girdiğiniz metinden algıladığı 18 farklı gereksinim kategorisini gösterir.

## Kategori Bazında Kullanım Örnekleri

### Gıda Ürünleri

**Örnek 1: Çölyak Hastası**
```
Gereksinimler: "Çölyak hastasıyım, glütensiz ürün arıyorum"
Kategori: "Gıda"
Ürün: "Quinoa Ekmeği"
İçerik: "Quinoa unu, pirinç unu, xanthan gum, maya"
Etiketler: "Glütensiz Sertifikalı"
```

**Örnek 2: Vegan Beslenme**
```
Gereksinimler: "Vegan yaşıyorum, hayvansal ürün içermesin"
Kategori: "Gıda"
Ürün: "Badem Sütü"
İçerik: "Su, badem, doğal tatlandırıcı"
Etiketler: "Vegan, Organik"
```

### Kozmetik Ürünleri

**Örnek 1: Hassas Cilt**
```
Gereksinimler: "Hassas cildim var, parfümsüz ve hipoalerjenik ürün"
Kategori: "Kozmetik"
Ürün: "Nemlendirici Krem"
İçerik: "Aqua, glycerin, ceramides, niacinamide"
Etiketler: "Fragrance-Free, Hypoallergenic"
```

**Örnek 2: Etik Tüketim**
```
Gereksinimler: "Hayvan testleri yapılmamış, cruelty-free ürün"
Kategori: "Kozmetik"
Ürün: "Doğal Ruj"
İçerik: "Shea butter, candelilla wax, mineral pigments"
Etiketler: "Cruelty-Free, Vegan, Organic"
```

### Giyim Ürünleri

**Örnek 1: Alerjik Reaksiyon**
```
Gereksinimler: "Polyester alerjim var, doğal kumaş istiyorum"
Kategori: "Giyim"
Ürün: "Pamuklu T-shirt"
İçerik: "%100 organik pamuk, doğal boyalar"
Etiketler: "GOTS Sertifikalı, Organik"
```

**Örnek 2: Sürdürülebilirlik**
```
Gereksinimler: "Çevre dostu, sürdürülebilir üretim ürünü"
Kategori: "Giyim"
Ürün: "Geri Dönüştürülmüş Ceket"
İçerik: "Geri dönüştürülmüş polyester, organik pamuk"
Etiketler: "Recycled, Sustainable, Fair Trade"
```

## Gelişmiş Özellikler

### Çoklu Gereksinim Kontrolü

Sistem aynı anda birden fazla gereksinimi kontrol edebilir:

```
Gereksinimler: "Glütensiz, vegan, helal, organik ve düşük tuzlu ürün arıyorum"
```

### Kategori Bağımsız Analiz

Aynı gereksinim farklı kategorilerde farklı şekilde değerlendirilir:

- **"Cruelty-free"** gıda için: Hayvansal ürün içermez
- **"Cruelty-free"** kozmetik için: Hayvan testleri yapılmamış
- **"Cruelty-free"** giyim için: Hayvan derisi/kürkü içermez

## Sorun Giderme

### API Hatası Alıyorum
- Backend sunucusunun çalıştığından emin olun
- Gemini API anahtarının doğru ayarlandığından emin olun
- İnternet bağlantınızı kontrol edin

### Sonuç Gelmiyor
- Tüm zorunlu alanları doldurduğunuzdan emin olun
- Birkaç saniye bekleyin, AI analizi zaman alabilir

### Yanlış Sonuç Alıyorum
- Gereksinimlerinizi daha açık yazın
- Ürün kategorisini doğru belirtin
- İçerik/malzeme listesini tam ve doğru girin
- Ürün etiketlerini kontrol edin

## API Doğrudan Kullanımı

Sistemi programatik olarak kullanmak için:

```bash
curl -X POST http://localhost:5001/api/complete_workflow \
  -H "Content-Type: application/json" \
  -d '{
    "user_requirements": "Vegan, cruelty-free ürün",
    "product_category": "Kozmetik",
    "product_name": "Doğal Ruj",
    "product_ingredients": "Shea butter, candelilla wax",
    "product_tags": "Vegan, Cruelty-Free"
  }'
```

## İpuçları

### Daha İyi Sonuçlar İçin

1. **Açık ve Net Olun**: Gereksinimlerinizi mümkün olduğunca açık yazın
2. **Doğru Kategori**: Ürün kategorisini doğru belirtin
3. **Tam Bilgi**: Ürünün tam içerik/malzeme listesini girin
4. **Sertifikaları Belirtin**: Varsa sertifika bilgilerini ekleyin
5. **Birden Fazla Gereksinim**: Birden fazla gereksiniminizi aynı anda belirtebilirsiniz

### Sistem Sınırları

- Sistem sadece verdiğiniz bilgileri analiz eder
- Ürün hakkında ek araştırma yapmaz
- Medikal tavsiye vermez, sadece uygunluk değerlendirmesi yapar
- Sertifika doğrulaması yapmaz

## Destek

Herhangi bir sorunuz veya sorununuz varsa:
1. Bu kılavuzu tekrar okuyun
2. README.md dosyasını inceleyin
3. GitHub Issues sayfasında yeni bir konu açın

