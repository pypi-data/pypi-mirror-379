
import uuid

def uuid_for_nona(value):
    
    if isinstance(value, str):
        if value == ' ':
            return None
        else:
            return uuid.UUID(value)
    else:
        return None