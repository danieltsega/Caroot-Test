from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    year_level = models.IntegerField()
    student_id = models.CharField(max_length=20, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Laptop(models.Model):
    owner_type_choices = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('guest', 'Guest'),
    ]

    owner_type = models.CharField(max_length=10, choices=owner_type_choices)
    laptop_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    # Define ForeignKey fields for each user type
    student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.owner_type == 'student':
            return f"{self.student.first_name}'s Laptop"
        elif self.owner_type == 'staff':
            return f"{self.staff.first_name}'s Laptop"
        elif self.owner_type == 'guest':
            return f"Guest's Laptop"

