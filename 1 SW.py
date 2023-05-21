# число = int(input("Введите трехзначное число: "))

# сотни = число // 100
# десятки = (число // 10) % 10
# единицы = число % 10

# сумма_цифр = сотни + десятки + единицы
# print("Сумма цифр:", сумма_цифр)




# def solve_paper_cranes(S):
#     с = S / 6
#     p = с
#     к = 4 * с
#     return p, к, с

# # Пример использования:
# S = 36
# p, к, с = solve_paper_cranes(S)
# print(f"Петя: {p}, Катя: {к}, Сережа: {с}")






# def is_lucky_ticket(ticket_number):
#     # Преобразуем номер билета в строку
#     ticket_str = str(ticket_number)

#     # Проверяем длину номера билета
#     if len(ticket_str) != 6:
#         return False

#     # Вычисляем сумму первых трех цифр и сумму последних трех цифр
#     sum_first_half = int(ticket_str[0]) + int(ticket_str[1]) + int(ticket_str[2])
#     sum_second_half = int(ticket_str[3]) + int(ticket_str[4]) + int(ticket_str[5])

#     # Проверяем, является ли билет счастливым
#     if sum_first_half == sum_second_half:
#         return True
#     else:
#         return False

# # Пример использования:
# ticket_number = 385916
# is_lucky = is_lucky_ticket(ticket_number)
# if is_lucky:
#     print("У вас счастливый билет!")
# else:
#     print("У вас обычный билет.")





# def can_break_chocolate(n, m, k):
#     # Проверяем, если k равно 1, то шоколадку можно всегда отломить
#     if k == 1:
#         return True

#     # Проверяем, если шоколадка имеет всего одну дольку, то отломить k долек невозможно
#     if n == 1 and m == 1:
#         return False

#     # Проверяем, если n или m равно 1, то шоколадку можно отломить только по одной оси,
#     # и в этом случае отломить k долек невозможно, если k больше n или m
#     if n == 1 or m == 1:
#         return k > max(n, m)

#     # Проверяем, если k равно некоторому числу, меньшему или равному половине общего числа долек,
#     # то шоколадку можно отломить так, чтобы отломленные дольки составляли прямоугольник
#     if k <= (n * m) // 2:
#         return True

#     return False

# # Пример использования:
# n = 4
# m = 6
# k = 8
# result = can_break_chocolate(n, m, k)
# if result:
#     print("Можно отломить", k, "долек от шоколадки размером", n, "×", m)
# else:
#     print("Невозможно отломить", k, "долек от шоколадки размером", n, "×", m)

