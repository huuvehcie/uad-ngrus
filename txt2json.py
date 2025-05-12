#!/usr/bin/env python3

# Скрипт для обновления поля description в JSON-файле на основе второго столбца текстового файла
# Формат текстового файла: имя_пакета|описание
# Аргументы командной строки: <input.json> <input.txt> [<output.json>]
# Если output.json не указан, перезаписывается input.json

import json
import sys
import os
from datetime import datetime

# Конфигурация
LOG_FILE = "update_json.log"

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

# Функция для чтения текстового файла и создания словаря пакет:описание
def read_text_file(text_file):
    descriptions = {}
    with open(text_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "|" not in line:
                log_message(f"ПРЕДУПРЕЖДЕНИЕ: Некорректная строка в текстовом файле, пропущена: {line}")
                continue
            package, description = line.split("|", 1)
            # Восстанавливаем экранированный символ |, если он был
            description = description.replace("\\|", "|")
            descriptions[package] = description
    return descriptions

# Проверка аргументов командной строки
if len(sys.argv) not in [3, 4]:
    log_message("ОШИБКА: Неверное количество аргументов. Использование: python3 update_json_descriptions.py <input.json> <input.txt> [<output.json>]")
    sys.exit(1)

input_json = sys.argv[1]  # Входной JSON-файл
input_text = sys.argv[2]  # Входной текстовый файл
output_json = sys.argv[3] if len(sys.argv) == 4 else input_json  # Выходной JSON-файл (или перезапись входного)

# Инициализация файла логов
with open(LOG_FILE, "w", encoding="utf-8") as log_f:
    log_f.write("")
log_message("Начало выполнения скрипта.")

# Проверка существования входных файлов
check_file(input_json)
check_file(input_text)

# Чтение текстового файла
log_message(f"Чтение текстового файла: {input_text}")
try:
    descriptions = read_text_file(input_text)
except Exception as e:
    log_message(f"ОШИБКА: Не удалось прочитать текстовый файл: {e}")
    sys.exit(1)

log_message(f"Найдено {len(descriptions)} описаний в текстовом файле.")

# Чтение JSON-файла
log_message(f"Чтение JSON-файла: {input_json}")
try:
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    log_message(f"ОШИБКА: Не удалось прочитать JSON: {e}")
    sys.exit(1)

# Обновление описаний в JSON
updated_count = 0
for package in descriptions:
    if package in data and isinstance(data[package], dict) and "description" in data[package]:
        old_description = data[package]["description"]
        new_description = descriptions[package]
        data[package]["description"] = new_description
        updated_count += 1
        log_message(f"Обновлено описание для пакета '{package}':")
        log_message(f"  Старое: {old_description}")
        log_message(f"  Новое: {new_description}")
    else:
        log_message(f"ПРЕДУПРЕЖДЕНИЕ: Пакет '{package}' не найден в JSON или не имеет поля description, пропущен.")

# Проверка, были ли обновления
log_message(f"Обновлено {updated_count} описаний.")

# Запись обновленного JSON
log_message(f"Запись обновленного JSON в: {output_json}")
try:
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
except Exception as e:
    log_message(f"ОШИБКА: Не удалось записать JSON: {e}")
    sys.exit(1)

# Проверка наличия экранированных символов в выходном JSON
with open(output_json, "r", encoding="utf-8") as f:
    content = f.read()
    if "\\" in content:
        log_message("Экранированные символы (например, \\n, \\t) найдены в выходном JSON, сохранены буквально.")
        log_message("Пакеты с экранированными символами в описании:")
        for package, info in data.items():
            if isinstance(info, dict) and "description" in info and "\\" in info["description"]:
                log_message(f"  {package}: {info['description']}")
    else:
        log_message("Экранированные символы в выходном JSON не найдены.")

log_message("Выполнение скрипта завершено.")
