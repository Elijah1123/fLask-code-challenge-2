from flask import Blueprint, jsonify
from models.guest import Guest

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]), 200
from models import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship("Appearance", backref="episode", cascade="all, delete-orphan")
