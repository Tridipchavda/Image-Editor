import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
import random
import math
import requests
import datetime
import time
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wikipedia
from selenium.webdriver import ActionChains
from matplotlib import pyplot
import numpy as np
import cv2
import pyautogui
import keyboard
from geopy.geocoders import Nominatim
import folium
import smtplib

engine = pyttsx3.init()

"""
    Search Any File in Desktop
    Search any song
    Play song
    Select Random numbers
    Plot a Graph by giving equation
    Search any query on google, youtube
    Search any meaning and speak it
    Wikipedia on any topic
    Convert file to pdf
    Can create any type of file
    Solve Quadratic Roots equation
    Give weather report of any place
    Login to facebook and insta with any id
    send mails to person
    Generate password by itself
    Can ShutDown the system
    Search Buses from one place to another
    Search route from google maps
    Read any type of txt file in specific folder
    Can identify faces from image
    Can convert txt to handwriting
    Connect to saved WI-FI network
    Show Nearby Networks
    open cmd
    Add, Multiply, Subtract any type of numbers
    Differenciate simple function
"""

mail_dictonary = {
    'mummy':'chavdagirish489@gmail.com',
    'mom':'chavdagirish489@gmail.com',
    'mum':'chavdagirish489@gmail.com',
    'papa':'chavdagirish489@gmail.com',
    'archit':'architsc21@gmail.com',
    'amit sir':'amit.rathod@vgceg.ac.in',
    'vinod sir':'vdthummar@vgecg.ac.in',
    'me':'chavdatridip007@gmail.com'
}
def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<=12):
        Speak("Good Morning Sir")
    elif(hour>=12 and hour<=16):
        Speak("Good Afternoon Sir")
    else:
        Speak("Good Evening Sir")
    
    Speak(" How may i help you ?")

def Command():
    jarvis = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        jarvis.pause_threshold =1;
        audio=jarvis.listen(source)
    try:
        print("Recognizing..")
        query=jarvis.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
        return query

    except Exception as e:
        plotgraph()
        print("No command found from user")
        Speak("No command found from user")

continuer = 0
confirm = 0

def FindWord():
    file = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File")

    word = input("Type the word you want to search :")
    content = open(file ,"r")
    result = content.read()
        
    if word in result.lower():
        return True
    else:
        return False

def Find(Path,to_find):
    global continuer,confirm
    
    continuer = 0
    os.chdir(Path)
   
    for files in os.listdir():
        if(confirm==1):
            print(os.path.join(os.getcwd(),to_find))
            confirm+=1
            break        
        if(confirm==2):
            break
        if "." in files:
            continuer+=1
            try:
                if files == to_find:    
                    confirm=1
            except:
                continue
   
        else:
            if(confirm==1):
                break
            try:
                please = os.path.join(Path,files)
                os.chdir(please)
               
                Find(os.getcwd(),to_find)
                a = os.listdir()          

                if(continuer==len(files)):
                    os.chdir(please)

            except:
                continue

def Solve_roots(a,b,c):
    D = (b*b) - (4*a*c)
    print(f"The discriminant is {D}")

    if D>0:
        alpha = (-b+math.sqrt(D))/(2*a)
        beta = (-b-math.sqrt(D))/(2*a)
        alpha = round(alpha,2)
        beta = round(beta,2)
        print(f"The Roots of the quadratic equation are {alpha} and {beta}")
        Speak(f"The Roots of the quadratic equation are {alpha} and {beta}")
    elif D==0:
        beta = (-b-sqrt(D))/(2*a)
        beta = round(beta,2)
        print(f"The Root of the quadratic equation is {beta}")
        Speak(f"The Root of the quadratic equation is {beta}")
    else:
        print(f"The Roots of the quadratic equation are not possible")
        
        Speak(f"The Roots of the quadratic equation are not possible")   

