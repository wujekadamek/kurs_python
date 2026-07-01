# 1. Uzyj modulu datetime, aby zapisac czas rozpoczecia pracy nad projektem
#    jako zmienna start_time
# 2. Symuluj prace nad projektem przez wywolanie time.sleep()
#    z losowo wybranym krotkim czasem (np. od 1 do 5 sekund)
# 3. Uzyj modulu datetime ponownie, aby zapisac czas zakonczenia pracy nad
#    projektem jako zmienna end_time
# 4. Oblicz laczny czas pracy nad projektem przez odjecie start_time od end_time
#    i wyswietl wynik.
# 5. Jesli laczny czas pracy przekracza 3 sekundy, wyswietl komunikat o duzej
#    ilosci wlozonego czasu, w przeciwnym razie poinformuj o krotkim czasie pracy.

import datetime
import time
import random

start_time = datetime.datetime.now()
print("Czas rozpoczecia zadania: ", start_time.strftime("%H:%M:%S %d.%m.%Y"))

sleep_time = random.randint(1,5)
time.sleep(sleep_time)

end_time = datetime.datetime.now()
print("Czas zakonczenia zadania: ", end_time.strftime("%H:%M:%S %d.%m.%Y"))

total_work_time = end_time - start_time
print("Czas pracy:", total_work_time)

if total_work_time.total_seconds() > 3:
    print("Duzo czasu wlozonego w projekt.")
else:
    print("Krotki czas pracy nad projektem.")