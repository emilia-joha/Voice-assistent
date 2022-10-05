import speech_recognition as sr
import datetime
from playsound import playsound
from gtts import gTTS
import os
import schedule
import time


def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
    
    try:
        data=input.recognize_google(audio)
        print("your question is, " + data)
    except sr.UnknownValueError:
        print("Sorry I did not hear your question, please repeat again.")
    
    return data


def light_movement_1():
    respond("Time to move for a bit.")
    time.sleep(0.5)
    respond("jump 3 times")

def light_movement_2():
    pass

def medium_movement_1():
    pass

def medium_movement_2():
    pass

def hard_movement_1():
    pass

def hard_movement_2():
    pass


def time_check(movement):
    strTime=datetime.datetime.now().strftime("%H:%M")

    if strTime== "11:59" and movement=="light" or strTime == "15:00" and movement=="light":
        light_movement_1()
    
    elif strTime=="12:00" and movement=="light":
        light_movement_2()
    
    if strTime== "09:00" and movement=="medium" or strTime == "15:00" and movement=="medium":
        medium_movement_1()
    
    elif strTime=="12:00" and movement=="medium":
        medium_movement_2()
    
    if strTime== "09:00" and movement=="hard" or strTime == "15:00" and movement=="hard":
        hard_movement_1()
    
    elif strTime=="12:00" and movement=="hard":
        hard_movement_2()


def check(movement):
    schedule.every(1).minutes.do(time_check, movement)
  
    while True:
        schedule.run_pending()
        time.sleep(1)



def respond(output):
    print(output)
    response=gTTS(text=output, lang='en')
    file = os.path.dirname(__file__) + "\\" + "output.mp3"
    response.save(file)
    playsound(file)
    os.remove(file)


if __name__=='__main__':
    num=0
    output="Hi, my name is Polar Bear. I will help you with your daily routines. "
    respond(output)
          
    while(1):
        respond("First you have to select movement difficulty; light, medium or hard.")
        text=talk().lower()
        
        if text==0:
            continue
            
        if "light" in text:
            respond("You will have the light movment program over the day.")
            check("light")
            
            
        elif "medium" in text:
            respond("You will have the medium movment program over the day.")
            check("medium")

        elif "hard" in text:
            respond("You will have the hard movment program over the day.") 
            check("hard")
        
        else:
           respond("This program is not available")