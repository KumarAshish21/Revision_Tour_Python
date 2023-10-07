def isPrime(N):
    if N > 1:
        for i in range(2, int(N**0.5) + 1):
            if N%i==0:
                return "No"
                break
        else:
            return "Yes"
    else:
        return "No"
N = int(input("Enter the Number :"))
print(isPrime(N))
    