per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму которую планируете положить под %"))
deposit = []

for i in per_cent.values():
    usl = money / 100 * i
    deposit.append(int(usl))

print("deposit =", deposit)

max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max_deposit)