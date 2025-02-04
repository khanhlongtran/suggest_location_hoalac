import random

# Dữ liệu món ăn của các quán
restaurants = {
    "Huong Viet Restaurant": ["Phở gà", "Bánh cuốn", "Gà nướng mật ong", "Canh măng chua", "Chả giò", "Gà luộc"],
    "Cua Đồng Không Tên": ["Lẩu cua đồng", "Bánh đa cua", "Cua rang me", "Lẩu thập cẩm", "Canh cua đồng", "Gỏi cua"],
    "Nhà Hàng Nguyễn Gia": ["Cơm tấm sườn", "Gà chiên mắm", "Canh bí đỏ", "Bò lúc lắc", "Sườn nướng mật ong",
                            "Cà ri gà"],
    "Nhà Hàng Thanh Vũ 79": ["Lẩu cua đồng", "Gà ri nướng", "Bánh xèo", "Gà ri kho gừng", "Lẩu gà ri",
                             "Canh gà ri nấu măng"],
    "Hoa Lac Vien": ["Lẩu cua", "Lẩu bò", "Lẩu sữa", "Cơm xôi gà", "Cạnh khoai tây", "Sườn nướng"],
    "Quang Vinh Quán": ["Cơm gà", "Vịt quay", "Canh mướp", "Gà hấp lá chanh", "Bún riêu", "Cơm chiên"]
}

# Dữ liệu sở thích của người dùng
user_preferences = {
    "lẩu": True,
    "gà": True,
    "cơm": True
}


# Hàm lọc món ăn dựa trên sở thích
def recommend_dishes(preferences, restaurants):
    recommended_dishes = []

    for restaurant, dishes in restaurants.items():
        for dish in dishes:
            # Kiểm tra xem món ăn có phù hợp với sở thích người dùng không
            if "lẩu" in dish.lower() and preferences["lẩu"]:
                recommended_dishes.append((restaurant, dish))
            elif "gà" in dish.lower() and preferences["gà"]:
                recommended_dishes.append((restaurant, dish))
            elif "cơm" in dish.lower() and preferences["cơm"]:
                recommended_dishes.append((restaurant, dish))

    # Tránh trùng lặp món ăn, giữ món khác nhau
    unique_recommended = list(set(recommended_dishes))
    return unique_recommended


# Hàm gợi ý món ăn
def get_recommendations(user_preferences, restaurants):
    recommendations = recommend_dishes(user_preferences, restaurants)

    if recommendations:
        print("Món ăn gợi ý cho bạn:")
        for restaurant, dish in recommendations:
            print(f"Quán: {restaurant} - Món ăn: {dish}")
    else:
        print("Không có món ăn nào phù hợp với sở thích của bạn.")


# Gọi hàm để gợi ý món ăn
get_recommendations(user_preferences, restaurants)
