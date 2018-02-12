def calculate_pay (hours, rate):
    if float(hours) <= 40:
        pay = float(hours)*float(rate)
        print('Pay: $' + str(pay))
    else:
        overtime_pay = (40*float(rate) + (float(hours) - 40) * (1.5 * float(rate)))
        print('Pay: $' + str(overtime_pay))
hours = input('Enter Hours: ')
rate = input('Enter Rate: $')
calculate_pay (hours, rate)