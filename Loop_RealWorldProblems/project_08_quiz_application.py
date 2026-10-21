'''
Mini Project 8: Quiz Application
'''
questions = [
    "What is the capital of India?",
    "Which language is this program written in?",
    "How many days are there in a week?",
    "What is 12 x 12?",
    "Which planet is known as the Red Planet?"
]
answers = ["delhi", "python", "7", "144", "mars"]

total_questions = len(questions)
score = 0

print("----- PYTHON QUIZ -----")

for i in range(total_questions):
    print(f"\nQ{i + 1}. {questions[i]}")
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", answers[i])

percentage = score / total_questions * 100

if percentage >= 80:
    message = "Excellent"
elif percentage >= 60:
    message = "Good"
else:
    message = "Keep Practicing"

print("\n----- QUIZ RESULT -----")
print("Score       :", score, "/", total_questions)
print("Percentage  :", percentage, "%")
print("Performance :", message)
