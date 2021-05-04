from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)
from database_connection import get_database_connection

class IncorrectUserError(Exception):
    pass

class ExistingUsernameError(Exception):
    pass

class UsernameTooShortError(Exception):
    pass

class PasswordTooShortError(Exception):
    pass

class RecycleService:
    '''this class is responsible for the app's functions'''
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        '''logging in a user by finding the user from the database with their username
        and checking if the password given matches the password found in the database'''
        user = self._user_repository.find_user(username)
        if not user or user.password != password:
            raise IncorrectUserError('Username or password incorrect')
        self._user = user
        return user

    def register(self, username, password):
        '''creating a user with the given username and password'''
        duplicate_user = self._user_repository.find_user(username)
        if duplicate_user:
            raise ExistingUsernameError(f'There already exists a user with the username: {username}')
        if len(username) < 3:
            raise UsernameTooShortError('Username has to be at least three characters long')
        if len(password) <4:
            raise PasswordTooShortError('Password has to be at least four characters long')
        user = self._user_repository.create_user(User(username, password))
        return user

    def recycle_list(self):
        '''getting the amount of items recycled from the database matching with the current user'''
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        get_recycle = connection.execute(
            'select bottles_cans, cardboard, electronics, glass, metal, plastic, paper, batteries, clothes from recycle where username_id = ?', (username_id,)).fetchone()
        return get_recycle

    def recycle_list_update(self, amount, what_to_update):
        '''update amount of material recycled'''
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set {} = ({}+?) where username_id = ?'.format(what_to_update, what_to_update),
            (amount, username_id,))
        connection.commit()


recycle_service = RecycleService()
