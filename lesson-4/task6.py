prime = [1 for i in range(101)]
prime[0] = prime[1] = 0
i = 2
while i * i <= len(prime):
    if prime[i]:
        j = i * 2
        while j <= len(prime):
            prime[j] = 0
            j += i
    i += 1
for i in range(len(prime)):
    if prime[i]:
        print(i)
