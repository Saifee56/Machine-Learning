from pydantic import BaseModel

class MoscowHouse(BaseModel):
    Apartment_type:float
    Metro_station:float
    Minutes_to_metro:float
    Region: float
    Number_of_rooms: float
    Area: float
    Living_area:float
    Kitchen_area:float
    Floor:float
    Number_of_floors: float
    RenovationL:float