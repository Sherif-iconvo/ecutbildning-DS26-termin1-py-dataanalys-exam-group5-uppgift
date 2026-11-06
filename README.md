# ecutbildning-DS26-termin1-py-dataanalys-exam-group5-uppgift

Grupp 5 – Examinerande gruppuppgift i kursen *Pythonprogrammering och statistisk dataanalys* (DS26) på EC Utbildning. E-handel: kampanjanalys och beslutsunderlag med nyckeltal.

## Om projektet

Vi är analysteamet på en fiktiv e-handelsplattform. Ledningen vill ha ett snabbt och reproducerbart beslutsunderlag inför nästa kampanjperiod. Rapport-notebooken besvarar:

1. **Vad säljer?** – vilka kategorier driver mest intäkt
2. **Var säljer vi?** – vilka städer står för störst intäkt
3. **När säljer vi?** – tidsmönster under den observerade perioden
4. **Hur ser en typisk order ut?** – AOV (Average Order Value) och spridning
5. **Topp-listor** – topp-3 kategorier efter intäkt
6. **Avvikelser** – oväntade mönster som sticker ut

Notebooken avslutas med rubriken **Rekommendationer** med 2–3 rekommendationer baserade på resultaten.

**Dataset:** `../data/ecommerce_sales.csv`
Kolumner: `order_id`, `date`, `city`, `category`, `price`, `units`, `revenue`

## Projektstruktur

```
├── data/
│   └── ecommerce_sales.csv     # rådata
├── notebooks/
│   └── report.ipynb            # rapporten – importerar från src/ och visar resultaten
├── src/
│   ├── io_utils.py             # funktioner för att läsa in data
│   ├── metrics.py              # funktioner för nyckeltal
│   ├── viz.py                  # funktioner för diagram
│   └── ecommerce.py            # klassen EcommerceAnalyzer
├── requirements.txt
└── README.md
```

## Så kör du projektet

1. **Klona repot**
   ```bash
   git clone https://github.com/Sherif-iconvo/ecutbildning-DS26-termin1-py-dataanalys-exam-group5-uppgift.git
   
   ```

2. **Skapa och aktivera en virtuell miljö**
   ```bash
   python -m venv .venv
   ```
   - Git Bash: `source .venv/Scripts/activate`

3. **Installera beroenden**
   ```bash
   pip install -r requirements.txt
   ```
4. **Kör rapporten**
   Öppna notebooks/report.ipynb i VS Code eller Jupyter Notebook och kör alla celler i ordning. Se till att projektets virtuella miljö är vald som Python-kernel.


## Arbetssätt (Agilt)

- `main` måste vara skyddad – alla ändringar görs i egna branches och slås ihop via Pull Requests.
- Varje PR granskas av minst en annan gruppmedlem innan den mergas.
- Varje medlem ansvarar främst för en modul i `src/` för att undvika merge-konflikter.
- Vi kan komma att använda **GitHub Issues** och **GitHub Projects** för att planera och följa upp arbetet på ett agilt sätt:
    - **Issues** – varje arbetsuppgift (t.ex. en funktion i `metrics.py`, ett diagram eller en del av rapporten) skapas som en issue med en kort beskrivning och tilldelas en ansvarig gruppmedlem.
    - **Projects (Kanban-tavla)** – issues läggs på en projekttavla med kolumnerna *Att göra*, *Pågår*, *Granskas* och *Klart*, så att alla i gruppen ser vad som är på gång.
    - **Koppling till Pull Requests** – en PR länkas till sin issue (t.ex. `Closes #3` i PR-beskrivningen), så stängs issuen automatiskt när PR:en mergas.
    - **Korta avstämningar** – vi stämmer av tavlan regelbundet, fördelar nya uppgifter och lyfter eventuella hinder.


## Gruppmedlemmar och ansvarsområden

** Grundläggande uppsättning/förarbete:**
| Namn | Ansvarsområde | Status |
|------|---------------|--------|
| Sherif Khairallah | Repo, miljö, README | klar |

** Arbetsuppgifter:**
| Namn | Analysfråga | Status |
|------|-------------|--------|
| _Edvin_ | Vad säljer vi? | Klar |
| _Ona_ | Var säljer vi? |  Klar|
| _Sherif_ | När säljer vi? | klar |
| _Bezabeh_ | Hur ser en typisk order ut? | Klar |
| _Henrik_ | Topp-listor  | Klar |
| _Mahmoud_ | Eventuella avvikelser | Klar |


## Miljö

