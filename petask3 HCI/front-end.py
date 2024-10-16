from tkinter import *
from PIL import Image
import customtkinter
import os  # Import os module to check if files exist
import tkinter

# Create the main window
window = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
window.title("Metflix")
window.geometry('800x400')

# Define the image directory
image_directory = r"C:\Users\micae.DESKTOP-KTO2U6D\OneDrive\Desktop\HCI\petask3 HCI"

# Set window icon
icon_path = os.path.join(image_directory, 'logo.png')
if os.path.exists(icon_path):
    icon = PhotoImage(file=icon_path)
    window.iconphoto(True, icon)
else:
    print(f"Error: {icon_path} not found. Skipping setting the window icon.")

# Function to handle button clicks
def clicker(option):
    print(f"{option} clicked")

    # Clear any existing content in the content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create a canvas and a scrollbar in the content_frame
    canvas = Canvas(content_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = customtkinter.CTkScrollbar(content_frame, orientation=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the buttons
    frame_inside_canvas = Frame(canvas)
    canvas.create_window((0, 0), window=frame_inside_canvas, anchor="nw")

    #popup window when an image is clicked
    def open_popup(image_name):
        popup = Toplevel(window)
        popup.title(f"{image_name} - Details")
        popup.geometry('800x400')
        label = Label(popup, text=f"You clicked on {image_name}!", font=("Arial", 15))
        label.pack(pady=20)
        close_button = Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

    # For the Homepage
    if option == "Homepage":
        # Load the images for the buttons
        button_images = ['Zero.jpg', 'shenhe.jpg', 'Zerotwo.jpg', 'Owari.jpg', 'kitagawa.jpg', 'savage.jpg', 
                         'girl.jpg', 'whitegirl.jpg', 'kayoko.jpg', 'catgirl.jpg', 'Phantom.jpg', 'neon.jpg',
                         'cute.jpg','Angel.jpg','purple.jpg','Rock.jpg', 'control.jpg','Ganyu.jpg']  #pictures name

        #to customize the picture size and the spacing
        for i, image_name in enumerate(button_images):
            image_path = os.path.join(image_directory, image_name)
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image_resized = image.resize((90, 120), Image.LANCZOS)
                ctk_image = customtkinter.CTkImage(light_image=image_resized, dark_image=image_resized, size=(90, 120))
            else:
                print(f"Error: {image_path} not found.")
                continue  #kung walang image iiskip nya

            #create a button with the CTkImage
            button = customtkinter.CTkButton(
                frame_inside_canvas,
                text="",
                image=ctk_image,
                fg_color="#756e91",
                hover_color="#484358",
                command=lambda img_name=image_name: open_popup(img_name),  # Open popup on click
                width=0,
                height=0
            )
            # to arrange buttons in a grid with a maximum of 5 buttons per row
            button.grid(row=i // 5, column=i % 5, padx=20, pady=30)

    # Update the scroll region to encompass the whole frame_inside_canvas
    frame_inside_canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Create a frame for the buttons on the left side
button_frame = customtkinter.CTkFrame(window, fg_color="transparent")
button_frame.pack(side='left', pady=10, padx=10)

# Create a content frame to hold dynamic content
content_frame = customtkinter.CTkFrame(window, fg_color="transparent")
content_frame.pack(side='right', fill='both', expand=True)

# Define the options and their corresponding absolute image paths
options = {
    "Homepage": os.path.join(image_directory, "home.png"),
    "Trending": os.path.join(image_directory, "movie.png"),
    "Favorites": os.path.join(image_directory, "bookmark.png")
}

# Resize dimensions for the images
resize_size = (60, 60)

# Create buttons with images
for option, image_path in options.items():
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found. Skipping {option} button.")
        continue  # Skip to the next option if the image file is not found

    # Load and resize the image
    original_image = Image.open(image_path)
    resized_image = original_image.resize(resize_size, Image.LANCZOS)

    # Create a CTkImage from the resized image
    ctk_image = customtkinter.CTkImage(light_image=resized_image, dark_image=resized_image, size=resize_size)

    # Create a button with the CTkImage
    button = customtkinter.CTkButton(
        button_frame,
        image=ctk_image,
        text="",  # Set text to empty to avoid showing text beside the icon
        command=lambda opt=option: clicker(opt),  # Pass option to the clicker
        width=10,
        height=100,
        hover_color="#383838",
        fg_color=button_frame.cget("fg_color"),
    )
    # Store a reference to the image to prevent garbage collection
    button.image = ctk_image
    button.pack(side='top', anchor='w', pady=15)

# Start the main loop
window.mainloop()
