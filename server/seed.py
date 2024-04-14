from config import db, app
from models import Todo


# Function to seed the database with initial data
with app.app_context():
    print("Deleting all records...")
    db.drop_all()
    db.create_all()
    
    print("Creating todo tasks...")
    todo1 = Todo(text="Finish homework", complete=False)
    todo2 = Todo(text="Go to the gym", complete=False)
    todo3 = Todo(text="Buy groceries", complete=True)
    
    db.session.add(todo1)
    db.session.add(todo2)
    db.session.add(todo3)

    # Commit the changes
    db.session.commit()

# Run the seed function if this script is executed
# if __name__ == "__main__":
#     seed_database()