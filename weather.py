
# IMPORT REQUIRED MODULES

from cProfile import label
from multiprocessing import current_process
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# DRIVER CODE

# CREATE OBJECT
root=Tk()

#  ADD TITLE
root.title("Weather App")

# ADD WINDOW SIZE
root.geometry("900x600+300+200")
root.resizable(False,False)

# EXPLICIT FUNCTION TO GET WEATHER DETAILS

def getWeather():
    try:
        city=textfield.get()
 
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj = TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        # print(result)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # ACCESING API KEY
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=81b50e9d955dbcc0459a88e335cd22fb"
        
        # EXTRACTING WEATHER DATA 
        json_data= requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        
        
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    # SHOWING ERROR MESSAGE IF ENTERED INVALID CITY NAME
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry !!")

# ADDING SEARCH BOX IMAGE

Search_image = PhotoImage(file ="images\search_box.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=15)

textfield=Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#333333",border=0,fg="white")
textfield.place(x=45,y=20)
textfield.focus()

# INSERTING SEARCH_ICON
Search_icon = PhotoImage(file="images\search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="grey",command=getWeather)
myimage_icon.place(x=475,y=15)

# INSERTING WEATHER LOGO
Logo_image = PhotoImage(file="images\logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#  INSERTING BOTTOM DESCRIPTION BOX

Frame_image = PhotoImage(file="images\info.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=4,pady=4,side=BOTTOM)

name=Label(root,font=("arial",12,"bold"))
name.place(x=30,y=100)

# DATE AND TIME
clock=Label(root,font=("Helvetica",15))
clock.place(x=30,y=130)

# WIND
label1=Label(root,text="WIND",font=("Helvetica",10,'bold'),fg="white",bg="red")
label1.place(x=70,y=507)

# HUMIDITY 
label2=Label(root,text="HUMIDITY",font=("Helvetica",10,'bold'),fg="white",bg="red")
label2.place(x=270,y=507)

# DESCRIPTION
label3=Label(root,text="DESCRIPTION",font=("Helvetica",10,'bold'),fg="white",bg="red")
label3.place(x=470,y=507)

# PRESSURE
label4=Label(root,text="PRESSURE",font=("Helvetica",10,'bold'),fg="white",bg="red")
label4.place(x=670,y=507)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=540,y=150)

c=Label(font=("arial",15,'bold'))
c.place(x=500,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="red")
w.place(x=70,y=530)
 
h=Label(text="...",font=("arial",20,"bold"),bg="red")
h.place(x=280,y=530)

d=Label(text="...",font=("arial",15,"bold"),bg="red")
d.place(x=450,y=530)

p=Label(text="...",font=("arial",20,"bold"),bg="red")
p.place(x=680,y=530)


root.mainloop()

