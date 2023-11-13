import random
import sqlite3
import speech_recognition as sr

# Function 
def randoming(board):
    lol = random.choice(board)
    return lol

def createTable(nameDB, nametable, column1, Type, column2, ):
    con = sqlite3.connect(nameDB)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {nametable} ({column1} {Type}, {column2} {Type});")
    con.commit()
    con.close()

def insert(nameDB, args1, args2 ):
    con = sqlite3.connect(nameDB)
    cur = con.cursor()
    cur.execute(f"INSERT INTO urls VALUES ('{args1}','{args2})")
    con.commit()
    con.close()

def cmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query} \n')
    except sr.UnknownValueError:
        query = str(input('Command: '))

    return query


