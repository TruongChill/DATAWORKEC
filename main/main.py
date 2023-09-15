

import matplotlib.pyplot as plt

# Dữ liệu mạng xã hội
mang_xa_hoi = ['Facebook', 'Instagram', 'Youtube', 'Tiktok', 'Zalo', 'Khác']
so_luong = [70, 23, 55, 45, 70, 11]
ty_le = [100, 32.86, 78.57, 64.29, 100, 15.71]

# Tạo biểu đồ tròn
plt.pie(so_luong, labels=mang_xa_hoi, autopct='%1.1f%%')

# Đặt tiêu đề cho biểu đồ
plt.title('Thống kê các trang mạng xã hội được sử dụng')

# Hiển thị biểu đồ
plt.show()