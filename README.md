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

2. **Set up the environment and install dependencies:**

   ```bash
   make install
   ```

3. **Set up the database:**

   ```bash
   make migrate
   ```

4. **Create a superuser:**

   ```bash
   make createadmin
   ```

5. **Run the development server:**

   ```bash
   make run
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Available Make Commands

- `make install`: Set up virtual environment and install dependencies
- `make run`: Start the Django development server
- `make migrate`: Apply database migrations
- `make createadmin`: Create a superuser account
- `make collectstatic`: Collect static files
- `make test`: Run the test suite
- `make seed`: Seed the database with initial data
- `make clean`: Remove Python cache files

## Running Tests

To run the tests, use:

```bash
make test
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
