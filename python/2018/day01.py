file = open ("day01.txt")
#file = ["1", "-2", '3', "1"]
answer = 0
for line in file:
    number = int(line)
    answer += number

print(answer)
file.close()

def part2():
    file = open("day01.txt").read().split()
    #file = [+7, +7, -2, -7, -4]
    doubles = set()
    frequency = 0

    while True:
        for line in file:
            number = int(line)
            frequency += number
            if frequency in doubles:
                print(frequency)
                return
            doubles.add(frequency)

part2()