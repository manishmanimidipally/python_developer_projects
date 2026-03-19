import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

image_path = None

def upload_image():
    global image_path
    file = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if file:
        image_path = file
        label_status.config(text="Image Loaded ✔")

def add_watermark():
    global image_path

    if not image_path:
        messagebox.showerror("Error", "Please upload an image first!")
        return

    text = entry_text.get()
    if not text:
        messagebox.showerror("Error", "Enter watermark text!")
        return

    try:
        img = Image.open(image_path).convert("RGBA")

        watermark_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)

        width, height = img.size

        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
        position = (width - text_width - 20, height - text_height - 20)

        draw.text(position, text, fill=(255, 255, 255, 128), font=font)

        watermarked = Image.alpha_composite(img, watermark_layer)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png")]
        )

        if save_path:
            watermarked.convert("RGB").save(save_path)
            messagebox.showinfo("Success", "Watermark added and saved!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Image Watermarking App")
window.geometry("400x300")

title = tk.Label(window, text="Watermark App", font=("Arial", 18))
title.pack(pady=10)

btn_upload = tk.Button(window, text="Upload Image", command=upload_image)
btn_upload.pack(pady=10)

label_status = tk.Label(window, text="No image selected")
label_status.pack()

entry_text = tk.Entry(window, width=30)
entry_text.pack(pady=10)
entry_text.insert(0, "Enter watermark text")

btn_watermark = tk.Button(window, text="Add Watermark", command=add_watermark)
btn_watermark.pack(pady=20)

window.mainloop()