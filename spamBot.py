import pyautogui, time

def main():
    script = input("Enter text file path: ")     #<-- use '.txt' files as the program reads them easier
    #note: you will need to copy the file path of the file to use it unless it is in the same folder as this program
    print("Running...")

    time.sleep(5)     #<-- gives the user time to switch to whatever application they want to use the program on and can be changed as needed

    f = open(script, 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(1.25)     #<-- can be changed as needed

print("Online.")
time.sleep(1)

main()
