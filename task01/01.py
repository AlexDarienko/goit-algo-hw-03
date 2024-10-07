import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dst_dir):
    # Створити директорію призначення, якщо вона не існує
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Проходимо по всіх елементах у вихідній директорії
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        
        # Якщо це директорія, викликаємо функцію рекурсивно
        if os.path.isdir(item_path):
            copy_and_sort_files(item_path, dst_dir)
        
        # Якщо це файл, копіюємо його в відповідну піддиректорію за розширенням
        elif os.path.isfile(item_path):
            file_ext = os.path.splitext(item)[1][1:]  # Отримуємо розширення без крапки
            if not file_ext:  # Якщо немає розширення, присвоїти "no_extension"
                file_ext = "no_extension"
            
            # Створюємо директорію для файлів з цим розширенням
            ext_dir = os.path.join(dst_dir, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy2(item_path, ext_dir)

def main():
    # Парсимо аргументи командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument('src_dir', help="Шлях до вихідної директорії")
    parser.add_argument('dst_dir', nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням dist)")
    
    args = parser.parse_args()

    # Перевіряємо наявність вихідної директорії
    if not os.path.exists(args.src_dir):
        print(f"Вихідна директорія {args.src_dir} не існує.")
        return
    
    # Викликаємо функцію для копіювання та сортування файлів
    copy_and_sort_files(args.src_dir, args.dst_dir)
    print(f"Файли успішно скопійовано та відсортовано у директорію {args.dst_dir}")

if __name__ == "__main__":
    main()
