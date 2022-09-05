import random
from data import question_data
from question_model import Quiz
from quiz_brain import Quizbrain
score=0
count=1
while 2>1:
    question = random.choice(question_data[0]["results"])
    new_quiz=Quiz(question)
    answer = input(f"Q{count}: {new_quiz.text} ? (TRUE/FALSE) or ('EXIT' to exit the quiz) ").title()
    if answer == new_quiz.ans:
        print("You got it right!")
        print(f"Correct answer was {new_quiz.ans}")
        score += 1
        count+=1
        print(f"Your current score is {score}/{count-1} ")
    elif answer=="Exit":
        print(f"Your final score is :{score}/{count-1}")
        break
    else:
        count+=1
        print("That's Wrong ")
        print(f"The correct answer was {new_quiz.ans}")
        print(f"You current score is {score}/{count-1}")

# question_bank=[]
# for ques in question_data:
#     question=Quiz(ques)
#     question_bank.append(question)
#
# quest=Quizbrain(question_bank)
# quest.next_question()
