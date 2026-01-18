import tkinter as tk
from .text_model import SmartPiChat

def run_gui():
    ai = SmartPiChat()

    def send_message():
        text = user_input.get().strip()
        if not text:
            return
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + text + "\n")
        response = ai.respond(text)
        chat_box.insert(tk.END, "SmartPi: " + response + "\n\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.see(tk.END)
        user_input.delete(0, tk.END)

    root = tk.Tk()
    root.title("SmartPi Chat")
    root.geometry("600x500")

    chat_box = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
    chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    user_input = tk.Entry(root, font=("Arial", 14))
    user_input.pack(padx=10, pady=(0,10), fill=tk.X)
    user_input.bind("<Return>", lambda e: send_message())

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(pady=(0,10))

    root.mainloop()
