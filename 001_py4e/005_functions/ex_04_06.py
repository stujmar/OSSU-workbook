def computepay(flt_hours, flt_rate):
        if flt_hours > 40:
                ot_hours = flt_hours - 40
                flt_pay = ot_hours * flt_rate * 1.5 + (40 * flt_rate)
                return flt_pay
        else:
                flt_pay = flt_hours * flt_rate
                return flt_pay

hrs = input("Enter Hours:")
p = computepay(10, 20)
print("Pay", p)