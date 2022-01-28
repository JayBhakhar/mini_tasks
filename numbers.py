def credit_card_validator():
    # https://www.sapling.com/7966257/checksum-credit-card :- check link for understand how algorithm works
    number = str(input("Please enter 16 digit Number: "))
    try:
        if len(number) == 16:
            last_num = int(number[-1])
            num = []
            for i in number[1:-1:2]:
                num.append(int(i))
            for i in number[0:-1:2]:
                a = int(i) * 2
                if len(str(a)) > 1:
                    num1 = []
                    for i in str(a):
                        num1.append(int(i))
                    num.append(sum(num1))
                else:
                    num.append(a)
            x = sum(num) + last_num
            print(num)
            print(x)
            if x % 10 == 0:
                print("valid card number")
            else:
                print("invalid card number")
        else:
            print("invalid card number")
    except:
        print("String is not allow")


credit_card_validator()
