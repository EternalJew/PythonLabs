from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
 
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category = 'success')
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again!', category = 'error')
        else:        
            flash('incorrect email, try again!', category = 'error')
        
        
    return render_template("login.html", boolean = True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email = email).first()
        
        if user:
            flash('Email already exist', category = 'error')
        elif len(email) < 4:
            flash('email is so small', category = 'error')
        elif len(first_name) < 2:
            flash('name is so small', category = 'error')
        elif password1 != password2:
            flash('passwords dont match', category = 'error')
        elif len(password1) < 7:
            flash('password is so small', category = 'error')
        else:
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created!', category = 'success')
            return redirect(url_for('views.home'))
            
    
    return render_template("sign_up.html")