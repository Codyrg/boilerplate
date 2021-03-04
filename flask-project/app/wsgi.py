from app import app

# run with gunicorn --bind 0.0.0.0:5000 wsgi:app
if __name__ == "__main__":
    app.run()