def log_in_fb(username1,password1):
    
    PATH = 'C:/Users/tridip/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'
    drive= webdriver.Chrome(PATH)
    
    drive.get("https://www.facebook.com/")
    
    
    user_ = drive.find_element_by_name('email')
    user_.send_keys(username1)

    pass_ = drive.find_element_by_name('pass')
    pass_.send_keys(password1)
    pass_.submit()

    Speak("login successful ")


def log_in_insta(username1,password1):
    
    PATH = 'C:/Users/tridip/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'
    drive= webdriver.Chrome(PATH)
    
    drive.get("https://www.instagram.com/")
    time.sleep(2)
    user_ = drive.find_element_by_name('username')
    user_.send_keys(f"{username1}")

    pass_ = drive.find_element_by_name('password')
    pass_.send_keys(f"{password1}")
    pass_.submit()
    time.sleep(5)
    try:
        confirm = drive.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
        confirm.click()
        Speak("Login succesfull ")
    except Exception as e:
        Speak("login Failed ")
        print(e)
def Create_file():
    if query.startswith("create text file "):
        query = query.split("create text file ")
        s = open(f"C:/Users/tridip/Desktop/A.I/Builded_file/{query[1]}.txt","w+")
        print(f"File {query[1]}.txt is created succesfully")
    elif query.startswith("create python file "):
        query = query.split("create python file ")
        s = open(f"C:/Users/tridip/Desktop/A.I/Builded_file/{query[1]}.py","w+")
        print(f"File {query[1]}.py is created succesfully")
    elif query.startswith("create pdf file "):
        query = query.split("create pdf file ")
        s = open(f"C:/Users/tridip/Desktop/A.I/Builded_file/{query[1]}.pdf","w+")
        print(f"File {query[1]}.pdf is created succesfully")
    elif query.startswith("create image file "):
        query = query.split("create image file ")
        s = open(f"C:/Users/tridip/Desktop/A.I/Builded_file/{query[1]}.png","w+")
        print(f"File {query[1]}.png is created succesfully")
        
def Enter_details():
    Speak("Please Enter your insta id")
    a=input("Please Enter your insta id :")
    if(len(a) != 0):

        Speak("Please Enter your insta password")
        b=input("Please Enter your insta password :")
        if(len(b) != 0):
            log_in_insta(a,b)
        else:
            print("please Enter a valid password ")
            Enter_details()
    else:
        print("please Enter a valid username ")
        Enter_details()

    
def Route_A_B(query):
    try:
        query1 = query[1].split(" to ")
        print(query1[0])
        print(query1[1])

        PATH = 'C:/Users/tridip/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'

        driver= webdriver.Chrome(PATH)
        driver.get("https://www.google.co.in/maps/@22.4168315,71.319661,7z")
        time.sleep(1)

        A = driver.find_element_by_class_name("tactile-searchbox-input")
        A.send_keys(query1[1])
        time.sleep(2)
        
        direction = driver.find_element_by_id("searchbox-directions")
        direction.click()
        time.sleep(3)

        
        keyboard.write(query1[0])
        keyboard.press('enter')

    except Exception as e:
        print(e)
        print("Please define your route properly")
        Speak("Pleas3 define your route properly")

def Buses_A_B(query):
    
    
   
    query1 = query[1].split(" to ")
        
    final1 = query1[0].replace(" ",",")
    final2 = query1[1].replace(" ",",")
    print(final1)
    print(final2)

    PATH = 'C:/Users/tridip/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'

    driver= webdriver.Chrome(PATH)
    driver.get("https://www.redbus.in/")
    time.sleep(1)
        
    A = driver.find_element_by_class_name("db")
    A.send_keys(query1[0])
    time.sleep(1)

    B = driver.find_element_by_id("dest")
    B.send_keys(query1[1])
    time.sleep(1)
            
    C = driver.find_element_by_id("search_btn")
    C.click()
    time.sleep(1)

    D = driver.find_element_by_class_name("current.day")
    D.click()
    time.sleep(1)

    C.click()
    Speak('Search successful')

    

    
