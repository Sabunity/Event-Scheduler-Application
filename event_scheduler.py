# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 07:45:26 2024

@author: SabUnity Ltd
"""
import datetime


class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

def create_event(events):
    # Function to create a new event
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    date_str = input("Enter event date (YYYY-MM-DD): ")
    time_str = input("Enter event time (HH:MM): ")
    
    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return
    
    event = Event(title, description, date, time)
    events.append(event)
    print("Event created successfully!")

def list_events(events):
    # Function to list all events
    if not events:
        print("No events found.")
        return
    
    events.sort(key=lambda x: (x.date, x.time))
    for event in events:
        print(f"Title: {event.title}")
        print(f"Description: {event.description}")
        print(f"Date: {event.date}")
        print(f"Time: {event.time}")
        print()

def delete_event(events, title):
    # Function to delete an event by title
    for event in events:
        if event.title == title:
            events.remove(event)
            print("Event deleted successfully!")
            return
    print("Event not found.")

def search_events(events, query):
    # Function to search events by date, time, or keyword
    matching_events = []
    for event in events:
        if query in event.title or query in event.description:
            matching_events.append(event)
        elif query == event.date.strftime('%Y-%m-%d'):
            matching_events.append(event)
        elif query == event.time.strftime('%H:%M'):
            matching_events.append(event)
    return matching_events

def edit_event(events, title):
    # Function to edit an existing event
    for event in events:
        if event.title == title:
            print("\nOptions for editing:")
            print("1. Edit Title")
            print("2. Edit Description")
            print("3. Edit Date")
            print("4. Edit Time")
            choice = input("Enter your choice: ")
            if choice == '1':
                new_title = input("Enter new title: ")
                event.title = new_title
            elif choice == '2':
                new_description = input("Enter new description: ")
                event.description = new_description
            elif choice == '3':
                new_date = input("Enter new date (YYYY-MM-DD): ")
                event.date = datetime.datetime.strptime(new_date, '%Y-%m-%d').date()
            elif choice == '4':
                new_time = input("Enter new time (HH:MM): ")
                event.time = datetime.datetime.strptime(new_time, '%H:%M').time()
            else:
                print("Invalid choice. No changes made.")
            break
    else:
        print("Event not found.")

def main():
    # The main function to control the entire app
    events = []
    while True:
        print("\nOptions:")
        print("1. Create Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Event")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_event(events)
        elif choice == '2':
            list_events(events)
        elif choice == '3':
            title = input("Enter the title of the event to delete: ")
            delete_event(events, title)
        elif choice == '4':
            query = input("Enter search keyword, date (YYYY-MM-DD), or time (HH:MM): ")
            matching_events = search_events(events, query)
            if matching_events:
                print("Matching Events:")
                list_events(matching_events)
            else:
                print("No matching events found.")
        elif choice == '5':
            title = input("Enter the title of the event to edit: ")
            edit_event(events, title)
        elif choice == '6':
            print("Thank you for choosing our App! Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()