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

