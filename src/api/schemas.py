from pydantic import BaseModel

class CarInput(BaseModel):
    Brand: str
    Model: str
    Year: int
    Mileage: float
    Fuel_Type: str
    Transmission: str
    Condition: str
