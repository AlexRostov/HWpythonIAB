# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
#                 - A (3,6); B (2,1) -> 5,09
#                 - A (7,-5); B (1,-1) -> 7,21
ax, ay = float(input(" Введите координаты ax: ")), float(input(" Введите координаты ay: "))
bx, by = float(input( "Введите координаты bx: ")), float(input( "Введите координаты by: "))
print("Расстояние между точками А и Б = ", round(((bx - ax) ** 2 + (by - ay) ** 2) ** (1 / 2), 2))
