<div align="center">

<img width="350" height="250" alt="Stopwatch" src="https://github.com/user-attachments/assets/29e118fd-2433-4865-b2fd-e147ae67e25b" />

<div align="center">

  <h1>⏱ Modern Stopwatch</h1>

  <p>Современный, минималистичный и стильный секундомер для Windows, написанный на Python и PyQt6.</p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Qt-PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt6" />
    <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />
  </p>

</div>

---

# ✨ Особенности

* **🎨 Современный кастомный UI:** Тёмная тема с лаконичным дизайном и плавными закруглениями.
* **🖼 Безрамочный режим (Frameless):** Кастомная панель заголовка с удобными кнопками сворачивания и закрытия.
* **📍 Центрирование при запуске:** Окно приложения всегда открывается строго по центру экрана.
* **📌 Режим Always-on-Top:** Секундомер фиксируется поверх всех остальных окон для удобного отслеживания времени.
* **🚀 Полная автономность:** Сборка в один единый файл `.exe` со встроенной иконкой.

---

# 🛠 Технологии

* **Language:** Python
* **GUI Framework:** PyQt6
* **Compiler:** PyInstaller

---

## 🚀 Быстрый запуск из исходного кода

### 1. Клонирование репозитория
git clone https://github.com/Emergeflow/Stopwatch.git
cd Stopwatch

### 2. Установка зависимостей
pip install PyQt6

### 3. Запуск приложения
python Stopwatch.py

---

## 📦 Сборка в .exe

Если вы хотите собрать приложение в один исполняемый файл с собственной иконкой:

1. Установите PyInstaller:
   pip install pyinstaller

2. Выполните команду сборки:
   pyinstaller --noconsole --onefile --icon=Stopwatch.ico --add-data "Stopwatch.ico;." Stopwatch.py

Готовый файл **Stopwatch.exe** появится в папке **dist/**.

---

<div align="center">

  <sub>Developed with ❤️ by **Emergeflow**</sub>

</div>
