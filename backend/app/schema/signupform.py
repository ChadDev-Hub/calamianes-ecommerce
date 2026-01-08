from pydantic import BaseModel, EmailStr



class SignUpForm(BaseModel):
    username:str
    firstname:str
    lastname:str
    email:EmailStr
    password:str