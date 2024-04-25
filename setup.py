import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from PIL import Image, ImageTk
import random
import os
from gtts import gTTS
from playsound import playsound


class NutritionManager(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.height = ttk.DoubleVar(value=0)
        self.weight = ttk.DoubleVar(value=0)
        self.health_status = ttk.StringVar(value="")
        self.data = []
        self.colors = master_window.style.colors

        instruction_text = "Vui lòng nhập thông tin của bạn để quản lý dinh dưỡng: "
        instruction = ttk.Label(self, text=instruction_text, width=50)
        instruction.pack(fill=X, pady=10)

        self.create_form_entry("Chiều cao (cm): ", self.height)
        self.create_form_entry("Cân nặng (kg): ", self.weight)
        self.create_form_entry("Tình trạng sức khỏe: ", self.health_status)

        self.create_buttonbox()

        self.table = self.create_table()

    def create_form_entry(self, label, variable):
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)

        form_field_label = ttk.Label(master=form_field_container, text=label, width=15)
        form_field_label.pack(side=LEFT, padx=12)

        form_input = ttk.Entry(master=form_field_container, textvariable=variable)
        form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return form_input

    def create_buttonbox(self):
        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))

        submit_btn = ttk.Button(
            master=button_container,
            text="Gửi",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )

        submit_btn.pack(side=RIGHT, padx=5)

    def create_table(self):
        coldata = [{"text": "Bữa ăn"}, {"text": "Mô tả"}, {"text": "Hình ảnh"}]

        print(self.data)

        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(self.colors.light, None),
        )

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        return table

    def on_submit(self):
        """Tính toán và gợi ý bữa ăn dựa trên thông tin của người dùng."""
        height = self.height.get()
        weight = self.weight.get()
        health_status = self.health_status.get()

        # Tính toán bữa ăn gợi ý dựa trên chiều cao, cân nặng và tình trạng sức khỏe
        suggested_meals = calculate_meals(height, weight, health_status)

        # Cập nhật bảng với các bữa ăn gợi ý
        self.table.destroy()
        self.data = suggested_meals
        self.table = self.create_table()

        # Phát âm thông tin chiều cao và cân nặng
        info_text = f"Bạn đã nhập chiều cao là {height} centimet và cân nặng là {weight} kilogram."
        tts_info = gTTS(info_text, lang="vi")
        tts_info.save("voice_info.mp3")
        playsound("voice_info.mp3")
        os.remove("voice_info.mp3")

        # Phát âm gợi ý các bữa ăn
        demo = f"Khi bạn bị {health_status} bạn nên"
        tts_meal = gTTS(demo, lang="vi")
        tts_meal.save("voice_demo.mp3")
        playsound("voice_demo.mp3")
        os.remove("voice_demo.mp3")
        for meal in suggested_meals:
            meal_text = f" {meal[1]}"
            tts_meal = gTTS(meal_text, lang="vi")
            tts_meal.save("voice_meal.mp3")
            playsound("voice_meal.mp3")
            os.remove("voice_meal.mp3")


