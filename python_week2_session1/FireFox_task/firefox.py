# favorite_websites.py

import webbrowser

websites = {
    "google": "https://www.google.com",
    "youTube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com"
}

def open_website(url):
    firefox_path="C:/Program Files/Mozilla Firefox/firefox.exe %s"
    webbrowser.get(firefox_path).open(url)

def print_menu():
    print("Favorite Websites:")
    for index, site in enumerate(websites, start=1):
        print(f"{index}. {site}")

def open_favorite_website():
    print_menu()
    choice = (input("Enter the website you want to open: ")).lower()
    
    if choice in websites.keys():
    
     open_website(websites[choice])
    else:
        print("Invalid choice. Please select a valid option.")
