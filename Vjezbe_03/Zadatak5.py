import asyncio

async def secure_data(podaci):
    await asyncio.sleep(3)

    enkriptirani_podaci = {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }

    return enkriptirani_podaci


async def main():
    osjetljivi_podaci = [
        {'prezime': 'Horvat', 'broj_kartice': '1234567890123456', 'CVV': '123'},
        {'prezime': 'Novak', 'broj_kartice': '9876543210987654', 'CVV': '456'},
        {'prezime': 'Kovac', 'broj_kartice': '1111222233334444', 'CVV': '789'}
    ]

    zadaci = [
        asyncio.create_task(secure_data(podaci))
        for podaci in osjetljivi_podaci
    ]

    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)


asyncio.run(main())