# Django Leave

Django Leave is a web-based application developed using the Django framework, designed to simplify and automate the process of managing employee leave requests within an organization. It allows employees to submit leave applications with relevant details and supporting documents, while providing HR personnel and authorized administrators with tools to review, approve, reject, or delete these requests.

### Getting Started

These instructions will guide you through setting up Django Leave on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv leave_env
    cd leave_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-leave.git
    cd django-leave

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create a super user. This account will be used to access the admin dashboard and manage users.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

- User Authentication & Authorization: Secure login system with role-based access control to ensure users can only access functionalities relevant to their role (employee or HR).

- Leave Request Creation: Employees can create and submit leave requests with required details and file attachments.

- Leave Request Update & Deletion: Employees can update or delete their leave requests if they are still in Pending status.

- Approval Workflow: HR personnel can view all submitted requests and approve or reject them, excluding their own submissions to prevent conflict of interest.

- Email Notifications: Automated email alerts are sent to employees upon submission, approval, or rejection of leave requests, ensuring timely updates.

- Leave Status Management: Requests move through statuses (Pending, Approved, Rejected) and are displayed accordingly.

- Filtering & Search: Integrated filtering using django-filter allows users to search and narrow down requests based on various criteria.

- Pagination: Leave requests are paginated for better readability and smoother navigation when dealing with large data sets.

- Detailed View: Users can view comprehensive details of each leave request on a dedicated page.

- Feedback Messaging: Clear user feedback via Django’s messaging framework helps guide and inform users through each action.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project

