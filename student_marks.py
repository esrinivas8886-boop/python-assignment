# 1. ask the users to enter details
student_name = input("enter student name:")
# marks in integer format
maths = int(input("enter maths marks:"))
science = int(input("enter science marks:"))
english = int(input("enter english marks:"))
#validate the marks
if(maths<0 or maths>100) or (science<0 or science>100) or (english<0 or english>100):
    print("invalid marks enterd")
else:
    # 3. calculate total and average percentage
    total_marks = maths + science + english
    percentage = (total_marks / 300) * 100
    # 4. display basic details
    print("\nstudent name:", student_name)
    print(f"total marks: {total_marks}")
    print(f"percentage: {percentage:.2f}")
    # 5. determine pass/faile status
    if maths < 40 or science < 40 or english < 40:
        print("status: fail")
    else:
        print("status: pass")
        # 6. assaign Grade (only if passed)
        if percentage >=75:
            grade= "A"
        elif percentage >=60:
            grade= "B"
        else:
            grade= "C"
             # 40-60 percentage
    print(f"Grade: {grade}")

    