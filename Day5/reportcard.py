scores = {"Math":78,"Python":92,"English":55,"  Science":34}
#print each score anf subject
print("Report card:")
total = 0
for subject,score in scores.items():
    print(f"{subject}:{score}")
    total += score

#Average to one decimal place:

average = total/len(scores)
print(F"aVERAGE:{average:.1f}")


#Grade from average:

if average>=80:
    grade = "A"
elif average>=60:
    grade = "B"
elif average>=40:
    grade = "C"
else:
    grade="Needs work"
    print(f"Grade:{grade}")

#Best and worst subject:
best = ""
best_score = -1
worst = ""
worst_score = 101

for subject,score in scores.items():
    if score>best_score:
        best_score=score
        best = subject

    if score < worst_score:
        worst_score = score
        worst = subject
print(f"Best:  {best} ({best_score})")
print(f"Worst: {worst} ({worst_score})")

#How many subjects passed(>=40)?
passed = 0

for score in scores.values():
    if score>=40:
        passed +=1
print(f"Passed {passed} of {len(scores)} subjects")

#Sretch:Which subject must be retaken?

for subject,score in scores.items():
    if score<=40:
        print(f"{subject}with {score}must be retaken")

#Or use this method to store subject in the set
retakes = set()
for subject,score in scores.items():
    if score<=40:
        retakes.add(subject)
print(f"Retakes:{retakes}")


    