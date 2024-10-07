import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Запитуємо у користувача рівень рекурсії
    order = int(input("Введіть рівень рекурсії: "))
    
    # Налаштовуємо вікно Turtle
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Створюємо Turtle
    t = turtle.Turtle()
    t.speed("fastest")
    
    # Малюємо сніжинку Коха
    size = 300
    koch_snowflake(t, order, size)
    
    # Завершуємо малювання
    turtle.done()

if __name__ == "__main__":
    main()
