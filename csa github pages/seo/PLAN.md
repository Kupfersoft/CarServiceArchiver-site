# SEO yayın ve içerik planı — v3

## Yapılanlar

- 14 dilde ana sayfa başlığı, H1, açıklama ve doğal dilde görünür SSS.
- 56 sayfanın tamamında sayfaya özel başlık ve meta description.
- GitHub Actions yayımında **gerçek repo adresinden** otomatik mutlak canonical, her sayfa için 14 dil + x-default hreflang, Open Graph, X/Twitter paylaşım etiketleri.
- Ana sayfalar için `SoftwareApplication` JSON-LD; uygulama henüz yayımlanmadığından `offers` ve sahte yorum/puan yok. Gerçek Store yayını sonrası ücretsiz fiyat teklifini ekle.
- `sitemap.xml` (56 URL, karşılıklı 14 dil bağlantıları) ve `robots.txt` GitHub Actions sırasında oluşturulur.
- 1200×630 statik sosyal kart; mevcut logo kullanıldı, ekran görüntüsü değildir.
- Anahtar kelime önerileri CSV dosyasında. Bunlar **arama hacmi verisi değildir**.

## Teknik notlar

- **Google `meta keywords` etiketini sıralamada KULLANMAZ.** Bu nedenle yanıltıcı bir meta anahtar kelime yığını eklemedik. İfadeler ilgili sayfa başlığı, metin ve SSS'de doğal biçimde ele alındı.
- `FAQPage` rich result şeması koymadık; Google'ın güncel görünürlük şartlarında sıradan yazılım sitelerine fayda sağlamıyor.
- `SoftwareApplication` şeması Google'ın rich-result yönergelerinde review veya aggregateRating isteyebilir. Kullanıcı yorumu bulunmadığı için asla uydurma puan eklemedik; schema işaretlemesi Google'da zengin sonuç garantisi değildir.
- Sitenin kişisel veri ve KVKK ile ilgili hukuki eksikleri teknik SEO ile giderilmez; hukuki metinler yayımdan önce ayrıca değerlendirilmelidir.
- İlk sürümün mağaza bağlantısı henüz bilinmiyor, uydurma bir Microsoft Store bağlantısı eklenmedi.
- `robots.txt` GitHub Pages proje alt klasöründe barınıyorsa ana alan adının robot kuralları yerine geçmez. Search Console üzerinden `sitemap.xml` göndermek daha önemlidir.

## Yayın sonrası

1. Gerçek `https://...github.io/.../` sayfa URL'sini kontrol et.
2. [Google Search Console](https://search.google.com/search-console/about) ile mülk doğrula, gerçek `/sitemap.xml` adresini gönder.
3. Google URL Denetleme ile TR/EN ve diğer dil ana sayfalarını test et. `hreflang`, canonical, `og:image` açıldığını doğrula.
4. Mağaza yayına girdikten sonra resmî Store URL'sini 14 dilin ana sayfasına ücretsiz indirme bağlantısı olarak ekle; açıklama/structured data güncelle.
5. Gerçek, anonim örnek verili ekran görüntüleri ekleyip açıklayıcı alt metinler yaz; bu paket sahte UI görüntüsü üretmez.
6. Search Console gösterim / tıklama ve sorgu verilerini ölçerek özellikle TR/EN/DE/ES başlıklarını revize et.

**Sıralama veya indeksleme garantisi yoktur.**
