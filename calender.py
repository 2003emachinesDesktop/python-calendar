import sqlite3
import calendar

from datetime import date

text_calendar = calendar.TextCalendar()



con = sqlite3.connect("calendar.db")
cur = con.cursor()


cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE IF NOT EXISTS calendar(" \
"id INTEGER PRIMARY KEY AUTOINCREMENT, " \
"year INTEGER," \
"month TEXT," \
"day INTEGER)" \
)

cur.execute("CREATE TABLE IF NOT EXISTS events(" \
"id INTEGER PRIMARY KEY ,"
#"id INTEGER PRIMARY KEY AUTOINCREMENTS"
"start_day INTEGER,"
"end_day INTEGER,"
"event_name TEXT,"
"start_time TEXT,"
"end_time TEXT,"
#"FOREIGN KEY(id) REFERENCES calendar(id))"
"FOREIGN KEY(start_day) REFERENCES calendar(id))"
)

con.commit()



print("welcome to your calendar:")



#"""
while True:
    print("type 1 to display calendar, 2 to see saved events, or 3 to create a new event")
    
    value=input("input:")


    if value == "1":
        current_date = date.today()

        current_year = current_date.year

        text_calendar.pryear(current_year)


#"""    
    elif value == "2":
        print("will fix later")

#"""
    elif value == "3":
        print("please input event details to save to calendar")

        event_name = input('event name:')
        year = input('year in YYYY format:')
        month = input('month in MM format:')
        start_date = input('event date in DD format:')
        start_time = input('start time:')
        end_date = input('end date in DD format:')
        end_time = input('end time:')


        cur.execute("INSERT INTO calendar(year, month, day) VALUES (?,?,?)",(year, month, start_date))
        calendar_id = cur.lastrowid

        cur.execute("INSERT INTO events(id,start_day, end_day, event_name, start_time, end_time) VALUES (?,?,?,?,?,?)",(calendar_id, start_date,end_date, event_name, start_time, end_time))
        cur.execute("INSERT INTO events(start_day, end_day, event_name, start_time, end_time) VALUES (?,?,?,?,?)",(calendar_id, end_date, event_name, start_time, end_time))


        print("thanks, your event has been saved")

    #con.commit()
    #con.close()
#"""