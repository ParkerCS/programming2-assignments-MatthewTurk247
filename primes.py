def find_primes_in(interval):
    potential_primes = [x for x in range(3, interval + 1) if x % 2 != 0 and x >= 2]
    if interval >= 2:
        potential_primes.insert(0, 2)

    for i in potential_primes:
        if i != 0:
            print("{:.2f}%".format(50 * i / len(potential_primes)))
            for j in range(i + 1, len(potential_primes)):
                try:
                    if potential_primes[j] % i == 0:
                        potential_primes[j] = 0
                except:
                    pass

    print("100.00%")
    print("Almost there!")
    while 0 in potential_primes:
        potential_primes.remove(0)
    return potential_primes

print(find_primes_in(1000))