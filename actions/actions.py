# This files contains your custom actions which can be used to run
# custom Python code.
#See this guide on how to implement these action:
#  https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from dotenv import load_dotenv

class RegistrationForm(FormAction):
    def name(self):

        return "information_form"
     
    @staticmethod
    def required_slots(tracker):
        if tracker.get_slot("confirm_registration")==True:
            return ["confirm_registration","full_name","email","education","registered_as","level_of_courses",
            "previous_course","contact_no","interest","skill"]
        else:
            return ["full_name","email","education","registered_as","level_of_courses",
            "previous_course","contact_no","interest","skill"]

 
    def submit(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    )-> List[Dict]:
        return []
#
#         dispatcher.utter_message(text="Hello World!")
#
              
    def slot_mappings(self) -> Dict[Text, Union[Dict,  List[DeprecationWarning]]]:

        return {
            "confirm_registeration":[
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),

            ],
            "full_name":[
                self.from_entity(entity="full_name"),
                self.from_intent(intent="deny", value="None"),


            ],
            "email":[
                self.from_entity(entity="email"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value="None"),
                

            ],
            "education":[
                self.from_entity(entity="education"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="inform"),

            ],
            "registered_as":[
                self.from_entity(entity="reg_as"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="inform", value=True),

            ],
            
            "level_of_courses":[
                self.from_entity(entity="level"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="inform"),

            ],
            
            "previous_course":[
                self.from_entity(entity="previous_course"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="inform"),
            ],
            "contact_no":[
                self.from_entity(entity="contact_no"),
                self.from_intent(intent="deny", value="None"),
              
            ],
            "skill":[
                self.from_entity(entity="skill"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="inform"),
            ],
            "interest":[
                self.from_entity(entity="interest"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="inform"),
            ]
            
            
        }