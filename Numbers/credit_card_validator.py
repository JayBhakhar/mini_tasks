# https://www.sapling.com/7966257/checksum-credit-card :- check link for understand how algorithm works

def is_credit_card_valid(card: str) -> bool:
    numbers = [int(number) for number in card]
    if len(numbers) != 16:
        raise ValueError("Credit card is not 16 digits")

    sequence = [number for number in numbers[1:-1:2]]

    for number in numbers[0:-1:2]:
        if len(str(number * 2)) <= 1:
            sequence.append(number * 2)
        else:
            two_digit = [int(number) for number in str(number * 2)]
            sequence.append(sum(two_digit))

    x = sum(sequence) + numbers[-1]

    return x % 10 == 0


