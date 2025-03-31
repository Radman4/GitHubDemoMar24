import tkinter as tk

class FeedbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Feedback")

        # Create a label for the feedback entry
        self.label = tk.Label(root, text="Please provide your feedback:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Create a text box for entering feedback
        self.feedback_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.feedback_entry.pack(pady=10)

        # Create the submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_feedback, font=("Arial", 12))
        self.submit_button.pack(pady=10)

    def submit_feedback(self):
        # Get the feedback entered by the user
        feedback = self.feedback_entry.get()

        # Print the feedback to the console
        print(f"Customer Feedback: {feedback}")

        # Clear the text entry field
        self.feedback_entry.delete(0, tk.END)


# Create the main Tkinter window
root = tk.Tk()

# Instantiate the FeedbackApp class
app = FeedbackApp(root)

# Run the Tkinter event loop
root.mainloop()
