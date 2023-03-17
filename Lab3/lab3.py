from pathlib import Path

folder_name = input("folder name:")
folder = Path(folder_name)
if folder.is_dir():
    folder_count = len([1 for file in folder.iterdir()])

print(f"В папке {folder_name} есть {folder_count} объектов")