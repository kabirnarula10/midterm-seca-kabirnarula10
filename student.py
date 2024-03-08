"""
Module for defining Student class.

This module provides a class for representing students, their enrolled courses, and grades.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): The name of the student.
        student_id (int): The unique ID of the student.
        enrolled_courses (list): A list of courses the student is enrolled in.
        grades (dict): A dictionary to store grades for courses and assessments.

    Methods:
        enroll_course(course): Enrolls the student in a course.
        drop_course(course): Drops a course from the student's enrollment.
        submit_grade(course, assessment, grade): Submits a grade for a student in a course.
    """

    def __init__(self, name, student_id):
        """
        Initializes a Student object with a name and an ID.

        Args:
            name (str): The name of the student.
            student_id (int): The unique ID of the student.
        """
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []
        self.grades = {}
        pass


    def enroll_course(self, course):
        """
        Enrolls the student in a course if prerequisites are met.

        Args:
            course (Course): The course object to be enrolled in.

        Returns:
            None
        """
        if all (prereq in self.enrolled_courses for prereq in course.prerequisites):
            self.enrolled_courses.append(course)
        else:
            raise ValueError("Pre not found")

        

    def drop_course(self, course):
        """
        Drops a course from the student's enrollment.

        Args:
            course (Course): The course object to be dropped.

        Returns:
            None
        """
        
        if course in self.enroll_courses:
            self.enroll_courses.remove(course)
        else:
            raise ValueError("course not found")


    def submit_grade(self, course, assessment, grade):
        """
        Submits a grade for a student in a course.

        Args:
            course (Course): The course object.
            assessment (str): The assessment name.
            grade (float): The grade for the assessment.

        Returns:
            None
        """
        if course in self.enroll_courses:
            if course.course_name not in self.grades:
                self.grades[course.course_name] = {}
            self.grades[course.course_name][assessment] = grade
        else:
            raise ValueError("Student not enrolled")
        pass
