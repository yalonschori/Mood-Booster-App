import customtkinter as ctk
from CTkToolTip import *


class Custom_button:
    def __init__(
        self,
        placement,
        text,
        command,
        color="#5A96E3",
        hover_color="#0A6EBD",
        tooltip_text="",
        text_color="white",
    ):
        self.placement = placement
        self.text = text
        self.command = command
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.tooltip_opactity = 0 if tooltip_text == "" else 1
        self.tooltip_text = tooltip_text
        self.button = ctk.CTkButton(
            self.placement,
            text=self.text,
            command=self.command,
            fg_color=self.color,
            hover_color=self.hover_color,
            text_color=self.text_color,
        )
        self.tooltip = CTkToolTip(
            self.button, message=self.tooltip_text, alpha=self.tooltip_opactity
        )

    def pack_button(self):
        self.button.pack()

    def place_button(self, x, y):
        self.button.place(x=x, y=y)
