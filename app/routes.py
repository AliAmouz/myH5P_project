from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Course
from . import db, login_manager

main_bp = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main_bp.route('/')
def index():
    return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    courses = Course.query.all()
    return render_template('dashboard.html', courses=courses)

@main_bp.route('/course/<int:course_id>')
@login_required
def course(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course.html', course=course)

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
