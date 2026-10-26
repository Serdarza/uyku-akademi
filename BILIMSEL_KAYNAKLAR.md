# Uyku Akademi — bilimsel içerik ve veri şeffaflığı
Son içerik gözden geçirme tarihi: **26 Ekim 2026**. Bu dosya editoryal kaynak eşlemesini belgeler; bağımsız tıbbi uzman hakemliği yapıldığı anlamına gelmez.

## İçerik kapsamı
- `assets/akademi-data.js`: 12 eğitim modülü, 10 gelişimsel yaş bandı, 11 araştırma/rehber incelemesi, 4 tez veya tez literatürü incelemesi, 6 kurgu vaka, bilimsel sözlük.
- `assets/akademi.js`: etkileşimli dersler, ilerleme, araştırma filtreleri, veriye dayalı grafikler ve kullanıcı tarafından girilen en son yedi uyku gününün görselleştirilmesi.
- `data/research.json`: PubMed ve ClinicalTrials.gov üzerinden otomatik güncellenen bibliyografik kayıtlar. **Bu kayıtlar otomatik olarak tam metin okunmuş, Türkçeye çevrilmiş veya uzman incelemesinden geçmiş sayılmaz.**
- `eski-egitim.html`: önceki eğitim sayfasının korunmuş arşivi.

## Grafiklerde veri türünün ayrılması

