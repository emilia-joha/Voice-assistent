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


def easy_movement_1():
    respond("Time to move for a bit.")
    time.sleep(0.5)
    respond("jump 3 times")

def fun():
    pass

def time_check_movement(movement):
    strTime=datetime.datetime.now().strftime("%M")

    if strTime== "05" and movement=="easy" or strTime == "15" and movement=="easy" or strTime == "25" and movement=="easy" or strTime == "35" and movement=="easy"or strTime == "45" and movement=="easy" or strTime == "55" and movement=="easy":
        easy_movement_1()
    

def time_check_routine():
    strTime=datetime.datetime.now().strftime("%H:%M")

    if strTime== "08:00:
        respond("It's time to get up.")
    
    elif strTime== "12:00":
        respond("It's time to have a break and eat som lunch.")

    elif strTime== "15:00":
        respond("It's time to have a short break.")

    elif strTime== "16:30:00":
        respond("You have done a good job today, time to put it aside.")


def time_check_drink():
    strTime=datetime.datetime.now().strftime("%M")
    
    if strTime== "08" or strTime == "18" or strTime == "28" or strTime == "38"or strTime == "48" or strTime == "58":
        respond("Don't forget to drink a glass of water")

def time_check_fun():
    strTime=datetime.datetime.now().strftime("%M")
    
    if strTime== "09" or strTime == "19" or strTime == "29" or strTime == "39"or strTime == "49" or strTime == "59":
        fun()


def check(movement):
    schedule.every(1).minutes.do(time_check, movement)
    schedule.every(1).minutes.do(time_check_routine)
    schedule.every(1).minutes.do(time_check_drink)
  
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
    output="Hi, my name is Pingu. I will help you with your daily routines. "
    respond(output)
          
    while(1):
        respond("First you have to select movement difficulty; easy, medium or hard.")
        text=talk().lower()
        
        if text==0:
            continue
            
        if "easy" in text:
            respond("You will have the easy movment program over the day.")
            check("easy")
            
            
        elif "medium" in text:
            respond("You will have the medium movment program over the day.")
            check("medium")

        elif "hard" in text:
            respond("You will have the hard movment program over the day.") 
            check("hard")
        
        else:
           respond("This program is not available")