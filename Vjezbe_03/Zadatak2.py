import asyncio

async def dohvati_korisnike():
    await asyncio.sleep(3)
    korisnici = [
        {"ime": "Marko", "godine": 25},
        {"ime": "Ana", "godine": 30}
    ]
    return korisnici

async def dohvati_proizvode():
    await asyncio.sleep(5)
    proizvodi = [
        {"naziv": "Laptop", "cijena": 1000},
        {"naziv": "Mobitel", "cijena": 500}
    ]
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(
        dohvati_korisnike(),
        dohvati_proizvode()
    )

    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

asyncio.run(main())