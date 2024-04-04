import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation
import random
from PIL import Image, ImageTk

Hello 
class NutritionManager(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.height = ttk.DoubleVar(value=0)
        self.weight = ttk.DoubleVar(value=0)
        self.health_status = ttk.StringVar(value="")
        self.data = []
        self.colors = master_window.style.colors

        instruction_text = "Please enter your information for nutrition management: "
        instruction = ttk.Label(self, text=instruction_text, width=50)
        instruction.pack(fill=X, pady=10)

        self.create_form_entry("Height (cm): ", self.height)
        self.create_form_entry("Weight (kg): ", self.weight)
        self.create_form_entry("Health Status: ", self.health_status)

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
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )

        submit_btn.pack(side=RIGHT, padx=5)

    def create_table(self):
        coldata = [{"text": "Meal"}, {"text": "Description"}, {"text": "Image"}]

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
        """Calculate and suggest meals based on user information."""
        height = self.height.get()
        weight = self.weight.get()
        health_status = self.health_status.get()

        # Calculate suggested meals based on height, weight, and health status
        suggested_meals = calculate_meals(height, weight, health_status)

        # Update table with suggested meals
        self.table.destroy()
        self.data = suggested_meals
        self.table = self.create_table()


def calculate_meals(height, weight, health_status):
    # Dummy function to calculate suggested meals
    # You can replace this with your actual logic to suggest meals based on user information
    # This function should return a list of tuples containing meal information
    # For example: [("Breakfast", "Healthy breakfast option", "breakfast_image.jpg"), ...]
    suggested_meals = []
    # Mock database of meals
    meals_database = [
        {
            "name": "Breakfast",
            "description": "Healthy breakfast option",
            "image": "breakfast_image.jpg",
        },
        {
            "name": "Lunch",
            "description": "Healthy lunch option",
            "image": "lunch_image.jpg",
        },
        {
            "name": "Dinner",
            "description": "Healthy dinner option",
            "image": "dinner_image.jpg",
        },
    ]
    
    random.shuffle(meals_database)
    for meal in meals_database[:3]:  # Let's say we suggest 3 meals
        suggested_meals.append((meal["name"], meal["description"], meal["image"]))
    return suggested_meals


def load_image(image_path, size=(100, 100)):
    """Load and resize an image."""
    image = Image.open("anh_co_the.jpg")
    image = image.resize(size, Image.ANTIALIAS)  # Resize image to specified size
    photo = ImageTk.PhotoImage(image)
    return photo


if __name__ == "__main__":
    app = ttk.Window("Nutrition Manager", "superhero", resizable=(False, False))
    nutrition_manager = NutritionManager(app)

    # Load and display images in the table
    for i, (anh_chuc_nang, description, image_path) in enumerate(
        nutrition_manager.data
    ):
        image = load_image("anh_co_the.jpg")
        nutrition_manager.table.set_image(i, 2, image)
    app.mainloop()
