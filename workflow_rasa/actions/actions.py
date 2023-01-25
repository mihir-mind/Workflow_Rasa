import re

from typing import Text, List, Any, Dict, Union
from rasa_sdk import Tracker, FormValidationAction, Action
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

        valid_mo_num = re.match(r'(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+', slot_value)
        if valid_mo_num:
            mo_num = slot_value.replace("-", "")
            mo_num = mo_num.replace(r"\(.*\)","")
            if len(mo_num) > 10:
                if mo_num.startswith("+"):
                    valid_mo_num = True
                else:
                    valid_mo_num = False
            elif len(mo_num) < 10:
                valid_mo_num = False

        if valid_mo_num:
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


class ActionSendPortfolioLink(Action):

    def name(self) -> Text:
        return "action_send_portfolio_link"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        import time
        # List of all Portfolio links
        utter_send_portfolio_link = ["utter_send_portfolio_link_edge_ai", "utter_send_portfolio_link_super_app", "utter_send_portfolio_link_nft_base", "utter_send_portfolio_link_home_rent", "utter_send_portfolio_link_ai_base"]
        time.sleep(10)
        for link in utter_send_portfolio_link:
            time.sleep(1)
            dispatcher.utter_message(response=link)
        return [UserUtteranceReverted()]