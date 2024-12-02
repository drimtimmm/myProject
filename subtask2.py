n = 0
m = 10^100
s = 0
x = 0
while x != -1:
    x = int(input("Input the number of sequence: "))
    n = n + 1
    if x != -1:
        s = s + x
        if m > x:
            m = x
if n == 0:
    m = -1
    a = -1
else:
    a = s/n
n = n - 1
print("Count of numbers of sequence: ", n)
print("Sum of sequence: ", s)
print("Minimum number of sequence: ", m)
print("Mean of numbers of sequence: ", a)
