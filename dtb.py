import sqlite3


def convert_image_to_binary(file_path):
    with open(file_path, "rb") as file:
        binary_data = file.read()
    return binary_data


def insert_image_into_database(file_path, conn):
    binary_data = convert_image_to_binary(file_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (image_data) VALUES (?)", (binary_data,))
    conn.commit()


def retrieve_image_from_database(image_id, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT image_data FROM images WHERE id=?", (image_id,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return None


def luu_anh_nhi_phan_vao_tep(binary_data, file_path):
    with open(file_path, "wb") as file:
        file.write(binary_data)


# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect("image_database.db")

# Tạo bảng dữ liệu nếu chưa tồn tại
conn.execute(
    """CREATE TABLE IF NOT EXISTS images
                (id INTEGER PRIMARY KEY,
                image_data BLOB)"""
)

# Chèn hình ảnh vào cơ sở dữ liệu
duong_dan_anh = r"D:\Du_an_mau\anh_co_the.jpg"
insert_image_into_database(duong_dan_anh, conn)

# Truy xuất hình ảnh từ cơ sở dữ liệu
id_anh = 1
binary_image_data = retrieve_image_from_database(id_anh, conn)

# Lưu trữ hình ảnh đã truy xuất vào một tệp
if binary_image_data:
    luu_anh_nhi_phan_vao_tep(binary_image_data, "anh_truy_xuat.jpg")

# Đóng kết nối cơ sở dữ liệu
conn.close()
