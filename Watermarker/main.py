import tkinter as tk
from PIL import Image, ImageTk,ImageFont,ImageDraw
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import ttk


def browse_images():
    global image,im,file_name
    filename = fd.askopenfilename(title='Browse for images', initialdir='/', filetypes=[('png Files', '*png')])
    file_name = filename.split('/')[-1]
    print(file_name)
    im = Image.open(filename)
    im.thumbnail((300, 300))
    image = ImageTk.PhotoImage(im)
    picture_canvas.create_image(150,150,image=image)
    print('i AM DONE')

def watermark_image():
    global image,im,watermarked_image
    fonts = {
    'font-1': './assets/ALBA____.ttf',
    'font-2': './assets/ALBAS___.TTF',
    'font-3': './assets/East_Lift.ttf',
    'font-4': './assets/pricedown bl.ttf',
    'font-5': './assets/font.ttf',
    }
    text = txt_input.get()
    color = color_input.get()
    font = font_input.get()
    if font in fonts:
        font = fonts[font]
    bottom_left_corner = (5,125)

    watermarked_image = im.copy()
    draw = ImageDraw.Draw(watermarked_image)
    font = ImageFont.truetype(font,20)
    draw.text(bottom_left_corner,text,color,font=font)
    image = ImageTk.PhotoImage(watermarked_image)
    picture_canvas.itemconfigure(picture,image=image)

def save_image():
    global watermarked_image,file_name
    print(file_name)
    file_name = file_name.split('/')[-1]
    print(file_name)
    watermarked_image.save(f'./images/{file_name}')
    showinfo(title='Saved File', message=f'The watermarked {file_name} has been saved to the images folder.')

# Configure the window
root = tk.Tk()
root.title('Watermarking App')
root.config(padx=5, pady=5)

# Widgets
file_name = './assets/defaultim.png'
browse_btn = ttk.Button(text='Browse', command=browse_images)
browse_btn.config(width=30)

txt_label = tk.Label(text='Text')
txt_input = ttk.Entry(width=23)

color_label = tk.Label(text='Color')
color_input = ttk.Combobox(values=['red','yellow','green','purple','orange','black','pink'])

font_label = tk.Label(text='Font')
font_input = ttk.Combobox(values=['font-1','font-2','font-3','font-4','font-5'])

watermarker_btn = ttk.Button(text='Watermark Image', command=watermark_image)
watermarker_btn.config(width=30)
save_btn = ttk.Button(text='Save Image',command=save_image)
save_btn.config(width=30)

im = Image.open(file_name)
im.thumbnail((300, 300))
image = ImageTk.PhotoImage(image=im)

picture_canvas = tk.Canvas(width=300, height=300)
picture = picture_canvas.create_image(150, 150, image=image)
# Placing the widgets

browse_btn.grid(row=0, column=1, columnspan=3)

txt_label.grid(row=2, column=1)
txt_input.grid(row=2, column=2)

color_label.grid(row=3, column=1)
color_input.grid(row=3, column=2)

font_label.grid(row=4, column=1)
font_input.grid(row=4, column=2)

watermarker_btn.grid(row=5, column=1, columnspan=4)
save_btn.grid(row=6, column=1, columnspan=4)

picture_canvas.grid(row=0, column=5, rowspan=10)

root.mainloop()
