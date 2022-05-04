n = int(input("Write n: "))
k = int(input("Write k: "))
sum = 0

if 1 <= n <= 4:
    if n == 1:
        for i in range(1,10):
            if i % k == 0:
                sum += i
    if n == 2:
        for i in range(11,100):
            if i % k == 0:
                sum += i
    if n == 3:
        for i in range(101,1000):
            if i % k == 0:
                sum += i
    if n == 4:
        for i in range(1001,10000):
            if i % k == 0:
                sum += i
    print("The amount of numbers is: ", sum)
else: print("Введите n в диапазоне от 1 до 4")
