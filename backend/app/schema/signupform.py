from pydantic import BaseModel, EmailStr



class SignUpForm(BaseModel):
    user_name:str
    firstname:str
    lastname:str
    email:EmailStr
    password:str