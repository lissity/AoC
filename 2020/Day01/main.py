# Obtain input
numbers = [int(line.strip()) for line in open('2020/Day01/input.txt', 'r').readlines()]

# Part 1
for i in range(0, len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if (numbers[i] + numbers[j] == 2020):
            num1 = numbers[i]
            num2 = numbers[j]
            break

print(f"Part 1: The numbers {num1} and {num2} add up to 2020. The product is {num1 * num2}.")

# Part 2
for i in range(0, len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
            if (numbers[i] + numbers[j] + numbers[k] == 2020):
                num1 = numbers[i]
                num2 = numbers[j]
                num3 = numbers[k]
                break

print(f"Part 2: The numbers {num1}, {num2}, and {num3} add up to 2020. "
      f"The product is {num1 * num2 * num3}.")