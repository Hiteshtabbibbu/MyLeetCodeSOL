'''
Amicable Pair(Two numbers are amicable if the first is equal to the sum of divisors of the second, and if the second number is equal to the sum of divisors of the first).
'''

#SOLUTION
n1 = 1184
n2 = 1210
summ = 0
for i in range(1,n2//2+1):
    if n2%i ==0:
        summ += i
if summ == n1:
    print("yeah it is Amicable pair")
else:
    print("Nopee..")
