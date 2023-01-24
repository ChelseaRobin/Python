from datetime import datetime

def getDate():
    # current datetime
    now = datetime.now()
    current_date = now.date()
    return current_date

def addDate(file, current_date):
    file.write(f'{current_date}    ')

def addLines(file, playerName, rounds):
    file.write(f'{playerName}    ')
    file.write(f'{rounds} \n')