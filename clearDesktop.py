import os
import sys

print("**************************")
print("This program will delete all your desktop files.")

x = ""
while (x != "yes") and (x != "no"):
    x = str(input("Are you sure that you want to continue? (yes/no): "))
    x.lower()

if x == "no":
    print("program ended.")
    sys.exit()

print("............")
print("\n")

desktop = "~/Desktop"

desktop_path = os.path.expanduser(desktop)
files_on_desktop = os.listdir(desktop_path)

for file_name in files_on_desktop:
    file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile:
        os.remove(file_path)
        print(f"Deleted: {file_name}")

print("All files on the desktop have been deleted.")
