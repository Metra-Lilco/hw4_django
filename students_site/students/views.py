from django.http import HttpResponse
from faker import Faker

from students.models import Student


fake = Faker()


def index(request):
    return HttpResponse("You're at the students index page.")


def generate_student(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=17, maximum_age=80)
    Student.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date
    )
    return HttpResponse(f"New student created: "
                        f"{first_name} {last_name} {birth_date}")


def generate_students(request):
    count = int(request.GET.get("count", 100))
    if count <= 0:
        return HttpResponse("<h1 style='color: red;'>"
                            "Note that query must be greater than '0'!</h1>")
    count = min(count, 100)
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=17, maximum_age=80)
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date
        )
    all_students = Student.objects.all()
    return HttpResponse(f'''
    <h1>{count} students data generated!</h1>
    <h2>Here they are:</h2>
    <li>{all_students}</li>
    ''')
