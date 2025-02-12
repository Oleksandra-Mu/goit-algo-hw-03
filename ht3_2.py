# Завдання 2

# Напишіть програму на Python, яка використовує рекурсію 
# для створення фракталу «сніжинка Коха» за умови, 
# що користувач повинен мати можливість вказати рівень рекурсії.

import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve():
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    order = int(input("Введіть рівень рекурсії: "))
    size=300
    t.goto(-size / 2, 0)
    t.pendown()
    
    # Малюємо сніжинку Коха
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
        
    window.mainloop()


draw_koch_curve()