from pathlib import Path
import asyncio, random, time, json

output_dir = Path("RS_Vjezbe/Vjezbe_01/frontend/public")
output_dir.mkdir(parents=True, exist_ok=True)

async def fetch_tasks(delay):
    print("[Zadaci] Početak dohvaćanja...")
    await asyncio.sleep(delay)

    tasks = [
        {"id": 1, "title": "Izraditi početnu stranicu",
         "done": True, "priority": "Visoki"},
        {"id": 2, "title": "Povezati frontend i backend",
         "done": True, "priority": "Visoki"},
        {"id": 3, "title": "Dodati autentifikaciju",
         "done": False, "priority": "Srednji"},
        {"id": 4, "title": "Testirati API",
         "done": False, "priority": "Niski"}
    ]

    print("[Zadaci] Dohvaćanje završeno.")
    return tasks


async def fetch_users(delay):
    print("[Korisnici] Početak dohvaćanja...")
    await asyncio.sleep(delay)

    users = [
        {"id": 1, "name": "Ana Horvat",
         "role": "Administrator", "active": True},
        {"id": 2, "name": "Marko Kovač",
         "role": "Korisnik", "active": True},
        {"id": 3, "name": "Ivana Marić",
         "role": "Korisnik", "active": False}
    ]

    print("[Korisnici] Dohvaćanje završeno.")
    return users


async def fetch_statistics(delay):
    print("[Statistika] Početak dohvaćanja...")
    await asyncio.sleep(delay)

    statistics = {
        "total_tasks": 4,
        "completed_tasks": 2,
        "pending_tasks": 2,
        "completion_percentage": 50,
        "average_completion_time": "2 dana"
    }

    print("[Statistika] Dohvaćanje završeno.")
    return statistics


async def sequential_execution(delays):
    print("\n=== SEKVENCIJALNO IZVRŠAVANJE ===")

    tasks = await fetch_tasks(delays["tasks"])
    users = await fetch_users(delays["users"])
    statistics = await fetch_statistics(delays["statistics"])

    return {
        "tasks": tasks,
        "users": users,
        "statistics": statistics
    }


async def concurrent_execution(delays):
    print("\n=== KONKURENTNO IZVRŠAVANJE ===")

    tasks, users, statistics = await asyncio.gather(
        fetch_tasks(delays["tasks"]),
        fetch_users(delays["users"]),
        fetch_statistics(delays["statistics"])
    )

    return {
        "tasks": tasks,
        "users": users,
        "statistics": statistics
    }


async def test_order_1(delays):
    print("\n=== TEST 1: Zadaci, Korisnici, Statistika ===")

    return await asyncio.gather(
        fetch_tasks(delays["tasks"]),
        fetch_users(delays["users"]),
        fetch_statistics(delays["statistics"])
    )


async def test_order_2(delays):
    print("\n=== TEST 2: Statistika, Zadaci, Korisnici ===")

    return await asyncio.gather(
        fetch_statistics(delays["statistics"]),
        fetch_tasks(delays["tasks"]),
        fetch_users(delays["users"])
    )


async def test_order_3(delays):
    print("\n=== TEST 3: Korisnici, Statistika, Zadaci ===")

    return await asyncio.gather(
        fetch_users(delays["users"]),
        fetch_statistics(delays["statistics"]),
        fetch_tasks(delays["tasks"])
    )


async def main():

    random.seed(42)

    delays = {
        "tasks": random.uniform(1, 3),
        "users": random.uniform(1, 3),
        "statistics": random.uniform(1, 3)
    }

    print("Vremena čekanja:")
    for source, delay in delays.items():
        print(f"{source}: {delay:.2f} sekunde")

    t1 = time.perf_counter()
    sequential_results = await sequential_execution(delays)
    t2 = time.perf_counter()

    sequential_time = t2 - t1

    t3 = time.perf_counter()
    concurrent_results = await concurrent_execution(delays)
    t4 = time.perf_counter()

    concurrent_time = t4 - t3

    with open(output_dir / "podaci.json", "w", encoding="utf-8") as file:
        json.dump(concurrent_results, file, ensure_ascii=False, indent=4)

    print("\nPodaci su spremljeni u frontend/public/podaci.json")

    t5 = time.perf_counter()
    order_1_results = await test_order_1(delays)
    t6 = time.perf_counter()

    order_1_time = t6 - t5

    t7 = time.perf_counter()
    order_2_results = await test_order_2(delays)
    t8 = time.perf_counter()

    order_2_time = t8 - t7

    t9 = time.perf_counter()
    order_3_results = await test_order_3(delays)
    t10 = time.perf_counter()

    order_3_time = t10 - t9

    results = {
        "sequential": {
            "execution_time": sequential_time,
            "data": sequential_results
        },
        "concurrent": {
            "execution_time": concurrent_time,
            "data": concurrent_results
        },
        "order_1": {
            "execution_time": order_1_time,
            "data": order_1_results
        },
        "order_2": {
            "execution_time": order_2_time,
            "data": order_2_results
        },
        "order_3": {
            "execution_time": order_3_time,
            "data": order_3_results
        }
    }

    print("\n=== USPOREDBA IZVRŠAVANJA ===")

    print(f"Sekvencijalno vrijeme: {sequential_time:.2f} sekunde")
    print(f"Konkurentno vrijeme: {concurrent_time:.2f} sekunde")

    print("\n=== USPOREDBA RAZLIČITOG REDOSLIJEDA ===")

    print(f"Test 1: {order_1_time:.2f} sekunde")
    print(f"Test 2: {order_2_time:.2f} sekunde")
    print(f"Test 3: {order_3_time:.2f} sekunde")

    print("\n=== REDOSLIJED VRAĆENIH REZULTATA ===")

    print("Test 1: Zadaci, Korisnici, Statistika")
    print("Test 2: Statistika, Zadaci, Korisnici")
    print("Test 3: Korisnici, Statistika, Zadaci")

    print("\n=== REZULTATI ===")
    print(results)

    return results


if __name__ == "__main__":
    results = asyncio.run(main())