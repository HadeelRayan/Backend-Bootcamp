

def sieve_of_eratosthenes():
    main_numbers_list = list(range(4, 150))
    prime_numbers_list = [2, 3]

    for num in main_numbers_list:
        is_prime = True
        for prime in prime_numbers_list:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers_list.append(num)
            multiples = num * 2
            while multiples <= 150:
                if multiples in main_numbers_list:
                    main_numbers_list.remove(multiples)
                multiples += num

    return prime_numbers_list


def main():
    prime_numbers = sieve_of_eratosthenes()
    print("Total prime numbers:", len(prime_numbers))
    print("Prime numbers found:", prime_numbers)


if __name__ == "__main__":
    main()
