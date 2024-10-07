def hanoi_tower(n, source, auxiliary, target, state):
    if n == 1:
        # Переміщуємо один диск з source на target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        # Перемістити n-1 дисків з source на auxiliary
        hanoi_tower(n-1, source, target, auxiliary, state)
        
        # Перемістити найбільший диск з source на target
        hanoi_tower(1, source, auxiliary, target, state)
        
        # Перемістити n-1 дисків з auxiliary на target
        hanoi_tower(n-1, auxiliary, source, target, state)

# Основна функція для запуску програми
def solve_hanoi(n):
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    hanoi_tower(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")

# Викликаємо функцію з кількістю дисків
solve_hanoi(3)