| Grafik | Sayılar | Anlamı | Kaynak |
|---|---|---|---|
| Uyku süresi bantları | 0–3 ay 14–17; 4–12 ay 12–16; 1–2 yaş 11–14; 3–5 yaş 10–13 saat | 24 saatlik **uzman önerileri** (bireysel gözlem değil) | [WHO 2019](https://www.ncbi.nlm.nih.gov/books/NBK541173/), [AASM 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4877308/) |
| Galland yaş grubu dağılımı | Bebek 12,8 (9,7–15,9); toddler/okul öncesi 11,9 (9,9–13,8); çocuk 9,2 (7,6–10,8) saat | 34 gözlemsel çalışmadaki yaş gruplarından türetilen ortalamalar ve ±1,96 SS **gözlemsel aralıklar**; öneri değil | [Galland ve ark. (2012)](https://pubmed.ncbi.nlm.nih.gov/21784676/) |
| Müdahale bileşenleri | %68 bağımsız dalma, %53 rutin, %47 uyku hijyeni; %49 gece süresi, %47 uyanma sonucu | 59 çalışma içinde ele alınan bileşen veya değerlendirilen sonuç sıklığı; **başarı oranı değil** | [Pétrin ve ark. (2026)](https://pubmed.ncbi.nlm.nih.gov/41996955/) |
| Randomize deney kolları | 14 / 15 / 14 bebek | Üç grubun örneklem büyüklüğü; **müdahale etkililiği ölçümü değil** | [Gradisar ve ark. (2016)](https://pubmed.ncbi.nlm.nih.gov/27221288/) |
| İki süreçli uyku ritmi | Nicel ölçek kullanılmıyor | **Kavramsal/temsili illüstrasyon**, araştırmada ölçülen veri değil | Eğitimsel açıklama |
| Kullanıcı günlüğü | Kullanıcının girdiği gece ve gündüz saatleri | Kullanıcının cihazında hesaplanan kişisel kayıt; rehber aralığına karşı **tanısal olmayan karşılaştırma** | Kullanıcı girdisi |

**Önemli:** AASM 2016, normal çeşitlilik ve sağlık sonucu kanıtlarının yetersizliği nedeniyle dört aydan küçük bebekler için ayrı konsensüs bandı belirlememiştir. İlk üç aylık 14–17 saatlik öneri WHO/NSF kaynaklıdır. WHO kılavuzundaki uyku süresi önerileri için kanıt niteliği çok düşük olarak değerlendirilmiştir. 12. ay iki konsensüs yaş aralığının sınırında yer aldığından bireysel gelişim bağlamında değerlendirilmelidir.

## Örnek araştırmalar ve editoryal sınırlılıklar

- [AASM Paruthi 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5078711/): yayımlanmış çalışmaların sistematik değerlendirmesi ve modifiye RAND konsensüsü. Bireysel yatış saati reçetesi değildir.
- [Mindell 2009](https://pubmed.ncbi.nlm.nih.gov/19480226/): 405 anne ve 7–36 aylık çocuklarla yatış rutini deneyi. Kısa dönem ve yöntem bağlamı önemlidir.
- [Gradisar 2016](https://pubmed.ncbi.nlm.nih.gov/27221288/): 6–16 ayda 43 bebeklik randomize deney. Sonuçlar ilk aylara genellenemez.
- [Price 2012](https://pubmed.ncbi.nlm.nih.gov/22966034/): müdahalenin beş yıllık izlemi; başlangıçta 326, izlemde 225 aile. İzlem kaybı ve istatistiksel güç dikkate alınmalı.
- [Reuter 2020](https://pubmed.ncbi.nlm.nih.gov/31965638/): 476 taranan kayıttan 12 çalışma; bazı kısa dönem etkiler mütevazı, bazı eğitim sonuçları tutarsız.
- [2023 aktigrafi derlemesi](https://pubmed.ncbi.nlm.nih.gov/37671613/): 11 müdahale çalışması; sadece ikisinde düşük yanlılık riski. Cihazla ölçüm otomatik hatasızlık sağlamaz.
- [Pétrin 2026](https://pubmed.ncbi.nlm.nih.gov/41996955/): 59 çalışma; gündüz uykuları gece sonuçlarına göre seyrek incelenmiş.
- [2024 davranışsal uykusuzluk derlemesi](https://pubmed.ncbi.nlm.nih.gov/38394890/): 21 araştırma ve 2.363 çocuk; yaş, yöntem ve tanı farklılıkları önemlidir.
- [AAP 2022](https://doi.org/10.1542/peds.2022-057990): bir yaş altında sırtüstü yatış başlangıcı, sert-düz ayrı yüzey, yumuşak nesnelerden uzak tutma, ilk altı ay oda paylaşımı gibi öneriler davranışsal amaçlardan önce gelir.

## Türkiye'den tez ve çalışmalar

1. [Gülsen Sırtbaş Işık, Hacettepe Üniversitesi, 2023](https://openaccess.hacettepe.edu.tr/items/03ec22ce-4be9-469a-8088-0495d97cc3c2): üniversite açık arşivi ve özetten doğrulanan, 81 prematüre bebeği içeren doktora tezi. Gelişim/uyku ilişkilerinin analizi; uyku eğitimi randomize deneyi değil.
2. [Emel Okur Fatih, Ankara Üniversitesi, 2023, YÖK 836922](https://tezara.org/theses/836922): YÖK künyesini aktaran üçüncü taraf tez özeti, sekiz haftalık aile eğitimi ve çok küçük uygulama grubu. **Tam metnin tüm yöntem ve ek tabloları bağımsız olarak incelenmiş değildir.**
3. [Esin Zeren, Bozok Üniversitesi, 2019, YÖK 576957](https://tezara.org/theses/576957): üçüncü taraf tez künyesi ve özet. Klinik güvenli uyku rehberinin yerini tutmaz.
4. [Bayram & Ergin 2025](https://dergipark.org.tr/tr/pub/cg/article/1577271): YÖK sisteminde incelenen 36 tez. Çalışmalar yalnız uykuyu değil, 0–3 yaşta beslenme, tuvalet ve diğer rutinleri de kapsar.
5. [Okur Fatih & Köksal Akyol 2020](https://dergipark.org.tr/tr/pub/ausbid/article/759561): altı anneyle nitel görüşmeler. Müdahale etkinliği veya Türkiye geneli yaygınlık tahmini değildir.

## Yayın ve güvenlik politikası
1. Klinik rehber, randomize deney, sistematik derleme, gözlemsel çalışma ve tezler görünür şekilde ayrılır.
2. İstatistiksel anlamlılık, klinik etkililik veya bireysel başarı olasılığıyla karıştırılmaz.
3. Örnek takvimler/illüstrasyonlar ölçülmüş klinik veri gibi sunulmaz.
4. Otomatik bibliyografik arşivden özet ve sonuç **uydurulmaz**.
5. Bebeklerde güvenli uyku, beslenme, büyüme ve prematürite gibi durumlar davranışsal hedeflerden önce değerlendirilir.
6. Acil solunum belirtisi, morarma, yanıtsızlık veya nöbette Türkiye'de **112**.
7. Web sitesi tanı koymaz, ilaç önermez veya hekim-ebeveyn klinik kararını ikame etmez.
