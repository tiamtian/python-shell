import os
def run(**args):
    print("[*] in dirlister module.")
    files = os.listdir(".")

    return str(files)