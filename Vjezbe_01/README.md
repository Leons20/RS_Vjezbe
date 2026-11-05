# TaskFlow – Asinkrono dohvaćanje podataka

## 1. Opis projekta

Projekt simulira dohvaćanje podataka iz triju različitih vanjskih izvora pomoću Pythona i biblioteke `asyncio`.

Simuliraju se sljedeći izvori podataka:

- **Zadaci (`fetch_tasks`)** – dohvaća popis zadataka koji sadrži identifikator, naziv, status dovršenosti i prioritet.
- **Korisnici (`fetch_users`)** – dohvaća popis korisnika s njihovim identifikatorima, imenima, ulogama i statusom aktivnosti.
- **Statistika (`fetch_statistics`)** – dohvaća statističke podatke o zadacima, uključujući ukupan broj zadataka, broj dovršenih i nedovršenih zadataka, postotak dovršenosti i prosječno vrijeme završetka.

Svaki izvor simulira mrežno čekanje pomoću `asyncio.sleep()`, pri čemu je trajanje čekanja nasumično odabrano između 1 i 3 sekunde.

Nakon dohvaćanja podaci se objedinjuju u jednu strukturu koja sadrži tri skupine: `tasks`, `users` i `statistics`. Konkurentno dohvaćeni podaci spremaju se u datoteku `frontend/public/podaci.json`, a zatim se prikazuju u Vue 3 aplikaciji TaskFlow.

## 2. Vremena čekanja

Za ponovljivost rezultata korišten je `random.seed(42)`.

| Izvor podataka | Funkcija           | Vrijeme čekanja |
| -------------- | ------------------ | --------------: |
| Zadaci         | `fetch_tasks`      |          2,28 s |
| Korisnici      | `fetch_users`      |          1,05 s |
| Statistika     | `fetch_statistics` |          1,55 s |

## 3. Usporedba sekvencijalnog i konkurentnog izvođenja

### Sekvencijalno izvođenje

U sekvencijalnoj verziji svaka se asinkrona funkcija poziva i čeka prije nego što započne sljedeća. Zbog toga se vremena čekanja zbrajaju.

Očekivano ukupno vrijeme:

**2,28 + 1,05 + 1,55 = 4,88 sekundi**

### Konkurentno izvođenje

U konkurentnoj verziji koristi se `asyncio.gather()`, koji omogućuje pokretanje više asinkronih operacija bez čekanja da se svaka pojedinačno završi.

Budući da se operacije čekanja odvijaju istovremeno, ukupno vrijeme približno odgovara najduljem pojedinačnom čekanju.

Očekivano ukupno vrijeme:

**2,28 sekundi**

### Izmjerena vremena izvođenja

Vrijednosti u tablici dobivene pokretanjem programa pomoću `time.perf_counter()`.

| Način izvođenja | Izmjereno vrijeme |
| --------------- | ----------------: |
| Sekvencijalno   |            4,90 s |
| Konkurentno     |            2,29 s |

Konkurentno izvođenje u ovom primjeru je znatno brže jer se vrijeme čekanja različitih izvora preklapa.

## 4. Odgovori na teorijska pitanja

### Zašto se koristi `asyncio.sleep()`, a ne `time.sleep()`?

`asyncio.sleep()` je asinkrona funkcija koja privremeno zaustavlja izvođenje trenutačne korutine i prepušta kontrolu event loopu. Dok jedna korutina čeka, event loop može pokrenuti ili nastaviti izvođenje drugih korutina.

`time.sleep()` blokira cijelu dretvu u kojoj se izvršava. Ako se koristi unutar asinkrone funkcije, blokira event loop i sprječava druge korutine da se izvršavaju tijekom čekanja.

Zbog toga je za simulaciju mrežnog čekanja u asinkronom programu prikladniji `asyncio.sleep()`.

### Što je event loop?

Event loop je mehanizam koji upravlja izvođenjem asinkronih operacija. On prati korutine i odlučuje koju će nastaviti izvršavati kada neka od njih čeka na rezultat operacije.

Kada korutina naiđe na `await`, može prepustiti kontrolu event loopu. Event loop tada može nastaviti izvršavanje druge korutine koja je spremna za rad.

### Kako funkcionira `asyncio.gather()`?

`asyncio.gather()` prima više korutina i omogućuje njihovo konkurentno izvođenje. Rezultate vraća tek kada se sve predane korutine završe.

Rezultati su uvijek poredani prema redoslijedu argumenata predanih funkciji `asyncio.gather()`, a ne prema redoslijedu kojim su korutine završile izvođenje.

### Mijenja li promjena redoslijeda argumenata u `asyncio.gather()` redoslijed rezultata?

Da. Redoslijed rezultata prati redoslijed argumenata.

Primjerice:

- `asyncio.gather(fetch_tasks(), fetch_users(), fetch_statistics())` vraća rezultate redom: zadaci, korisnici, statistika.
- `asyncio.gather(fetch_statistics(), fetch_tasks(), fetch_users())` vraća rezultate redom: statistika, zadaci, korisnici.
- `asyncio.gather(fetch_users(), fetch_statistics(), fetch_tasks())` vraća rezultate redom: korisnici, statistika, zadaci.

Redoslijed završetka korutina ne utječe na redoslijed rezultata.

## 5. Zaključak

Primjer pokazuje prednost asinkronog konkurentnog izvođenja kod operacija koje uključuju čekanje, kao što su dohvaćanje podataka s vanjskih izvora.

Sekvencijalno izvođenje čeka završetak svake operacije prije pokretanja sljedeće, dok konkurentno izvođenje omogućuje preklapanje vremena čekanja. Zbog toga je konkurentni pristup učinkovitiji u ovom primjeru.

Objedinjeni podaci spremaju se u JSON datoteku i prikazuju u frontend aplikaciji TaskFlow.

### URL frontend aplikacije

https://rs-vjezbe-1-frontend-83sb.onrender.com
