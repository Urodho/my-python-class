import random

questions = [
  {

    "question": "What is the capital city of Tanzania?",
        "options": {
            "A": "Dodoma",
            "B": "Arusha",
            "C": "Dar es Salaam",
            "D": "Mwanza"
        },
        "answer": "A"
  },
  { 

            "question": "Which language is spoken most widely in Tanzania?",
        "options": {
            "A": "French",
            "B": "English",
            "C": "Swahili",
            "D": "Arabic",
        },
             "answer": "C"
        
  }
 ]
score = 0

random.shuffle(questions)
for q in questions:
            print(q["question"])
            for option, answer in q["options"].items():
                print(f"{option}: {answer}")
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}.")

print("\nQuiz Finished")
print(f"Your score is: {score} out of {len(questions)}")

if score == len(questions):
    print("Execellent!")
elif score >= len(questions) / 2:
    print("Good!")
else:
     print("Try again!")         