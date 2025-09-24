                      # *-* Python 4 - MINI *-* #


def times(n, times, withSep=True):
    repeat = [n for _ in range(times)]
    if withSep:
        print(*repeat, sep='\n')
    else:
        print(*repeat)

# * PRINT ALTS

def say(message=""):
  return print(message)

def csay(msg, color="default"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "default": "\033[0m"
    }
    print(f"{colors.get(color,'')}{msg}\033[0m")

# * INPUTS

def inputInt(inputMessage=""):
  return int(input(inputMessage))

def inputFloat(inputMessage=""):
  return float(input(inputMessage))

# * SIMPLE OPERATIONS

def double(x):
   return x*2

def triple(x):
   return x*3

# * DEBUG

def debug(var):
    print("DEBUG:", repr(var))

def typeOf(var):
    print(type(var).__name__)

# * TEXT ALTS

def upper(text):
    return text.upper()

def lower(text):
    return text.lower()

def reverse(text):
    return text[::-1]

def length(text):
    return len(text)

# * LOGIC

def isEven(n):
    return n % 2 == 0

def isOdd(n):
    return n % 2 != 0

def greater(a,b):
    return a if a>b else b

def smaller(a,b):
    return a if a<b else b

# * HUD

def border(text, char="*"):
    print(char * (len(text)+4))
    print(f"{char} {text} {char}")
    print(char * (len(text)+4))

def banner(text):
    print("~"*len(text))
    print(text)
    print("~"*len(text))

def mirror(text):
    print(text + text[::-1])

# * MATH

def sum(num=0.0, num2=0.0, num3=0.0, num4=0.0, num5=0.0, num6=0.0):
    return num+num2+num3+num4+num5+num6

def sub(num=0.0, num2=0.0, num3=0.0, num4=0.0, num5=0.0, num6=0.0):
    return num-num2-num3-num4-num5-num6

def mul(num=1.0, num2=1.0, num3=1.0, num4=1.0, num5=1.0, num6=1.0):
    return num*num2*num3*num4*num5*num6

def div(dividend=1.0, divider=1.0):
    if divider == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return dividend/divider

def perc(num=0.0, perc=0.0):
    r = (num * perc) / 100
    return r

def sqrt(num=0.0):
    if num < 0:
        raise ValueError("It is not possible to calculate the square root of a negative number")
    return num ** 0.5