# Training and Placement Portal

## Overview

The Training and Placement Portal is a comprehensive web application designed to facilitate seamless job applications for college students. Developed using a robust technology stack including Python, PHP, HTML, CSS, JavaScript, and Django, this portal aims to streamline the placement process while offering adaptive recommendations for students' skill enhancement and career advancement.

## Features

- **Seamless Job Applications:** Empower students to apply for their desired jobs with ease.
- **Adaptive Recommendation System:** Evaluates students’ performance and suggests relevant courses for skill enhancement and career advancement.
- **User-friendly Interface:** Intuitive and easy-to-navigate frontend developed using PHP, HTML, CSS, and JavaScript.
- **Robust Backend:** Secure and scalable backend built with Python and Django.
- **Database Management:** Efficient data handling with PHPMyAdmin and SQL.

## Technology Stack

### Frontend
- **PHP**
- **HTML**
- **CSS**
- **JavaScript**

### Backend
- **Python**
- **Django**

### Database
- **PHPMyAdmin**
- **SQL**

## Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- Django
- PHP
- MySQL
- PHPMyAdmin

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/training-and-placement-portal.git
    cd training-and-placement-portal
    ```

2. **Backend Setup:**

    - Navigate to the backend directory:
      ```sh
      cd backend
      ```
    - Create a virtual environment and activate it:
      ```sh
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```
    - Install the required Python packages:
      ```sh
      pip install -r requirements.txt
      ```
    - Run database migrations:
      ```sh
      python manage.py migrate
      ```
    - Start the Django development server:
      ```sh
      python manage.py runserver
      ```

3. **Frontend Setup:**

    - Navigate to the frontend directory:
      ```sh
      cd ../frontend
      ```
    - Ensure PHP is properly configured and run the PHP server:
      ```sh
      php -S localhost:8000
      ```

4. **Database Setup:**

    - Import the SQL database using PHPMyAdmin.
    - Configure the database settings in the Django project to connect to your MySQL database.

### Usage

1. **Access the application:**
   - Visit `http://localhost:8000` for the PHP frontend.
   - Visit `http://127.0.0.1:8000` for the Django backend (API and admin interface).

2. **Admin Interface:**
   - To manage the portal, access the Django admin interface at `http://127.0.0.1:8000/admin`.
   - Use the admin credentials to log in and manage job postings, user profiles, and recommendations.

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch 
3. Commit your changes 
4. Push to the branch 
5. Open a pull request.

