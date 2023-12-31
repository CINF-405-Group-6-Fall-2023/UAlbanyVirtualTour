# views.py
from django.http import Http404
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
        },    

        'campus-center': {
            'title': 'Campus Center',
            'mission': "The Campus Center provides a convenient place for a diverse community to socialize, collaborate, get involved, experience events, enhance the quality of student life and contribute to the University’s co-curricular and educational mission.",
            'ideals': "We value diversity, inclusion, sustainability, student involvement, and community engagement.",
            'vision': "Be the nexus of collaboration, connection, and service; enriching the experience of the entire University at Albany community and beyond.",
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
            'history': "Just two months after UAlbany's predecessor, the State Normal School at Albany, opened in December 1844, its first library was opened in one room of a former train depot on State Street, with the School receiving its first private donation, a bequest of $300 to purchase library books, at around the same time.",
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
                    'Main Office': '518-442-3995',
                    'Fax': '518-442-5099',
                    'Email': 'pac@albany.edu',
                    'Address': 'UAlbany Performing Arts Center PAC 266 1400 Washington Avenue Albany, NY 12222',
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
            'mission': "Taconic is home to the University's Academic Advising Offices. You will go here to meet with you advisors every semester to plan your academic career and classes as an undergraduate student.",
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
            'mission': "The Life Sciences Building houses the University's forays into research on RNA science and technology, neuroscience, microbiology, molecular evolution of disease, and molecular and cell biology. Any student looking to pursue a career in Life Sciences will become well acquainted with this building over the course of their academic career here at the University, as this building houses many of the labs, machines, and research facilities that they will be using in their education.",
            'history': "The Life Sciences Initiative that calls this building home was founded on the philosophy that scientific discovery is a multidisciplinary, collaborative and highly interactive enterprise. Discovery occurs at the frontiers and intersections of science and Life Sciences faculty provide a critical focus for collaborative discovery across traditional departments as well as with other University at Albany and regional scientists.",
            'amenities': ['Molecular Biology Core Facility', 'Tissue Culture Core Facility', 'Structural Chemistry Core Facility', 'RNA Epitranscriptomics and Proteomics Resource (REPR) Facility', 'Biological Research Facility ', 'Laboratory Animal Facility', 'Greenhouse Facility', 'X-Ray Crystallography Facility Core', 'Meeting Rooms, Auditorium, and Conference Facilities', 'RNA Institute'],
        },
	
	'science-library': {
            'title': 'Science Library',
            'mission': "The Science Library will be an important location to anyone pursuing a degree in STEM. It contains hundreds of thousands, if not a million different cataloged scientific resources, in addition to a preservation department dedicated to maintaining current and antique materials, and a special collection of historical manuscripts and other materials gathered in the University’s archives.",
            'history': "The Science Library was opened in September 1999, to house the University's scientific resources, in addition to the M. E. Grenander Department of Special Collections & Archives, and the Library Preservation Laboratory. The building now also houses International Programs and the New York State Writers Institute.",
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

	'massry-center': {
            'title': 'Massry Center for Business',
            'mission': "The Massry center is a school for business, providing high-quality education and advanced knowledge through scholarly and applied research, and engaging effectively with alumni and the business and academic communities. It also offers innovative and distinctive niche programs and experiential learning opportunities, in collaboration with campus and corporate partners. These programs provide our students with a competitive edge in the job market. With the school’s strong pipelines to the business community, the majority of our students are placed in jobs before graduation and have access to top executives in leading firms. School of Business alumni become a powerful network of leaders truly shaping the business world.",
            'ideals': "The Massry aims to nuture sophisticated, ethical, globally-oriented leaders for a digital economy. It will accomplish this by providing rigorous business education, advancing knowledge through scholarly and applied research, and engaging alumni and the business community. It will offer innovative programs that make students technologically adept and provide them a competitive edge. From opportunity to impact: It will serve as a gateway to opportunities for students, staff, and faculty so that they can have a positive impact on their professions and communities.",
            'vision': "The Massry works to enhance the Center's standing as an innovative, research-oriented, diverse business school that provides experiential learning for our students and professional development for our students, staff, and faculty.",
            'leadership': [
                'Dr. Kevin J. Williams Interim Dean',
                'Janet Marler Associate Dean and Professor',
                'William Wales Associate Dean for Research and Standish Professor of Entrepreneurship and Chair, Management',
                'Tara Curley Vice Dean, Finance and Administrative Operations',
                'Ann Hughes Director of Development',
            ],
            'access_hours_contact': {
                'building_access': [
                    'On-Site: Monday - Friday, 9 a.m. to 5 p.m.',
                ],
                'contact_info': {
	            'Main Office': '518-956-8320',
	            'Address': 'The Massry Center for Business PAC 266 1400 Washington Avenue Albany, NY 12222',
                },
            },
        },

        'university-hall-admissions': {
            'title': 'University Hall Admissions',
            'mission': "We, at UAlbany, know there's greatness already in you - it's been there all along. Our offer to you is a simple one: let us help you be the best you. UAlbany is one of only 146 Research 1 institutions in the nation, it's students and faculty represent more than 100 nations, and it's one of only 290 institutions with a chapter of Phi Beta Kappa. We want you to see what we see — a blazing potential thats ready to be unleashed, and we'd love to have you join our family.",
            'additional_info': [
		'COSTS 2022-2023: NYS Resident Tuition: $7,070 || Out-of-State Tuition: $24,910 || Room, Board & Fees: $18,895',
                'ENROLLMENT: 12,654 undergraduates || 4,421 graduate students || 2,800 new first-years || 1,300 new transfers',
	    ],
	    'enroll': [
		{'name': 'Enroll as a First Year Student', 'link': 'https://www.albany.edu/admissions/how-apply-first-year-student/'},
                {'name': 'Enroll as a Transfer Student', 'link': 'https://www.albany.edu/admissions/how-apply-transfer-student/'},
                {'name': 'Scholarships & Aid', 'link': 'https://www.albany.edu/admissions/scholarships-aid/'},
            ],
	    'amenities': ['We offer 9 Schools & Colleges', '1200 World-Class Faculty Members with an 18:1 Student-Faculty Ratio', '170+ Research Labs & Centers', '300+ Student Clubs', ' And 19 NCAA Division I Athletic Teams'],
            'access_hours_contact': {
                'building_access': [
                    'Appointments: 9 a.m. to 5 p.m. Monday to Friday',
                    'Phones: 9 a.m. to 4 p.m. Monday to Friday',
                ],
                'contact_info': {
                    'Main Office': '518-442-5435',
                    'Fax': '518-437-3617',
                    'Email': 'ugadmissions@albany.edu',
                    'Address': 'University Hall 112 1400 Washington Avenue Albany, NY 12222',
                },
            },
        },

	'colonial-quad': {
            'title': 'Colonial Quad',
            'mission': "Colonial Quad is a sophomore year living space on campus. It is closest to Collins Circle and Mail Services.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-5911",
                },
            },
            'quad_dorms': ['Hamilton Hall', 'Herkimer Hall', 'Johnson Hall', 'Livingston Tower', 'Paine Hall', 'Zenger Hall', 'Morris Hall', 'Delancey Hall', 'Clinton Hall'],
        },
	    
	'dutch-quad': {
            'title': 'Dutch Quad',
            'mission': "Dutch Quad is a sophomore year living space on campus. It is closest to the Campus Center and Broadview.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-5900",
                },
            },
            'quad_dorms': ['Ten Eyck Hall', 'Ten Broeck Hall', 'Van Rensselaer Hall', 'Stuyvesant Tower', 'Ryckman Hall', 'Bleeker Hall', 'Beverwyck Hall', 'Van Cortlandt Hall', 'Schuyler Hall'],
        },

	'indigenous-quad': {
            'title': 'Indigenous Quad',
            'mission': "Indigenous Quad is a freshman year living space on campus. It is closest to the Campus Center and Broadview.", 
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-5940",
                },
            },
            'quad_dorms': ['Cayuga Hall', 'Adirondack Hall', 'Oneida Hall', 'Mohawk Tower', 'Onondaga Hall', 'Mahican Hall', 'Montauk Hall', 'Seneca Hall', 'Tuscarora Hall'],
        },
	    
	'state-quad': {
            'title': 'State Quad',
            'mission': "State Quad is a freshman year living space on campus. It is closest to Collins Circle and Mail Services.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-5920",
                },
            },
            'quad_dorms': ['Irving Hall', 'Fulton Hall', 'Whitman Hall', 'Eastman Tower', 'Tappan Hall', 'Cooper Hall', 'Steinmetz Hall', 'Anthony Hall', 'Melville Hall'],
        },

	'empire-commons': {
            'title': 'Empire Commons',
            'mission': "Empire Commons is an upperclassman apartment-style living space on campus. It is closest to Collins Circle and the main campus buildings.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-956-6250",
                },
            },
            'amenities': ['Single Bedrooms', 'Fully furnished living rooms', 'Fully Equipped Kitchens', 'Apartment Laundry Room', 'Utilities', 'Outdoor Courts', 'Gym', 'Community Building', 'Parking'],
        },

	'liberty-terrace': {
            'title': 'Liberty Terrace',
            'mission': "Liberty Terrace is an upperclassman apartment-style living space on campus. It is closest to Broadview Center and Guilderland.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-956-8300",
                },
            },
            'amenities': ['Single Bedrooms', 'Fully furnished living rooms', 'Fully Equipped Kitchens', 'Elevators', 'Utilities', 'Softball Field', 'Gym', 'Community Area', 'Parking'],
        },
	    
	'freedom-apartments': {
            'title': 'Freedom Apartments',
            'mission': "Freedom Apartments is an upperclassman apartment-style living space on campus. It is closest to Stuyvesant Plaza and the Albany Nanotech Complex.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-5830",
                },
            },
            'amenities': ['Double Bedrooms', 'Fully furnished living rooms', 'Fully Equipped Kitchens', 'Accessibility', 'Utilities', 'Patio', 'Gender Inclusive Housing', 'Shuttle Bus Stop', 'Parking'],
        },
		
	'boor-sculpture-studio': {
            'title': 'Boor Sculpture Studio',
            'mission': "If the Fine Arts Building is where you can further your education in 2-dimensional and digital art, then the Boor Sculpture Studio is where you will learn about several disciplines in 3-dimensional art. Inside the building, you will find tools, machines, and rooms dedicated to woodwork, welding, spray-painting, plasterwork, and all sorts of other crafts skills.",
            'history': "After the death of her husband in 1978, Terri Boor was inspired to further her art education at UAlbany and to make a generous donation towards the construction of the Studio, which now bears her name. The Studio celebrated its 20th Anniversary in 2022.",
            'amenities': ['General Classrooms with well stocked supply closets and tool cabinets', 'Plaster Workshop', 'Ventilated Spray-Painting Room', 'Wood Workshop', 'Clay-Firing Kilns', 'Welding and Metal Workshop', 'Foundry', 'Presentation Spaces'],
        },
	    
    	'broadview-center': {
            'title': 'SEFCU Arena at Broadview Center',
            'mission': "In the spring of 1992, the University at Albany opened the Broadview Center SEFCU Arena, an $11 million state-of-the-art facility.  The SEFCU Arena is the home for UAlbany's men's and women's basketball teams, and has an .11 mile indoor track.  The arena also serves as a major venue of community events such as concerts, sporting events and University activities. In 2017, the University at Albany has unveiled a new video scoreboard in SEFCU Arena that was made possible by a $1 million donation from Ed Swyer and Stuyvesant Plaza. The new board, which hangs above center court, will provide an video feed of the game, in-game statistics, and replay for the men's and women's basketball games. The SEFCU Arena is available to rent to non-commercial entities for special events, games and practices. Full Arena rental is available for a daily flat rate or individual courts and/or track may be rented by the hour. Payments Accepted:  SEFCU Arena accepts cash and credit card transactions.  Accepted credit cards are Visa, AmEx, Mastercard and Discover.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
                },
            },
            'amenities': ['Basketball Court', '.11 mile track', 'Training facilities', 'Stage', 'Modular Configuration'],
        },
	    
	'fallon-field': {
            'title': 'John Fallon Field',
            'mission': "John Fallon Field, the home for UAlbany men's and women's lacrosse, was completed in the fall of 2005. Fallon, a former UAlbany student-athlete, and a partner at Kay Scholer LLP in New York City, made a significant contribution to fund the construction of the all-weather turf field with permanent stands and press box. John Fallon Field is available to rent to non-commercial entities for lacrosse and field hockey games and practices at an hourly rate.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
		},
	    },	
            'amenities': ['All Weather Field', '2500 Person Capacity', 'Fieldturf Vertex Prime Turf'],
        },

	'bob-ford-field-at-tom-mary-casey-stadium': {
            'title': 'Bob Ford Field at Tom & Mary Casey Stadium',
            'mission': "The field is named in honor of Bob Ford, who coached UAlbany football from its inception until 2013. It is $19 million multi sport complex that house 8500 seats, a 39x22 Daktronics Scoreboard and five luxury suites. The stadium just celebrated its 10th birthday, as construction was completed in Spring of 2013. Tom & Mary Casey Stadium is available to rent to non-commercial entities for special events, games and practices. Casey Stadium (press box, concourse and field) can be rented for a daily flat rate or access to Bob Ford Field only can be rented hourly. Payments Accepted:  Tom & Mary Casey Stadium accepts cash and credit card transactions. Accepted credits cards are: Visa, AmEx, Mastercard and Discover. Special campus parking is allocated for Football game days.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
		},
	    },	
            'amenities': ['Luxury Suites', '8500 Person Capacity', 'Hot Food', 'Hot and Cold Beverages', 'Dedicated Parking'],
        },
	
	'track-field-complex': {
            'title': 'Track and Field Complex',
            'mission': "The new track and field venue, located adjacent to the Physical Education building in the site of former University Field, has a 9-lane IAAF certified track. The surface is Olympic-caliber Beynon BSS 2000 that features a force reduction layer of butyl rubber and full-depth color Polyurethane. There is a natural turf infield that includes a throws area as well as an irrigation system. There is also a separate hammer throw area adjacent to the venue. The venue, which is used strictly for track and field activities, was completed in the fall of 2013.",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
		},
	    },	
            'amenities': ['Beynon BSS 2000 Track Surface', 'Hammer Throw', 'Covered Stands'],
	},
			
	'ualbany-field': {
            'title': 'UAlbany Field',
            'mission': "UAlbany Field, just to the west of the Physical Education Building and Track & Field Complex, serves as the home venue for the UAlbany softball program. The facility has been used throughout the program's transition from NCAA Division III to its present Division I affiliation. UAlbany Field is available to rent to non-commercial entities for softball games and practices at an hourly rate",
	    'access_hours_contact': {
                'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
		},
	    },	
            'amenities': ['Heated Dugouts', 'New Foul Poles', 'New Backstop & Fencing', 'Inning by Inning Scoreboard'],
	},
	
	'varsity-field': {
            'title': 'Varsity Field',
            'mission': "In addition to the primary stadiums, UAlbany is also host to a number of less formal sporting fields used for practice, intramurals and general student use. Some of these fields at UAlbany are available to rent to non-commercial entities for various games and practices at an hourly rate",
	    'access_hours_contact': {
		'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
		},
	    },	
            'amenities': ['New Warning Track & Foul Poles', 'Inning by Inning Scoreboard', 'Bullpens & Hitting Cages'],
	},
	
	'other-facilities': {
            'title': 'Practice, Recreation and Intramural Fields',
            'mission': "In addition to the primary stadiums and fields, UAlbany is also host to a number of less formal sporting fields used for practice, intramurals and general student use. Some of these fields at UAlbany are available to rent to non-commercial entities for various games and practices at an hourly rate",
	    'access_hours_contact': {
		'contact_info': {
                    'Phone Number': "518-442-2562",
		    'Email': 'mbenson@albany.edu',
		},
	    },	
            'amenities': ['Tennis Courts', 'Indoor Basketball Courts', 'Oudoor Basketball Courts', 'Grass Fields', 'Turf Fields', 'Low Ropes Course'],
	},
	
	'physical-education-building': {
            'title': 'Practice, Recreation and Intramural Fields',
            'mission': "The Physical Education Building on the Campus of UAlbany houses serves the unvirsity as a whole, with special focus on health education, campus recreation and varsity athletes. The Building is will equipped with fitness centers, weight rooms, specialized areas for group fitness classes, all while encouraging a holistic approach for physical well being. Undergraduates have access to these facilities at no additional charge, while heavily discounted passes are available to graduate students and faculty. UAlbany seeks to promote a dynamic and all inclusive enviroment the enhances both the physical and academic aspects of exercise science.",
	    'access_hours_contact': {
		'contact_info': {
                        'Phone Number': "518-442-2627",
			'Email': 'campusrec@albany.edu',
		},
	    },	
            'amenities': ['Basketball Court', 'Training Rooms', 'Weight Rooms', 'Sports Medicine Center', 'Basketball Courts', 'Group Exercise Classes'],
	    'hours': [
                'Monday: 7 a.m. to 10 p.m.',
                'Tuesday: 7 a.m. to 10 p.m.',
                'Wednesday: 7 a.m. to 10 p.m.',
                'Thursday: 7 a.m. to 10 p.m.',
                'Friday: 7 a.m. to 8 p.m.',
                'Saturday: 11 a.m. to 7 p.m.',
                'Sunday: 11 a.m. to 7 p.m.',
            ],
	},
 
	'albany-nanotech': {
            'title': 'Albany Nanotech Complex',
            'mission': "The Albany NanoTech Complex is home to UAlbany's College of Nanoscale Science and Engineering. The site offers a fully-integrated research, development, prototyping, and educational facility that provides strategic support through outreach, technology acceleration, business incubation, pilot prototyping, and test-based integration support for onsite corporate partners including IBM, GlobalFoundries, Samsung, Applied Materials, Tokyo Electron, ASML and Lam Research, as well as other “next generation” nanotechnology research activities, including hands-on internships for students along with career opportunities.",
	    'access_hours_contact': {
     		'contact_info': {
                    'Phone Number': "315-792-7500",
		    'Email': 'admissions@sunypoly.edu',
		 },
	    },	
            'amenities': ['NanoFab Extension', 'NanoFab 200', 'Library', 'NYS Data Center', 'Advanced Cybersecurity Research Lab'],
        },

	'etec': {
	    'title': 'Emerging Technology and Entrepreneurship Complex (ETEC)',
	    'mission': 'ETEC is a $180 million, 246,000 square foot state-of-the-art building that “houses” researchers, educators and entrepreneurs under the same roof as some of UAlbany\’s fastest-growing programs. It is the largest instructional building on the Uptown Campus, housing 40+ labs and employing more than 200 full-time faculty and researchers and 100 research and industry partners.',
	    'ideals': 'WEATHER. CLIMATE. EMERGENCY PREPAREDNESS. SUSTAINABILITY. These disciplines are preparing tomorrow\’s leaders to tackle the most serious challenges facing humankind. Individually, they yield new, critical knowledge; but when co-located inside ETEC, UAlbany\’s newest state-of-the-art and environmentally sustainable facility, they become a striking example of how a whole can be greater than the sum of its parts. ETEC is a hub for innovation, scholarship, applied research and commercial development designed to foster cross-disciplinary collaborations to confront complex problems. Inside, students, faculty and researchers work hand-in-hand with entrepreneurs to translate new knowledge into creative solutions that fuel economic growth and create jobs.',
	    'vision': 'By leveraging an asset that no other university in New York can - UAlbany\’s proximity to the nerve center of New York State policy and decision-making through its location across the street from the New York State Division of Homeland Security and Emergency Services (DHSES), Office of Emergency Management and the New York State Police - ETEC offers UAlbany students, faculty and staff unparalleled applied learning and research opportunities in partnership with key agencies working to make New York safer, more prepared and more resilient.',
	    'amenities': [
		    'The College of Emergency Preparedness, Homeland Security and Cybersecurity',
		    'The College of Nanotechnology, Science, and Engineerings: Department of Environmental Engineering and Department of Electrical and Computer Engineering.',
		    'The College of Arts and Sciences: Department of Atmospheric and Environmental Sciences and Department of Chemistry research labs',
		    'Atmospheric Sciences Research Center',
		    'Center of Excellence in Weather & Climate Analytics',
		    'The National Weather Service’s  Regional Forecast Office and Training Program',
		    'The New York State Mesonet',
		    'The Small Business Development Center',
		    'Office for Innovation Development and Commercialization/Technology Transfer',
		    'Cybersecurity and Artificial Intelligence Institute',
		    'Private partners such as TruWeather Solutions LLC',
	    ],
	},	 
    }
    
    building_info_selected = dict(building_info.get(building_slug, {}))
    if not building_info_selected:
        raise Http404("Building not found")
    return render(request, 'articles/article.html', {'building_info': building_info_selected})
