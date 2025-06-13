# portfolio_app/app/routes/main.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import ContactMessage
from datetime import datetime

main_bp = Blueprint('main', __name__)

# Route for the main portfolio page
@main_bp.route('/')
def index():
    return render_template('index.html')

# Route for handling contact form submissions
@main_bp.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            new_message = ContactMessage(
                name=name,
                email=email,
                message=message,
                timestamp=datetime.now().isoformat()
            )
            db.session.add(new_message)
            db.session.commit()
            flash('Your message has been sent successfully!', 'success')
            # Pass the name to the success route
            return redirect(url_for('main.success', name=name))
        except Exception as e:
            db.session.rollback() # Rollback in case of an error
            print(f"Database error: {e}")
            flash('An error occurred while saving your message. Please try again later.', 'danger')
            return render_template('index.html') # Or a dedicated error page

# Route for the success page, now accepting a name
@main_bp.route('/success/<name>')
def success(name):
    # Pass the captured name to the template
    return render_template('success.html', name=name)