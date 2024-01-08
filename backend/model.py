from pydantic import BaseModel
# Serializes and Validates
class Todo(BaseModel):# Inherits The BaseModel class
    title: str
    description: str
    # Managemet library of files which specifies name and description.
