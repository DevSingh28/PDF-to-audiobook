from tkinter import *
from tkinter import filedialog, messagebox
import PyPDF2
from gtts import gTTS

window = Tk()
window.title("PDF to Audiobook")
window.config(pady=20, padx=20)
cursive_font = ("Comic Sans MS", 24, "bold")
label_color = "blue"


def open_file():
    pdf_path = filedialog.askopenfilename(filetypes=[('PDF Files', "*.pdf")])
    return pdf_path


def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as data:
        reader = PyPDF2.PdfReader(data)
        for page in reader.pages:
            text += page.extract_text()
    return text


def text_to_speech(text, language='en'):
    gtt = gTTS(text=text, lang=language, slow=False)
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[('Music Files', "*.mp3")])
    if save_path:
        gtt.save(save_path)
        messagebox.showinfo("Success", "File Saved Successfully.")


def final():
    label2.config(text="Please wait patiently while the conversion is in progress...", fg="red")
    output = open_file()
    text = pdf_to_text(output)
    text_to_speech(text)


canvas = Canvas(width=200, height=200)
image_data = PhotoImage(file="download (2).png")
canvas.create_image(100, 100, image=image_data)
canvas.pack()

label1 = Label(text='Select Your File', font=cursive_font, fg=label_color)
label1.pack()

button1 = Button(text='Select the File', command=final)
button1.pack()

label2 = Label(text="The conversion time increases as the size of your PDF file grows.", fg=label_color)
label2.pack()

window.mainloop()
