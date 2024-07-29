complex_dict = {
    "personal_info": {
        "name": "Ashwani Kumar",
        "age": 30,
        "gender": "Male",
        "contact": {"phone": "+91-9876543210", "email": "ashwani@example.com"},
        "address": {
            "house_number": "123",
            "street": "Main Bazaar",
            "city": "Sirsa",
            "district": "Sirsa",
            "state": "Haryana",
            "postal_code": "125055",
            "country": "India",
        },
    },
    "education": {
        "high_school": {
            "name": "Govt Senior Secondary School",
            "year_of_passing": 2010,
            "percentage": 85.4,
        },
        "undergraduate": {
            "college": "University of Delhi",
            "degree": "B.Tech in Computer Science",
            "year_of_passing": 2014,
            "cgpa": 8.5,
        },
        "postgraduate": {
            "college": "IIT Delhi",
            "degree": "M.Tech in Software Engineering",
            "year_of_passing": 2016,
            "cgpa": 9.0,
        },
    },
    "professional_experience": [
        {
            "company": "Infosys",
            "role": "Software Engineer",
            "duration": "2016-2018",
            "technologies_used": ["Java", "Spring", "Hibernate"],
        },
        {
            "company": "TCS",
            "role": "Senior Software Developer",
            "duration": "2018-2021",
            "technologies_used": ["Python", "Django", "ReactJS"],
        },
        {
            "company": "Netatech Engineering",
            "role": "Lead Software Developer",
            "duration": "2021-Present",
            "technologies_used": ["Python", "Flask", "Docker", "Kubernetes"],
        },
    ],
    "skills": {
        "programming_languages": ["Python", "Java", "C++", "JavaScript"],
        "web_technologies": ["HTML", "CSS", "JavaScript", "ReactJS", "Angular"],
        "databases": ["MySQL", "PostgreSQL", "MongoDB"],
        "tools": ["Git", "Docker", "Kubernetes", "Jenkins"],
    },
    "projects": [
        {
            "title": "Bluetooth Reader",
            "description": "A universal Bluetooth receiver designed to read data from various Bluetooth-enabled devices.",
            "technologies": ["Python", "Bluetooth"],
            "status": "Completed",
        },
        {
            "title": "School Portal",
            "description": "A comprehensive portal for managing school activities, including student and teacher logins, assignment uploads, and exam results.",
            "technologies": ["Docker", "Flask", "ReactJS"],
            "status": "Ongoing",
        },
    ],
    "languages_known": {
        "native": ["Hindi"],
        "fluent": ["English"],
        "basic": ["Punjabi"],
    },
    "hobbies": ["Reading", "Travelling", "Coding", "Playing Cricket"],
    "social_profiles": {
        "linkedin": "https://www.linkedin.com/in/ashwani-kumar",
        "github": "https://github.com/ashwanikumar",
    },
    "search_history": {
        "recent_searches": [
            "Oxford Dictionary",
            "Python tutorials",
            "Latest technology trends",
        ],
        "frequently_visited": ["stackoverflow.com", "github.com", "medium.com"],
    },
    "bookmarks": [
        {"title": "Python Documentation", "url": "https://docs.python.org/3/"},
        {"title": "Flask Documentation", "url": "https://flask.palletsprojects.com/"},
        {"title": "Docker Documentation", "url": "https://docs.docker.com/"},
    ],
    "api_responses": {
        "oxford_dictionary": {
            "word": "example",
            "definitions": [
                "A thing characteristic of its kind or illustrating a general rule.",
                "A printed or written problem or exercise designed to illustrate a rule.",
            ],
            "phonetic_spelling": "/ɪɡˈzɑːmpəl/",
            "examples_of_usage": [
                "This is a good example of how Europe’s constituent nations are still individually very different.",
                "It is important to cite examples to support your argument.",
            ],
            "synonyms": ["sample", "specimen", "instance", "case"],
        }
    },
}

print(complex_dict["education"]["postgraduate"]["cgpa"])


def finddict_value(dict):
    """a function to find a key value from dectnory"""
    for i in dict:
        print(i)
    a = str(input("enter a key from showing on top "))
    kv = int(input("\nwhat you want to see\n1.keys inside this\n2.values inside this"))

    """to defferenciate between keys and values"""
    if kv == 1:
        for i in dict[a]:
            print(i)
        b = str(input("enter a key from showing on top "))
        kv = int(input("\nwhat you want to see\n1.keys inside this\n2.values inside this"))
        """to defferenciate between keys and values"""
        if kv == 1:
            for i in dict[a][b]:
                print(i)
            c = str(input("enter a key from showing on top "))
            kv = int(input("\nwhat you want to see\n1.keys inside this\n2.values inside this"))
            """to defferenciate between keys and values"""
            if kv==2:
                print(dict[a][b][c])
            else:
                print("not key/value abliable")
        if kv == 2:
            print(dict[a][b])
        else:
            ("entered value in valid")
    if kv == 2:
        print(dict[a])


finddict_value(complex_dict)


