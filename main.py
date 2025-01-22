import json
import tkinter as tk
from tkinter import ttk, messagebox

def get_training_program(age_group, course, weight_category, run_3km, run_100m, pull_ups):
    # Загрузка программ тренировок из файла JSON
    with open('training_programs.json', 'r', encoding='utf-8') as file:
        programs = json.load(file)
    
    try:
        # Получение программы тренировок на основе данных пользователя
        training_program_3km = programs[age_group][course][weight_category]["3 км"][run_3km]
        training_program_100m = programs[age_group][course][weight_category]["100 м"][run_100m]
        training_program_pull_ups = programs[age_group][course][weight_category]["подтягивания"][pull_ups]
        
        return f"Программа тренировок на основе оценки за бег на 3 км: {training_program_3km}\n" \
               f"Программа тренировок на основе оценки за бег на 100 м: {training_program_100m}\n" \
               f"Программа тренировок на основе оценки за подтягивания: {training_program_pull_ups}"
    except KeyError:
        return "Персонализированная программа тренировок будет разработана на основе ваших данных."

def show_training_program():
    age_group = age_group_var.get()
    course = course_var.get()
    weight_category = weight_category_var.get()
    run_3km = run_3km_var.get()
    run_100m = run_100m_var.get()
    pull_ups = pull_ups_var.get()
    
    training_program = get_training_program(age_group, course, weight_category, run_3km, run_100m, pull_ups)
    
    messagebox.showinfo("Ваша программа тренировок", training_program)

# Создание основного окна
root = tk.Tk()
root.title("Подбор программы тренировок")

# Параметры для выбора
age_groups = ["16-17 лет", "18-19 лет", "19-20 лет", "21-22 года", "23 и более лет"]
courses = ["1 курс", "2 курс", "3-5 курс"]
weight_categories = ["50-60 кг", "61-70 кг", "71-80 кг", "81-90 кг", "90 и более кг"]
ratings = ["оценка 2", "оценка 3", "оценка 4", "оценка 5"]

# Создание виджетов для ввода данных
ttk.Label(root, text="Возрастная группа").grid(column=0, row=0, padx=10, pady=5)
age_group_var = tk.StringVar()
ttk.Combobox(root, textvariable=age_group_var, values=age_groups).grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Курс").grid(column=0, row=1, padx=10, pady=5)
course_var = tk.StringVar()
ttk.Combobox(root, textvariable=course_var, values=courses).grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Весовая категория").grid(column=0, row=2, padx=10, pady=5)
weight_category_var = tk.StringVar()
ttk.Combobox(root, textvariable=weight_category_var, values=weight_categories).grid(column=1, row=2, padx=10, pady=5)

ttk.Label(root, text="Оценка за бег на 3 км").grid(column=0, row=3, padx=10, pady=5)
run_3km_var = tk.StringVar()
ttk.Combobox(root, textvariable=run_3km_var, values=ratings).grid(column=1, row=3, padx=10, pady=5)

ttk.Label(root, text="Оценка за бег на 100 м").grid(column=0, row=4, padx=10, pady=5)
run_100m_var = tk.StringVar()
ttk.Combobox(root, textvariable=run_100m_var, values=ratings).grid(column=1, row=4, padx=10, pady=5)

ttk.Label(root, text="Оценка за подтягивания").grid(column=0, row=5, padx=10, pady=5)
pull_ups_var = tk.StringVar()
ttk.Combobox(root, textvariable=pull_ups_var, values=ratings).grid(column=1, row=5, padx=10, pady=5)

# Кнопка для получения программы тренировок
ttk.Button(root, text="Получить программу тренировок", command=show_training_program).grid(column=0, row=6, columnspan=2, padx=10, pady=20)

# Запуск основного цикла обработки событий
root.mainloop()