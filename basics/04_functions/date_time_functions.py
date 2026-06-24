import time
import datetime

ticks = time.time() # <-- liczy czas od 01.01.1970 00:00
print(ticks)

timeData = time.localtime()
print(timeData)
print(timeData.tm_year)

timeData = time.localtime(10) # <-- 10 sekund od 01.01.1970 00:00
print(timeData)
print(timeData.tm_year)

result = time.asctime(time.localtime())
print(result)

timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S", timeData))

timeStr = "21:37:00 02.04.2005"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)

i = 0
while i < 12:
    time.sleep(0.001)
    print(time.asctime(time.localtime()))
    i += 1

tStart = time.perf_counter()
time.sleep(0.1)
tEnd = time.perf_counter()
print("Code took:", (tEnd - tStart), "seconds.")

dateTimeObj = datetime.datetime.now()
print(dateTimeObj)
#print(dir(dateTimeObj))
dateTimeObj = datetime.datetime(2025, 3, 10)
dateTimeObj = datetime.datetime(2025, 3, 10, 22, 59, 59)
print("date(): ", dateTimeObj.date())
print("time(): ", dateTimeObj.time())
print("timestamp(): ", dateTimeObj.timestamp())
print("today(): ", dateTimeObj.today())
print("year(): ", dateTimeObj.year)
print("month(): ", dateTimeObj.month)
print("day(): ", dateTimeObj.day)
print("hour(): ", dateTimeObj.hour)
print("minute(): ", dateTimeObj.minute)
print("second(): ", dateTimeObj.second)

print("format:", dateTimeObj.strftime("%H:%M:%S %d.%m.%Y"))

dateTimeObj = dateTimeObj.now()
print("format:", dateTimeObj.strftime("%H:%M:%S %d.%m.%Y"))

datetime1 = datetime.datetime(2025,1,1,23,59,59)
datetime2 = datetime.datetime(2030,1,1,23,59,59)
print(datetime2 > datetime1)
print(datetime2 < datetime1)

date1 = datetime.date(2025,1,1)
date2 = datetime.date(2027,1,1)
print(date2 > date1)
print(date2 < date1)