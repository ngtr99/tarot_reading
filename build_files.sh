# Install dependencies
pip install -r requirements.txt

# Make migrations and migrate the database
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput