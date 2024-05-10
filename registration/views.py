# views.py
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.base import ContentFile
from .forms import LaptopRegistrationForm
from .models import Laptop
import qrcode
from io import BytesIO
from django.http import HttpResponse


def register_laptop(request):
    if request.method == 'POST':
        form = LaptopRegistrationForm(request.POST)
        if form.is_valid():
            laptop = form.save(commit=False)
            # Additional processing if needed
            laptop.save()

            # Generate QR code with 'cute' formatted laptop info
            qr_data_str = f"🖥️ Laptop Name: {laptop.laptop_name}\n" \
                f"🔍 Model: {laptop.model}\n" \
                f"🎨 Color: {laptop.color}\n" \
                f"🔢 Serial Number: {laptop.serial_number}\n"

            # Add owner information based on the owner type
            if laptop.student:
                qr_data_str += f"👤 Owner: {laptop.student.first_name} {laptop.student.last_name}\n" \
                   f"🆔 ID: {laptop.student.student_id}\n" \
                   f"🖼️ Image: {request.build_absolute_uri(laptop.student.profile_image.url)}\n"
            elif laptop.staff:
                qr_data_str += f"👤 Owner: {laptop.staff.first_name} {laptop.staff.last_name}\n" \
                   f"🆔 ID: {laptop.staff.staff_id}\n" \
                   f"🖼️ Image: {request.build_absolute_uri(laptop.staff.profile_image.url)}\n"
            elif laptop.guest:
                qr_data_str += f"👥 Guest Owner: {laptop.guest.first_name} {laptop.guest.last_name}\n" \
                   f"🖼️ Image: {request.build_absolute_uri(laptop.guest.profile_image.url)}\n"

# The rest of the QR code generation code remains the same
         # The rest of the QR code generation code remains the same


            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data_str)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer)
            barcode_image = buffer.getvalue()

            # Save the QR code image to the Laptop model's 'barcode' field
            barcode_image_content = ContentFile(barcode_image, name='barcode.png')
            laptop.barcode.save(barcode_image_content.name, barcode_image_content, save=True)
            return redirect('registration_success', laptop_id=laptop.id)
    else:
        form = LaptopRegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

def registration_success(request, laptop_id):
    laptop = Laptop.objects.get(pk=laptop_id)
    barcode_url = laptop.barcode.url  # Assuming 'barcode' is an ImageField in your Laptop model

    context = {
        'barcode_url': barcode_url,
    }
    return render(request, 'registration_success.html', context)


def dashboard_view(request):
    # Fetch counts for different types of laptops
    total_registered_laptops = Laptop.objects.all().count()
    total_student_laptops = Laptop.objects.filter(owner_type='student').count()
    total_staff_laptops = Laptop.objects.filter(owner_type='staff').count()
    total_guest_laptops = Laptop.objects.filter(owner_type='guest').count()
    
    context = {
        'total_registered_laptops': total_registered_laptops,
        'total_student_laptops': total_student_laptops,
        'total_staff_laptops': total_staff_laptops,
        'total_guest_laptops': total_guest_laptops,
    }
    return render(request, 'dashboard.html', context)