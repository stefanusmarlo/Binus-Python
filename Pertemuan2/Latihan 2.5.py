import math

def calculate_haversine_distance(lat1, lon1, lat2, lon2):
    """
    Menghitung jarak Haversine antara dua titik di permukaan bumi.
    
    Args:
        lat1 (float): Lintang titik pertama (dalam derajat).
        lon1 (float): Bujur titik pertama (dalam derajat).
        lat2 (float): Lintang titik kedua (dalam derajat).
        lon2 (float): Bujur titik kedua (dalam derajat).
    
    Returns:
        float: Jarak dalam kilometer.
    """
    
    R = 1234.0
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
      
    distance = R * c 
    
    return distance
    
    jarak = calculate_haversine_distance(titik1_lat, titik1_lon, titik2_lat, titik2_lon)
    
    print("Jarak antara dua titik adalah: {jarak:.2f} km")
