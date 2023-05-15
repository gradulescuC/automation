# Varianta 1:


name = input("Enter student name: ")
mathNote = int(input("Enter math note: "))
chemistryNote = int(input("Enter chemistry note: "))
physicsNote = int(input("Enter physics note: "))
biologyNote = int(input("Enter biology note: "))
informaticsNote = int(input("Enter informatics note: "))
averageNote = float((mathNote + chemistryNote + physicsNote + biologyNote + informaticsNote) / 5)
print(f"{name} average note is {averageNote}.")

# --------------------------------------------------------

# Varianta 2:
student_name = "Alexander"

math = 8.5
chemistry = 8
physics = 9.2
biology = 9.3
info = 9.1

def calculate_average(note1, note2, note3, note4, note5):
    return (note1 + note2 + note3 + note4 + note5) / 5

print(f"The average of the grades of {student_name} is {calculate_average(math, chemistry, physics, biology, info)}")