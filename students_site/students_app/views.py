from django.http import HttpResponse
from faker import Faker

from students_app.models import Student
from students_app.models import Teacher


fake = Faker()


def index(request):
    return HttpResponse("<h1>You're at the students index page.</h1>")


def generate_student(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=17, maximum_age=80)
    Student.objects.create(
        first_name=first_name, last_name=last_name, birth_date=birth_date
    )
    return HttpResponse(
        f"New student created:<br>"
        f"Name: {first_name} {last_name}<br>Birth date: {birth_date}"
    )


def generate_students(request):
    count = int(request.GET.get("count", 100))
    if count <= 0:
        return HttpResponse(
            "<h1 style='color: red;'>" "Note that query must be greater than '0'!</h1>"
        )
    count = min(count, 100)
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=17, maximum_age=80)
        Student.objects.create(
            first_name=first_name, last_name=last_name, birth_date=birth_date
        )
    return HttpResponse(f"<h1>{count} students data generated!</h1>")


def teachers(request):
    list_of_teachers = Teacher.objects.all()
    output = ""
    for teacher in list_of_teachers:
        output += f"<li>Name: {teacher.first_name} {teacher.last_name}. \
        Birth date: {teacher.birth_date}. Subject: {teacher.subject}</li>"
    return HttpResponse(output)
