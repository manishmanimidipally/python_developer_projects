import tkinter as tk
import time
import random

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python programming is fun and powerful",
    "Typing speed improves with regular practice",
    "Artificial intelligence is the future of technology",
    "Practice daily to increase your typing accuracy"
]

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.text_to_type = random.choice(sentences)
        self.start_time = None

        # Title
        self.label_title = tk.Label(root, text="Typing Speed Test", font=("Arial", 18))
        self.label_title.pack(pady=10)

        # Sentence display
        self.label_text = tk.Label(root, text=self.text_to_type, wraplength=500, font=("Arial", 12))
        self.label_text.pack(pady=10)

        # Input box
        self.entry = tk.Text(root, height=5, width=60)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        # Button
        self.btn_submit = tk.Button(root, text="Submit", command=self.calculate_results)
        self.btn_submit.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_results(self):
        end_time = time.time()

        if self.start_time is None:
            return

        time_taken = end_time - self.start_time
        user_input = self.entry.get("1.0", tk.END).strip()

        # WPM calculation
        word_count = len(self.text_to_type) / 5
        wpm = (word_count / time_taken) * 60

        # Accuracy calculation
        correct_chars = sum(1 for i in range(min(len(user_input), len(self.text_to_type)))
                            if user_input[i] == self.text_to_type[i])
        accuracy = (correct_chars / len(self.text_to_type)) * 100

        # Display result
        self.result_label.config(
            text=f"Time: {time_taken:.2f}s | WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%"
        )

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
