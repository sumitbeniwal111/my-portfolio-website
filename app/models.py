# portfolio_app/app/models.py
from app import db
from datetime import datetime

class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Text, nullable=False, default=lambda: datetime.now().isoformat())

    def __repr__(self):
        return f"<ContactMessage {self.name} - {self.email}>"