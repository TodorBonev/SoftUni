class Class:
    students = []
    grades = []

    def __init__(self, name, __students_count=22):
        self.name = name
        self.__students_count = __students_count

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"

    def add_student(self, student_name, grade):
        if len(self.students) < self.__students_count:
            self.students.append(student_name)
            self.grades.append(grade)

    def get_average_grade(self):
        sum = 0
        for i in self.grades:
            sum += i
        middle_grade = sum / (len(self.grades))
        return middle_grade