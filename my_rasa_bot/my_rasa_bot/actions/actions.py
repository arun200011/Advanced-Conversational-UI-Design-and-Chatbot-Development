from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionTrackOrder(Action):
    def name(self) -> Text:
        return "action_track_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your order is being processed and will be delivered soon!")
        return []

class ActionRecommendProduct(Action):
    def name(self) -> Text:
        return "action_recommend_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = tracker.latest_message.get('text', '').lower()

        # Use previous messages if no keyword found
        full_history = " ".join([e['text'] for e in tracker.events if e.get('event') == 'user' and 'text' in e])
        
        if "laptop" in message or "laptop" in full_history:
            response = "I recommend the HP Spectre x360 or MacBook Air."
        elif "phone" in message or "phone" in full_history:
            response = "You might like the Samsung Galaxy S23 or iPhone 14."
        elif "shoes" in message or "shoes" in full_history:
            response = "Nike Air Max and Adidas Ultraboost are great options."
        else:
            response = "Could you specify what type of product you're looking for?"

        dispatcher.utter_message(text=response)
        return []

class ActionLogComplaint(Action):
    def name(self) -> Text:
        return "action_log_complaint"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_msg = tracker.latest_message.get("text", "")
        complaint_id = f"CMP{random.randint(1000, 9999)}"

        dispatcher.utter_message(text=f"Thank you for reporting the issue. We've logged your complaint as ID: {complaint_id}. Our team will get back to you shortly.")
        return []

class ActionEscalateToHuman(Action):
    def name(self) -> Text:
        return "action_escalate_to_human"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sure, I’ll connect you to a human agent. Please wait...")
        # In production, you would trigger a live chat handover here
        return []
