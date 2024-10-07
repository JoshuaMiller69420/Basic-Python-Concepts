# python has 3 logical operaters: and, or, and mot


good_attendance = False  # ture or TURE - those are not valid/usable
good_grades = True
is_student = False

# if good_attendance and good_grades: You need both
# if good_attendance or good_grades: You need one of them
if is_student and (good_attendance or good_grades):
    print("You can join NTHS")
elif not is_student:
    print("Your're not a student!")
else:
    print("Not qualified")
