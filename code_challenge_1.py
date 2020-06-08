def get_sum_of_multiples(max_number):
    number_list = [*range(0, max_number, 1)]

    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, number_list)))

if __name__ == "__main__":
    sum = get_sum_of_multiples(1000)
    print(f'Here is the sum of multiples: {sum}')