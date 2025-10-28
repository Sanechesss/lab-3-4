import random
import time
# Запрашиваем количество примеров
N = int(input("Введите количество примеров: "))
# Переменные для статистики
correct_answers = 0
total_time = 0
print()
for i in range(1, N + 1):
    print(f"Вопрос {i}/{N}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct = a * b
    while True:
        try:
            start_time = time.time()
            answer = input(f"{a} × {b} = ")
            end_time = time.time()

            time_spent = end_time - start_time
            answer = int(answer)
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    if answer == correct:
        print(f"Верно! (Время: {time_spent:.1f} сек)")
        correct_answers += 1
    else:
        print(f"Неверно! Правильно: {correct} (Время: {time_spent:.1f} сек)")
    total_time += time_spent
    print()
print("---")
print("СТАТИСТИКА:")
print("---")
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / N:.1f} сек")
print(f"Правильных ответов: {correct_answers}/{N}")
print(f"Процент правильных: {correct_answers / N * 100:.1f}%")