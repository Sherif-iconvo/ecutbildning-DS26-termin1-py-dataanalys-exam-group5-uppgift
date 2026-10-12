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

**Dataset:** `data/ecommerce_sales.csv`
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

## Krav

- **Python 3.14** (utvecklat med Python 3.14.7)
- Paketen i `requirements.txt` (främst pandas, matplotlib, jupyter/ipykernel, seaborn, numpy)

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

| Namn | Ansvarsområde |
|------|---------------|
| Sherif Khairallah | Uppsättning av repo, miljö och requirements, README | KLAR
| _Namn_ | _t.ex. `io_utils.py` – inläsning av data och datakvalitet_ | ÖPPNA
| _Namn_ | _t.ex. `metrics.py` – nyckeltalsfunktioner_ | ÖPPNA
| _Namn_ | _t.ex. `viz.py` – visualiseringar_ |  ÖPPNA
| _Namn_ | _t.ex. `ecommerce.py` / rapport-notebook_ | ÖPPNA

Obs. Detta ska fastställas och senare uppdateras. Var och en kommer att ange sitt namn och sin roll eller sitt ansvarsområde i enlighet med vad vi kommit överens om vid det veckomöte vi ska hålla.
