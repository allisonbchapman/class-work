def calculate_pay (hours, rate):
    if float(hours) <= 40:
        pay = hours*rate
    else:
        pay = 40 * rate + (hours - 40) * (1.5 * rate)
    return pay
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: $'))
    print(calculate_pay(hours, rate))
except:
    print('Please enter a number')