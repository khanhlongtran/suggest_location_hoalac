import numpy as np
from sklearn.cluster import KMeans
from math import radians, cos, sin, sqrt, atan2

# Hàm tính khoảng cách Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Bán kính Trái Đất (km)
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

# Dữ liệu nhà hàng
restaurants = np.array([
    [20.991506481089903, 105.51888871475545],  # Hương Việt
    [20.97927603774301, 105.52945802902266],   # Cua Đồng Không Tên
    [20.996172653542953, 105.52300204977304],  # Nhà Hàng Nguyễn Gia
    [20.9793974525488, 105.52955148498482],    # Nhà Hàng Thanh Vũ 79
    [21.009476862347196, 105.51734967977018],  # Hòa Lạc Viên
    [20.98493269679086, 105.52776017091672]    # Quang Vinh Quán
])

# Vị trí hiện tại của bạn

user_location = np.array([[21.006804312994568, 105.53073269698498]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(restaurants)
# Dự đoán cụm của người dùng
user_cluster = kmeans.predict(user_location)[0]
# Liệt kê các nhà hàng trong cụm của người dùng
nearest_restaurants = []
for idx, label in enumerate(kmeans.labels_):
    if label == user_cluster:
        distance = haversine(user_location[0][0], user_location[0][1], restaurants[idx][0], restaurants[idx][1])
        nearest_restaurants.append((idx, distance))
# Sắp xếp nhà hàng theo khoảng cách tăng dần
nearest_restaurants = sorted(nearest_restaurants, key=lambda x: x[1])

# Tên nhà hàng để hiển thị
restaurant_names = [
    "Hương Việt",
    "Cua Đồng Không Tên",
    "Nhà Hàng Nguyễn Gia",
    "Nhà Hàng Thanh Vũ 79",
    "Hòa Lạc Viên",
    "Quang Vinh Quán"
]
# In ra nhà hàng gần nhất
print("Suggest nhà hàng gần bạn nhất trong cụm:")
for idx, dist in nearest_restaurants:
    print(f"{restaurant_names[idx]} - {dist:.2f} km")
