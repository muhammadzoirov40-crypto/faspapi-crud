from pydantic import BaseModel


class StudentIn(BaseModel):
    name: str
    age: int

class StudentOut(BaseModel):
    id: int
    name: str
    age: int

    model_config = {"from_attributes": True}

class StudentPatch(BaseModel):
    name: str
    age: int
