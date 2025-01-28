# Job Management Assignment

This project is a Django-based application for managing freelancers and their skills.

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST framework
- PostgreSQL (or any other preferred database)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/job_management_assignment.git
   cd job_management_assignment
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Update the `DATABASES` setting in `settings.py` with your database configuration.
   - Apply the migrations:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## API Endpoints

- **List Freelancers:** `GET /api/freelancers/`
- **Create Freelancer:** `POST /api/freelancers/`
- **Retrieve Freelancer:** `GET /api/freelancers/<id>/`
- **Update Freelancer:** `PUT /api/freelancers/<id>/`
- **Delete Freelancer:** `DELETE /api/freelancers/<id>/`

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
