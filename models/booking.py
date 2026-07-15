from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer,primary_key=True)
    driver_id = Column(Integer,ForeignKey('driver.id'),nullable=False)
    car_id = Column(Integer,ForeignKey('car.id'),nullable=False)
    drive = relationship("Driver",back_populates="bookings")
    car = relationship("Car",back_populates="bookings")
    