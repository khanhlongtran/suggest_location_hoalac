import numpy as np
from sklearn.neighbors import NearestNeighbors
from math import radians, cos, sin, sqrt, atan2


# Hàm tính khoảng cách Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Bán kính Trái Đất (km)
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# Hàm xây dựng đặc trưng cho mỗi nhà hàng (bạn có thể điều chỉnh nếu cần)
def build_feature_vector(restaurant, user_preferences):
    # Ví dụ, chúng ta chỉ sử dụng thông tin về menu và sở thích của người dùng để xây dựng đặc trưng
    # Bạn có thể thay đổi để thêm các đặc trưng khác (ví dụ: đánh giá, loại món ăn, v.v.)
    feature_vector = []

    # Thêm các đặc trưng của nhà hàng vào vector
    feature_vector.append(len(restaurant['menu']))  # Ví dụ: số món ăn trong menu

    # Bạn có thể thêm các đặc trưng khác ở đây, ví dụ: độ phổ biến, loại món ăn, v.v.
    return feature_vector


# Hàm gợi ý các món ăn dựa trên Ban đầu -> user preference -> suggest based on this
# Sau một thời gian -> dựa vào history -> chọn ra những món hay ăn nhất -> thay đổi preference (hoặc add vào preference của user) -> nhét vào mô hình AI để nó suggest lại

def knn_recommend_dishes(user_preferences, restaurants_data, user_location, k=3):
    # Đảm bảo k không vượt quá số lượng nhà hàng
    k = min(k, len(restaurants_data))

    # Xây dựng vector đặc trưng cho các nhà hàng (bỏ qua thông tin về khoảng cách lúc này)
    restaurant_vectors = np.array(
        [build_feature_vector(restaurant, user_preferences) for restaurant in restaurants_data])

    # Tính toán KNN để tìm các nhà hàng gần người dùng
    knn = NearestNeighbors(n_neighbors=k)
    knn.fit(restaurant_vectors)

    distances, indices = knn.kneighbors([restaurant_vectors[0]])  # Đề xuất cho người dùng đầu tiên

    recommendations = []
    for i in range(k):
        # Đề xuất nhà hàng và menu
        recommended_restaurant = restaurants_data[indices[0][i]]
        restaurant_name = recommended_restaurant['name']
        menu = recommended_restaurant['menu']

        # Sau khi gợi ý nhà hàng, tính khoảng cách đến các nhà hàng này
        lat_restaurant, lon_restaurant = recommended_restaurant['location']
        lat_user, lon_user = user_location
        distance = haversine(lat_user, lon_user, lat_restaurant, lon_restaurant)

        recommendations.append({
            "restaurant": restaurant_name,
            "menu": menu,
            "distance": distance
        })

    return recommendations


# Dữ liệu nhà hàng
restaurants_data = [
    {"name": "Hương Việt", "location": [20.991506481089903, 105.51888871475545], "menu": ["Cơm", "Bánh mì", "Phở"]},
    {"name": "Cua Đồng Không Tên", "location": [20.97927603774301, 105.52945802902266], "menu": ["Cua đồng", "Lẩu"]},
    {"name": "Nhà Hàng Nguyễn Gia", "location": [20.996172653542953, 105.52300204977304], "menu": ["Bún đậu", "Gà"]},
    {"name": "Nhà Hàng Thanh Vũ 79", "location": [20.9793974525488, 105.52955148498482], "menu": ["Cơm tấm", "Nước ép"]},
    {"name": "Hòa Lạc Viên", "location": [21.009476862347196, 105.51734967977018], "menu": ["Lẩu", "Bánh cuốn"]},
    {"name": "Quang Vinh Quán", "location": [20.98493269679086, 105.52776017091672], "menu": ["Gỏi cuốn", "Cơm chiên"]}
]

# Vị trí của người dùng
user_location = [20.999083161679504, 105.52817448652945]

# Gợi ý món ăn từ nhà hàng gần người dùng
user_preferences = {}  # Bạn có thể thay thế bằng thông tin sở thích người dùng
recommendations = knn_recommend_dishes(user_preferences, restaurants_data, user_location)

# In ra kết quả
for rec in recommendations:
    print(f"Restaurant: {rec['restaurant']}, Distance: {rec['distance']:.2f} km, Menu: {', '.join(rec['menu'])}")
