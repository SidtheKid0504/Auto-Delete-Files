import os
import time
import shutil

def main():
    path = input("Enter File Path: ")

    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown = True):
            for n in files:
                path = os.path.join(root, n)

                os.remove(path)
                print("Path Deleted")

            for n in dirs:
                path = os.path.join(root, n)

                shutil.rmtree(path)
                print("Path Deleted")

    else:
        print("Path Doesn't Exist")

if __name__ == "__main__":
    while True:
        main()