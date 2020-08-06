import re
str = '''
    rishikumar2005@gmail.com
    the above email is my ant this one too rishikumar@gamil.com
    323728jdhjf@gmail.com
    hfwj37813@hfj

'''
com = re.findall(r"\w+@\S+\w",str)
l1 = []
i = 0
for match in com:
    i = i+1
    print(match)
    l1.append(match)

print(f"Total number of emails is {i}")

