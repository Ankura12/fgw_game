f = open("ankur.txt",)
# print(f.tell())
print(f.readline())
f.seek(0)
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
print(f.readline())
f.close()
