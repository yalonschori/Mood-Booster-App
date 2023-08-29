# UI and Controller
import os
import customtkinter as ctk
from ui_elements import Custom_button
from api_requests import Api_requests
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.environ.get("API_KEY")
dog_url = "https://api.thedogapi.com/v1/images/search"
cat_url = "https://api.thecatapi.com/v1/images/search"
headers = {"x-api-key": API_KEY}
query_params = {"has_breeds": 1}


current_request = []


def test_command():
    print("works")


def call_api(animal: str):
    global current_request
    welcome_label.pack_forget()
    if animal.lower() == "dog":
        current_request = []
        current_request = dog_api_request.call_api()
    elif animal.lower() == "cat":
        current_request = []
        current_request = cat_api_request.call_api()


def get_pet_info_command():
    global current_request
    if current_request:
        try:
            msg = f"Breed:   {current_request[0]['name']}\n Life Span:   {current_request[0]['life_span']}\n Weight:   {current_request[0]['weight']['metric']}kg \n Height:   {current_request[0]['height']['metric']}cm \n Bred for:   {current_request[0]['bred_for']}"
            CTkMessagebox(master=root, message=msg, title="Info!")
        except KeyError:
            try:
                msg = f"Breed:   {current_request[0]['name']}\n Life Span:   {current_request[0]['life_span']}\n Weight:   {current_request[0]['weight']['metric']}kg \n Height:   {current_request[0]['height']['metric']}cm \n Bred for:   {current_request[0]['breed_group']}"
            except KeyError:
                CTkMessagebox(master=root, message="No Breed Info :(", title="Info!")
    else:
        CTkMessagebox(
            master=root,
            message="Please Generate an Image",
            title="Info!",
            icon="warning",
        )


root = ctk.CTk()
root.geometry("400x500")
root.title("Mood Booster App")
root.resizable(False, False)
ctk.set_appearance_mode("light")

image_frame = ctk.CTkFrame(
    root,
    width=300,
    height=300,
    border_color="grey",
    border_width=2,
)
image_frame.pack_propagate(False)


welcome_label = ctk.CTkLabel(
    image_frame, text="Click On A\n Generate Button\n To Start!"
)

image_label = ctk.CTkLabel(image_frame, text="")


dog_api_request = Api_requests(
    api_key=API_KEY,
    headers=headers,
    url=dog_url,
    widget=image_label,
    params=query_params,
)

cat_api_request = Api_requests(
    api_key=API_KEY,
    headers=headers,
    url=cat_url,
    widget=image_label,
    params=query_params,
)


call_dog_api_button = Custom_button(
    placement=root,
    text="Generate Dog!",
    command=lambda: call_api("dog"),
    color="#272829",
    hover_color="#61677A",
    tooltip_text="Generate A Random Dog Image",
)

call_cat_api_button = Custom_button(
    placement=root,
    text="Generate Cat!",
    command=lambda: call_api("cat"),
    color="#F8F5F1",
    hover_color="#DDDDDD",
    tooltip_text="Generate A Random Cat Image",
    text_color="black",
)


get_info_button = Custom_button(
    placement=root,
    text="Get Info",
    command=get_pet_info_command,
)

image_frame.pack(pady=30)
welcome_label.pack(pady=130, padx=50)
image_label.pack(pady=10, padx=10)
get_info_button.place_button(y=350, x=125)
call_dog_api_button.place_button(x=50, y=400)
call_cat_api_button.place_button(x=200, y=400)
root.mainloop()
