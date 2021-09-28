import django
import os
import random
from faker import Faker
import warnings
# the below line is copied from wsgi file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project5.settings')
django.setup()


def lead_data(ne=100):
    for _ in range(ne):
        f = Faker('en_US')
        nb = random.randrange(12, 400)
        data = {
            "name": f.name(),
            "age": random.randrange(12, 32),
            "description": f.sentence(nb_words=nb),


        }
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            Employee.objects.create(**data)

    print(f'{ne} data filled')


if __name__ == '__main__':
    # autopip8 will shift this to up so imorting here as it should be after django setup
    from app5.models import Employee
    print('filling Employee')
    lead_data()
