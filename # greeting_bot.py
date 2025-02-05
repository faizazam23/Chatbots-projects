import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import Scrollbar, Text

# Define chatbot responses using pattern-response pairs
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you ?", ["I'm good, how about you?", "I'm doing well!"]),
    (r"what is your name ?", ["I'm an AI chatbot!", "You can call me ChatBot!"]),
    (r"who created you ?", ["I was created using NLTK in Python!", "A developer built me with NLTK."]),
    (r"what is the weather like\??", ["I can't check real-time weather, but you can visit weather.com!"]),
    (r"quit", ["Goodbye!", "Take care!", "See you later!"]),
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Function to handle user input
def send_message():
    user_input = user_entry.get()
    if user_input.lower() == "quit":
        chat_display.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n")
        root.quit()
        return
    
    chat_display.insert(tk.END, f"You: {user_input}\n")
    response = chatbot.respond(user_input)
    
    if response:
        chat_display.insert(tk.END, f"Chatbot: {response}\n")
    else:
        chat_display.insert(tk.END, "Chatbot: I'm not sure how to respond to that.\n")

    user_entry.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x500")

# Chat Display Area
chat_display = Text(root, wrap=tk.WORD, width=50, height=20)
chat_display.pack(pady=10)

# Scrollbar for chat display
scrollbar = Scrollbar(root, command=chat_display.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_display.config(yscrollcommand=scrollbar.set)

# User Input Field
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=10)

# Send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the GUI loop
root.mainloop()
