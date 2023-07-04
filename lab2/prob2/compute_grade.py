def check(name, id):
    final_data=0
    while True:
        raw_input = input(name)
        try:
            data = float(raw_input)
            if  data>= 0 and data<= 100:
                final_data = data
                break
            else:
                print('Please enter a score in the range [0, 100]')
        except ValueError:
            print('Please enter a score as a decimal number')
    return final_data

def calculate(mid, final):
    mid = (mid / 100) * 40
    final = (final / 100) * 60
    grade = mid + final
    def final_grade():
        if(grade < 50):
            return 'F'
        elif(grade >= 50 and grade < 60):
            return 'D'
        elif(grade >= 60 and grade < 70):
            return 'C'
        elif(grade >= 70 and grade < 80):
            return 'B'
        elif(grade >= 80 and grade <= 100):
            return 'A'
    return grade, final_grade()
    
id = int(input('Please enter your student ID: '))
midterm = check('Please enter the student\'s midterm exam mark (0-100): ', id)
final = check('Please enter the student\'s final exam mark (0-100): ', id)
grade, final_grade = calculate(midterm, final)
print('Student ID ' + str(id) + ' has the total mark as ' + str(grade) + ' and has grade ' + final_grade)

    

    