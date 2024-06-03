from flask import Blueprint, render_template, redirect, url_for, request, session, send_from_directory
from app.models import db, User, Course, Enrollment

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    user = User.query.get(session['user_id'])
    courses = user.courses
    return render_template('dashboard.html', courses=courses)

@main_bp.route('/course/<int:course_id>')
def course(course_id):
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    course = Course.query.get(course_id)
    return render_template('course.html', course=course)
