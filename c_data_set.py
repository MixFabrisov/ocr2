import shutil
import os

charchest = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", 
            "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

# Каталог с набором данных
data_dir = 'Cyrillic_jpeg_shift_rotate'
# Каталог с данными для обучения
train_dir = 'train'
# Каталог с данными для проверки
val_dir = 'val'
# Каталог с данными для тестирования
test_dir = 'test'
# Часть набора данных для тестирования
test_data_portion = 0.2
# Часть набора данных для проверки
val_data_portion = 0.1
# Количество элементов данных в одном классе
nb_images = 2752

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    for name in charchest:
        os.makedirs(os.path.join(dir_name, name))


create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)

def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index):
        for char in charchest:
            shutil.copy2(os.path.join(source_dir, char + "/" + char + str(i) + ".jpeg"), 
                        os.path.join(dest_dir, char))



start_val_data_idx = int(nb_images * (1 - val_data_portion - test_data_portion))
start_test_data_idx = int(nb_images * (1 - test_data_portion))
print(start_val_data_idx)
print(start_test_data_idx)

copy_images(0, start_val_data_idx, data_dir, train_dir)
copy_images(start_val_data_idx, start_test_data_idx, data_dir, val_dir)
copy_images(start_test_data_idx, nb_images, data_dir, test_dir)

