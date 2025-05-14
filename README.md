
# OSINT Google Dorks Automation Tool (with Chrome)

A small Python tool to semi-automatically execute Google Dorks and save the found links into a file.  
The tool uses **Chrome (via undetected-chromedriver)** and performs the queries **visibly in the browser**.

---

## Features
- Executes Google Dork searches visibly in the Chrome browser.
- Automatically extracts all result links.
- Saves all results to `results.txt`.
- Simulates human-like behavior (delays).

---

## Requirements
- Python 3.x
- Google Chrome (must be installed locally)
- Virtual environment recommended

---

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

1. Add your Dorks to `dorks.txt` (one Dork per line).
2. Start the tool:
```bash
python dorkscanner.py
```

3. A **visible Chrome window** will open, and the Dork search will be performed.
4. Found links will be:
    - Displayed in the terminal.
    - Saved in `results.txt`.

---

## Notes
- **The Chrome window remains open during the search.**  
- Seeing Dork search queries like `intitle:index of passwd` in the search bar is **normal and expected**.
- This tool is intended for educational and research purposes only. Excessive scraping may violate Google's terms of service.
