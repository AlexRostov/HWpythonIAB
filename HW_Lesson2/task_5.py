import time

start = int(input("Нижний предел: "))
finish = int(input("Верхний предел: "))
rand_nam = int((time.time() % 1) * (finish - start) + start)
print(f"Сдучайное число в диапазоне от {start} до {finish}: {rand_nam}")
print(time.time())