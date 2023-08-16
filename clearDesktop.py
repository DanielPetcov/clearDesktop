import os

desktop = "~/Desktop/path"

desktop_path = os.path.expanduser(desktop)

files_on_desktop = os.listdir(desktop_path)

for file_name in files_on_desktop:
    file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile:
        os.remove(file_path)
        print(f"Deleted: {file_name}")

print("All files on the desktop have been deleted.")
