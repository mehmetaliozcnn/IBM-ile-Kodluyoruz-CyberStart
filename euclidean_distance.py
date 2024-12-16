# Öklid mesafesi hesaplayan bir fonksiyon tanımlıyoruz
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Noktaları tanımlıyoruz
points = [
    (1, 2),
    (4, 6),
    (5, 1),
    (0, 0),
    (2, 3)
]

# Mesafeleri hesaplamak için bir liste oluşturuyoruz
distances = []

# Tüm nokta çiftleri arasındaki mesafeyi hesaplıyoruz
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktayı iki kez karşılaştırmamak için j, i+1'den başlar
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"Mesafe {points[i]} ve {points[j]} arasında: {distance:.2f}")

# Minimum mesafeyi buluyoruz
min_distance = min(distances)
print(f"\nEn küçük mesafe: {min_distance:.2f}")
