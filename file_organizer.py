from pathlib import Path
import shutil


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists():
        print("Folder does not exist.")
        return

    if not folder.is_dir():
        print("Please enter a folder path.")
        return

    organized = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        if file.name == Path(__file__).name:
            continue

        extension = file.suffix.lower()

        if not extension:
            category = "No Extension"
        else:
            category = extension[1:].upper()

        target_folder = folder / category
        target_folder.mkdir(exist_ok=True)

        target_file = target_folder / file.name

        if target_file.exists():
            print(f"Skipped duplicate: {file.name}")
            continue

        try:
            shutil.move(str(file), str(target_file))
            organized += 1
            print(f"Moved: {file.name} -> {category}/")
        except OSError as error:
            print(f"Could not move {file.name}: {error}")

    print(f"\nDone. Organized {organized} file(s).")


def main():
    print("File Organizer")
    print("Enter the path of the folder you want to organize.")

    folder_path = input("Folder path: ").strip().strip('"')

    if not folder_path:
        print("Folder path cannot be empty.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
