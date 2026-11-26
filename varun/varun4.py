marks = int(input("Enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 40:
    print("D grade")
else:
    print("Fail")    