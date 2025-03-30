from app import db  # Import SQLAlchemy object from your Flask app
from app import User  # Import the User model

class DBHelper:
    def register(self, username, password, email):
        try:
            # Create a new user
            new_user = User(username=username, email=email, age=password)  # You can replace 'age' with the password field in your User model
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Error registering user: {e}")
            return False

    def login(self, username, password):
        try:
            # Query the database for a user with matching username and password
            user = User.query.filter_by(username=username).first()
            if user and user.age == password:  # Replace 'age' with your password field
                return True
            return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def update_user(self, username, field, value):
        try:
            # Find the user
            user = User.query.filter_by(username=username).first()
            if user:
                setattr(user, field, value)  # Dynamically set the field
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def delete_user(self, username):
        try:
            # Find and delete the user
            user = User.query.filter_by(username=username).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def view_all_users(self):
        try:
            # Query all users
            return User.query.all()
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []