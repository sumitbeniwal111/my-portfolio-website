# portfolio_app/run.py
import os
from app import create_app, db

app = create_app()

# Corrected way to create tables on application startup
# This code block runs when 'run.py' is executed and 'app' is created
with app.app_context():
    db.create_all()
    print("Database tables ensured to be created.") # Optional: Add a print statement for confirmation

if __name__ == '__main__':
    # Ensure static and templates directories exist (good for initial setup)
    os.makedirs('app/static/css', exist_ok=True)
    os.makedirs('app/static/js', exist_ok=True)

    print(f"Starting Flask app.")
    # In development, debug=True. For production, set debug=False and use a production WSGI server.
    app.run(debug=False)