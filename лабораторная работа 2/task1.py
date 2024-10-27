money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
money_capital_ = money_capital + salary - spend  # останется от подушки безопасности после первого месяца
months = 1
while money_capital_ + salary >= spend:
    spend *= 1.05
    money_capital_ = money_capital_ + salary - spend
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
