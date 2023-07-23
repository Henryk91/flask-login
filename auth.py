from models import User
from flask import session
from werkzeug.security import check_password_hash

class AuthService(object):
    """
    Mock user auth service
    """
    def __init__(self):
        self.users = []
        self.username_table= {u.username: u for u in self.users}

    def _get_user_with_username(self,username):
        return self.username_table.get(username, None)
    
    def login_user(self, username, password):
        user = self._get_user_with_username(username)
        if user and check_password_hash(user.password, password):
            # Remember which user has logged in
            session["user_id"] = user.id
            return user
        
    def add_users(self, users):
        if len(users) > 0:
            for user in users:
                self.users.append(user)
            self.username_table= {u.username: u for u in self.users}

