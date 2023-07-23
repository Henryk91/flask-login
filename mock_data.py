from models import User


def add_mock_data(auth_service):
    # Add data for display and test purposes
    users = [
        User(1, 'test1@test.com', 'first-pass'),
        User(2, 'test2@test.com', 'another-pass'),
    ]
    auth_service.add_users(users)