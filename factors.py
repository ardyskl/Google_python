#!/usr/bin/env python3

import math
import sys
import traceback

def main():

    try:
        # finding all factors
        def all_factors(n):
            factor_values = []
            for i in range(1, n + 1):
                if n % i == 0:
                    factor_values.append(i)
            print("All factors: ", factor_values)

        # finding prime factors
        def primes(n):
            i = 2
            factors = []
            while n % 2 == 0:
                factors.append(2)
                n = n / 2


                for i in range(3, int(math.sqrt(n))+1, 2):
                    while (n % i == 0):
                        factors.append(i)
                        n = n / i

            if n > 2:
                factors.append(n)
                print("Prime Factorisation is:", *factors)
                print("The prime factor is: " + str(factors[-1]))

        cont = "y"
        while(cont.lower() == "y"):

            n = int(input("Enter a number: "))
            primes(n)
            all_factors(n)

            cont = input("Do you want to factorise more? [y to continue] & [n to exit]: ")

            if cont == "n":
                print("Thanks for using our factors app!")
                quit()

    except KeyboardInterrupt:
        print("\n--- Shutdown requested exiting ---")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
