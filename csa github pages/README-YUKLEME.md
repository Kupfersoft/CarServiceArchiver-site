# Car Service Archiver — GitHub Pages 14 Dil + SEO (v3)

Bu sürüm, önceki **14 dilli ve 56 HTML sayfalı** sitenin devamıdır. Tasarım, yasal metinler ve bütün dil yolları korunur. Electron / SQLite / Windows uygulaması değişmez.

## Nasıl yayımlayacağız? (önemli: bu sürüm GitHub Actions kullanıyor)

1. Bu ZIP'in içindeki dosya ve klasörleri GitHub'daki **açık** web sitesi deposunun kök dizinine yükle. `.github/workflows/pages.yml`, `scripts/build_site.py`, `seo/` klasörlerini de yüklemeyi unutma.
2. GitHub deposunda **Settings → Pages → Build and deployment → Source: GitHub Actions** seç.
3. **Actions** sekmesinde `Deploy Car Service Archiver 14-language SEO site` iş akışının başarıyla çalıştığını kontrol et. Gerekirse `Run workflow` ile manuel çalıştır.
4. **Settings → Pages → Visit site** bağlantısıyla gerçek web adresini aç. `privacy.html` ve `sitemap.xml` dosyalarını ziyaret edip doğrula.
5. [Google Search Console](https://search.google.com/search-console/about) üzerinden siteyi doğrula, `sitemap.xml` adresini gönder.

**Neden GitHub Actions?** GitHub kullanıcı adını ve gerçek site URL'ni bilmiyoruz. İş akışı bunları depodan otomatik belirleyip 56 sayfanın canonical, hreflang, Open Graph, SoftwareApplication JSON-LD ve XML sitemap adreslerini **gerçek URL ile** oluşturuyor. Böylece sahte veya başka bir GitHub kullanıcısına işaret eden SEO bağlantıları bulunmuyor.

Bu siteyi `Deploy from a branch` ile yayımlarsan HTML sayfaları açılabilir ama gerekli mutlak canonical/hreflang/OG ve sitemap oluşturulmaz. **v3 için GitHub Actions seçmen gerekiyor.**

### Özel alan adı

İleride alan adı satın alırsan köke `CNAME` adlı dosya ekleyip içine yalnızca `example.com` yaz. GitHub Pages'te bu alan adını ayrıca doğruladıktan sonra bir sonraki Actions yayını yeni canonical ve sitemap URL'lerini üretir.

### Yerel test (isteğe bağlı)

`python scripts/build_site.py --site-url https://ornek.github.io/car-service-archiver-site/`

Bu komut `_site/` klasörüne yayıma hazır sürümü oluşturur. Adres yalnızca test örneğidir; gerçek dağıtım otomatik algılar.

## SEO içerikleri

- 14 dilde sayfa başlıkları, doğal H1, özelleştirilmiş sayfa açıklamaları ve ana sayfada kullanıcıya faydalı SSS.
- Her sayfanın kendi canonical URL'si ve 14 dil karşılığı + `x-default` bağlantısı.
- 56 bağlantılı `sitemap.xml`, `robots.txt`.
- Yazılım (SoftwareApplication) JSON-LD; henüz yayında olmayan uygulama için sahte satın alma teklifi, **sahte yorum/puan yok**.
- Open Graph / Twitter kartları için tasarımla uyumlu `assets/social-preview.png`.
- `seo/anahtar-kelimeler-14-dil.csv`: her dilde 4 arama hedefi (gerçek arama hacmi verisi değil).
- `seo/PLAN.md`: sonraki geliştirmeler ve sınırlamalar.

**Google `meta keywords` etiketini kullanmıyor.** Spam gibi anahtar kelime yığmak yerine doğal sayfa metnine odaklandık.

## Yayından önce önemli notlar

- Uygulama Microsoft Store'da henüz yayımlanmadı; **sahte indirme düğmesi veya Store URL'si eklemedik.** Yayından sonra 14 dilde gerçek bağlantı eklenecek.
- Ayrı KVKK sayfası, kişisel telefon, ev adresi veya gerçek kişi adı bu dosyalara eklenmedi. **Bu tercih hukuki yükümlülükleri otomatik ortadan kaldırmaz.** Gizlilik/EULA metinleri hukuki ve dilsel inceleme gerektiren taslaklardır.
- Site çerez analitiği, takip pikseli, haricî font veya çeviri API'si kullanmaz.
- Sitemap ve SEO işaretlemeleri **Google sıralamasında garanti vermez.** Search Console ile sonuçları gözlemlemelisin.
- GitHub Pages proje alt klasöründeki `robots.txt`, alan adının kökündeki robot kuralları yerine geçmez.
