import selenium, os, time
from selenium import webdriver

ffd = input("Do you need to install Fire Fox? y/n >> ")

if ffd == "y":
    os.system('start firefox.exe')
    os.system('cls')
if ffd == "n":
    os.system('cls')

while True:
    driver = webdriver.Firefox()

    driver.get("https://google.com/")

    try:
        driver.delete_all_cookies()
    except:
        print()

    fmenu = input("Enter question you need an answer too >> ")

    ffmenu = fmenu.replace("+", "%2B")
    fffmenu = ffmenu.replace(" ", "+")
    ffffmenu = fffmenu.replace("/", "%2F")

    print("\nClearing Cookies...")

    try:
        driver.delete_all_cookies()
        print("\nCookies Cleared")
    except:
        print("\nNo Cookies to be deleted")

    try:
        driver.get(f"https://brainly.com/app/ask?q={ffffmenu}")
        exbr = input("Press enter when your done with the current session and ready for your next answer...")
        driver.close()
    except:
        print("Unable to open Brainly... Make sure the browser is open as you enter your question!")
        time.sleep(3.0)
    
    os.system('cls')
