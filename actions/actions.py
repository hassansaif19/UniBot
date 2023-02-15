from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher



class ActionAggregatecalculator(Action):

    def name(self) -> Text:
        return "custom_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        InterMarksFetch= float(tracker.get_slot('InterMarks'))
        TestMarksFetch= float(tracker.get_slot('TestMarks'))

        print(InterMarksFetch, TestMarksFetch)    
        
        
        # if not InterMarksFetch:
        #     msg = f"I have got following value {InterMarksFetch} "
        #     dispatcher.utter_message(text=msg)
        #     return []
        # if not TestMarksFetch:
        #     msg = f"I have got following value {TestMarksFetch} "
        #     dispatcher.utter_message(text=msg)
        #     return []
        
        retval=0.5*((InterMarksFetch*100)/1100)+0.5*((TestMarksFetch))
        retstr= retval                
        msg = f"Calculated Aggregate is {retstr}"
        dispatcher.utter_message(text=msg)
        
        return []




class ActionViewStudyPlan (Action):
    
    def name(self) -> Text:
        return "action_view_study_plan"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        Semester = float(tracker.get_slot('Semester'))
        print(Semester) 
        
        sem1 = "SEMESTER # 1\nCL117 - Intro to Info and Comm. Technologies Cr = 1\nCL118 - Programming Fundamentals Lab Cr = 1\nCS118 - Programming Fundamentals Cr = 3\nEE117 - Applied Physics Cr = 3\nMT119 - Calculus 1 Cr = 3\nSL150 - English Lab Cr = 1\nSS150 - English Cr = 3\nSS111 - Islamic Studies Cr = 3\n\nTotal Credit Hours = 17\n\n"
        sem2 = "SEMESTER # 2\nCL217 - OOP Lab Cr = 1\nCS217 - OOP Cr = 3\nEE227 - DLD Cr = 3\nEL227 DLD Cr = 1\nMT224 - Calculus 2 Cr = 3\nSL152 - Communications Lab\nSS152 - Communications Cr = 3\nSS113 - Pakistan Studies\n\nTotal Credit Hours = 17\n\n"
        sem3 = "SEMESTER # 3\nCL218 - Data Structures Lab Cr = 1\nCS218 - Data Structures Cr = 3\nEE229 - COAL Cr = 3\nEL229 - COAL Lab Cr = 1\nMT104 - Linear Algebra Cr = 3\nMG223 - Management Cr = 3\n\nTotal Credit Hours = 17\n\n"
        sem4 = "SEMESTER # 4\nCL219 - DB Lab Cr = 1\nCL220 - OS Lab Cr = 1\nCS219 - DB Cr = 3\nCS220 - OS Cr = 3\nCS302 - Algo Cr = 3\nMG220 - Marketing Cr = 3\n\nTotal Credit Hours = 17"
        sem5 = "SEMESTER # 5\nCL301 - CNET Lab Cr = 1\nCS3001 - CNET Cr = 3\nCS3004 - SDA Cr = 3\nCS3005 - Automata Cr = 3\nCS4043 - Advanced Programming Cr = 3\nSS2007 - Technical Business Writing Cr = 3\n\nTotal Credit Hours = 16\n\n"
        sem6 = "SEMESTER # 6\nAL2002 - AI Lab Cr = 1\nAI2002 - AI Cr = 3\nCS2008 - Numerical Computing Cr = 3\nCS3006 - PDC Cr = 3\nCS3009 - Software Engineering Cr = 3\nMG4011 - Entrepreneurship Cr = 3\n\nTotal Credit Hours = 16\n\n"
        sem7 = "SEMESTER # 7\nAI4004 - Game Theory Cr = 3\nCS3002 - Information Security Cr = 3\nCS4001 - Professional Practices in IT Cr = 3\nCS4091 - FYP-1 Cr = 3\nCS4102 - KGLD Cr = 3\n\nTotal Credit Hours = 14\n\n"
        sem8 = "SEMESTER # 8\nCS4075 - Cloud Computing Cr = 3\nCS4083 - Distributed Data Engineering Cr = 3\nCS4092 - FYP-2 Cr = 3\nCS4085 - MLOPS Cr = 3\n\nTotal Credit Hours = 12\n\n"
       
       
       
        if Semester == 1:
                dispatcher.utter_message(text=sem1)
                print(sem1)
                
        elif Semester == 2:
                dispatcher.utter_message(text=sem2)
                
        elif Semester == 3:
                dispatcher.utter_message(text=sem3)
        elif Semester == 4:
                dispatcher.utter_message(text=sem4)
                
        elif Semester == 5:
                dispatcher.utter_message(text=sem5)
                
        elif Semester == 6:
                dispatcher.utter_message(text=sem6)
                
        elif Semester == 7:
                dispatcher.utter_message(text=sem7)
        
        elif Semester == 8:
                dispatcher.utter_message(text=sem8)
        
        else:
            dispatcher.utter_message(text='Invalid Semester Choosen')
            
        return []