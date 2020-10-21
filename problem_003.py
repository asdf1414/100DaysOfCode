################################################################################
# The Sieve of Eratosthenes is an algorithm used to generate all prime 
# numbers smaller than N. The method is to take increasingly larger prime 
# numbers, and mark their multiples as composite. For example, to find all 
# primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), 
# then [6, 9, 12, ...] (multiples of three), and so on. Once we have done 
# this for all primes less than N, the unmarked numbers that remain will 
# be prime.
################################################################################

def generate_primes(n):
    # generate list of all odd numbers from 2 to n
    primes = [i for i in range(2, n + 1) if i%2 != 0 or i == 2]

    for i in primes:
        # enter loop if prime factor of i <= n
        if i*i <= n:
            num_to_remove = i*2

            while True:
                # break loop if compound  number >= n
                if num_to_remove >= n: break
                # check if compound  number is in list
                elif num_to_remove in primes:
                    # delete compound  number from list
                    del primes[primes.index(num_to_remove)]
                # add i to num_to_remove and redo loop
                num_to_remove += i
        else:
            return primes


print(generate_primes(100))