- **Python:** 3.14 (utvecklat och testat med Python 3.14.7)
- **Paket:** alla med exakta versioner i `requirements.txt`. De viktigaste:

| Paket | Version | Används till |
|-------|---------|--------------|
| pandas | 3.0.6 | inläsning, rensning och beräkning av nyckeltal |
| numpy | 2.5.4 | numeriska beräkningar (t.ex. konsistenskontroll av intäkt) |
| matplotlib | 3.11.2 | diagram i `src/viz.py` |
| jupyter / ipykernel | 1.1.1 / 7.4.0 | köra `notebooks/report.ipynb` |

Installera allt med `pip install -r requirements.txt` (se *Så kör du projektet*).


## Nyckeltal

Alla nyckeltal beräknas i `src/metrics.py` på den rensade datan och nås via klassen `EcommerceAnalyzer`.

| Nyckeltal | Definition | Används för | Resultat |
|-----------|------------|-------------|----------|
| **Total intäkt** | Summan av `revenue` | Totalnivå | 3 502 767,23 SEK
| **Antal ordrar** | Antal unika `order_id` | Överblick om totala ordrar | 2500 stycken
| **AOV** (Average Order Value) | Total `revenue` / antal `order_id` | Hur stor en typisk order är | 1 401,11 SEK
| **Förändring mot föregående månad (MoM %)** | (månad − föregående månad) / föregående månad × 100 | Trender och dippar | Se nedan
| **Topp 2 stad efter intäkt** | Summan av `revenue` per stad | Se hur städerna presterar |Stockholm: 1 227 201,94 SEK, Göteborg: 859 019,65 SEK
| **Genomsnittlig sålda enheter** | Summa av `units` / Summan av `order_id` | Se snittet av enhter per order | 2.99 stycken
| **Topp 3 kategori efter intäkt** | Summan `revenue` per `category` | Vilka kategorier som har presterat bäst| Elektronik: 1 364 228,07 SEK, Sports: 734 653,42 SEK, Clothing: 586 744,91
| **Antal avvikande värden** | IQR beräkning | Se hur mycket ordrar som är utanför vår snittorder | 111 stycken


Här följer nyckeltal värdena (från notebooken, efter lätt städning):

- **Förändring mot föregående månad (MoM %):**
månatliga intäkter och procentuell förändring från månad till månad (MoM %):
               sum     mean  count  pct_change
period                                        
2024-01  664083.32  1492.32    445         NaN
2024-02  548462.03  1536.31    357       -17.4
2024-03  487602.00  1186.38    411       -11.1
2024-04  580194.83  1343.04    432        19.0
2024-05  632165.16  1459.97    433         9.0
2024-06  590259.89  1398.72    422        -6.6


# Vårt förslag till ledningen: 

Under perioden 1 januari – 30 juni 2024 omsatte e-handeln 3 502 767 SEK fördelat på 2 500 ordrar.
 
- Insikt A – Elektronik driver verksamheten, med stora ordrar:**
 
- Insikt B – Ordervärdet, inte antalet ordrar, avgör starka och svaga perioder:
 
- Insikt C – Stark koncentration till storstäderna: Stockholm och Göteborg är de två största marknaderna .
 
## Rekommendationer
 
1. Prioritera Stockholm och Göteborg. Dessa städer står för cirka 60 % av de totala intäkterna och bör prioriteras vid framtida marknadsföring. Dessa städer står för cirka 60 % av de totala intäkterna och bör prioriteras vid framtida marknadsföring

2. Höj ordervärdet i svaga perioder (mars och helger) - Paketerbjudanden, tillbehörsförslag i kassan och en tröskel för fri frakt strax över medianordern (1 089 SEK).

3. Planera kampanjer efter kategoriernas starka månader - Elektronikkampanjer i januari–februari, kläder i april och sport inför sommaren.
 
4. Utred de avvikande ordrarna (111 ordrar (4,4 %) är avvikande enligt IQR-metoden) i stället för att ta bort dem. Var kommer de ifrån?

*Begränsning:* Analysen bygger på sex månaders data utan kostnader eller marginaler, så vi kan inte avgöra om mönstren är säsongsbundna eller vilken lönsamhet åtgärderna ger. Åtgärderna bör därför testas och utvärderas med nyckeltalen ovan.

### Figurer
Rapporten innehåller flera visualiseringar bland annat stapeldiagram över intäkter per kategori och stad, försäljning över tid samt boxplot för att identifiera avvikande värden.
Samtliga diagram med tillhörande analyser och förklaringar finns i notebooks/report.ipynb