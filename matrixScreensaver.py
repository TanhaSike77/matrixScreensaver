import sys, time, random

WIDTH = 80
try:

    column = [0] * WIDTH

    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                column[i] = random.randint(4, 14)
            if column[i] == 0:
                print(" ", end="")
            else:
                print(random.choice([1,0]), end="")
                column[i] -= 1
            
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()