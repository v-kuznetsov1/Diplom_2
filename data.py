
class TestDataCreateUser:

    RETURN_STATUS_CODE_200 = ['success', 'user', 'email', 
                              'name', 'accessToken', 'refreshToken']
    
    RETURN_EXISTING_USER = {
        "success": False,
        "message": "User already exists"
        }
    
    RETURN_WITHOUT_REQUIRED_FIELDS = {
        "success": False,
        "message": "Email, password and name are required fields"
        }
    

class TestDataLoginUser:

    RETURN_STATUS_CODE_200 = ['success', 'accessToken', 'refreshToken', 
                              'user', 'email', 'name']
    
    RETURN_STATUS_CODE_401 = {
        "success": False,
        "message": "email or password are incorrect"
        }
    


class TestDataChangeUser:
    
    CHANGE_USER_SUCCESS = ['success', 'user', 'email', 'name']
    
    RETURN_STATUS_CODE_401 = {
        "success": False,
        "message": "You should be authorised"
        }


class TestDataOrder:
    
    INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
        }
    
    INGREDIENTS_EMPTY_LIST = {"ingredients": []}

    STATUS_CODE_200 = ['success', 'name', 'order', 'number']

    RETURN_STATUS_CODE_400 = {
        "success": False,
        "message": "Ingredient ids must be provided"
        }
    
    RETURN_MESSAGE_INVALID_HASH = {
        "success": False,
        "message": "One or more ids provided are incorrect"
        }

    INGREDIENTS_INVALID_HASH = {
        "ingredients": ["61c0c5a71d1f82001bdaaa2d",
                        "61c0c5a71a1f82001bdaaa2d"]
                        }
    
    RETURN_USER_ORDERS = ["success", "orders", "_id", "ingredients", "status", 
                          "name", "createdAt", "updatedAt", "number",
                          "total", "totalToday"]
    
    RETURN_STATUS_CODE_401 = {
        "success": False,
        "message": "You should be authorised"
        }

