class Hogwarts:
    faculty = "empty"
    founder = "empty"
    student_number = "empty"
    def set_info(self, faculty_name, founder_name, st_num):
        self.faculty = faculty_name
        self.founder = founder_name
        self.student_number = st_num
    def get_info(self):
        print(self.faculty, self.founder, self.student_number)
_Harry_potter = Hogwarts()
_Harry_potter.set_info("sdfsf","fdsfwd",42)
_Harry_potter.get_info()