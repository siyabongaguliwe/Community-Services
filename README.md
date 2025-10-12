🏘️ Community Services API
A Django + Django REST Framework backend for connecting township and suburban communities through housing listings, local services, and events. Built as part of the ALX Capstone Project.

🚀 Features
🔐 User registration, login, logout, and profile management

🏠 Housing listings with location, price, and owner details

🛠️ Local services with categories, ratings, and provider info

📅 Community events with organizer and location

⭐ Reviews for services with rating and comment

📦 RESTful API endpoints for all models

🔒 CSRF protection and secure password handling

🧪 Browsable API interface for testing

🧩 Technologies Used
Python 3.12

Django 5.2

Django REST Framework

SQLite (development) / PostgreSQL (optional)

HTML & CSS (for auth templates)

Git & GitHub

📁 Project Structure
Code
Community-Services/
├── django_blog/
│   ├── blog/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── static/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md
🔗 API Endpoints
Resource	Endpoint	Method	Description
Listings	/api/listings/	GET/POST/PUT/DELETE	Manage housing listings
Services	/api/services/	GET/POST/PUT/DELETE	Manage local services
Events	/api/events/	GET/POST/PUT/DELETE	Manage community events
Reviews	/api/reviews/	GET/POST/PUT/DELETE	Rate and review services
Auth	/login/, /register/, /logout/, /profile/	GET/POST	User authentication
🧪 How to Test
Run the server:

bash
python manage.py runserver
Visit:

Code
http://127.0.0.1:8000/api/
Use Postman or browser to test endpoints.

📌 Setup Instructions
Clone the repo:

bash
git clone https://github.com/siyabongaguliwe/Community-Services.git
cd Community-Services
Install dependencies:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Start the server:

bash
python manage.py runserver
📝 License
This project is open-source and built for educational purposes under the ALX Africa program.
