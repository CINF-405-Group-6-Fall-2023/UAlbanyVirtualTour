# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'landing.html')

def map_view(request):
    return render(request, 'map/index.html')

def get_building_info(request, building_slug):
    building_info = {
        'lecture-center': {
            'title': 'Lecture Center',
            'mission': "The Lecture Center, as its name states, is where you'll go to see many of your lectures. It holds 25 different large halls, auditoriums, and computer rooms that can seat upwards of 50, if not 100, students each, and lessons on a wide variety of subjects will take place there.",
            'history': "The Lecture Center was first built in 1969, and has undergone many changes and renovations since then, with the replacement of old electrical, plumbing, and ventilation systems and lighting and carpet, and the addition of new audio-visual systems continuing up through 2023, in the University’s efforts to make the campus, safer, more accessible, and on top of modern trends in technology.",
            'amenities': ['25 Different Lecture Halls, Auditoriums, and Computer Rooms', 'In-Door Seating', 'Outdoor Fountain with additional seating and tables', 'Financial Aid/Dean/Registrar Office', 'Argo Tea Shop', 'Connected pathways to the basement levels of every surrounding class building'],
            'values': "None",
        },
        
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

        'university-library': {
            'title': 'University Library',
            'mission': "The University Library will be a major part of your academic career here at UAlbany! Not only does it offer both borrowable physical academic and entertainment media, it also offers free access to several online databases of peer-reviewed articles and journals, study rooms, several open computers, and cheap printing services at just 5 cents per blank-and-white page. It also has a reference desk and many librarians and library assistants who can help you find the media and research materials that you need.",
            'history': "Just two months after UAlbany’s predecessor, the State Normal School at Albany, opened in December 1844, its first library was opened in one room of a former train depot on State Street, with the School receiving its first private donation, a bequest of $300 to purchase library books, at around the same time.",
            'amenities': ['Entertainment Media Collection', 'Textbook and Antique Reference Book Collection', 'Newspaper Microfiche Collection', 'Multimedia Collection and borrowable Technology Collection', 'Reference Desk', 'Several open Computer Stations', 'Black-and-White and Color Printing Stations', 'Silent Studying Areas and borrowable enclosed Group Work Rooms'],
            'hours': [
                'Monday: 8:30am - 11pm',
                'Tuesday: 8:30am - 11pm',
                'Wednesday: 8:30am - 11pm',
                'Thursday: 8:30am - 11pm',
                'Friday: Fri: 8:30am - 1am',
                'Saturday: Sat: 10am - 1am',
                'Sunday: 12pm - 7:30pm',
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

        'catskill-building': {
            'title': 'Catskill Building',
            'mission': "Catskill is home to The Department of Mathematics and Statistics. If you plan on taking any courses on those subjects, they will likely be in here.",
            'history': "Originally built in 1968 as the Business Administration Building, it was renovated and renamed the Catskill Building in 2019.",
            'amenities': ['Department of Mathematics and Statistics', 'Several Class, Lecture, and Study Rooms dedicated to the above subjects', 'Mail Services', 'Rapid Copy Printing Services', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },
        
        'arts-and-sciences-building': {
            'title': 'Arts and Sciences Building',
            'mission': "The Arts and Sciences Building is home to the Departments of Anthropology; Geography and Planning; and Sociology. If you plan on taking any courses on those subjects, they will likely be in here.",
            'history': "Originally called the Administration Building, it was first built in 1968.",
            'amenities': ['Department of Anthropology', 'Department of Geography and Planning', 'Department of Sociology ', 'Several Class, Lecture, Study, and Laboratory Rooms dedicated to the above subjects', 'Several high-tech testing and measurement devices that can be used to advance your research', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },
                
        'fine-arts-building': {
            'title': 'Fine Arts Building',
            'mission': "The Fine Arts Building is home to the Department of Art and Art History, as well as several lecture, computer, and studio classrooms, in addition to many individual and shared undergraduate studio spaces, twenty graduate studios, the University Art Museum, and the University’s collections of preserved and donated art. Here you can learn and practice art skills like painting, drawing, design, printmaking, photography, and photo and video editing, as well as take various courses in art history. In the Art Museum, you can see exhibits on art donated by established artists, older media taken from the University’s art archives, and works done by graduate students, with exhibits changing every semester.",
            'history': "The Fine Arts Building started construction in 1966, and finished in 1968, though the Museum was founded before then in 1967 and was designed by architect Edward Durell Stone.",
            'amenities': ['Department of Art and Art History', 'Many Lecture, Computer, and Studio Classrooms', 'Individual and Shared Undergraduate Studio Spaces', 'Twenty Graduate Studios', 'University Art Museum', 'Collections Study Space', 'Art Department Offices'],
        },
        
        'earth-science-and-mathematics-building': {
            'title': 'Earth Science and Mathematics Building',
            'mission': "While the Earth Science and Mathematics Building ironically no longer holds the Departments of Earth Science or Mathematics, many courses on various scientific and mathematics subjects still take place there, and you can expect to take a class there at least once if you are pursuing a degree in STEM.",
            'history': "This building was originally built as the Earth and Atmospheric Science Building in 1968.",
            'amenities': ['Several Class, Lecture, Study, and Laboratory Rooms dedicated to the subjects in STEM ', 'Several high-tech testing and measurement devices that can be used to advance your research', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },
                
        'biology-building': {
            'title': 'Biology Building',
            'mission': "The Biology Building is home to the Department of Biological Sciences. If you plan on taking any courses on that subject, they will likely be in here.",
            'history': "Originally called the Biological Science Building, it was first built in 1966.",
            'amenities': ['Department of Biological Sciences', 'Several Class, Lecture, Study, and Laboratory Rooms dedicated to the above subject', 'Several high-tech testing and measurement devices that can be used to advance your research', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },
        
        'chemistry-building': {
            'title': 'Chemistry Building',
            'mission': "The Chemistry Building is home to the Department of Chemistry, as well as Technical Services. If you plan on taking any courses on chemistry, they will likely be in here.",
            'history': "It was originally built in 1966.",
            'amenities': ['Department of Chemistry', 'Several Class, Lecture, Study, and Laboratory Rooms dedicated to the above subject', 'Several high-tech testing and measurement devices that can be used to advance your research', 'Technical Services', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },
    
        'physics-building': {
            'title': 'Physics Building',
            'mission': "The Physics Building is home to the Departments of Physics. If you plan on taking any courses on that subject, they will likely be in here.",
            'history': "It was originally built in 1966.",
            'amenities': ['Departments of Physics', 'Several Class, Lecture, Study, and Laboratory Rooms dedicated to the above subject', 'Several high-tech testing and measurement devices that can be used to advance your research', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },
    
        'taconic-building': {
            'title': 'Taconic Building',
            'mission': "Taconic is home to the University’s Academic Advising Offices. You will go here to meet with you advisors every semester to plan your academic career and classes as an undergraduate student.",
            'history': "Originally called the Education Building, it was first built in 1966.",
            'amenities': ['Important Sub-Locations', 'Academic Advising Offices', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },

        'humanities-building': {
            'title': 'Humanities Building',
            'mission': "The Humanities Building is home to the Departments of English; Philosophy; East Asian Studies; Languages, Literatures, and Cultures; and Women’s, Gender, and Sexuality Studies. If you plan on taking any courses on those subjects, they will likely be in here.",
            'history': "It was originally built in 1966.",
            'amenities': ['Department of English', 'Department of Philosophy', 'Department of East Asian Studies', 'Department of Languages, Literatures, and Cultures', 'Department of Women’s, Gender, and Sexuality Studies', 'Several Class, Lecture, and Study Rooms dedicated to the above subjects', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },

        'social-science-building': {
            'title': 'Social Science Building',
            'mission': "The Social Science Building is home to the Departments of Communication; History; and Psychology. If you plan on taking any courses on those subjects, they will likely be in here.",
            'history': "It was originally built in 1966.",
            'amenities': ['Department of Communication', 'Department of History', 'Department of Psychology', 'Several Class, Lecture, Study, and Laboratory Rooms dedicated to the above subjects', 'Several high-tech testing and measurement devices that can be used to advance your research', 'Small display cases and several bulletin boards displaying the University’s history and achievements, notable works or research done on various subjects, and outstanding student work', 'Comfortable seating areas'],
        },

        'life-sciences-building': {
            'title': 'Life Sciences Building',
            'mission': "The Life Sciences Building houses the University’s forays into research on RNA science and technology, neuroscience, microbiology, molecular evolution of disease, and molecular and cell biology. Any student looking to pursue a career in Life Sciences will become well acquainted with this building over the course of their academic career here at the University, as this building houses many of the labs, machines, and research facilities that they will be using in their education.",
            'history': "The Life Sciences Initiative that calls this building home was founded on the philosophy that scientific discovery is a multidisciplinary, collaborative and highly interactive enterprise. Discovery occurs at the frontiers and intersections of science and Life Sciences faculty provide a critical focus for collaborative discovery across traditional departments as well as with other University at Albany and regional scientists.",
            'amenities': ['Molecular Biology Core Facility', 'Tissue Culture Core Facility', 'Structural Chemistry Core Facility', 'RNA Epitranscriptomics and Proteomics Resource (REPR) Facility', 'Biological Research Facility ', 'Laboratory Animal Facility', 'Greenhouse Facility', 'X-Ray Crystallography Facility Core', 'Meeting Rooms, Auditorium, and Conference Facilities', 'RNA Institute'],
        },
	
		'science-library': {
            'title': 'Science Library',
            'mission': "The Science Library will be an important location to anyone pursuing a degree in STEM. It contains hundreds of thousands, if not a million different cataloged scientific resources, in addition to a preservation department dedicated to maintaining current and antique materials, and a special collection of historical manuscripts and other materials gathered in the University’s archives.",
            'history': "The Science Library was opened in September 1999, to house the University’s scientific resources, in addition to the M. E. Grenander Department of Special Collections & Archives, and the Library Preservation Laboratory. The building now also houses International Programs and the New York State Writers Institute.",
            'amenities': ['Several open Computer Stations', 'Silent Studying Areas and borrowable enclosed Group Work Rooms', 'Alice Hastings Murphy Preservation Department and Preserved Material Exhibits', 'Library Storage Facility', 'M.E. Grenander Department of Special Collections & Archives', 'New York State Writers Institute'],
            'hours': [
                'Monday: 8:30am - 9pm',
                'Tuesday: 8:30am - 9pm',
                'Wednesday: 8:30am - 9pm',
                'Thursday: 8:30am - 9pm',
                'Friday: Fri: 8:30am - 5pm',
                'Saturday: Closed',
                'Sunday: Closed',
            ],
        },
		
		'boor-sculpture-studio': {
            'title': 'Boor Sculpture Studio',
            'mission': "If the Fine Arts Building is where you can further your education in 2-dimensional and digital art, then the Boor Sculpture Studio is where you will learn about several disciplines in 3-dimensional art. Inside the building, you will find tools, machines, and rooms dedicated to woodwork, welding, spray-painting, plasterwork, and all sorts of other crafts skills.",
            'history': "After the death of her husband in 1978, Terri Boor was inspired to further her art education at UAlbany and to make a generous donation towards the construction of the Studio, which now bears her name. The Studio celebrated its 20th Anniversary in 2022.",
            'amenities': ['General Classrooms with well stocked supply closets and tool cabinets', 'Plaster Workshop', 'Ventilated Spray-Painting Room', 'Wood Workshop', 'Clay-Firing Kilns', 'Welding and Metal Workshop', 'Foundry', 'Presentation Spaces'],
        },
    }

    building_info_selected = dict(building_info.get(building_slug, {}))
    return render(request, 'articles/article.html', {'building_info': building_info_selected})