def Weather_report(nested):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=aa6495514a361e8e4cc74128df69e452&q='

    final = api_address + nested
    json_data = requests.get(final).json()

    formated0 = json_data['name']
    formated1 = json_data['coord']['lon']
    formated2 = json_data['coord']['lat']
    formated3 = json_data['weather'][0]['description']
    formated4 = json_data['weather'][0]['main']
    formated5 = json_data['main']['temp']
    formated6 = json_data['main']['pressure']
    formated7 = json_data['main']['humidity']
    formated8 = json_data['visibility']

    print("City :"+formated0)
    print("Longitude :"+str(formated1))
    print("latitude :"+str(formated2))
    print("Weather Type :"+formated4)
    print("Description :"+formated3)
    print("Temperature :"+str(int(formated5)-273))
    print("Pressure :"+str(formated6))
    print("Humidity :"+str(formated7))
    print("Visibility :"+str(formated8))
            
    Speak(f"City name {formated0} Latitude {formated2} Longitude {formated1} ")
    Speak(f"Weather report {formated4}")
    Speak(f"Description {formated3}")
    Speak(f"Temperature {int(formated5)-273} degree celsius Pressure {formated6}")
    Speak(f"Humidity is {formated7} Visibility {formated8}")
    
def plot_graph():
    inp1 = input("Enter the equation :")
    if (len(inp1) != 0):
        inp1 = inp1.split(' = ')
        print(inp1[1])
        if "^" in inp1[1]:
            var = inp1[1].split('^')
            
            if '+' in var[1]:
                num = var[1].split(" + ")
                ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                if ("/" in num[0]):
                    num1 = num[0].split("/")
                    for i in range(21):
                        ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) + int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
                for i in range(21):
                    ex2[i] = ex1[i]**int(num[0]) + int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            elif '-' in var[1]:
                num = var[1].split(" - ")
                ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                if ("/" in num[0]):
                    num1 = num[0].split("/")
                    for i in range(21):
                        ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) - int(num[1])
                    pyplot.plot(ex1,ex2)
                    pyplot.show()
                for i in range(21):
                    ex2[i] = ex1[i]**int(num[0]) - int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            elif '*' in var[1]:
                num = var[1].split(" * ")
                ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                if ("/" in num[0]):
                    num1 = num[0].split("/")
                    for i in range(21):
                        ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) * int(num[1])
                    pyplot.plot(ex1,ex2)
                    pyplot.show()
                for i in range(21):
                    ex2[i] = ex1[i]**int(num[0]) * int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            elif '/' in var[1]:
                num = var[1].split(" / ")
                ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                if ("/" in num[0]):
                    num1 = num[0].split("/")
                    for i in range(21):
                        ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) / int(num[1])
                    pyplot.plot(ex1,ex2)
                    pyplot.show()
                for i in range(21):
                    ex2[i] = ex1[i]**int(num[0]) / int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            else:
                var = inp1[1].split('^')
                ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
                for i in range(21):
                    ex2[i] = ex1[i]**int(var[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
def Search_engine(query):
    if query.endswith('youtube'):
        if query.endswith('in youtube'):
            final = semi_final[1].split('in youtube')
            print(final[0])
            driver.get("https://www.youtube.com/")

            search = driver.find_element_by_name('search_query')
            search.send_keys(final[0])

            button = driver.find_element_by_id('search-icon-legacy')
            button.click()
        else:
            final = semi_final[1].split('youtube')
            print(final[0])
            driver.get("https://www.youtube.com/")

            search = driver.find_element_by_name('search_query')
            search.send_keys(final[0])

            button = driver.find_element_by_id('search-icon-legacy')
            button.click()
    elif query.endswith('google'):
        if query.endswith('in google'):
            final = semi_final[1].split('in google')
            print(final[0])
            driver.get("https://www.google.co.in/webhp")

            search = driver.find_element_by_name('q')
            search.send_keys(final[0])
            search.submit()
        else:
            final = semi_final[1].split('google')
            print(final[0])
            driver.get("https://www.google.co.in/webhp")

            search = driver.find_element_by_name('q')
            search.send_keys(final[0])
            search.submit()
    elif query.endswith(' to buy'):
        final = semi_final[1].split(' to buy')
        print(final[0])

        driver.get("https://www.amazon.com")
        time.sleep(0.4)
                
        search = driver.find_element_by_id('twotabsearchtextbox')
        search.send_keys(final[0])
        search.submit()

        driver.execute_script("window.open('about:blank','tab2');")
        driver.switch_to.window("tab2")

        driver.get("https://www.flipkart.com")
        time.sleep(0.4)
                
        search = driver.find_element_by_name('q')
        search.send_keys(final[0])
        search.submit()

                
    elif query.endswith('near me'):
        final = semi_final[1].split('near me')
        print(final[0])

        driver.get("https://www.google.co.in/maps/@22.4168315,71.319661,7z")
        time.sleep(3)

        location = driver.find_element_by_id("widget-mylocation")
        location.click()

        keyboard.press('enter')
        A = driver.find_element_by_class_name("tactile-searchbox-input")
        A.send_keys(semi_final[1])
        time.sleep(0.1)

        direction = driver.find_element_by_id("searchbox-searchbutton")
        direction.click()

    else:
        driver.get("https://www.google.co.in/webhp")
                
        search = driver.find_element_by_name('q')
        search.send_keys(semi_final[1])
        search.submit()
        if "meaning of" in query:
            try:
                info = driver.find_element_by_class_name("L1jWkf.h3TRxf")
                info1 = info.text
                Speak(info1)
                print(info1)
            except Exception as e:
                print(e)
if __name__ == "__main__":

    Wish()
    while True:
        
        query = Command().lower()
        
        #wishing
        if(query=="good morning" or query=="good evening" or query=="good afternoon"):
            Wish()
        #info_of_jarvis
        elif (query=="close" or query=="clause" or query=="close program" or query=="close the program"):
            break
        elif "tell me about yourself" in query:
            Speak("I am Jarvis Model number 5112,002 ,specially designed as AI")
        #about_time  
        elif "tell me the time" in query:
            h=str(datetime.datetime.now().hour)
            m=str(datetime.datetime.now().minute)
            Speak("The time is "+h+" hour and "+m+"minutes")
            print("The time is "+h+" hour and "+m+"minutes")
        #read_the_file
        elif "read the file " in query:
            final_path = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File")
            content = open(final_path ,"r")
            result = content.read()
            print(result)
            Speak(result)   
        #about_time
        elif "what's the time" in query:
            h=str(datetime.datetime.now().hour)
            m=str(datetime.datetime.now().minute)
            Speak("The time is "+h+" hour and "+m+"minutes")
            print("The time is "+h+" hour and "+m+"minutes")
        #about_time
        elif "what is the time" in query:
            h=str(datetime.datetime.now().hour)
            m=str(datetime.datetime.now().minute)
            Speak("The time is "+h+" hour and "+m+"minutes")
            print("The time is "+h+" hour and "+m+"minutes")
        #login_to_facebook
        elif "login to my facebook account" in query:
            log_in_fb("9727491924","78787788")
        #login_to_facebook
        elif "login to facebook account" in query:
            log_in_fb("9727491924","78787788")
        #login_to_facebook
        elif "login to facebook" in query:
            log_in_fb("9727491924","78787788")
        #findword from file:
        elif ("find the word" in query or "search the word" in query):
            print(FindWord())
        #generate password
        elif ("generate password" in query or "generate the password" in query):
            number = list(range(0,10))

            capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
                       "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            special = ["!","@","#","$","%","^","&","*","(","_",")","<",">","+","{","}","."]

            PASSWORD = ''
            for i in range(random.randint(8,15)):
               j = random.randint(1,3)
               if j==1:
                   PASSWORD = PASSWORD+str(number[random.randint(0,8)])
               elif j==2:
                   PASSWORD = PASSWORD+(capital[random.randint(0,51)])
               elif j==3:
                   PASSWORD = PASSWORD+(special[random.randint(0,16)])

            Speak("Your password is generated succesfully") 
            print(PASSWORD) 
                
        #play any music
        elif "search for song" in query:
            Speak("Enter the name of the song")
            song_name=input("Enter the name of song to search :")
            PATH = 'C:/Users/tridip/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'

            driver = webdriver.Chrome(PATH)
            driver.get("https://www.jiosaavn.com/")
            driver.maximize_window()
            time.sleep(2)

            pop_cancel = driver.find_element_by_class_name('c-btn.c-btn--senary.c-btn--tiny')
            pop_cancel.click()
            time.sleep(1)
            
            search_box = driver.find_element_by_class_name("rbt-input-main.form-control.rbt-input")
            search_box.send_keys(song_name)
            keyboard.press('enter')
            time.sleep(4)   

            new = driver.find_element_by_css_selector('span.o-snippet__action-final.o-icon-ellipsis.o-icon--xlarge.c-btn-overflow')
            new.click()
            time.sleep(2)
        
    
            x=new.location['x']
            y=new.location['y']

            pyautogui.moveTo(x-100,y+216)
            pyautogui.click()
            
        #shutdown PC
        elif "shut down my pc" in query:
            Speak("Are you sure")
            shutdown = input("Are you sure (y/n) :")
            if shutdown=="y":
                print("ShutDown Start")
                os.system("shutdown -s")
        #mail
        elif "mail to " in query:
            query = query.split("mail to ")
            name = query[1] 
            print(query[1])
            if query[1] in mail_dictonary:
                Speak('What message you want to convey')
                data=input('What message you want to convey :')
                server = smtplib.SMTP("smtp.gmail.com",587)
                server.ehlo()
                server.starttls()
                server.login("chavdatridip007@gmail.com","78787788")
                server.sendmail("architsc21@gmail.com",mail_dictonary[name],data)
                server.close()
            
        #select number random
        elif "select a number " in query:
            query = query.split("select a number from")
            numbers = query[1].split(" to ")
            number_1 = numbers[0]
            number_2 = numbers[1]
            rand_num = random.randint(int(number_1),int(number_2))

            Speak("I will choose "+str(rand_num)+" for this .")
            print("I will choose "+str(rand_num)+" for this .")
        elif "select number " in query:
            query = query.split("select number from")
            numbers = query[1].split(" to ")
            number_1 = numbers[0]
            number_2 = numbers[1]
            rand_num = random.randint(int(number_1),int(number_2))

            Speak("I will choose "+str(rand_num)+" for this .")
            print("I will choose "+str(rand_num)+" for this .")
        elif "choose number " in query:
            query = query.split("choose number from")
            numbers = query[1].split(" to ")
            number_1 = numbers[0]
            number_2 = numbers[1]
            rand_num = random.randint(int(number_1),int(number_2))


            Speak("I will choose "+str(rand_num)+" for this .")
            print("I will choose "+str(rand_num)+" for this .")
        elif "choose a number " in query:
            query = query.split("choose a number from")
            numbers = query[1].split(" to ")
            number_1 = numbers[0]
            number_2 = numbers[1]
            rand_num = random.randint(int(number_1),int(number_2))

            Speak("I will choose "+str(rand_num)+" for this .")
            print("I will choose "+str(rand_num)+" for this .")
        #search any file in desktop
        elif "search file" in query:
            user_input = input("Enter the file name here :")
            Path = '/Users/tridip/Desktop'

            Find(Path,user_input)            
        #show nearby networks
        elif ("show networks" in query or "show the networks" in query):
            p = subprocess.Popen(["cmd","/k","netsh wlan show networks"])
            p.wait()
        #connect to Wi-Fi
        elif ("connect to the home network" in query or "connect to me" in query):
            os.system("netsh wlan connect ssid=Me name=Me")
        #login_to_instagram
        elif "login to my instagram account" in query:
            log_in_insta("tridip_chavda","78787788")
        #login_to_instagram
        elif "login to my instagram" in query:
            log_in_insta("tridip_chavda","78787788")
        #login_to_instagram
        elif "login to instagram account" in query:
            Enter_details()
        #login_to_instagram
        elif "login to instagram" in query:
            Enter_details()
        #login_to_instagram
        elif "login to the instagram" in query:
            Enter_details()
        #open_google
        elif "open google" in query:
            browser=webbrowser.open("https://www.google.co.in/search")
        #open youtube
        elif "open youtube" in query:
             browser=webbrowser.open("https://www.youtube.com/")
        #open stackoverflow
        elif "open stack overflow" in query:
             browser=webbrowser.open("https://stackoverflow.com")
        #open cmd
        elif "open cmd" in query:
            webbrowser.open('C:\Windows\system32\cmd.exe')
        #find differenciation
        elif "find the differentiation" in query:
            import differenciation
        #create_file
        elif "create " in query:
            Create_file()

        #convert text to hand writing
        elif "convert text to handwriting" in query:
            Speak("Please Enter the text here ")
            print("Please Enter the text here : \n")
            print("(please write only one paragraph) \n")
            text=input()
            pywhatkit.text_to_handwriting(text,rgb=[0,0,0])
        #weather report
        elif query.startswith("give weather report "):
            city = query.split('give weather report of ')
            Weather_report(city[1])
        elif query.startswith("weather report " ):
            city = query.split('weather report of ')
            Weather_report(city[1])
        elif query.startswith("the weather report " ):
            city = query.split('the weather report of ')
            Weather_report(city[1])
        #detect the face
        elif "detect the face in image" in query:
            face_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            
            def detect_file():
                Speak("Enter the file name :")
                file = input("Enter the file name :")
                if file=='exit':
                    print("Exiting..")
                    
                elif(file != ''):
                    if(file.endswith(".jpg")):
                        try:
                            img = cv2.imread(f"C:/Users/tridip/Desktop/A.I/read_faces/{file}")
                            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            faces = face_file.detectMultiScale(img,1.1,11)
                            for (x,y,w,h) in faces:
                                cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0),2)
                            cv2.imshow('img',img)
                            cv2.waitKey()
                        except Exception as e:
                            Speak('File Does not exist')
                            print('File Does not exist')
                    
                        else:
                            Speak("Please Enter an existed file")
                            print("Please Enter an existed file")
                            detect_file()
                    else:
                        Speak("Please Enter the extention also (.jpg,.jpeg,.png)")
                        print("Please Enter the extention also (.jpg,.jpeg,.png)")
                        detect_file()
                else:
                    Speak("Please enter the file name")
                    print("Please enter the file name")
                    detect_file()

            detect_file()

        #locate place
        elif query.startswith("locate "):
            place = query.split("locate ")
            locator = Nominatim(user_agent="myGeocoder")        
            place_e = place[1].replace(" ",",")
            try:
                print(place_e)
                location = locator.geocode(f"{place_e}")
                print(location.latitude)
                print(location.longitude)
                map = folium.Map(location =[location.latitude,location.longitude])
                
                map.get_root().render()
                map.save("map.html")
                webbrowser.open("map.html")
            except:
                print("No such place found")
                Speak('No such place found')
        #txt_to_pdf
        elif query.startswith("convert file to pdf"):
            file_name = str(datetime.datetime.now().minute)
            opened_file = input("Enter file(.txt) name here :")
            webbrowser.open(opened_file)
            time.sleep(1)
            pyautogui.hotkey('ctrl','p')
            time.sleep(0.6)
            keyboard.press('enter')
            time.sleep(0.6)
            keyboard.write(file_name)
            keyboard.press('enter')
            time.sleep(1)
            Speak("File converted succesfully")
        #info_wikipedia
        elif query.startswith("wikipedia"):
            search = query.split('wikipedia')
            try:
                info =wikipedia.summary(search[1],sentences='3')
                Speak(info)
                print(info)
            except Exception as e:
                Speak(e)
        #ploting_a_graph
        elif (query=="plot the graph" or query=="plotagraph" or query=="plot a graph"):
            plot_graph()

        #From A to B
        elif query.startswith("find route from "):

            query = query.split("find route from ")
            Route_A_B(query)

        elif query.startswith("find the route from "):

            query = query.split("find the route from ")
            Route_A_B(query)

        elif query.startswith("find a route from "):

            query = query.split("find a route from ")
            Route_A_B(query)

        #Buses
        elif query.startswith("find buses from"):

            query = query.split("find buses from ")
            Buses_A_B(query)

        elif query.startswith("find bus from"):

            query = query.split("find bus from ")
            Buses_A_B(query)
        #add
        elif query.startswith("add "):
            add= query.split('add ')
            add1= add[1].split(' and ')
            try:
                if "." in query:
                    num1=float(add1[0])
                    num2=float(add1[1])
                    total=num1+num2
                    stotal=str(round(total))
                    print(total)
                    Speak(f"The Sum of {num1} and {num2} is approximately {stotal}")
                else:
                    num1=int(add1[0])
                    num2=int(add1[1])
                    total=num1+num2
                    stotal=str(total)
                    print(total)
                    Speak(f"The Sum of {num1} and {num2} is {stotal}")
            except Exception as e:
                print(e)    
                Speak("if you said '+' between two numbers ,,you should use'and' instead of '+'")
                Speak("Problem in addition, Invalid input ")
        #subtract
        elif query.startswith("subtract "):
            sub= query.split('subtract ')
            sub1= sub[1].split(' and ')
            try:
                if "." in query:    
                    num1=float(sub1[0])
                    num2=float(sub1[1])
                    total=num1-num2
                    stotal=str(round(total))
                    print(total)
                    Speak(f"The Subtract of {num1} and {num2} is approximately {stotal}")
                else:
                    num1=int(sub1[0])
                    num2=int(sub1[1])
                    total=num1-num2
                    stotal=str(total)
                    print(total)
                    Speak(f"The Subtract of {num1} and {num2} is {stotal}")
            except Exception as e:
                print(e)    
                Speak("if you said '-' between two numbers ,,you should use 'and' instead of '-'")
                Speak("Subtraction of this numbers are not possible ")
        #multiply
        elif query.startswith("multiply "):
            mul= query.split('multiply ')
            mul1= mul[1].split(' and ')
            try:
                if "." in query:
                    num1=float(mul1[0])
                    num2=float(mul1[1])
                    total=num1*num2
                    
                    stotal=str(round(total))
                    print(total)
                    Speak(f"The Product of {num1} and {num2} is approximately {stotal}")
                else:
                    num1=int(mul1[0])
                    num2=int(mul1[1])
                    total=num1*num2
                    
                    stotal=str(total)
                    print(total)
                    Speak(f"The Product of {num1} and {num2} is {stotal}")
            except Exception as e:
                print(e)    
                Speak("if you said '*' between two numbers ,,you should use 'and' instead of '-'")
                Speak("Product of this numbers are not possible ")
        #roots of the quadratic equation
        elif "find the roots of the quadratic equation" in query:
            sentence=query.split("find the roots of the quadratic equation ")
            main=sentence[1]
            print(sentence[1])
            
            try:
                main1=main.split("coefficients are")
                A=main1[1][1]
                B=main1[1][2]
                C=main1[1][3]
                A1=int(A)
                B1=int(B)
                C1=int(C)
                Solve_roots(A1,B1,C1)
            except Exception as e:
                print(e)
                Speak("Please enter the valid coefficents")
        #play_music
        elif ("play music" in query or "play songs" in query):
            dir_music="F:/New 2016"
            music=os.listdir("F:/New 2016")
            print(len(music))
            random_num =random.randint(0,len(music))
            os.startfile(os.path.join(dir_music,music[random_num]))
        #searching    
        elif "search for "in query:
            PATH = 'C:/Users/tridip/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'
            semi_final = query.split("search for ")
            print(semi_final[1])
            driver= webdriver.Chrome(PATH)

            Search_engine(query)

        time.sleep(5)



