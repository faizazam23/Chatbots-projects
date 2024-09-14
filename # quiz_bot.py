# quiz_bot.py

def quiz():
    questions = {
        "What is the capital of France?": "a",
        "What is 2 + 2?": "b",
        "Which planet is known as the Red Planet?": "c"
    }
    options = [
        ["a) Paris", "b) London", "c) Rome", "d) Madrid"],
        ["a) 3", "b) 4", "c) 5", "d) 6"],
        ["a) Earth", "b) Venus", "c) Mars", "d) Jupiter"]
    ]
    answers = ["a", "b", "c"]
    
    score = 0
    
    for i, (question, answer) in enumerate(questions.items()):
        print(question)
        for option in options[i]:
            print(option)
        user_answer = input("Your answer: ").lower()
        
        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}\n")
    
    print(f"Quiz completed! Your score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
