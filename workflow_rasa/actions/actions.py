import re
import phonenumbers

from typing import Text, List, Any, Dict, Union
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.types import DomainDict


class ValidateDetailsForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_details_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
       ) -> Dict[Text, Any]:
        """Validate name value."""

        slot_value = slot_value.strip()
        if len(slot_value) > 1 and not slot_value.isdigit():
            # validation succeeded, set the value of the "name" slot to value
            return {"name": slot_value}
        else:
            dispatcher.utter_message(response="utter_wrong_name")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"name": None}


    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
       ) -> Dict[Text, Any]:
        """Validate email value."""

        slot_value = slot_value.strip()
        valid_email = re.fullmatch(re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'), slot_value)
        if valid_email:
            # validation succeeded, set the value of the "email" slot to value
            return {"email": slot_value}
        else:
            dispatcher.utter_message(response="utter_wrong_email")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"email": None}


    def validate_mobile(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
       ) -> Dict[Text, Any]:
        """Validate mobile value."""

        slot_value = slot_value.strip()
        mobile_number = phonenumbers.parse(slot_value)

        if phonenumbers.is_possible_number(mobile_number):
            # validation succeeded, set the value of the "mobile" slot to value
            return {"mobile": slot_value}
        else:
            dispatcher.utter_message(response="utter_wrong_mobile")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"mobile": None}


    def validate_country(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
       ) -> Dict[Text, Any]:
        """Validate country value."""

        slot_value = slot_value.strip()
        if len(slot_value) > 1 and not slot_value.isdigit() and slot_value.isalpha():
            # validation succeeded, set the value of the "mobile" slot to value
            return {"country": slot_value}
        else:
            dispatcher.utter_message(response="utter_wrong_country")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"country": None}



# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""

#     def name(self) -> Text:
#         return ACTION_DEFAULT_FALLBACK_NAME

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="my_custom_fallback_template")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]