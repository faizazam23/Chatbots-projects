# greeting_bot.py

def greet_user():
    print("Hello! I'm your simple chatbot.")
    name = input("What's your name? ")
    
    # Greeting based on the time of day
    from datetime import datetime
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    print(f"{greeting}, {name}!")
    print("How can I help you today?")

if __name__ == "__main__":
    greet_user()
