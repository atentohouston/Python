import os
import pyperclip
from pytube import YouTube
from tkinter import Tk, Entry, Button, Label, messagebox, font

# Función para descargar el audio de YouTube y mostrar un mensaje de confirmación
def download_audio():
    youtube_url = url_entry.get().strip()
    if youtube_url:
        try:
            yt = YouTube(youtube_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            
            if audio_stream is None:
                messagebox.showerror("Error", "No se encontró stream de audio disponible.")
                return

            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            filename = f"{yt.title}.mp3"

            # Descargar audio
            audio_stream.download(output_path=downloads_folder, filename=filename)

            messagebox.showinfo("Descarga completada", f"Descargado: {filename} en {downloads_folder}")

            # Abrir carpeta de descargas
            os.startfile(downloads_folder)

            # Limpiar el campo de entrada
            url_entry.delete(0, 'end')

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descargar: {str(e)}")
    else:
        messagebox.showwarning("Error", "Ingrese un enlace de YouTube válido.")

# Función para pegar el enlace desde el portapapeles
def paste_url():
    url_entry.delete(0, 'end')
    url = pyperclip.paste()
    url_entry.insert(0, url)

# Configuración de la ventana
window = Tk()
window.title("Descargar Música MP3 de YouTube")
window.geometry("450x250")
window.configure(bg='black')

# Fuente personalizada
custom_font = font.nametofont("TkDefaultFont")
custom_font.configure(family="Arial", size=12, weight="bold")

# Etiquetas
Label(window, text="Ingrese el link de YouTube", bg='black', fg='yellow', font=custom_font, pady=10).pack()
url_entry = Entry(window, font=custom_font, width=40)
url_entry.pack(pady=5)

# Botones
paste_button = Button(window, text="Pegar Enlace", command=paste_url, bg='yellow', fg='black', font=custom_font)
paste_button.pack(pady=5)

download_button = Button(window, text="Descargar", command=download_audio, bg='yellow', fg='black', font=custom_font)
download_button.pack(pady=5)

window.mainloop()
