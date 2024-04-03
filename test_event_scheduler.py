# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:55:22 2024

@author: SabUnity Ltd
"""
import unittest
import datetime
from event_scheduler import *

# Event class definition here

class TestEventScheduler(unittest.TestCase):
    def setUp(self):
        self.events = []
    
    def test_create_event(self):
        # Test creating a new event
        create_event(self.events)
        self.assertEqual(len(self.events), 1)

    def test_delete_event(self):
        # Test deleting an event
        event = Event("Test Event", "Test Description", datetime.date.today(), datetime.time(12, 0))
        self.events.append(event)
        delete_event(self.events, "Test Event")
        self.assertEqual(len(self.events), 0)

    def test_search_events(self):
        # Test searching events by title
        event1 = Event("Event 1", "Description 1", datetime.date.today(), datetime.time(12, 0))
        event2 = Event("Event 2", "Description 2", datetime.date.today(), datetime.time(12, 0))
        self.events.extend([event1, event2])
        matching_events = search_events(self.events, "Event")
        self.assertEqual(len(matching_events), 2)

    def test_edit_event(self):
        # Test editing an event
        event = Event("Test Event", "Test Description", datetime.date.today(), datetime.time(12, 0))
        self.events.append(event)
        edit_event(self.events, "Test Event")
        self.assertEqual(self.events[0].title, "New Title")

if __name__ == "__main__":
    unittest.main()
