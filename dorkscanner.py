
import time
import random
import urllib.parse
import undetected_chromedriver as uc

def read_dorks(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def google_search(driver, dork):
    try:
        query = urllib.parse.quote(dork)
        driver.get(f"https://www.google.com/search?q={query}")
        time.sleep(random.uniform(3, 6))

        results = driver.find_elements("css selector", "div#search .tF2Cxc")
        links = []
        for res in results:
            try:
                link = res.find_element("tag name", "a").get_attribute("href")
                print(f"[+] {link}")
                links.append(link)
            except:
                continue

        return links
    except Exception as e:
        print(f"[!] Fehler: {e}")
        return []

if __name__ == "__main__":
    try:
        options = uc.ChromeOptions()
        options.headless = False
        driver = uc.Chrome(options=options)

        dorks = read_dorks('dorks.txt')
        with open('results.txt', 'w') as output:
            for dork in dorks:
                print(f"[*] Suche nach: {dork}")
                results = google_search(driver, dork)
                for link in results:
                    output.write(f"{dork}: {link}\n")
                time.sleep(random.uniform(10, 20))

    except KeyboardInterrupt:
        print("\n[!] Script durch Nutzer abgebrochen (Strg + C). Alles wird sauber beendet.")

    finally:
        driver.quit()
