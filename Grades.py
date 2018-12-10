#--By Calvin Milush, Tyler Milush
#--12 December, 2018
#--This program determines a test's letter grade, given a percentage score.

#--Calvin Milush
#-Initializes variables:
score = 0
scoreList = []
counter = 0
total = 0

#--Calvin Milush
#-Looped input for test scores:
while (score != -1):
    score = input("Input test score (-1 to exit loop): ")
    if (score != -1):
        scoreList.append(score)
        counter += 1
        total += score
    else:
        break

#--Tyler Milush
#-Assigns a letter grade to each inputted score:
letterList = []
for i in range(counter):
    if scoreList[i] >= 90:
        letterList.append("A")
    elif scoreList[i] >= 80 and scoreList[i] <= 89:
        letterList.append("B")
    elif scoreList[i] >= 70 and scoreList[i] <= 79:
        letterList.append("C")  
    elif scoreList[i] >= 60 and scoreList[i] <= 69:
        letterList.append("D")  
    elif scoreList[i] < 60:
        letterList.append("F")
print
print "List of scores: ", scoreList
print "Grade of each score: ", letterList
print
        
#--Calvin Milush       
#-Calculates and prints average (if greater than 0):
if (counter > 0):
    avg = total / float(counter)
    print "%0s %0.2f" % ("Average test score: ", avg)
else:
    print "Error: Requires at least one test score."
    
#--Tyler Milush
#-Assigns a letter grade to the average:
avgLetter = ""
if(avg >= 90):
    avgLetter = "A"
elif(avg >= 80 and avg <=89):
    avgLetter = "B"
elif(avg >= 70 and avg <=79):
    avgLetter = "C"
elif(avg >= 60 and avg <=69):
    avgLetter = "D"
elif(avg < 60):
    avgLetter = "F"
print "Letter grade of average: ", avgLetter
