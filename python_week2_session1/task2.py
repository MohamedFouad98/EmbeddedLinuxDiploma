import time
import pyautogui

# Function to open Visual Studio Code
def open_vscode():
    pyautogui.press('win')  # Press the Windows key
    time.sleep(2)
    pyautogui.write('Visual Studio Code')  # Search for VSCode
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)  # Wait for VSCode to open
    
def install_extension(extension_name):
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(5)
    pyautogui.write(f"ext install {extension_name}")
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(10)  # Wait for extension installation to complete
    '''
    Main function
    '''
def main():
    open_vscode()
    extensions = [
        "llvm-vs-code-extensions.vscode-clangd",
        "matepek.vscode-catch2-test-adapter",
        "amiralizadeh9480.cpp-helper",
        "twxs.cmake",
        "ms-vscode.cmake-tools"
     ]
    for extension in extensions:
       install_extension(extension)
    print("Downloading extensions is done")   
     

if __name__ == "__main__":
    main()