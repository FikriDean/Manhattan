# Perpusnas - Museum Nasional

# def manhattan_distance(x0, y0, x1, y1):
#     # Menghitung jarak Manhattan
#     distance = abs(x0 - x1) + abs(y0 - y1)

#     # Mengkonversi jarak ke dalam satuan kilometer
#     distance_km = distance * 111.12

#     return distance_km


# # Koordinat Perpusnas
# x1, y1 = -6.180655, 106.826927

# # Koordinat Museum Nasional Indonesia
# x0, y0 = -6.176450, 106.822383


# Bundaran HI - Perpusnas

# distance = manhattan_distance(x0, y0, x1, y1)

# print("Jarak Manhattan antara Museum Nasional Indonesia dan Perpustakaan Nasional adalah", distance, "km")


# def manhattan_distance(x0, y0, x1, y1):
#     # Menghitung jarak Manhattan
#     distance = abs(x0 - x1) + abs(y0 - y1)

#     # Mengkonversi jarak ke dalam satuan kilometer
#     distance_km = distance * 111.12

#     return distance_km


# # Koordinat Bundaran HI
# x0, y0 = -6.195453, 106.823041

# # Koordinat Perpusnas
# x1, y1 = -6.180655, 106.826927

# distance = manhattan_distance(x0, y0, x1, y1)

# print("Jarak Manhattan antara Bundaran HI dan Perpustakaan Nasional adalah", distance, "km")


# Monas - Bundaran HI

# def manhattan_distance(x0, y0, x1, y1):
#     # Menghitung jarak Manhattan
#     distance = abs(x0 - x1) + abs(y0 - y1)

#     # Mengkonversi jarak ke dalam satuan kilometer
#     distance_km = distance * 111.12

#     return distance_km


# # Koordinat Monas
# x0, y0 = -6.175362, 106.827188

# # Koordinat Bundaran HI
# x1, y1 = -6.195453, 106.823041

# distance = manhattan_distance(x0, y0, x1, y1)

# print("Jarak Manhattan antara Monas dan Bundaran HI adalah", distance, "km")


# Perpusnas - PT. Citra Inspekindo Mandiri

def manhattan_distance(x0, y0, x1, y1):
    # Menghitung jarak Manhattan
    distance = abs(x0 - x1) + abs(y0 - y1)

    # Mengkonversi jarak ke dalam satuan kilometer
    distance_km = distance * 111.12

    return distance_km


# Koordinat Perpusnas
x0, y0 = -6.180655, 106.826927

# Koordinat PT. Citra Inspekindo Mandiri
x1, y1 = -6.170222, 106.818410

distance = manhattan_distance(x0, y0, x1, y1)

print("Jarak Manhattan antara Perpustakaan Nasional Republik Indonesia dan PT. Citra Inspekindo Mandiri adalah", distance, "km")
