str_hours = input("Enter Hours:")
str_rate = input("Enter Rate:")

try: 
    flt_hours = float(str_hours)
    flt_rate = float(str_rate)
except:
    print("Error, please enter numeric input")
    quit()

if flt_hours > 40:
    ot_hours = flt_hours - 40
    flt_pay = ot_hours * flt_rate * 1.5 + (40 * flt_rate)
    # print(ot_hours, "hours of overtime. Total Pay:", flt_pay)
    print(flt_pay)
else:
    flt_pay = flt_hours * flt_rate
    print("Regular Rate:", flt_pay)

