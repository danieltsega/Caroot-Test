import os

import sys
import django

# Add the project directory to the Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LaptopSecuritySystem.settings")

# Initialize Django
django.setup()

# Now you can import the models
from registration.models import Student, Staff, Guest

import requests
from django.core.files.base import ContentFile
from faker import Faker
from django.db import transaction

# Initialize Faker for generating fake data
fake = Faker()

# Function to download image from URL and return its ContentFile
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return ContentFile(response.content)
    return None

# Function to add sample students
def add_sample_students():
    for _ in range(10):
        first_name = fake.first_name()
        middle_name = fake.first_name()  # Add fake middle name
        last_name = fake.last_name()
        gender = fake.random_element(elements=('Male', 'Female'))
        department = fake.random_element(elements=('Computer Science', 'Electrical Engineering', 'Mechanical Engineering'))
        year_level = fake.random_int(min=1, max=4)
        student_id = fake.unique.random_number(digits=8)
        
        student = Student.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            department=department,
            year_level=year_level,
            student_id=student_id,
            profile_image=download_image('https://picsum.photos/200'),
        )
        print(f"Added student: {student}")

# Function to add sample guests
def add_sample_guests():
    for _ in range(10):
        first_name = fake.first_name()
        middle_name = fake.first_name()  # Add fake middle name
        last_name = fake.last_name()
        gender = fake.random_element(elements=('Male', 'Female'))
        job_title = fake.job()
        
        guest = Guest.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            job_title=job_title,
            profile_image=download_image('https://picsum.photos/200'),
        )
        print(f"Added guest: {guest}")

# Function to add sample staff
def add_sample_staff():
    for _ in range(10):
        first_name = fake.first_name()
        middle_name = fake.first_name()  # Add fake middle name
        last_name = fake.last_name()
        gender = fake.random_element(elements=('Male', 'Female'))
        job_title = fake.job()
        
        staff = Staff.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            job_title=job_title,
            profile_image=download_image('https://picsum.photos/200'),
        )
        print(f"Added staff: {staff}")

# Main function to add sample data
def add_sample_data():
    add_sample_students()
    add_sample_guests()
    add_sample_staff()

    transaction.commit()

# Run the script to add sample data
if __name__ == "__main__":
    add_sample_data()
