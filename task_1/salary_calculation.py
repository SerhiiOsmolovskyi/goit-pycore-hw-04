def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Некоректний формат даних у рядку: {line.strip()}")
            
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            
            return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка: {e}")


path_to_file = "./task_1/salary.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
