def findSquare(number):
    return number ** 2


def isArmstrong(number):
    original = number
    sum = 0

    while (number != 0):
        lastDigit = number % 10
        sum += lastDigit ** 3
        number //= 10

    if sum == original:
        return True
    else:
        return False


def isPalindrome(number):
    original = number
    reverse = 0
    while (number != 0):
        lastDigit = number % 10
        reverse = reverse * 10 + lastDigit
        number //= 10

    return reverse == original


def add(number1, number2):
    return number1 + number2


def sub(number1, number2):
    return number1 - number2


def divide(number1, number2):
    return number1 / number2


def product(number1, number2):
    return number1 * number2


a = int(input("Enter a number: "))
print(isPalindrome(a))
