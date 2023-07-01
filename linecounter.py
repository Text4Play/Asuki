import os

lines = 0

def count(dir):
    global lines
    for i in os.listdir(dir):
        if os.path.isfile(f"{dir}/{i}") and i.endswith(".py"):
            text = open(f"{dir}/{i}").read()
            lines += len(text.splitlines())
        elif os.path.isdir(i):
            count(f"{dir}/{i}")

if __name__ == '__main__':
    text = open("main.py").read()
    lines += len(text.splitlines())
    count("game")
    print(f"Total lines: {lines}")
    input()