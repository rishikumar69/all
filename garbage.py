f = open("C:\\Users\\Rishi\\Desktop\\database for web.TXT", 'r+')
content = f.read()
print(content)
for i in range(1, 11):
    f.write(f"{i}\nhi")
# print(content)

f.close()