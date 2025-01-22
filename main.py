import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

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

def show_image():
    image_window = tk.Toplevel(root)
    image_window.title("Нормативы ССК")
    img = Image.open("normatives.png")  # Убедитесь, что файл normatives.png находится в той же папке
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(image_window, image=img)
    panel.image = img
    panel.pack()

# Создание основного окна
root = tk.Tk()
root.title("спортсмен росгвардии")

# Главная страница
ttk.Label(root, text="спортсмен росгвардии", font=("Helvetica", 24)).grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# Кнопка для подбора программы тренировок
ttk.Button(root, text="Подбор программы тренировок", command=lambda: create_training_program_window()).grid(column=0, row=1, padx=10, pady=10)

# Кнопка для открытия изображения с нормативами ССК
ttk.Button(root, text="Нормативы ССК", command=show_image).grid(column=1, row=1, padx=10, pady=10)

def create_training_program_window():
    training_program_window = tk.Toplevel(root)
    training_program_window.title("Подбор программы тренировок")

    # Параметры для выбора
    age_groups = ["16-17 лет", "18-19 лет", "19-20 лет", "21-22 года", "23 и более лет"]
    courses = ["1 курс", "2 курс", "3-5 курс"]
    weight_categories = ["50-60 кг", "61-70 кг", "71-80 кг", "81-90 кг", "90 и более кг"]
    ratings = ["оценка 2", "оценка 3", "оценка 4", "оценка 5"]

    # Создание виджетов для ввода данных
    ttk.Label(training_program_window, text="Возрастная группа").grid(column=0, row=0, padx=10, pady=5)
    ttk.Combobox(training_program_window, textvariable=age_group_var, values=age_groups).grid(column=1, row=0, padx=10, pady=5)

    ttk.Label(training_program_window, text="Курс").grid(column=0, row=1, padx=10, pady=5)
    ttk.Combobox(training_program_window, textvariable=course_var, values=courses).grid(column=1, row=1, padx=10, pady=5)

    ttk.Label(training_program_window, text="Весовая категория").grid(column=0, row=2, padx=10, pady=5)
    ttk.Combobox(training_program_window, textvariable=weight_category_var, values=weight_categories).grid(column=1, row=2, padx=10, pady=5)

    ttk.Label(training_program_window, text="Оценка за бег на 3 км").grid(column=0, row=3, padx=10, pady=5)
    ttk.Combobox(training_program_window, textvariable=run_3km_var, values=ratings).grid(column=1, row=3, padx=10, pady=5)

    ttk.Label(training_program_window, text="Оценка за бег на 100 м").grid(column=0, row=4, padx=10, pady=5)
    ttk.Combobox(training_program_window, textvariable=run_100m_var, values=ratings).grid(column=1, row=4, padx=10, pady=5)

    ttk.Label(training_program_window, text="Оценка за подтягивания").grid(column=0, row=5, padx=10, pady=5)
    ttk.Combobox(training_program_window, textvariable=pull_ups_var, values=ratings).grid(column=1, row=5, padx=10, pady=5)

    # Кнопка для получения программы тренировок
    ttk.Button(training_program_window, text="Получить программу тренировок", command=show_training_program).grid(column=0, row=6, columnspan=2, padx=10, pady=20)

# Создание переменных для хранения выбранных значений
age_group_var = tk.StringVar()
course_var = tk.StringVar()
weight_category_var = tk.StringVar()
run_3km_var = tk.StringVar()
run_100m_var = tk.StringVar()
pull_ups_var = tk.StringVar()

# Запуск основного цикла обработки событий
root.mainloop()