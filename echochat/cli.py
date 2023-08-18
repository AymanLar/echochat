import os
import openai
import argparse
from .historical_figures import short_name,HISTORICAL_FIGURES

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY 

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different engine based on availability and performance
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].text

def echochat():
    if openai.api_key is None:
        print("OPENAI_API_KEY is not set. Exiting.")
        exit()
    
    parser = argparse.ArgumentParser(description='Talk with historical figures.')
    parser.add_argument('figure', type=str, choices=short_name, help='Choose a historical figure')
    args = parser.parse_args()

    conversation_history = []

    print(f"Initiating conversation with {args.figure.capitalize()}...")
    print(f"{HISTORICAL_FIGURES[args.figure]} : Hi, How can I Help you")
    
    while True:
    
        user_input = input("> You: ")
        conversation_history.append(f'You: {user_input}')
        
    # Determine the assistant's name based on the selected figure
        assistant_name = HISTORICAL_FIGURES[args.figure]
        conversation_prompt = '\n'.join([f'You: {user_input}', f'{assistant_name}: '])
        response = generate_response(conversation_prompt)
        
        print(f"{assistant_name}: {response}")
        if user_input == "bye":
            exit()

if __name__ == '__main__':
    echochat()
