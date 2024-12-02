n = int(input("Enter a natural number (n ≥ 0): "))
q = 0
while q**2 <= n:
        q += 1
q -= 1
q = q**2
print("The largest square number less than or equal to n is ", q)