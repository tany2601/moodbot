from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionSuggestCopingMechanism(Action):
    def name(self) -> Text:
        return "action_suggest_coping_mechanism"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mood = tracker.latest_message.get('intent').get('name')

        coping_mechanisms = {
            "mood_great": [
                "Spend time with loved ones.",
                "Engage in a hobby you love.",
                "Practice gratitude by listing things you're thankful for."
            ],
            "mood_unhappy": [
                "Talk about your feelings with someone you trust.",
                "Listen to uplifting music.",
                "Try journaling your thoughts."
            ],
            "mood_happy": [
                "Treat yourself to something nice.",
                "Share your happiness with others.",
                "Go out and enjoy the weather."
            ],
            "mood_sad": [
                "Take a walk in nature.",
                "Try to meditate.",
                "Watch a movie that makes you laugh."
            ]
        }

        response = random.choice(coping_mechanisms.get(mood, []))
        dispatcher.utter_message(text=response)
        return []

class ActionSuggestMindfulnessExercise(Action):
    def name(self) -> Text:
        return "action_suggest_mindfulness_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mood = tracker.latest_message.get('intent').get('name')

        mindfulness_exercises = {
            "mood_great": [
                "Spend some time meditating or practicing mindfulness.",
                "Go for a run or do some exercise to release endorphins."
            ],
            "mood_unhappy": [
                "Try a grounding exercise: identify 5 things you can see, 4 you can feel, 3 you can hear, 2 you can smell, and 1 you can taste.",
                "Breathe in deeply for 4 seconds, hold for 4, and breathe out for 4."
            ],
            "mood_happy": [
                "Dance to your favorite song or do something creative.",
                "Practice mindfulness by focusing on the present moment."
            ],
            "mood_sad": [
                "Close your eyes and visualize a peaceful scene.",
                "Practice progressive muscle relaxation."
            ]
        }

        response = random.choice(mindfulness_exercises.get(mood, []))
        dispatcher.utter_message(text=response)
        return []
