
# OSINT Google Dorks Automation Tool (mit Chrome)

Ein kleines Python-Tool, um Google Dorks halbautomatisiert auszuführen und die gefundenen Links in eine Datei zu speichern.  
Das Tool nutzt **Chrome (über undetected-chromedriver)** und führt die Abfragen **sichtbar im Browser aus**.

---

## Features
- Führt Google-Dork-Suchen sichtbar im Chrome-Browser aus.
- Extrahiert alle Treffer-Links automatisch.
- Speichert alle Ergebnisse in `results.txt`.
- Simuliert menschliches Verhalten (Delays).

---

## Voraussetzungen
- Python 3.x
- Google Chrome (muss lokal installiert sein)
- Virtuelle Umgebung empfohlen

---

## Setup

1. Virtuelle Umgebung anlegen:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

---

## Nutzung

1. Trage deine Dorks in `dorks.txt` ein (eine Zeile pro Dork).
2. Starte das Tool:
```bash
python dorkscanner.py
```

3. Es öffnet sich ein **sichtbares Chrome-Fenster**, die Dork-Abfrage wird ausgeführt.
4. Gefundene Links werden:
    - Im Terminal angezeigt.
    - In `results.txt` gespeichert.

---

## Hinweise
- **Das Chrome-Fenster bleibt während der Abfrage offen.**  
- Dass die Dork-Suchanfragen wie z.B. `intitle:index of passwd` in der Suchleiste erscheinen, ist **normal und korrekt**.
- Dieses Tool ist nur zu Lern- und Forschungszwecken gedacht. Exzessives Scraping kann gegen die Nutzungsbedingungen von Google verstoßen.
