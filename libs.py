import os


def save_append_txt(file_name, data):
    with open(f"config\\{file_name}", 'a+') as f:
        f.write(f"{data}\n")
        f.close()


def open_folder(folder):
    os.system(f'start config\\{folder}')
