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


## Arbetssätt (Agilt)

- `main` måste vara skyddad – alla ändringar görs i egna branches och slås ihop via Pull Requests.
- Varje PR granskas av minst en annan gruppmedlem innan den mergas.
- Varje medlem ansvarar främst för en modul i `src/` för att undvika merge-konflikter.
- Vi kan komma att använda **GitHub Issues** och **GitHub Projects** för att planera och följa upp arbetet på ett agilt sätt:
    - **Issues** – varje arbetsuppgift (t.ex. en funktion i `metrics.py`, ett diagram eller en del av rapporten) skapas som en issue med en kort beskrivning och tilldelas en ansvarig gruppmedlem.
    - **Projects (Kanban-tavla)** – issues läggs på en projekttavla med kolumnerna *Att göra*, *Pågår*, *Granskas* och *Klart*, så att alla i gruppen ser vad som är på gång.
    - **Koppling till Pull Requests** – en PR länkas till sin issue (t.ex. `Closes #3` i PR-beskrivningen), så stängs issuen automatiskt när PR:en mergas.
    - **Korta avstämningar** – vi stämmer av tavlan regelbundet, fördelar nya uppgifter och lyfter eventuella hinder.


## Gruppmedlemmar och ansvarsområden (Detta är bara ett exempel; den korrekta strukturen kommer att fastställas genom omröstning.)

** Grundläggande uppsättning/förarbete:**
| Namn | Ansvarsområde | Status |
|------|---------------|--------|
| Sherif Khairallah | Repo, miljö, README | klar |

** Arbetsuppgifter:**
| Namn | Analysfråga | Status |
|------|-------------|--------|
| _Edvin_ | Vad säljer vi? | ÖPPNA |
| _Ona_ | Var säljer vi? |  ÖPPNA |
| _Sherif_ | När säljer vi? | klar |
| _Bezabeh_ | Hur ser en typisk order ut? | ÖPPNA |
| _Henrik_ | Topp-listor  | ÖPPNA |
| _Mahmoud_ | Eventuella avvikelser | ÖPPNA |

Obs. 
1) Detta ska fastställas och senare uppdateras. Var och en kommer att ange sitt namn och sin roll eller sitt ansvarsområde i enlighet med vad vi kommit överens om vid det veckomöte vi ska hålla.

2) En filansvarig för de delade filerna betyder inte att filansvarig skriver all kod utan bara håller filen konsekvent (namngivning, docstrings, inga dubbletter av funktioner) och granskar PR som rör den.


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

| Nyckeltal | Definition | Används för |
|-----------|------------|-------------|
| **Total intäkt** | Summan av `revenue` | Totalnivå, per kategori/stad/period |
| **Antal ordrar** | Antal unika `order_id` | Efterfrågan per period |
| **AOV** (Average Order Value) | Total intäkt / antal ordrar | Hur stor en typisk order är |
| **Förändring mot föregående månad (MoM %)** | (månad − föregående månad) / föregående månad × 100 | Trender och dippar |
| **Andel av intäkt** | Gruppens intäkt / total intäkt | T.ex. städernas betydelse |
| **Sålda enheter** | Summan av `units` | Volym per kategori/stad |

Här följer nyckeltal värdena (från notebooken, efter lätt städning):

- **Total intäkt & AOV & Förändring mot föregående månad (MoM %):**
månatliga intäkter och procentuell förändring från månad till månad (MoM %):
               sum     mean  count  pct_change
period                                        
2024-01  664083.32  1492.32    445         NaN
2024-02  548462.03  1536.31    357       -17.4
2024-03  487602.00  1186.38    411       -11.1
2024-04  580194.83  1343.04    432        19.0
2024-05  632165.16  1459.97    433         9.0
2024-06  590259.89  1398.72    422        -6.6

- **Total antal orders:** 2500
- **Genomsnittlig sålda enheter:** 2.99

- ** Andel av intäkt & Sålda enheter (per kategori/stad):**



### Figurer
