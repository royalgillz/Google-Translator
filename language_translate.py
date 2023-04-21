import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def set_rounded_button_style():
    style = ttk.Style()
    style.configure("RoundedButton", 
                    foreground="black", 
                    background="light blue", 
                    font=("Helvetica", 12),
                    borderwidth=0, 
                    focuscolor="none",
                    focusthickness=0,
                    anchor="center",
                    relief="flat",
                    padding=10)
    return style

#Since default options are allowed, we check for 
#explicitly given source and destination languages
def translate_function():
  #check if the source and target languages are empty  
  if (len(src_entry.get("1.0","end-1c"))>1):
    src_v = src_entry.get("1.0","end-1c").lower()
    src_v =src_v.replace(" ","")
  else:
    src_v = None
    
  if (len(dest_entry.get("1.0","end-1c"))>1):
    dest_v = dest_entry.get("1.0","end-1c").lower()
    dest_v =dest_v.replace(" ","")
  else:
    dest_v = None
  #Check if the text is empty. If so, prompt user to key it
  if (len(text_entry.get("1.0","end-1c"))<=1):
    messagebox.showerror(message="Enter a valid text")
  else:
  #Send the parameters based on user input provided  
    text_v = text_entry.get("1.0","end-1c")  
    if (not src_v) & (not dest_v):
      translated_text = translator_object.translate(text_v)
    elif (not src_v):
      translated_text = translator_object.translate(text_v,dest=dest_v)
    elif (not dest_v):
      translated_text = translator_object.translate(text_v,src=src_v)
    else:
      translated_text = translator_object.translate(text_v,src=src_v,dest=dest_v)
    #Display translated text on a prompt
    messagebox.showinfo(message = "TRANSLATED TEXT: "+translated_text.text)

#Function to clear the text boxes
def clear():
  dest_entry.delete("1.0","end-1c")
  src_entry.delete("1.0","end-1c")
  text_entry.delete("1.0","end-1c")


#Invoke call to class to view a window
window = Tk()
#Set dimensions of window and title
window.geometry("600x300")
window.title("Language Translator by Raman & Sehaj")

#Import the Translator class which will read the input and translate
#Default translation is done by detection of input and to English
translator_object = Translator()
#Title of the app
title_label = Label(window, text="Language Translator by Raman & Sehaj",font=("Gayathri", 12)).pack()
#Read inputs
#Text input
text_label = Label(window, text="Text to translate:").place(x=10,y=30)
text_entry = Text(window, width=50, height=5,font=("Ubuntu Mono",12), highlightthickness=1)
text_entry.place(x=130,y=30)
#Source language input
src_label = Label(window, text="Source language (when empty: auto-detect):").place(x=10,y=130)
src_entry = Text(window, width=30,height=2,font=("Ubuntu Mono",12), highlightthickness=1)
src_entry.place(x=310,y=130)
#Destination input
dest_label = Label(window, text="Target language (when empty: english-default):").place(x=10,y=180)
dest_entry = Text(window, width=30,height=2,font=("Ubuntu Mono",12), highlightthickness=1)
dest_entry.place(x=310,y=180)

#Translate function and clear function activated through buttons
button1 = ttk.Button(window, text='Translate', style='RoundedButton.TButton', command=translate_function).place(x=200, y=240)
button2 = ttk.Button(window, text='Clear', style='RoundedButton.TButton', command=clear).place(x=310, y=240)
#close the app
window.mainloop()
style = ttk.Style()
style.configure('RoundedButton.TButton', relief='flat', background='Light Blue', borderwidth=2,
                bordercolor='black', font=('Helvetica', 10, 'bold'), padding=10, foreground='black'
               )


