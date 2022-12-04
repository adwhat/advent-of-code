file=open("day01.txt") 

elf=0
elves=[]
for line in file:
    line=line.strip()
    if not line:
        elves.append(elf)
        elf=0
    else:
        elf=elf+int(line)
elves.append(elf)
elves=sorted(elves,reverse=True)
print(elves[0])
print(sum(elves[0:3]))