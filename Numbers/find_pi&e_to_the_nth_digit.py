from mpmath import mp


def find_pi_to_the_nth_digit():
    mp.dps = int(input("Enter a number :- ")) + 1
    if mp.dps < 52:
        print(mp.pi)
    else:
        print("Maximum number is 50")


def find_e_to_the_nth_digit():
    mp.dps = int(input("Enter a number :- ")) + 1
    if mp.dps < 52:
        print(mp.e)
    else:
        print("Maximum number is 50")


