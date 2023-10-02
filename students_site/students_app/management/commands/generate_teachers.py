from django.core.management.base import BaseCommand
from faker import Faker

from students_app.models import Teacher


fake = Faker()


class Command(BaseCommand):
    help = "Add the specified number of teachers to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "number", nargs="?", type=int, default=100, help="Number of teachers to add"
        )

    def handle(self, *args, **options):
        for i in range(options["number"]):
            professor = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=23, maximum_age=65),
                subject=fake.catch_phrase(),
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % professor.id)
            )
