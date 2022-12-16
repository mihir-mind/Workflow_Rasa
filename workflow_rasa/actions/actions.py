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
        print('>>>>>', slot_value.isdigit())
        if len(slot_value) > 1 and not slot_value.isdigit():
            # validation succeeded, set the value of the "name" slot to value
            return {"name": slot_value}
        else:
            dispatcher.utter_message(response="utter_wrong_name")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"name": None}


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