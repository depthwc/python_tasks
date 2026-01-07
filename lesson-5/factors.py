def factors(number):
    factors = list(filter(lambda factor: number%factor==0,range(1, number+1)))
    for i in factors:
        print(f"{i} is a factor of {number}")
        

factors(int(input("Enter a positive integer: ")))


def invest(amount, rate, years):
    current_amount=amount
    for i in range(1, years+1):
        increased_amount=(current_amount/100)*rate
        current_amount=current_amount+increased_amount
        print(f"year {i}: ${current_amount:.2f}")
        
    

amount, rate, years = map(int,input("Enter 'amount, rate, years' : ").split())
invest(amount, rate, years)