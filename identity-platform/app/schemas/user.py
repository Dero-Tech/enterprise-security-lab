from pydantic import BaseModel, Field, ConfigDict


class UserCreate(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    department: str
    role: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    department: str
    role: str

    model_config = ConfigDict(from_attributes=True)
