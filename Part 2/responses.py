from random import randint, random
import os
from dotenv import load_dotenv
import openai
import re
import json

load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')
regex_pattern = r'^[a-zA-Z0-9]{1000}$'

def ask_openai(question):
    # Define the initial conversation context and capabilities of the assistant
    csv_file_path = 'MarchMadnessGames2023.csv'
    csv_file_path2 = 'MarchMadnessTeams2023.csv'
    with open(csv_file_path, 'r') as file:
      csv_text = file.read()
    with open(csv_file_path2, 'r') as file:
        csv_text2 = file.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant knowledgeable in Python programming, nutrition, and current events, especially in the sports world. Your name is Randolph. You are a university professor so speak your responses in a very knowledgeable manner. YOU ARE INFORMED by the march madness 2023 games which are given by: " + csv_text + ". You are also informed by the teams in march madness which are given by this csv" + csv_text2},
            {"role": "user", "content": question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return answer




def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you are quiet'
    elif 'hello' in lowered:
        return 'Hello there! You need to code your AI Bot here'
    elif 'roll dice' in lowered:
        return f'You rolled a {randint(1, 6)}'
    elif 'help' in lowered:
        return '''You can say roll dice, 'magic8ball [question], or wyr'''
    elif 'magic8ball ' + regex_pattern:
        return magic8ball()
    elif 'wyr' in lowered:
        return wyr()
    else:
        return ask_openai(user_input)


def magic8ball():
    m = randint(1,9)
    if m == 1:
        return "Without a doubt."
    elif m == 2:
        return "Definitely."
    elif m == 3:
        return "Most likely."
    elif m == 4:
        return "Signs point to yes!"
    elif m == 5:
        return "Cannot predict now, the future is hazy."
    elif m == 6:
        return "Concentrate harder and try asking again!"
    elif m == 7:
        return "Very doubtful."
    elif m == 8:
        return "My sources are telling me no."
    elif m == 9:
        return "Outlook's not so great."


def wyr():
    scenarios = [
        "Would you rather eat pizza for every meal or never eat pizza again?",
        "Would you rather have the ability to fly or the ability to teleport?",
        "Would you rather uncontrollably break into song or unexpectedly lose your voice?",
        "Would you rather eat only fruit or vegetables for the rest of your life?",
        "Would you rather be a cat or a dog?",
        "Would you rather be fluent in every language or be able to talk with animals?",
        "Would you rather be able to run on your hands or write with your feet?",
        "Would you have one giant hand or one giant foot?",
        "Would you rather be a spider for a day or be an ant for a day?",
        "Would you rather watch only TV for a whole month or listen to only music for a whole month?",
        "Would you rather be super strong or super fast?"
    ]

    return scenarios[randint(0, len(scenarios)-1)]
