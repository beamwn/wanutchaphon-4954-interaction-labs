class ComEnStudent:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def take_courses(self, *courses):
        for i in courses:
            self.courses.append(i)

    def __str__(self):
        return f"{self.name} has taken these courses:{self.courses}"
        
class CoEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)
        
class DMEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)
        self.content_type = None

    def make_content_type(self, content_type):
        self.content_type = content_type

    def __str__(self):
        s = super().__str__()
        return s + f"\n specialized in creating content type:{self.content_type}"
    
if __name__ == "__main__":
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)