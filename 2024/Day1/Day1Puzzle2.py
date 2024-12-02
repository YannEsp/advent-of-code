
with open("Day1Input.txt") as f:
        file = list(f)
        #lines = f.readlines()

left = []
right = []
result = 0

for x, value in enumerate(file):

    file[x] = value.replace("   ", "|").replace("\n","")

    current_numbers = file[x].split("|")
    left.append(current_numbers[0])
    right.append(current_numbers[1])

for x in left:

    result += int(x) * right.count(x)

print(result)

