"""
Phần 1: Xác định Quan hệ & Vị trí khóa ngoại
1. Điền loại quan hệ 
Cặp đối tượng liên kết      Loại quan hệ (1-1 / 1-N / N-N)
Fleet – Driver              1-N
Driver – Car                N-N
2. Trả lời câu hỏi thiết kế
Khóa ngoại liên kết thực thể Driver với Fleet đặt ở bảng nào? Tại sao?
Khóa ngoại fleet_id phải đặt ở bảng Driver.
Tại sao: Vì đây là quan hệ 1-N (một đội xe có nhiều tài xế, nhưng một tài xế chỉ thuộc một đội xe). Trong cơ sở dữ liệu quan hệ, để biểu diễn quan hệ 1-N, ta phải đặt khóa ngoại tại bảng ở phía "Nhiều" (bảng con) để tham chiếu đến khóa chính của bảng ở phía "Một" (bảng cha).
Quan hệ Nhiều - Nhiều giữa Driver và Car được cấu hình qua bảng trung gian nào?
Quan hệ được cấu hình thông qua bảng trung gian Booking.
"""
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database import Base
class Fleet(Base):
    __tablename__ = "fleet"
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    drives = relationship("Driver",back_populates="fleet")