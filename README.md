1. Clone the Repository
    https://github.com/0188cs181047/hrms_backend
    cd hrms_backend

2. Set Up Python Virtual Environment
    # Windows
    python -m venv hrms_env
    hrms_env\Scripts\activate

    # Linux / Mac
    python3 -m venv hrms_env
    source hrms_env/bin/activate
3. Install Dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

4. Configure PostgreSQL Database
    DATABASES = {
        'default': dj_database_url.config(
            default="External db urls"
        )
    }

5. Apply Migrations
    python manage.py makemigrations
    python manage.py migrate

6. Create Superuser
    python manage.py createsuperuser

7. Testing APIs

    After deployment, your API base URL will be something like:
    https://hrms-backend-xxxx.onrender.com/api/

    Test endpoints like /attendance/, /employees/, etc.

    Use Postman or browser to verify responses.