import cs50

def calculate_quarters(amount):
    return amount // 0.25

def calculate_dimes(amount):
    return amount // 10

def calculate_nickels(amount):
    return amount // 5

def calculate_pennies(amount):
    return amount // 1

while True:
    change = cs50.get_float("How much change? " )
    remainder_after_quat = (change*100) % 25
    remainder_after_dimes = remainder_after_quat % 10
    remainder_after_nickels = remainder_after_dimes % 5
    remainder_after_pennies = remainder_after_nickels % 1
    try:
        if change >= 0:
            print(int(calculate_quarters(change)+calculate_dimes(remainder_after_quat)+calculate_nickels(remainder_after_dimes)+calculate_pennies(remainder_after_nickels)))
            break
        else:
            continue
    except ValueError:
        continue
    except:
        continue
print()
