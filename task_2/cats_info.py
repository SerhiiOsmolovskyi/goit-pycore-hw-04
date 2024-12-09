def get_cats_info(path):
    cats = [] 
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Некоректний формат даних у рядку: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    
    return cats

path_to_file = "./task_2/cats_file.txt"
cats_info = get_cats_info(path_to_file)
print(cats_info)
