import asyncio

# Korutina timer() definirana je, ali još nije pokrenuta
# Stanje korutine: CREATED

async def timer(name, delay):
    for i in range(delay, 0, -1):

        # Korutina se trenutačno izvršava
        # Stanje: RUNNING
        print(f'{name}: {i} sekundi preostalo...')

        # Korutina nailazi na await i privremeno zaustavlja izvršavanje
        # Stanje korutine: SUSPENDED
        # Event loop za to vrijeme može izvršavati druge korutine
        await asyncio.sleep(1)

        # Nakon 1 sekunde korutina nastavlja izvršavanje
        # Stanje: RUNNING

    # Odbrojavanje je završilo i ispisuje se završna poruka
    print(f'{name}: Vrijeme je isteklo!')

    # Korutina je završila izvršavanje
    # Stanje: CLOSED


async def main():

    # Stvaramo tri Task objekta
    # create_task() raspoređuje korutine za izvršavanje
    # Stanje Task objekata: PENDING

    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    # gather() čeka završetak svih triju zadataka
    # Dok jedan zadatak čeka (SUSPENDED), drugi se mogu izvršavati
    await asyncio.gather(*timers)

    # Kada svi timere završe:
    # Stanje svih Task objekata: DONE
    # Korutina main() nastavlja izvršavanje i završava


# asyncio.run() pokreće event loop i izvršava main()
asyncio.run(main())

# Nakon završetka svih zadataka event loop se zatvara
# Ukupno trajanje programa je približno 7 sekundi