import random

# Dictionary mapping keywords to roasts
roasts = {
    "exam": "Looks like you studied as much as a goldfish remembers.",
    "homework": "Did you do your homework or just stare at it until it felt sorry for you?",
    "sleep": "You sleep so much, even your dreams are tired of you.",
    "work": "Your work ethic is like a sloth on a Sunday.",
    "diet": "Your diet plan must be 'see food and eat it.'",
    "exercise": "You exercise? I thought walking to the fridge was your cardio.",
    "love": "Your love life is like a software update — always pending.",
    "money": "Your wallet is so empty, echoes live there.",
    "friends": "Your friends must be imaginary, because I don't see any.",
    "game": "You play games like a potato with thumbs."
}

# List of random roasts if no keyword matches
random_roasts = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're the reason the gene pool needs a lifeguard.",
    "If you were any slower, you'd be going backward.",
    "You're as sharp as a marble.",
    "You bring everyone so much joy... when you leave the room.",
    "You're proof that even evolution takes a break sometimes.",
    "You're like a software bug — annoying but kind of expected.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You're the human version of a participation trophy.",
    "You have something on your chin... no, the third one down."
]

def roast_chatbot():
    print("Welcome to the RoastBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("RoastBot: Finally, some peace and quiet. Bye!")
            break

        # Check for keywords in user input
        matched_roasts = [roast for keyword, roast in roasts.items() if keyword in user_input]

        if matched_roasts:
            # Pick a random roast from matched roasts
            response = random.choice(matched_roasts)
        else:
            # Pick a random roast from the general list
            response = random.choice(random_roasts)

        print(f"RoastBot: {response}")

if __name__ == "__main__":
    roast_chatbot()
