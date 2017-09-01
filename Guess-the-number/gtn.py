import random
import time
number=(random.randint(0,100))
number2=(random.randint(0,1000))



def rundis():
    guess=input("Pick a number from 1 to 100: ")
    if guess==number:
        print("""

         __ __   ___   __ __      __    __   ___   ____   __  __  __
|  |  | /   \ |  |  |    |  |__|  | /   \ |    \ |  ||  ||  |
|  |  ||     ||  |  |    |  |  |  ||     ||  _  ||  ||  ||  |
|  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  ||__||__||__|
|___, ||     ||  :  |    |  `  '  ||     ||  |  | __  __  __
|     ||     ||     |     \      / |     ||  |  ||  ||  ||  |
|____/  \___/  \__,_|      \_/\_/   \___/ |__|__||__||__||__|




         """)
        time.sleep(2)
        rundis2()

    elif guess>number:
        print("Lower")
        rundis()


    elif guess<number:
        print("Higher")
        rundis()

    else:
        print("1 to 100 NUMBERS ONLY")
        time.sleep(1)
        rundis()

def rundis2():
    guess=input("Pick a number from 1 to 1000: ")
    if guess==number2:
        print("""

         __ __   ___   __ __      __    __   ___   ____   __  __  __
|  |  | /   \ |  |  |    |  |__|  | /   \ |    \ |  ||  ||  |
|  |  ||     ||  |  |    |  |  |  ||     ||  _  ||  ||  ||  |
|  ~  ||  O  ||  |  |    |  |  |  ||  O  ||  |  ||__||__||__|
|___, ||     ||  :  |    |  `  '  ||     ||  |  | __  __  __
|     ||     ||     |     \      / |     ||  |  ||  ||  ||  |
|____/  \___/  \__,_|      \_/\_/   \___/ |__|__||__||__||__|




         """)
        time.sleep(2)
        rundis()

    elif guess>number2:
        print("Lower")
        rundis2()


    elif guess<number2:
        print("Higher")
        rundis2()

    else:
        print("1 to 1000 NUMBERS ONLY")
        time.sleep(1)
        rundis2()

rundis()
