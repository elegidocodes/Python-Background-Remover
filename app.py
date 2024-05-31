import os
from tkinter import Tk, filedialog, Button, Label
from rembg import remove
from PIL import Image


def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_label.config(text=folder_selected)
    return folder_selected


def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_label.config(text=folder_selected)
    return folder_selected


def process_images():
    input_folder = input_folder_label.cget("text")
    output_folder = output_folder_label.cget("text")

    if not input_folder or not output_folder:
        status_label.config(text="Please select both input and output folders.")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.jpg', '.png'))

            try:
                my_input = Image.open(input_path)
                my_output = remove(my_input)
                my_output.save(output_path)
                print(f"Processed {input_path} -> {output_path}")
            except Exception as e:
                print(f"Failed to process {input_path}: {e}")

    status_label.config(text="Image processing complete.")


# Set up the UI
root = Tk()
root.title("Background Remover")

# Set window size
window_width = 400
window_height = 250

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

input_folder_label = Label(root, text="No folder selected")
input_folder_label.pack(pady=10)
input_folder_button = Button(root, text="Select Input Folder", command=select_input_folder)
input_folder_button.pack(pady=5)

output_folder_label = Label(root, text="No folder selected")
output_folder_label.pack(pady=10)
output_folder_button = Button(root, text="Select Output Folder", command=select_output_folder)
output_folder_button.pack(pady=5)

process_button = Button(root, text="Process Images", command=process_images)
process_button.pack(pady=10)

status_label = Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
