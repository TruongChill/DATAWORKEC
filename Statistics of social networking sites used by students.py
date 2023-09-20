

import matplotlib.pyplot as plt

# Dữ liệu mạng xã hội
Social_Networking_sites = ['Facebook', 'Instagram', 'Youtube', 'Tiktok', 'Zalo', 'Khác']
so_luong = [70, 23, 55, 45, 70, 11]
ty_le = [100, 32.86, 78.57, 64.29, 100, 15.71]


plt.pie(so_luong, labels=Social_Networking_sites, autopct='%1.1f%%')


plt.title('Statistics of social networking sites used by students ')


plt.show()