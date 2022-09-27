from Automation10_Projects.Python_Automation.P1_PythonAutomation.introduction_to_programming.curs_07.POO_piloni.tst_encapsulation import \
    Student

school_object = Student("Andreea",15)
print(school_object.schoolName_public)
print(school_object._schoolName)
# print(school_object.__schoolNamePrivate)