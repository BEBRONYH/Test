import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMessageBox, QDialog

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

class TrainingProgramDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Подбор программы тренировок")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.age_group_label = QLabel("Возрастная группа")
        self.age_group_combo = QComboBox()
        self.age_group_combo.addItems(["16-17 лет", "18-19 лет", "19-20 лет", "21-22 года", "23 и более лет"])
        
        self.course_label = QLabel("Курс")
        self.course_combo = QComboBox()
        self.course_combo.addItems(["1 курс", "2 курс", "3-5 курс"])
        
        self.weight_category_label = QLabel("Весовая категория")
        self.weight_category_combo = QComboBox()
        self.weight_category_combo.addItems(["50-60 кг", "61-70 кг", "71-80 кг", "81-90 кг", "90 и более кг"])
        
        self.run_3km_label = QLabel("Оценка за бег на 3 км")
        self.run_3km_combo = QComboBox()
        self.run_3km_combo.addItems(["оценка 2", "оценка 3", "оценка 4", "оценка 5"])
        
        self.run_100m_label = QLabel("Оценка за бег на 100 м")
        self.run_100m_combo = QComboBox()
        self.run_100m_combo.addItems(["оценка 2", "оценка 3", "оценка 4", "оценка 5"])
        
        self.pull_ups_label = QLabel("Оценка за подтягивания")
        self.pull_ups_combo = QComboBox()
        self.pull_ups_combo.addItems(["оценка 2", "оценка 3", "оценка 4", "оценка 5"])
        
        self.get_program_button = QPushButton("Получить программу тренировок")
        self.get_program_button.clicked.connect(self.show_training_program)
        
        layout.addWidget(self.age_group_label)
        layout.addWidget(self.age_group_combo)
        layout.addWidget(self.course_label)
        layout.addWidget(self.course_combo)
        layout.addWidget(self.weight_category_label)
        layout.addWidget(self.weight_category_combo)
        layout.addWidget(self.run_3km_label)
        layout.addWidget(self.run_3km_combo)
        layout.addWidget(self.run_100m_label)
        layout.addWidget(self.run_100m_combo)
        layout.addWidget(self.pull_ups_label)
        layout.addWidget(self.pull_ups_combo)
        layout.addWidget(self.get_program_button)
        
        self.setLayout(layout)
    
    def show_training_program(self):
        age_group = self.age_group_combo.currentText()
        course = self.course_combo.currentText()
        weight_category = self.weight_category_combo.currentText()
        run_3km = self.run_3km_combo.currentText()
        run_100m = self.run_100m_combo.currentText()
        pull_ups = self.pull_ups_combo.currentText()
        
        # Проверка на заполнение всех полей
        if not age_group or not course or not weight_category or not run_3km or not run_100m or not pull_ups:
            QMessageBox.critical(self, "Ошибка", "Пожалуйста, заполните все поля")
            return
        
        training_program = get_training_program(age_group, course, weight_category, run_3km, run_100m, pull_ups)
        
        QMessageBox.information(self, "Ваша программа тренировок", training_program)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("спортсмен росгвардии")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.title_label = QLabel("спортсмен росгвардии")
        self.title_label.setStyleSheet("font-size: 24px;")
        self.title_label.setAlignment(Qt.AlignCenter)
        
        self.training_program_button = QPushButton("Подбор программы тренировок")
        self.training_program_button.clicked.connect(self.open_training_program_dialog)
        
        self.normatives_button = QPushButton("Нормативы ССК")
        self.normatives_button.clicked.connect(self.show_normatives)
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.training_program_button)
        layout.addWidget(self.normatives_button)
        
        self.setLayout(layout)
    
    def open_training_program_dialog(self):
        dialog = TrainingProgramDialog()
        dialog.exec_()
    
    def show_normatives(self):
        normatives_text = """
        Нормативы ССК:
        1. Бег на 3 км:
           - Оценка 2: > 15 минут
           - Оценка 3: 13-15 минут
           - Оценка 4: 11-13 минут
           - Оценка 5: < 11 минут
        2. Бег на 100 м:
           - Оценка 2: > 15 секунд
           - Оценка 3: 13-15 секунд
           - Оценка 4: 11-13 секунд
           - Оценка 5: < 11 секунд
        3. Подтягивания:
           - Оценка 2: < 5 раз
           - Оценка 3: 5-10 раз
           - Оценка 4: 11-15 раз
           - Оценка 5: > 15 раз
        """
        normatives_window = QDialog()
        normatives_window.setWindowTitle("Нормативы ССК")
        layout = QVBoxLayout()
        label = QLabel(normatives_text)
        label.setAlignment(Qt.AlignLeft)
        layout.addWidget(label)
        normatives_window.setLayout(layout)
        normatives_window.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())