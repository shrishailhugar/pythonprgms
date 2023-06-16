from time import sleep
def infinite_seq():
    num = 0
    while True:
        num += 1
        yield num

for i in infinite_seq():
    print(i, end="  ")
    # sleep(0.1)