#Bài toán: Cần tạo ra các loại Robot khác nhau (Robot Xây dựng, Robot Chiến đấu). 
# Các Robot này cần động cơ để chạy (Composition)
# Cần bảo mật thông tin pin (Encapsulation) 
# Có các thao tác khởi động phức tạp được ẩn đi (Abstraction)
# Mỗi loại Robot có cách làm việc riêng biệt (Polymorphism).

from abc import ABC, abstractmethod
# Hàm Setter để sạc pin (có kiểm soát logic)
def charge_battery(self, amount):
    if amount > 0:
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"Đã sạc. Pin hiện tại: {self.__battery_level}%")
    else:
        print("Lỗi: Không thể sạc số âm!")

# Abstraction: Giấu các bước phức tạp này đi (dùng dấu _ ở đầu để báo hiệu hàm nội bộ)
def _check_systems(self):
    return "Kiểm tra cảm biến... OK. Kiểm tra rơ-le... OK."

# Người dùng chỉ cần gọi hàm start_robot() đơn giản này
def start_robot(self):
    print(f"\n--- Đang khởi động {self.name} ---")
    print(self._check_systems())
    print(self.engine.start())
    print(f"{self.name} đã sẵn sàng hoạt động!")

# Polymorphism: Ép các class con phải tự định nghĩa hàm này
@abstractmethod
def perform_task(self):
    pass