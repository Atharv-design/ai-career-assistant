from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return render_template('index.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('auth.dashboard'))
    return render_template('login.html')

@auth_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')