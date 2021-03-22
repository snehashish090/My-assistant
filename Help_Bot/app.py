"""
Made by Snehashish Laskar
Made on 22-03-2021
Developer contact: snehashish.laskar@gmail.com
Developer profile: https://github.com/snehashish090
This is  bot to interact with
"""

# Importing all the required modules
import smtplib, ssl
import pywhatkit
import wikipedia
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Listing my contacts
contact = ["dad", "mamu"]
contact_email = {"dad": "sumanlaskar1@gmail.com"}

# Defining a help funtion 
def Help():
    print("-------HELP-------")
    print("Hi I am AVA a bot ")
    print("I am here to help you")
    print("You can ask me to do a few things for you\n")
    print("-------HELP-------")

# Defining a function to send emails on the user's behalf
def sendmail():
    print("to whom sir?")
    command1 = input()
    if command1 in contact:
            print("what do you wanna say?")
            message = input()
            re1 = contact_email.get(command1)
            sender = "SENDER'S EMAIL ADRESS"
            password = "PASSWORD FOR SENDERS EMAIL"
            port = 465
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
                    server.login(sender, password)
                    server.sendmail(sender, re1, message)
                    print("done!")

# Defining a function that will play songs on YouTube
def play():
    song = ui.replace("play", "")
    print("Playing %s", song)
    pywhatkit.playonyt(song)

# Defining a function that will search wikipedia for you
def search():
    person = ui.replace("search for", "")
    info = wikipedia.summary(person, 2)
    print(info)

# Defining a function that will open spotify for me!
def spotify():
    webbrowser.open('http://open.spotify.com')

# Defining a function that will automatically create a new github repo for me
def Config():
    name = input("enter the name of the repo you want me to make: ")
    description = input("enter the description:")
    driver = webdriver.Firefox(
        "D:\\Programing\\Python\\Automation\\GitHub_Automation")
    driver.get("https://github.com/")
    driver.find_element_by_xpath(
        "/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()
    input1 = driver.find_element_by_xpath("//*[@id=\"login_field\"]")
    input1.send_keys("snehashish090")
    input2 = driver.find_element_by_id("password")
    input2.send_keys("snehashish08036")
    button1 = driver.find_element_by_xpath(
        "/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()
    button2 = driver.find_element_by_xpath(
        "/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a").click()
    input3 = driver.find_element_by_xpath("//*[@id=\"repository_name\"]")
    input3.send_keys(name)
    input4 = driver.find_element_by_xpath(
        "//*[@id=\"repository_description\"]")
    input4.send_keys(description)
    input5 = driver.find_element_by_xpath(
        "//*[@id=\"repository_auto_init\"]").click()
    driver.find_element_by_xpath(
        "/html/body/div[4]/main/div/form/div[4]/button").click()
    driver.find_element_by_xpath(
        "/html/body/div[4]/main/div/form/div[4]/button").click()

# Defining all the valid commands
commands = {"repo": Config, "open spotify" : spotify, "search for": search, "play": play, "Help":Help, "help": Help, "Hi": "Hello", "hi" : "Hi", "your name": "My name is AVA", "send an email": sendmail}

# Main Bot Algorithm
while True:
    # Getting user input
    ui = input(">")
    # Checking if the user input is a commands
    for i,j in  commands.items():
        if i in ui:
            # Executing a the function for the commands if the response isn't a string
            if type(j) != str:
                j()
            # Printing the response if there is no command associated
            else:
                print(j)

        