def calculate_meals(height, weight, health_status):
    suggested_meals = []
    meals_database = [
        {
            "name": "Bữa sáng",
            "description": "Lựa chọn những bữa ăn lành mạnh với các loại thực phẩm sau",
            "image": "breakfast_image.jpg",
        },
        
    ]
    random.shuffle(meals_database)
    for meal in meals_database[:3]:
        suggested_meals.append((meal["name"], meal["description"], meal["image"]))
    
    if "ốm" in health_status.lower() or "sick" in health_status.lower():
        sick_meals = [
            {
                "name": "Súp gà",
                "description": "Súp gà ấm lòng và bổ dưỡng",
                "image": "chicken_soup_image.jpg",
            },
            {
                "name": "Cháo",
                "description": "Cháo dễ tiêu hóa và dễ chịu",
                "image": "porridge_image.jpg",
            },
            {
                "name": "Nước ép trái cây",
                "description": "Nước ép trái cây sảng khoái và giàu dinh dưỡng",
                "image": "smoothie_image.jpg",
            },
            {
                "name": "Bánh mì mềm",
                "description": "Bánh mì mềm dễ tiêu hóa",
                "image": "soft_bread_image.jpg",
            },
            {
                "name": "Gạo trắng",
                "description": "Gạo trắng dễ tiêu hóa",
                "image": "white_rice_image.jpg",
            },
        ]
        suggested_meals.extend([(meal["name"], meal["description"], meal["image"]) for meal in sick_meals])
    
    if "đau dạ dày" in health_status.lower():
        stomach_pain_meals = [
            {
                "name": "Cháo lúa mạch",
                "description": "Cháo lúa mạch dễ tiêu hóa và lành mạnh cho dạ dày",
                "image": "oat_porridge_image.jpg",
            },
            {
                "name": "Nước lọc",
                "description": "Nước lọc giúp giảm căng thẳng cho dạ dày",
                "image": "water_image.jpg",
            },
            {
                "name": "Bánh mì mềm",
                "description": "Bánh mì mềm dễ tiêu hóa và không gây kích ứng dạ dày",
                "image": "soft_bread_image.jpg",
            },
        ]
        suggested_meals.extend([(meal["name"], meal["description"], meal["image"]) for meal in stomach_pain_meals])
    
    if "tiểu đường" in health_status.lower():
        diabetes_meals = [
            {
                "name": "Rau cải xanh",
                "description": "Rau cải xanh giúp kiểm soát đường huyết",
                "image": "green_vegetables_image.jpg",
            },
            {
                "name": "Cà chua",
                "description": "Cà chua giàu chất chống oxy hóa và giảm nguy cơ tiểu đường",
                "image": "tomatoes_image.jpg",
            },
            {
                "name": "Cơm gạo lứt",
                "description": "Cơm gạo lứt giàu chất xơ và giúp kiểm soát đường huyết",
                "image": "brown_rice_image.jpg",
            },
            {
                "name": "Sữa chua không đường",
                "description": "Sữa chua không đường là nguồn canxi tốt cho người tiểu đường",
                "image": "plain_yogurt_image.jpg",
            },
            {
                "name": "Hải sản",
                "description": "Hải sản giàu omega-3 giúp giảm nguy cơ mắc bệnh tim và tiểu đường",
                "image": "seafood_image.jpg",
            },
        ]
        suggested_meals.extend([(meal["name"], meal["description"], meal["image"]) for meal in diabetes_meals])
    
    if "mỡ máu cao" in health_status.lower():
        high_cholesterol_meals = [
            {
                "name": "Cải ngọt",
                "description": "Cải ngọt giúp giảm mỡ máu",
                "image": "sweet_potato_image.jpg",
            },
            {
                "name": "Quả lựu",
                "description": "Quả lựu giàu chất chống oxy hóa và giảm cholesterol",
                "image": "pomegranate_image.jpg",
            },
            {
                "name": "Bơ",
                "description": "Bơ giàu chất béo không bão hòa lành mạnh cho tim mạch",
                "image": "avocado_image.jpg",
            },
            {
                "name": "Cá hồi",
                "description": "Cá hồi giàu omega-3 giúp giảm mỡ máu",
                "image": "salmon_image.jpg",
            },
            {
                "name": "Lúa mạch",
                "description": "Lúa mạch giúp giảm mỡ máu và cholesterol",
                "image": "barley_image.jpg",
            },
        ]
        suggested_meals.extend([(meal["name"], meal["description"], meal["image"]) for meal in high_cholesterol_meals])
    
    return suggested_meals





def load_image(image_path, size=(100, 100)):
    image = Image.open("anh_co_the.jpg")
    image = image.resize(size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


if __name__ == "__main__":
    app = ttk.Window("Quản lý dinh dưỡng", "superhero", resizable=(False, False))
    nutrition_manager = NutritionManager(app)

    for i, (meal_name, description, image_path) in enumerate(nutrition_manager.data):
        image = load_image("anh_co_the.jpg")
        nutrition_manager.table.set_image(i, 2, image)
    app.mainloop()
