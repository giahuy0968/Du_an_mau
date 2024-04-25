import os
from gtts import gTTS
from playsound import playsound
test = " Khi bị ốm bạn nên dùng Nước lọc. Nước súp lơ. Thực phẩm dễ tiêu hóa như bánh mì mềm và gạo trắng. Trái cây tươi như chuối, lê, táo. Nước cốt chanh. Sữa chua hoặc yogurt"
lst = ["150cm 30kg ",
"150cm 31kg" + test,
"150cm 32kg" + test,
"150cm 33kg" + test,
"150cm 34kg" + test,
"150cm 35kg" + test,
"150cm 36kg" + test,
"150cm 37kg" + test,
"150cm 38kg" + test,
"150cm 39kg" + test,
"150cm 40kg" + test,
"150cm 41kg" + test,
"150cm 42kg" + test,
"150cm 43kg" + test,
"150cm 44kg" + test,
"150cm 45kg" + test,
"150cm 46kg" + test,
"150cm 47kg" + test,
"150cm 48kg" + test,
"150cm 49kg" + test,
"150cm 50kg" + test,
"150cm 51kg" + test,
"150cm 52kg" + test,
"150cm 53kg" + test,
"150cm 54kg" + test,
"150cm 55kg" + test,
"150cm 56kg" + test,
"150cm 57kg" + test,
"150cm 58kg" + test,
"150cm 59kg" + test,
"150cm 60kg" + test,
"150cm 61kg" + test,
"150cm 62kg" + test,
"150cm 63kg" + test,
"150cm 64kg" + test,
"150cm 65kg" + test,
"150cm 66kg" + test,
"150cm 67kg" + test,
"150cm 68kg" + test,
"150cm 69kg" + test,
"150cm 70kg" + test,
]
for i in lst:
    if ("150" and "60") in i:
        tts = gTTS(i, tld="com.vn", lang="vi")
        # Tạo file mp3 và lưu giọng nói vào file
        tts.save("voice.mp3")
        # Kích hoạt file để phát ra âm thanh
        playsound("voice.mp3")
        # Xoá file âm thanh để tránh lặp lại file và không mở được file
        os.remove("voice.mp3")