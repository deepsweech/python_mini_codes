import random, sys, time

def roll(i):
    
    while i != 0:
        # 1-6
        n = random.randint(0,7)
        sys.stdout.write("Rolling dice: %d   \r" % n)
        sys.stdout.flush()
        
        # gets slower while reaching i
        time.sleep(1/float(i))
        i -= 1

if __name__ == "__main__":
    roll(50)
