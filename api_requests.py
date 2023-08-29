import requests
from PIL import Image
from io import BytesIO
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Api_requests:
    def __init__(self, widget, api_key, url, headers, params):
        self.widget = widget
        self.api_key = api_key
        self.url = url
        self.headers = headers
        self.params = params
        self.breed_info = []

    def call_api(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code == 200:
            data = response.json()
            image_response = requests.get(data[0]["url"])
            try:
                self.breed_info = data[0]["breeds"]
            except KeyError:
                self.breed_info = []
            image_data = BytesIO(image_response.content)
            img = ctk.CTkImage(
                light_image=Image.open(image_data),
                size=(290, 290),
            )
            self.widget.configure(text="", image=img)
            self.widget.image = img
            return self.breed_info
        else:
            CTkMessagebox(message=f"error {response.status_code}", title="Error")
