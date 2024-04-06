<h1 align="center">🎖️ ALGOLAB SONUÇLARI NASIL HESAPLANIR?🎖️</h1>

<a href="https://ituro-algolab-results.streamlit.app/" target="_blank"><img src="https://github.com/iturobotolympics/AlgoLAB/assets/151058538/6cfb360a-7d16-4302-9dec-c4b9f288b3b5" width="1400" /></a>

🌐 AlgoLAB sonuçlarını hesaplayabileceğiniz siteye yukarıdaki görsele tıklayarak gidebilirsiniz.

➡️ AlgoLAB kategorisinde bir problem için yazılan algoritma, aşağıda belirtilen kriterlere ve ağırlıklara göre puanlandırılır:
- Kriter-1 (%65): Probleme özel olarak hazırlanmış değerlendirme testleri
- Kriter-2 (%35): Yazılan algoritmanın boyutu

➡️ Bir yarışmacının bir problemden aldığı puan hesaplanmadan önce bir ön işleme gerçekleştirilir. Bunun için, tüm yarışmacıların o problemin çözümü olarak yazdıkları kodların boyutu [0, 100] aralığına eşlenir. Boyutu daha kısa olan kodun puanının daha yüksek olması gerektiği için ters orantılı bir eşleme yapılır. Kategoriye 5 yarışmacının katıldığı senaryoda örnek olarak yarışmacıların ilk problem için yazdıkları kodların boyutu ve eşlenmiş karşılıkları aşağıdaki tabloda verilmiştir:

   YARIŞMACI   |   GERÇEK KOD BOYUTU   |   EŞLENMİŞ PUAN
:-------------:|:---------------------:|:-----------------:
Yarışmacı-1    | 25                    | 100
Yarışmacı-2    | 47                    | 75.28
Yarışmacı-3    | 114                   | 0
Yarışmacı-4    | 86                    | 31.46
Yarışmacı-5    | 63                    | 57.3

➡️ Bu ön işlem gerçekleştirildikten sonra bir yarışmacının $i.$ problemden aldığı puan aşağıdaki gibi hesaplanır:
- $S_{P_{i}} = 0.65 \times S_{K_{1}} + 0.35 \times S_{K_{2}}, \quad$ $S_{K_{j}}: j.$ kriterden alınan puan

➡️ Problemler, aşağıda belirtildiği gibi kolaydan zora doğru ağırlıklandırılır:
- Problem-1: %5
- Problem-2: %10
- Problem-3: %20
- Problem-4: %25
- Problem-5: %40

➡️ Sonuç olarak, bir yarışmacının aldığı toplam skor aşağıda verildiği gibi hesaplanır:
$S_{T} = 0.05 \times S_{P_{1}} + 0.1 \times S_{P_{2}} + 0.2 \times S_{P_{3}} + 0.25 \times S_{P_{4}} + 0.4 \times S_{P_{5}}$.
