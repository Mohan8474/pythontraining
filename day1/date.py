from datetime import datetime

def diff(bday,jday):
    date1 = datetime.strptime(bday, "%d.%m.%Y")
    date2 = datetime.strptime(jday, "%d.%m.%Y")

    if (date2 - date1).days >= 365 * 18:
        return True
    else:
        return False

def start():
    bday = '09.07.2000'
    jday = '18.11.2022'
    result = diff(bday,jday)
    print(result)

start()