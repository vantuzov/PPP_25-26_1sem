

if __name__ == "__main__":
    import os

trace = []

def walk_dir(path, level=0):
    indent = "  " * level
    current_indent = "  " * (level - 1) if level > 0 else ""

    trace.append(f'{current_indent}Заходим в: {path}')

    structure = {"path": path, "dirs": [], "files": []}

    try:
        items = os.listdir(path)
    except PermissionError:
        print(f'{indent}Нет доступа: {path}')
        trace.append(f'{indent}Нет доступа: {path}')
        return structure

    dirs = []
    files = []

    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            dirs.append(item)
        else:
            files.append(item)

    if level == 0:
        print(f'Папка: "{path}"; Папок в ней: {dirs}; Файлов в ней: {files}')
    else:
        print(f'{indent}Папка: "{path}"; Папок в ней: {dirs}; Файлов в ней: {files}')

    for file in files:
        structure["files"].append(file)
        trace.append(f'{indent}Файл: {os.path.join(path, file)}')

    for dir_item in dirs:
        full_path = os.path.join(path, dir_item)
        trace.append(f'{indent}Каталог: {full_path}')
        sub_structure = walk_dir(full_path, level + 1)
        structure["dirs"].append(sub_structure)

        if not sub_structure["dirs"] and not sub_structure["files"]:
            print(f'{indent}  Пустая папка: {full_path}')

    trace.append(f'{current_indent}Выходим из: {path}')

    return structure

root = "."
print("Обход каталога:")
result = walk_dir(root)
