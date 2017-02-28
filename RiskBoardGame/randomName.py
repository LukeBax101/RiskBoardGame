import random

names = ["Sam","Luke","Alex","Molly","Ryan","Bradley","Matthew","Oakley"]
while len(names)>0:
    length = len(names)
    name = random.randint(0,length-1)
    first = names[name]
    names.remove(first)
    name2 = random.randint(0,(length-2))
    second = names[name2]
    names.remove(second)
    print(first,second)
