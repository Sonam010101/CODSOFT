import random
import re

class SupportBot:

    negative_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\bproduct\b.*',
            'technical_support': r'.*\btechnical support\b.*',
            'about_returns': r'.*\breturn policy\b.*',
            'general_query': r'.*\bhelp\b.*'
        }

    

    def make_exit(self, reply):
        reply = reply.lower()
        for command in self.exit_commands:
            if command in reply:
                return "Thanks for reaching out. Have a great day!"
        return None

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)

            if found_match and intent == 'ask_about_product':
                return self.ask_about_product()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_returns':
                return self.about_returns()
            elif found_match and intent == 'general_query':
                return self.general_query()

        return self.no_match_intent()

    def ask_about_product(self):
        responses = [
            "Our product is top-notch and has excellent reviews!",
            "You can find all product details on our website."
        ]
        return random.choice(responses)

    def technical_support(self):
        responses = [
            "Please visit our technical support page for detailed assistance.",
            "You can also call our tech support helpline for immediate help."
        ]
        return random.choice(responses)

    def about_returns(self):
        responses = [
            "We have a 30-day return policy.",
            "Please ensure the product is in its original condition when returning."
        ]
        return random.choice(responses)

    def general_query(self):
        responses = [
            "How can I assist you further?",
            "Is there anything else you'd like to know?"
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "I'm sorry, I didn't quite understand that. Can you please rephrase?",
            "My apologies, can you provide more details?"
        ]
        return random.choice(responses)



bot = SupportBot()

def get_response(message):
    
    exit_msg = bot.make_exit(message)
    if exit_msg:
        return exit_msg

    
    return bot.match_reply(message)
