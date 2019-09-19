# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import pymongo
from pymongo import MongoClient
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):
#
     def name(self) -> Text:
        return "action_hello_world"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        data = db.infosys
        inf = data.find()
        for item in inf:
            a=item["name"]
            b=item["package"]
            c=item["bond"]
            print(a)
        
        response = """name is {} and package is {} and bond is {}""".format(a,c,b)
        dispatcher.utter_message(response)

        return []
class ActionPackagebond(Action):
#
     def name(self) -> Text:
        return "action_packagebond"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        inf = data.find(myquery)
        for item in inf:
            a=item["name"]
            b=item["package"]
            c=item["bond"]
            print(a)
        
        response = """name is {} and package is {} and bond is {}""".format(a,c,b)
        dispatcher.utter_message(response)

        return []
