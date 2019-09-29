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
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s package is {} and bond is {}""".format(a,b,c)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("no data found")

       

        return []
class ActionLocationbond(Action):
#
     def name(self) -> Text:
        return "action_locationbond"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s  location is  {} and bond is {}""".format(a,d,c)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []
class ActionPackagelocation(Action):
#
     def name(self) -> Text:
        return "action_packagelocation"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s  location is  {} and package is {}""".format(a,d,b)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []
class ActionBondlocationpackage(Action):
#
     def name(self) -> Text:
        return "action_bondlocationpackage"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s  location is  {} and package is {} bond is {}""".format(a,d,b,c)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []
    
    
class ActionBond(Action):
#
     def name(self) -> Text:
        return "action_bond"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s   bond is {}""".format(a,c)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []
class ActionLocation(Action):
#
     def name(self) -> Text:
        return "action_location"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s   location is {}""".format(a,d)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []

class ActionPackage(Action):
#
     def name(self) -> Text:
        return "action_package"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                print(a)
            if not(a=="" or b=="" or c=="" ):
                response = """ {}'s   package is {}""".format(a,b)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []
    
    
class ActionProcess(Action):
#
     def name(self) -> Text:
        return "action_process"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                e=item["process"]
                round1=""
                for attr,value in e.items():
                    print(attr,value)
                    round1 += attr+" "+value+"\n"
                print(a)
            if not(a=="" or b=="" or c=="" or round1==""):
                response = """{}'s   process is {}""".format(a,round1)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))

       

        return []

class ActionRoundnumber(Action):
#
     def name(self) -> Text:
        return "action_roundnumber"

     def run(self,dispatcher, tracker, domain):
        connection = MongoClient('localhost', 27017)
        db = connection.placementbot
        cname=tracker.get_slot('company_name')
        rno=tracker.get_slot('round_number')
        data = db.companies
        myquery={"name":cname}
        
        inf = data.find(myquery)
        count = db.companies.count({"name":cname})
        print(count)
        print(count)
        if count!=1:
            dispatcher.utter_message("seems {} have not visited in our campus yet".format(cname))
        else:
            for item in inf:
                a=item["name"]
                b=item["package"]
                c=item["bond"]
                d=item["location"]
                e=item["process"]
                round1=""
                flag=0
                for attr,value in e.items():
                    if(rno == attr):
                        flag=1
                        round1+=" "+value
                    print(attr,value)
                    
                print(a)
                
            if not(a=="" or b=="" or c=="" or round1=="" or flag==0):
                response = """{}'s   round {} is {}""".format(a,rno,round1)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("seems {} does not have that number of round".format(cname))

       

        return []
