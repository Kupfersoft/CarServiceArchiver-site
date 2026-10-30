# Car Service Archiver — GitHub Pages + Store + Screenshots

Bu paket, kullanıcı tarafından gönderilen sitenin galeri öncesi TEMİZ sürümünden üretildi.

## Ne değişti?
- 14 dilde ana sayfadaki ilk buton resmi Microsoft Store bağlantısına yönlendirir: https://apps.microsoft.com/detail/9N3FVX0PR4BX
- Özellikler altına büyük 16:9 fotoğraf ve 7 adet seçilebilir küçük görsel eklendi. Görseller kırpılmaz.
- 14 ayrı yerel dilde `gallery.html` sayfası bulunur; 7 ekran görüntüsüne tıklanınca büyük açılır.
- Galeride oklarla veya klavyede sağ/sol ile ilerlenebilir; ESC ile kapatılır.
- 98 PNG (14 x 7) kendi dilinin klasöründe. Japonca için JA-FIXED görüntüleri kullanıldı.
- GitHub Actions derleme betiği galeri sayfalarını, hreflang bağlantılarını ve sitemap'i kapsayacak şekilde güncellendi.
- Gizlilik, EULA ve iletişim sayfalarının orijinal METİNLERİ değiştirilmedi.
- Ana sayfalardaki eski 'mağazaya link sonra eklenecek' FAQ metni güncellendi.

## Nasıl yayımlanır?
1. ZIP'i aç; İÇİNDEKİ tüm dosyaları repo ana dizinine ekle. ZIP'in kendisini yükleme.
2. `assets/screenshots` klasöründeki 98 resmi, `assets/showcase.js`, `assets/style.css`, `gallery.html` ve 13 dildeki galeri dosyalarını eksiksiz ekle.
3. GitHub → Settings → Pages → Source: **GitHub Actions** olmalı. `.github/workflows/pages.yml` mevcut akıştır.
4. Ana sayfadan ekran görüntülerini dene; Galeri ve Microsoft Store bağlantılarını kontrol et.
5. Eğer önceki bozuk galeri sürümünün dosyalarını eklediysen, git'te artık kullanılmayan yalnızca `/assets/screenshots` içindeki eski numaralandırmaları ve eski `gallery.html`'leri yenisiyle değiştir; farklı yol altındaki gereksiz eski resimleri sil.

## Lokal yapım kontrolü
`python scripts/build_site.py --site-url https://example.github.io/repo/`
Hazır çıktı `_site/` içine alınır. Gerçek GitHub Actions URL'sini kendisi belirler.
