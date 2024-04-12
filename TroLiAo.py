import pyttsx3
import speech_recognition
import os
from gtts import gTTS
from playsound import playsound
from datetime import date, datetime
import time;

t = time.localtime()
t = time.strftime("%H:%M:%S", t)
robot_brain = ""
#Tạo 1 AI có thể nghe được
robot_ear = speech_recognition.Recognizer()
while True:
    #Tạo 1 micro để nói âm thanh
    with speech_recognition.Microphone() as mic:
        print ("AI: Listening")
        #Ghi lại âm thanh đã nói vào micro
        audio = robot_ear.record(mic, duration=5)
        print ("AI: ...")
    try:
        #Đưa âm thanh đã ghi lại lên google để chuyển sang dạng text
        you = robot_ear.recognize_google(audio, language = "vi")
        #Đổi text thành chữ thường
        you = you.lower()
        print ("Người sử dụng: " + you)
    except:
        you = ""
        robot_brain ="Tôi không hiểu bạn nói gì cả"
        print ("AI: " + robot_brain)
        
    #So sánh nếu câu hỏi có trong text người nói sẽ thực hiện câu lệnh
    if "xin chào" in you:
        robot_brain = "xin chào bạn khoẻ không"
        print ("AI: " + robot_brain)
    elif "bạn gái" in you:
        robot_brain = "Bạn làm gì có bạn gái đâu mà hỏi"
        print ("AI: " + robot_brain)
    elif ("tôi" and "khỏe") in you:
        robot_brain = "như vậy tốt rồi nhớ giữ gìn sức khỏe nha"
        print ("AI: " + robot_brain)
    elif "khỏe" in you:
        robot_brain = "Tôi khỏe, còn bạn"
        print ("AI: " + robot_brain)
    elif "mấy giờ" in you:
        robot_brain = "Bây giờ là " + t
        print ("AI: " + robot_brain)
    elif "tạm biệt" in you:
        robot_brain = "tạm biệt hẹn gặp lại"
        print ("AI: " + robot_brain)
        tts = gTTS(robot_brain, tld ='com.vn', lang ='vi')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
        break
    else:
        robot_brain = "Tôi là AI được lập trình sẵn nên tôi không có câu trả lời cho câu hỏi hiện tại của bạn"
        print ("AI: " + robot_brain)
    #Text sẽ chuyển lên google để chuyển thành giọng nói
    tts = gTTS(robot_brain, tld ='com.vn', lang ='vi')
    #Tạo file mp3 và lưu giọng nói vào file
    tts.save("voice.mp3")
    #Kích hoạt file để phát ra âm thanh
    playsound("voice.mp3")
    #Xoá file âm thanh để tránh lặp lại file và không mở được file
    os.remove("voice.mp3")
    n = input("Bạn có tiếp tục hỏi AI không Y/N: ")
    if n == "N":
        robot_brain = "tạm biệt hẹn gặp lại"
        #Text sẽ chuyển lên google để chuyển thành giọng nói
        tts = gTTS(robot_brain, tld ='com.vn', lang ='vi')
        #Tạo file mp3 và lưu giọng nói vào file
        tts.save("voice.mp3")
        #Kích hoạt file để phát ra âm thanh
        playsound("voice.mp3")
        #Xoá file âm thanh để tránh lặp lại file và không mở được file
        os.remove("voice.mp3")
        break
        

