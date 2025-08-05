import random

def random_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    if(operator == '+'):
        result = num1 + num2 
    elif(operator == '-'):
        result = num1 - num2
    else:
        result = num1 * num2
        
    return f"{num1} {operator} {num2}", result

def math_quiz():
    score = 0
    rounds = 5
    
    print("---------Welcome to the Quiz----------")
    
    for r in range(rounds):
        hola ,h = random_question()
        
        res = input(f"How sey {hola} ")
        
        if(res == str(h)):
            print("Correct answer")
            score+=1
        else:
            print(f"Nooo, the answer is {h}")
        
    if(score == rounds):
        print("10 de 10")
    elif(score >= rounds // 2) :
        print("Casi")
    else:
        print("mal")
        
        

math_quiz()