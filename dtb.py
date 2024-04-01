import sqlite3


def convert_image_to_binary(image_path):
    with open(image_path, "rb") as file:
        binary_data = file.read()
    return binary_data


def insert_image_into_database(image_path, conn):
    binary_data = convert_image_to_binary(image_path)
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


def save_binary_to_file(binary_data, file_path):
    with open(file_path, "wb") as file:
        file.write(binary_data)


# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect("image_database.db")

# Tạo bảng dữ liệu
conn.execute(
    """CREATE TABLE IF NOT EXISTS images
                (id INTEGER PRIMARY KEY,
                image_data BLOB)"""
)

# Chèn hình ảnh vào cơ sở dữ liệu
image_path = "anh_co_the.jpg"
insert_image_into_database(image_path, conn)

# Truy xuất hình ảnh từ cơ sở dữ liệu
image_id = 1
binary_image_data = retrieve_image_from_database(image_id, conn)

# Lưu trữ hình ảnh đã truy xuất vào một tệp
if binary_image_data:
    save_binary_to_file(binary_image_data, "retrieved_image.jpg")

# Đóng kết nối cơ sở dữ liệu
conn.close()
