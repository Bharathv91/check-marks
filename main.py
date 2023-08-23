marks = int(input("Enter your marks:"))
if marks<35:
    print("failed")
elif marks>=35 and marks<50:
    print("passed in first class")
elif marks>=50 and marks<=80:
    print("passed in second class")
else:
    print("distinction")
