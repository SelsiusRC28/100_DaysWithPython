notes = input("Write the califications: ")

scores = [int(x) for x in notes.split(',')]

scores.sort(reverse=True)  

grades = [
    "A" if score >=90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

passing_examen = [i for i in scores if i >= 60]
failing_examen = [i for i in scores if i < 60]



for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Studen {i}: Score = {score} Grade = {grade}")

print("\n --------- Passing and Failing Students --------")
print(passing_examen)
print(failing_examen)