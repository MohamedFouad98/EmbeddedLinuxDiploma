import time
import pyautogui

def open_browser_and_mark_all_as_read():
    # Open the web browser 
    browser_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    point=[0,0]
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.write(browser_path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)  # Allow the browser to open

    # Navigate to Gmail 
    gmail_url = "https://mail.google.com"
    pyautogui.write(gmail_url)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)  # Allow Gmail to load

    
    pyautogui.click(199,161)
    time.sleep(2)
    pyautogui.click(233, 192)
    
    time.sleep(5)

def main():
    open_browser_and_mark_all_as_read()

if __name__ == "__main__":
    main()





