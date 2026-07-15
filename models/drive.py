from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Driver(Base):
    __tablename__ = 'driver'
    id = Column(Integer,primary_key=True)
    full_name = Column(String(20),nullable=False)
    status = Column(String(20),nullable=False)
    fleet_id = Column(Integer,ForeignKey('fleet.id'),nullable=False)
    fleet = relationship("Fleet",back_populates="drivers")
    bookings = relationship("Booking",back_populates="drive")
    cars = relationship("Car",secondary="booking",back_populates="drivers")