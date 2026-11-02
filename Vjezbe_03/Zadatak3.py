import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)

    if korisnik['lozinka'] == lozinka:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    await asyncio.sleep(3)

    for k in baza_korisnika:
        if (k['korisnicko_ime'] == korisnik['korisnicko_ime']
                and k['email'] == korisnik['email']):

            for l in baza_lozinka:
                if l['korisnicko_ime'] == korisnik['korisnicko_ime']:
                    return await autorizacija(l, korisnik['lozinka'])

    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."


async def main():
    korisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'
    }

    rezultat = await autentifikacija(korisnik)
    print(rezultat)


asyncio.run(main())