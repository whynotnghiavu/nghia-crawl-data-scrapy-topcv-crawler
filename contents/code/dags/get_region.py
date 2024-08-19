import os
import mysql.connector



north_cities = [
    "Hà Nội", "Bắc Giang", "Bắc Kạn", "Bắc Ninh", "Cao Bằng", "Điện Biên", "Hà Giang", "Hà Nam", "Hải Dương", 
    "Hải Phòng", "Hòa Bình", "Hưng Yên", "Lai Châu", "Lào Cai", "Lạng Sơn", "Nam Định", "Ninh Bình", "Phú Thọ", 
    "Quảng Ninh", "Sơn La", "Thái Bình", "Thái Nguyên", "Tuyên Quang", "Vĩnh Phúc", "Yên Bái"
]



central_cities = [
    "Đà Nẵng", "Bình Định", "Đắk Lắk", "Đắk Nông", "Gia Lai", "Hà Tĩnh", "Khánh Hòa", "Kon Tum", "Lâm Đồng", 
    "Nghệ An", "Ninh Thuận", "Phú Yên", "Quảng Bình", "Quảng Nam", "Quảng Ngãi", "Quảng Trị", "Thừa Thiên Huế", 
    "Thanh Hóa"
]




south_cities = [
    "Hồ Chí Minh", "An Giang", "Bà Rịa - Vũng Tàu", "Bạc Liêu", "Bến Tre", "Bình Dương", "Bình Phước", 
    "Bình Thuận", "Cà Mau", "Cần Thơ", "Đồng Nai", "Đồng Tháp", "Hậu Giang", "Kiên Giang", "Long An", 
    "Sóc Trăng", "Tây Ninh", "Tiền Giang", "Trà Vinh", "Vĩnh Long"
]






def determine_region(location):
    if any(city in location for city in north_cities):
        return 'Miền Bắc'
    elif any(city in location for city in central_cities):
        return 'Miền Trung'
    elif any(city in location for city in south_cities):
        return 'Miền Nam'
    else:
        return 'Khác'

def get_region():
    conn = mysql.connector.connect(
        host=os.getenv("CRAWLER_DATABASE_HOST"),
        user=os.getenv("CRAWLER_DATABASE_USERNAME"),
        password=os.getenv("CRAWLER_DATABASE_PASSWORD"),
        database=os.getenv("CRAWLER_DATABASE_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, location FROM jobs")
    rows = cursor.fetchall()

    for row in rows:
        job_id, location = row
        region = determine_region(location)
        
        cursor.execute("""
            UPDATE jobs
            SET region = %s
            WHERE id = %s
        """, (region, job_id))

    conn.commit()
    cursor.close()
    conn.close()

