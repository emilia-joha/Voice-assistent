import speech_recognition as sr
import datetime
from playsound import playsound
from gtts import gTTS
import os
import schedule
import time
import random
import json


def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
    
    try:
        data=input.recognize_google(audio)
        print("your question is, " + data)
    except sr.UnknownValueError:
        respond("Sorry I did not hear your question, please repeat again.")
    
    return data


def easy_movement_file():
    try:
        with open("easy_movement.json") as movement_file:
            movements=json.load(movement_file)
            return movements
            
    except:
        print("Tyvärr gick inte filen att öppna.")
        exit()


def medium_movement_file():
    try:
        with open("medium_movement.json") as movement_file:
            movements=json.load(movement_file)
            return movements
    
    except:
        print("Tyvärr gick inte filen att öppna.")
        exit()


def hard_movement_file():
    try:
        with open("hard_movement.json") as movement_file:
            movements=json.load(movement_file)
            return movements
            

    except:
        print("Tyvärr gick inte filen att öppna.")
        exit()


def joke_file():
    try:
        with open("joke.json") as joke_file:
            jokes=json.load(joke_file)
            return jokes
    
    except:
        print("Tyvärr gick inte filen att öppna.")
        exit()


def random_func(dictio):
    random_thing=random.choice(list(dictio))
    return random_thing


def easy_movement():
    movement_dict=easy_movement_file()
    random_movement=random_func(movement_dict)
    random_movement_str=movement_dict[random_movement]["movement"]

    respond(random_movement_str)
    time.sleep(20)
    respond("Good job!")

def medium_movement():
    movement_dict=medium_movement_file()
    random_movement=random_func(movement_dict)
    random_movement_str=movement_dict[random_movement]["set"]

    respond(random_movement_str)
    time.sleep(30)
    respond("well done!")


def hard_movement():
    movement_dict=hard_movement_file()
    random_movement=random_func(movement_dict)
    random_movement_str=movement_dict[random_movement]["set"]

    respond(random_movement_str)
    time.sleep(15)
    respond("wow, what a super job!")


def fun():
    joke_dict=joke_file()
    random_joke=random_func(joke_dict)
    random_joke_question=joke_dict[random_joke]["joke"]
    random_joke_answer=joke_dict[random_joke]["answer"]

    respond("Do you want to hear something fun?")
    time.sleep(0.5)
    respond(random_joke_question)

    if random_joke_answer != " ":
        respond(random_joke_answer)
        respond("ha ha ha")


def time_check_movement(movement):
    strTime=datetime.datetime.now().strftime("%M")

    if strTime== "05" and movement=="easy" or strTime == "15" and movement=="easy" or strTime == "25" and movement=="easy" or strTime == "35" and movement=="easy"or strTime == "45" and movement=="easy" or strTime == "55" and movement=="easy":
        easy_movement()
    elif strTime== "05" and movement=="medium" or strTime == "15" and movement=="medium" or strTime == "25" and movement=="medium" or strTime == "35" and movement=="medium"or strTime == "45" and movement=="medium" or strTime == "55" and movement=="medium":
        medium_movement()

    elif strTime== "05" and movement=="hard" or strTime == "15" and movement=="hard" or strTime == "25" and movement=="hard" or strTime == "35" and movement=="hard"or strTime == "45" and movement=="hard" or strTime == "55" and movement=="hard":
        hard_movement()

def time_check_routine():
    strTime=datetime.datetime.now().strftime("%H:%M")

    if strTime== "08:00":
        respond("It's time to get up.")
    
    elif strTime== "12:00":
        respond("It's time to have a break and eat som lunch.")

    elif strTime== "15:00":
        respond("It's time to have a short break.")

    elif strTime== "16:30":
        respond("You have done a good job today, time to put it aside.")


def time_check_drink():
    strTime=datetime.datetime.now().strftime("%M")
    
    if strTime== "08" or strTime == "18" or strTime == "28" or strTime == "38"or strTime == "48" or strTime == "58":
        respond("Don't forget to drink a glass of water")
        fun()


def check(movement):
    schedule.every(1).minutes.do(time_check_movement, movement)
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
        