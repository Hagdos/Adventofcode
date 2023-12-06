import regex as re


def twodigit(string):
    for char in string:
        if char.isdigit():
            ans = int(char)*10
            break
    for char in string[::-1]:
        if char.isdigit():
            ans += int(char)
            break
    return ans

def replacetext(string):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    for digit, text in enumerate(numbers):
        string = string.replace(text, str(digit))

    return string


def str2int(string, numbers):
    if string in numbers:
        string = numbers.index(string)
    return int(string)

def twodigit2(string):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "[0-9]"]
    regex = "|".join(numbers)
    # matches = re.finditer(f"(?={regex})" , string)
    matches = re.findall(regex, string, overlapped=True)
    digits = [matches[0], matches[-1]]

    answer = str2int(digits[0], numbers)*10+str2int(digits[1], numbers)

    return answer


def part1(data):
    ans = 0
    for line in data:
        ans += twodigit(line)

    return ans

def part2(data):
    ans = 0
    for line in data:
        ans += twodigit2(line)

    return ans


file = open('test.txt').readlines()

data = [x.strip() for x in file]

# print('The answer to part 1: ', part1(data))
print('The answer to part 2: ', part2(data))
