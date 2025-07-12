home_price = 10_00_000
has_good_credit = False

if has_good_credit:
    down_payment = float(home_price) * 0.1
    print(int(down_payment))
elif not has_good_credit:
    down_payment = float(home_price) * 0.2
    print(int(down_payment))
else:
    print(home_price)
print(home_price)
