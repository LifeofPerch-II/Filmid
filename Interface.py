import tkinter as tk
from tkinter import ttk, messagebox
import requests
#Tulevikus kasutan neid, et alla tõmmata ja tkinterisse saada filmi posterid
"""
from io import BytesIO
from PIL import ImageTk, Image
"""

#Enda api key
API_KEY = "92d9b9e2"

#filmi nime kaudu info saamine
def get_movie_info():
    #võtab textboxist filmi nime
    movie_title = entry.get().strip()
    #Vaatab, et kastis oleks midagiz
    if not movie_title:
        messagebox.showerror("Error", "Please enter a title")
        return
    #omdbapi leht, kust tõmban info filmi kohta
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # jagab info osadeks
    if data["Response"] == "True":
        info = (
            f"Nimi: {data['Title']}\n"
            f"Aasta: {data['Year']}\n"
            f"Žanr: {data['Genre']}\n"
            f"Direktor: {data['Director']}\n"
            f"IMDb hinnang: {data['imdbRating']}"
        )
        #Kuvab info väiksemas aknas
        messagebox.showinfo("Movie Info", info)
    else:
        messagebox.showerror("Error", f"Movie not found: {data['Error']}")

#Loop Tkinter akna
root = tk.Tk()
root.title("Filmid")
root.geometry("580x300")
#Tekst akna ülemises servas
label = tk.Label(root, text="Sisestage filmi pealkiri")
label.pack(pady=10)
#Loob välja kuhu kasutaja saab sisestada pealkirja
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
#Nupp mille vajutamisel käivitub info otsimine
button = tk.Button(root, text="OK", command=get_movie_info)
button.pack(pady=5)
#Hoiab akent käimas
root.mainloop()
