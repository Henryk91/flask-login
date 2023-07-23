from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from forms import LoginForm
from mock_data import add_mock_data
from models import User
from auth import AuthService

from werkzeug.security import check_password_hash
from helper import login_required

auth_service = AuthService()

# Configure application
app = Flask(__name__)
app.config.from_object('config')

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

Session(app)

@app.route("/")
@login_required
def index():
    """Show success page"""
    return render_template("index.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    if session.get('user_id'):
        session.pop('user_id')

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username and password was submitted
        form_data = request.form
        form = LoginForm(form_data)
        if not form.validate():
            flash('Invalid username or password.')
            return render_template("login.html")

        user = auth_service.login_user(form_data.get("username"), form_data.get("password"))

        if not user:
            flash('Email address or password mismatch!')
            return render_template("login.html")
        else:
            flash('You have successfully logged in!')
            # Redirect user to home page
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any session information
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route('/<path:my_path>')
def catch_all(my_path):
    """Catchall for other paths"""

    flash('Feature coming soon!')
    return redirect("/")

if __name__ == "__main__":
    if app.config.get('INIT_DATA'):
        add_mock_data(auth_service)
    app.run()
