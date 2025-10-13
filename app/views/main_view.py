import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.pack(padx=100, pady=100)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text=" C'est chiant les MCV AAAAAAAAAAAAAAAAAAAHHHHH !!!!")
        self.label.pack()

        self.button = tk.Button(self, text="Afficher message", command=self.controller.on_button_click)
        self.button.pack(pady=10)

    def show_message(self, message):
        self.label.config(text=message)
