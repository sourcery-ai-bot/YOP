# This script I wrote to help in determining the final grade for
# a class I teach.
#
#
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# By Tom Yarrish
# Version 0.1


midterm_total = raw_input("Enter the Midterm grade: ")
final_total = raw_input("Enter the Final Grade: ")
lab_total = raw_input("Enter the Lab Total Grade: ")
homework_total = raw_input("Enter the Homework Total Grade: ")
quiz_total = raw_input("Enter the Quiz Total Grade: ")

midterm_calc = float(midterm_total) * 0.2
final_calc = float(final_total) * 0.2
lab_calc = float(lab_total) * 0.3
homework_calc = float(homework_total) * 0.2
quiz_calc = float(quiz_total) * 0.1

extra_credit = raw_input("Enter extra credit score (Enter if none): ")

if extra_credit:
    grade = (midterm_calc + final_calc + lab_calc + homework_calc + quiz_calc) + int(extra_credit)
else:
    grade = (midterm_calc + final_calc + lab_calc + homework_calc + quiz_calc)

print "Grade is {}\n".format(int(grade))
