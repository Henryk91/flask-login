from werkzeug.security import generate_password_hash
import datetime

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = generate_password_hash(password)
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return "User(id='%s')" % self.id