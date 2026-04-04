# main.py
from config import load_config
from create import create_table
from insert import insert_from_console, insert_from_csv
from update import update_data
from query import query_all, query_by_name
from delete import delete_by_name

# Загружаем конфиг
config = load_config()

# Создаём таблицу
create_table(config)

# Добавление данных
insert_from_console(config)
insert_from_csv(config, "data.csv")

# Вывод всех контактов
query_all(config)

# Обновление данных
update_data(config, "Ali", new_phone="999999999")

# Удаление по имени
delete_by_name(config, "Ali")

# Финальный вывод
query_all(config)