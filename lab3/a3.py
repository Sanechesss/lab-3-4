prev = int(input())
curr = int(input())
if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr
if used <= 300:
    cost = 21.0
elif used <= 600:
    cost = 21 + (used - 300) * 0.06
elif used <= 800:
    cost = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
avg_price = cost / used
print("Предыдущее:", prev)
print("Текущее:", curr)
print("Использовано:", used)
print("К оплате:", round(cost, 2))
print("Ср. цена m^3:", round(avg_price, 2))

