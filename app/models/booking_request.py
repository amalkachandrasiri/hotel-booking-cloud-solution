from pydantic import BaseModel, Field
from typing import Literal

class BookingRequest(BaseModel):
    hotel: Literal[
        'Resort Hotel',
        'City Hotel'
    ]

    lead_time: int = Field(ge=0)

    arrival_date_year: int = Field(ge=2000)
    arrival_date_month: str
    arrival_date_week_number: int = Field(ge=1, le=53)
    arrival_date_day_of_month: int = Field(ge=1, le=31)

    stays_in_weekend_nights: int = Field(ge=0)
    stays_in_week_nights: int = Field(ge=0)

    adults: int = Field(ge=1)
    children: float = Field(ge=0)
    babies: int = Field(ge=0)

    meal: Literal[
        'BB',
        'FB',
        'HB',
        'SC',
        'Undefined'
    ]
    country: str
    market_segment: str
    distribution_channel: str

    is_repeated_guest: int = Field(ge=0, le=1)
    previous_cancellations: int = Field(ge=0)
    previous_bookings_not_canceled: int = Field(ge=0)

    reserved_room_type: str
    assigned_room_type: str

    booking_changes: int = Field(ge=0)
    deposit_type: Literal[
        'No Deposit',
        'Non Refund',
        'Refundable'
    ]
    agent: float = Field(ge=0)
    days_in_waiting_list: int = Field(ge=0)
    customer_type: str

    adr: float = Field(ge=0)

    required_car_parking_spaces: int = Field(ge=0)
    total_of_special_requests: int = Field(ge=0)