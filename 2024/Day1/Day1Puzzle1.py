
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

left.sort()
right.sort()

for i, x in enumerate(left):
    y = right[i]

    result += abs(int(x) - int(y))

print(result)

