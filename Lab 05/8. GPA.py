def grade (marks):
 if marks >= 97 and marks <= 100:
 return "A+"
 elif marks >= 93 and marks < 97:
 return "A"
 elif marks >= 90 and marks < 93:
 return "A-"
 elif marks >= 80 and marks < 90:
 return "B+"
 elif marks >= 75 and marks < 80:
 return "B"
 elif marks >= 70 and marks < 75:
 return "B-"
elif marks >= 67 and marks < 70:
  return "C+"
 elif marks >= 63 and marks < 67:
 return "C"
 elif marks >= 60 and marks < 63:
 return "C-"
 elif marks >= 0 and marks < 60:
 return "F"

def points(grade):
 if grade == "A+":
 return 4.00
 if grade == "A":
 return 4.00
 if grade == "A-":
 return 3.67
 if grade == "B+":
 return 3.33
 if grade == "B":
 return 3.00
 if grade == "B-":
 return 2.67
 if grade == "C+":
 return 2.33
 if grade == "C":
 return 2.00
 if grade == "C-":
 return 1.67
 if grade == "F":
 return 0.00

def gpa_calculator (marks_1, marks_2, marks_3, marks_4):
 print ("Your grades are", grade (marks_1), grade (marks_2), grade
(marks_3), grade (marks_4))
 GPA = (points (grade(marks_1)) + points (grade(marks_2)) + points
(grade(marks_3)) + points (grade(marks_4)))/4
 print ("Your GPA is", GPA)
