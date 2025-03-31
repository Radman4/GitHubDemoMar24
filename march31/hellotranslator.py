import tkinter as tk

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Translator")

        # Create a label to display the translated word
        self.translation_label = tk.Label(root, text="Translate 'Hello' here", font=("Arial", 16))
        self.translation_label.pack(pady=20)

        # Create buttons for each language
        self.create_buttons()

    def create_buttons(self):
        # English button
        self.button_english = tk.Button(self.root, text="English", command=self.translate_to_english)
        self.button_english.pack(side="left", padx=10)

        # Spanish button
        self.button_spanish = tk.Button(self.root, text="Espanol", command=self.translate_to_spanish)
        self.button_spanish.pack(side="left", padx=10)

        # French button
        self.button_french = tk.Button(self.root, text="Francois", command=self.translate_to_french)
        self.button_french.pack(side="left", padx=10)

        # German button
        self.button_german = tk.Button(self.root, text="Deutsch", command=self.translate_to_german)
        self.button_german.pack(side="left", padx=10)

    # Methods to translate "hello" to each language
    def translate_to_english(self):
        self.translation_label.config(text="Hello")

    def translate_to_spanish(self):
        self.translation_label.config(text="Hola")

    def translate_to_french(self):
        self.translation_label.config(text="Bonjour")

    def translate_to_german(self):
        self.translation_label.config(text="Hallo")

# Create the main Tkinter window
root = tk.Tk()

# Instantiate the TranslatorApp class
app = TranslatorApp(root)

# Run the Tkinter event loop
root.mainloop()
