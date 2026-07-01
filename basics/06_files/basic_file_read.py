fh = open("/home/adam/Pulpit/huj/kurs_python/kurs_python/test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)