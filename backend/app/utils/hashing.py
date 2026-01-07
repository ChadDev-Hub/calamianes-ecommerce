from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password:str):
    '''This function return the recommended hash for user password

    :params password: the user plain password
    '''
    return password_hash.hash(password)

def verify_password(password:str, hashed_password:str):
    """
    This will compare and verify the plain password and the hashed password and return Boolean
    
    :param password: A plain password
    :type password: str
    :param hashed_password: Description
    :type hashed_password: hashed password
    """
    return password_hash.verify(
        password = password,
        hash = hashed_password
        )