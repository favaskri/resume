from django.shortcuts import render

# Create your views here.
# resume_app/views.py
from django.shortcuts import render

def resume(request):
    resume_data = {
        'name': 'Favas',
        'title': 'Showroom Head',
        'contact': {
            'phone': '+91 9844666664',
            'email': 'hello@reallygreatsite.com',
            'website': 'www.reallygreatsite.com',
            'address': '123 Anywhere St., Any City, ST 12345'
        },
        'about': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pharetra in lorem at laoreet. Donec hendrerit libero eget est tempor, quis tempus arcu elementum. In elementum elit at dui tristique feugiat. Mauris convallis, mi at mattis malesuada, neque nulla volutpat dolor, hendrerit faucibus eros nibh ut nunc.',
        'education': [
            {'degree': 'Bachelor of Design', 'institution': 'Wardiere University', 'year': '2006 - 2008'},
            {'degree': 'Bachelor of Design', 'institution': 'Wardiere University', 'year': '2006 - 2008'}
        ],
        'expertise': ['Web Design', 'Branding', 'Graphic Design', 'SEO', 'Marketing'],
        'experience': [
            {'period': 'Jan 2022 - Present', 'company': 'Company Name', 'role': 'Digital Marketing Manager', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pharetra in lorem at laoreet. Donec hendrerit libero eget est tempor, quis tempus arcu elementum. In elementum elit at dui tristique feugiat.'},
            {'period': '2017 - 2019', 'company': 'Company Name', 'role': 'Social Media Manager', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pharetra in lorem at laoreet. Donec hendrerit libero eget est tempor, quis tempus arcu elementum. In elementum elit at dui tristique feugiat.'},
            {'period': '2015 - 2017', 'company': 'Company Name', 'role': 'Social Media Manager', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pharetra in lorem at laoreet. Donec hendrerit libero eget est tempor, quis tempus arcu elementum. In elementum elit at dui tristique feugiat.'}
        ],
        'languages': ['English', 'French'],
        'references': [
            {'name': 'Estelle Darcy', 'position': 'CEO', 'company': 'Wardiere Inc.', 'phone': '+123-456-7890', 'email': 'hello@reallygreatsite.com'},
            {'name': 'Harper Russo', 'position': 'CEO', 'company': 'Wardiere Inc.', 'phone': '+123-456-7890', 'email': 'hello@reallygreatsite.com'}
        ],
        'gender': 'male'  # Can be 'male' or 'female'
    }
    return render(request, 'resume_app/resume.html', {'resume': resume_data})
