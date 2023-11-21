# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'map/index.html')

def get_building_info(request, building_slug):
    building_info = {
        'campus-center': {
            'title': 'Campus Center',
            'mission': "The Campus Center provides a convenient place...",
            'values': "We value diversity, inclusion, sustainability...",
            'vision': "Be the nexus of collaboration, connection, and service...",
            'amenities': ['Auditorium', 'Dining', 'AcaDamien\'s Bookstore', 'Financial Aid/Dean/Registrar Office', 'Banking', 'Lounging Area', 'Wireless Internet'],
            'hours': [
                'Monday: 7:30 a.m. to 11 p.m.',
                'Tuesday: 7:30 a.m. to 11 p.m.',
                'Wednesday: 7:30 a.m. to 11 p.m.',
                'Thursday: 7:30 a.m. to midnight',
                'Friday: 7:30 a.m. to midnight',
                'Saturday: 9 a.m. to midnight',
                'Sunday: 10 a.m. to 11 p.m.',
            ],
        },
        # Add more buildings as needed
        'performing-arts-center': {
            'title': 'Performing Arts Center',
            'mission': "For over 50 years, the UAlbany Performing Arts Center (UAlbany PAC) has been a 'jewel in the crown' of the University at Albany and an important resource for the entire Capital Region community. Each year, the Prime Performance Series welcomes an array of national and international touring artists in music, dance and theatre. The Department of Music and Theatre presents approximately 40-50 concerts and three to four productions. A bustling hub of artistic activity, the UAlbany PAC boasts five unique performance theatres plus a dance studio, band/choral rehearsal rooms, scene/costume shops and both music and theatre libraries.",
            'performances': [
                {'name': 'Full Performance Schedule', 'link': 'https://www.albany.edu/pac/performance-schedule/'},
                {'name': 'Prime Performances', 'link': 'https://www.albany.edu/pac/prime-performances/'},
                {'name': 'Department Performances', 'link': 'https://www.albany.edu/pac/department-music-and-theatre-performances/'},
                {'name': 'High School Matinees', 'link': 'https://www.albany.edu/pac/high-school-matinees/'},
            ],
            'access_hours_contact': {
                'building_access': [
                    'Monday through Friday from 8am to 11pm',
                    'Saturdays from 9am to 9pm',
                    'Sundays from 9am to 7pm',
                    '* Holiday and Intercession access may have exceptions',
                ],
                'office_hours': [
                    'Monday through Friday from 8:30am to 4:30pm (academic year)',
                    '* Closed 12pm to 1pm for lunch',
                    'Monday through Friday from 8am to 4pm (summer months)',
                    '* Closed 12:30pm to 1pm for lunch',
                ],
                'contact_info': {
                    'main_office': '518-442-3995',
                    'fax': '518-442-5099',
                    'email': 'pac@albany.edu',
                    'address': 'UAlbany Performing Arts Center PAC 266 1400 Washington Avenue Albany, NY 12222',
                },
            },
        },
    }

    building_info_selected = building_info.get(building_slug, {})
    return render(request, 'articles/article.html', {'building_info': building_info_selected})