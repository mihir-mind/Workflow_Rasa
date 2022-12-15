# from rasa_sdk.forms import FormAction
from typing import Text, List, Any, Dict, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.types import DomainDict


class ValidateClientDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_client_details_form"

    # @staticmethod
    # def cuisine_db() -> List[Text]:
    #     """Database of supported cuisines"""

    #     return ["caribbean", "chinese", "french"]

    def validate_client_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate client name value."""

        print(">>>>><<<<<<", tracker.get_slot('client_name'))
        print("$$$$$$$$", value)

        if len(value) == 0 or len(value) > 1:
            # validation succeeded, set the value of the "name" slot to value
            return {"client_name": value}
        else:
            dispatcher.utter_message(response="utter_wrong_client_name")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"client_name": None}


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