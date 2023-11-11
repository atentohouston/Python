import subprocess
import getpass  


from tkinter import Tk, Entry, Button, Label, messagebox, font
from pytube import YouTube
import os
import pyperclip

# Función para descargar el audio de YouTube y mostrar un mensaje de confirmación
def download_audio():
    youtube_url = url_entry.get()

    if youtube_url:
        try:
            yt = YouTube(youtube_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            download_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{yt.title}.mp3")

            audio_stream.download(output_path=download_path)

            # Mostrar un mensaje de confirmación
            messagebox.showinfo("Descarga completada", f"Descargado: {yt.title}.mp3 en {download_path}")

            # Abrir la carpeta de descargas
            os.startfile(os.path.expanduser("~\\Downloads"))

            # Limpiar el campo de entrada
            url_entry.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", f"Error al descargar: {str(e)}")
    else:
        messagebox.showwarning("Error", "Ingrese un enlace de YouTube válido.")

# Función para pegar el enlace desde el portapapeles
def paste_url():
    url_entry.delete(0, 'end')
    url = pyperclip.paste()
    url_entry.insert(0, url)

window = Tk()
window.title("Descargar Música MP3 de YouTube")
window.geometry("400x200")  # Tamaño de la ventana

# Cambiar el color de fondo y el color de fuente
window.configure(bg='black')
window.option_add("*TButton*Background", "yellow")
window.option_add("*TButton*Foreground", "black")

# Estilo de fuente personalizado
custom_font = font.nametofont("TkDefaultFont")
custom_font.configure(family="Arial", size=14, weight="bold")  # Fuente más grande y negrita

# Configuración de margen
label_margin = 0.2

Label(window, text="Ingrese el link de YouTube", bg='black', fg='yellow', font=custom_font, pady=label_margin).pack()
Label(window, text="YouTube:", bg='black', font=custom_font).pack()

# Crear una etiqueta especial para "You" con color blanco
label_you = Label(window, text="YouTube", bg='black', fg='white', font=custom_font)
label_you.pack()

url_entry = Entry(window, font=custom_font)
url_entry.pack()

paste_button = Button(window, text="Pegar Enlace", command=paste_url, bg='black', fg='yellow', font=custom_font)
paste_button.pack()

download_button = Button(window, text="Descargar", command=download_audio, bg='black', fg='yellow', font=custom_font)
download_button.pack()

window.mainloop()



