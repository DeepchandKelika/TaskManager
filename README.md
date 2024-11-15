# Task Manager
Task Manager is a web-based application built using Django. It enables users to manage tasks efficiently with features like user authentication, task creation/editing, Google OAuth integration, and an admin interface to manage users and settings.
## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [GoogleOAuth Config](#GoogleOAuth-Config)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Admin Panel](#admin-panel)


## Features

- User registration and login (including Google OAuth)
- Task creation, editing, and deletion
- Custom admin panel for managing tasks and user invitations
- Responsive user interface with Bootstrap integration
- Invite new users via email

## Tech Stack

- Backend: Django, Django-Allauth
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default configuration)
- Others: Crispy Forms, Google OAuth integration

## Setup Instructions
### Prerequisites

- Python 3.10 or later
- Virtual environment tool (optional but recommended)
- Google OAuth config, shown next.

### GoogleOAuth Config

To enable Google OAuth, you need to obtain the Client ID and Client Secret from the Google Cloud Console.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or select an existing project).
3. Navigate to **APIs & Services** > **Credentials**.
4. Click on **Create Credentials** and select **OAuth Client ID**.
5. Configure the consent screen and save the settings.
6. Select **Web application** and provide the necessary information, such as the redirect URI (e.g., `http://127.0.0.1:8000/accounts/google/login/callback/`).
7. Click **Create** to generate the Client ID and Client Secret.
8. Add these credentials to your `.env` file as mentioned in step 4 of installation, [Environment Variables](#environment-variables).


### Installation

1) Clone the repository:
```
git clone https://github.com/DeepchandKelika/TaskManager.git
cd TaskManager
```

2) Create and activate a virtual environment (recommended):

  On Windows:
  
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
  
  On macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3) Install the dependencies:
  ```
  pip install -r requirements.txt
  ```

4) Configure environment variables:

Create a .env file in the project directory and add the following variables:

```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=<Your Google OAuth Client ID>
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=<Your Google OAuth Client Secret>
EMAIL_HOST=<Your Email Host>
EMAIL_PORT=<Your Email Port>
EMAIL_HOST_USER=<Your Email Address>
EMAIL_HOST_PASSWORD=<Your Email Password>
```

5) Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```

6) Create a superuser to access the admin panel:
```
python manage.py createsuperuser
```

7) Start the development server:
```
python manage.py runserver
```

8) Access the application at [http://localhost:8000](http://localhost:8000).

## Environment Variables

Ensure that sensitive information like keys and passwords are stored in a .env file or environment variables.
## Usage

- Register or log in using your credentials or with Google OAuth.
- Create, view, edit, and delete tasks.
- Admins can manage users and Google OAuth keys through the custom admin panel.

## Admin Panel

Admins can access the admin panel by navigating to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using their superuser credentials. The admin panel allows for managing tasks, user invitations, and more.

    
