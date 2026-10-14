#35. Print multiplication tables from 1 to 5.

for t in range(1, 6):
    print(f"--- Table {t} ---")
    for i in range(1, 11):
        print(f"{t} x {i} = {t * i}")