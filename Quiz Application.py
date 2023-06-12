import requests
import html
import json
import random

score_correct=0
score_incorrect=0
url="https://opentdb.com/api.php?amount=1"
endGame=""
while endGame !="quit":
    r=requests.get(url)
    if(r.status_code !=200):
        input("Sorry for the inconvinience! There is some trouble connecting to the server. You can retry by pressing enter or type 'quit' to quit the game")
    else:
        valid_answer=False
        answer_no=1
        data=json.loads(r.text)
        question=data['results'][0]['question']
        answers=data['results'][0]['incorrect_answers']
        correct_answer=data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print("Question: "+ html.unescape(question)+"\n")
        for answer in answers:
            print(str(answer_no)+" - "+html.unescape(answer))
            answer_no+=1
        while valid_answer== False:
            user_input= input("\nEnter the number associated to your answer: ")
            try:
                user_input=int(user_input)
                if user_input> len(answers) or user_input <=0:
                    print("Enter valid number")
                else:
                    valid_answer=True
            except:
                print("Invalid answer. Use numbers only")
                continue
        user_input=answers[int(user_input)-1]
        if user_input ==correct_answer:
            print("Congratulations! "+user_input+" is a correct answer")
            score_correct+=1
        else:
            print("Sorry, "+user_input+" is incorrect. The correct answer is: "+correct_answer)
            score_incorrect+=1
        
        print("Your score is: ")
        print("Correct answers: "+str(score_correct))
        print("Incorrect answers: "+str(score_incorrect))
        endGame=input("Press enter to play again or type 'quit' to exit the game\n").lower()
print("\nThank you for playing the game, Adios!")