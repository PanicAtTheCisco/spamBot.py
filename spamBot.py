import pyautogui, time, os

print("Online.\n")
time.sleep(1)

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    path += "\Text Files"   #<-- is the path to the directory where text files are stored for spamming

    files = findFiles(path)         #<-- finds the files in the 'Text Files' directory
    file = pickFile(files, path)  #<-- allows the user to select which file to use

    print("Running...")

    time.sleep(5)     #<-- gives the user time to switch to whatever application they want to use the program on and can be changed as needed

    f = open(file, 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(1.25)     #<-- can be changed as needed

def findFiles(path):
    return [f for f in os.listdir(path) if f.endswith('.txt')]
    
def pickFile(files, path):
    i = 0
    for file in files:
        print(i, ": ", file, "\n")
        i = i + 1

    pick = int(input("Enter file number: "))
    path += "\\"
    return str(path + files[pick])

main()
