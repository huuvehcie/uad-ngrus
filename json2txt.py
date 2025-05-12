#!/usr/bin/env python3

# Скрипт для извлечения имен пакетов и описаний из JSON-файла с сохранением экранированных символов
# Формат вывода: имя_пакета|описание
# Аргументы командной строки: <input.json> <output.txt>

import sys
import os
import re
from datetime import datetime

# Конфигурация
LOG_FILE = "extract.log"

# Функция для записи сообщений в лог и вывода на экран
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    with open(LOG_FILE, "a", encoding="utf-8") as log_f:
        log_f.write(log_entry + "\n")
    print(log_entry)

# Функция для проверки существования файла
def check_file(filepath):
    if not os.path.isfile(filepath):
        log_message(f"ОШИБКА: Файл '{filepath}' не существует.")
        sys.exit(1)

# Функция для экранирования символа | в описании
def escape_pipe(text):
    return text.replace("|", "\\|")

# Проверка аргументов командной строки
if len(sys.argv) != 3:
    log_message("ОШИБКА: Неверное количество аргументов. Использование: python3 extract_descriptions.py <input.json> <output.txt>")
    sys.exit(1)

input_json = sys.argv[1]  # Входной JSON-файл
output_file = sys.argv[2] # Выходной текстовый файл

# Инициализация файла логов
with open(LOG_FILE, "w", encoding="utf-8") as log_f:
    log_f.write("")
log_message("Начало выполнения скрипта.")

# Проверка существования входного JSON-файла
check_file(input_json)

# Инициализация выходного файла
with open(output_file, "w", encoding="utf-8") as f:
    f.write("")
log_message(f"Выходной файл '{output_file}' инициализирован.")

# Чтение JSON-файла как текста
log_message(f"Обработка JSON-файла: {input_json}")
try:
    with open(input_json, "r", encoding="utf-8") as f:
        json_text = f.read()
except Exception as e:
    log_message(f"ОШИБКА: Не удалось прочитать файл: {e}")
    sys.exit(1)

# Регулярное выражение для поиска пар "пакет": {... "description": "..." ...}
# Захватываем имя пакета и содержимое description, сохраняя экранированные символы
pattern = r'"([^"]+)":\s*\{[^}]*"description":\s*"((?:[^"\\]|\\.)*?)"'
matches = re.findall(pattern, json_text, re.DOTALL)

# Запись результатов
entry_count = 0
with open(output_file, "w", encoding="utf-8") as f:
    for package, description in matches:
        # Экранируем | в описании
        description = escape_pipe(description)
        # Записываем в формате пакет|описание
        f.write(f"{package}|{description}\n")
        entry_count += 1

log_message(f"Извлечено {entry_count} записей.")

# Проверка, что выходной файл не пустой
if os.path.getsize(output_file) == 0:
    log_message("ПРЕДУПРЕЖДЕНИЕ: Выходной файл пуст. Описания не были извлечены.")
else:
    log_message(f"Описания успешно записаны в '{output_file}'.")
    # Логирование первых трех строк вывода для отладки
    log_message("Пример вывода (первые 3 строки):")
    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()[:3]
        for line in lines:
            log_message(f"  {line.strip()}")

    # Проверка наличия экранированных символов
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        if re.search(r"\\", content):
            log_message("Экранированные символы (например, \\n, \\t) найдены в выводе, сохранены буквально.")
            log_message("Строки с экранированными символами:")
            for line in content.splitlines():
                if "\\" in line:
                    log_message(f"  {line.strip()}")
        else:
            log_message("Экранированные символы в выводе не найдены.")

log_message("Выполнение скрипта завершено.")
