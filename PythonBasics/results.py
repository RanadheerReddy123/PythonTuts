print("Exam Results")
marks = 35
if marks == 35:
    print("You are promoted!")
elif marks > 35:
    print("You passed the exam!")
    if marks >= 75 and marks <= 85:
        print("You got good marks:", marks)
    elif marks > 85 and marks <= 95:
        print("You got best marks:", marks)
    elif marks > 95:
        print("You got excellent marks:", marks)
    else:
        print("You got average marks:", marks)
else:
    print("You failed the exam:", marks)

