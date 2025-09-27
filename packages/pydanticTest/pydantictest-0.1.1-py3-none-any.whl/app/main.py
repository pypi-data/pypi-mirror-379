'''Pydantic Example'''
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    '''User model with validation'''
    name: str
    email: EmailStr
    age: int

def main(name="John Doe", email="john.doe@example.com", age=30):
    '''Main function to create and display a User instance'''
    user = User(name=name, email=email, age=age)
    print(user.name)
    print(user.email)
    print(user.age)

if __name__ == "__main__":
    main("John Doe", "john.doe@example.com", 30)
