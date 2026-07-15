from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database import Base
class Car(Base):
    __tablename__ = "car"
    id = Column(Integer,primary_key=True)
    license_plate = Column(String(20),nullable=False)
    status = Column(String(20))
    bookings = relationship("Booking",back_populates="car")
    drivers = relationship("Driver",secondary="booking",back_populates="cars")   