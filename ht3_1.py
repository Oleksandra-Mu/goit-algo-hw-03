# Завдання 1

# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, 
# переміщає їх до нової директорії та сортує в піддиректорії, 
# назви яких базуються на розширенні файлів.

# Також візьміть до уваги наступні умови:

# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: 
# шлях до вихідної директорії та шлях до директорії призначення 
# (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

# 2. Рекурсивне читання директорій:

# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.

# 3. Копіювання файлів:

# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, 
# використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, 
# помилки доступу до файлів або директорій.

from pathlib import Path
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='копіювання файлів')
    parser.add_argument("src", type = Path, help='Шлях до вихідної директорії')
    parser.add_argument("--dest", type = Path, default=Path("dist"), help='Шлях до директорії призначення')
    return parser.parse_args()

def copying_files(initial_path, destination_path):
    try:
        for item in initial_path.iterdir():
            if item.is_dir():
                copying_files(item, destination_path)
            else:
                extension = item.suffix[1:]
                if extension:
                    new_dir = destination_path / extension
                    new_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, new_dir)
    
    except Exception as e:
        print(f"помилка: {e}")


def main():
    args = parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)
    copying_files(args.src, args.dest)

if __name__ == "__main__":
    main()