# Uyku Akademi — Bilimsel Eğitim Kampüsü

Bilimsel bebek ve çocuk uykusu hakkında Türkçe, etkileşimli ve kaynaklı eğitim platformu.

**Canlı site:** https://serdarza.github.io/uyku-akademi/

## Eğitim içeriği

- 0–60 ay için 10 gelişimsel yaş grubu, genel uyku aralıkları ve dönemsel öğrenme hedefleri
- 12 ayrıntılı ders: uyku biyolojisi, güvenli uyku, yenidoğan, farklı yaş dönemleri, gündüz/gece uykusu, davranışsal müdahaleler, özel durumlar, araştırma okuryazarlığı
- 11 ayrıntılı makale, deney ve rehber değerlendirmesi; 4 tez/tez literatürü değerlendirmesi
- Gözlenen araştırma verilerini, klinik önerileri ve temsili şemaları ayıran grafikler
- Yedi günlük yerel uyku günlüğü, 6 eğitim vakası, ders sınavları, yerel öğrenme ilerlemesi
- PubMed ve ClinicalTrials.gov üzerinden otomatik güncellenen **yalnızca bibliyografik** araştırma kataloğu

## Dosyalar

- `index.html` — yeni akademi ana sayfası
- `akademi.html` — aynı uygulamaya alternatif doğrudan giriş
- `assets/akademi.css` — duyarlı tasarım
- `assets/akademi-data.js` — kaynaklı dersler, araştırmalar, tezler ve vaka içerikleri
- `assets/akademi.js` — filtreler, öğrenme, grafikler ve yerel uyku günlüğü
- `BILIMSEL_KAYNAKLAR.md` — yöntem, veri provenansı ve bilimsel şeffaflık
- `eski-egitim.html` — ilk sürüm eğitim arşivi
- `yas-egitimi.html`, `atlas.html`, `makale-akademisi.html`, `danisma.html` — önceki yardımcı eğitim sayfaları
- `data/research.json` — otomatik bibliyografik meta veriler

## Teknik işletim

GitHub Pages, `.github/workflows/pages.yml` ile `main` dalından yayınlanır. Günlük meta veri taraması `.github/workflows/research.yml` ve `scripts/sync_research.py` üzerinden yürür.

Kullanıcının işaretlediği dersler ve uyku günlüğü yalnızca tarayıcı yerel depolama alanına yazılır. Çerez veya veritabanı gerektiren bir sağlık profili sunucusu bulunmaz.

## Klinik sınırlar

Bu platform bilgilendirme ve öğrenme amaçlıdır; bireysel tıbbi tanı veya tedavi hizmeti değildir. Uyku ve beslenme programları özellikle 0–3 ayda katı klinik reçete olarak sunulmaz. Tez künye ve özetlerinin doğrulama seviyeleri `BILIMSEL_KAYNAKLAR.md` dosyasında açıkça belirtilir.
