from rest_framework import serializers
from django_testing.local_settings import MAX_STUDENTS_PER_COURSE
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, students):
        if len(students) > MAX_STUDENTS_PER_COURSE:
            return 400
        return 201
