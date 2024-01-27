from tkinter import *
import requests
root=Tk()
root.geometry("300x300")
ZIP = IntVar()
ZIP.set("")
api_key = "1ba1775477d439fe3da26d000031a42a"

def get_weather(api_key, ZIP):
    url= "http://api.openweathermap.org/data/2.5/weather"
    para={
        'q':ZIP,'appid':api_key,'units':'imperial'
    }
    try:
        responce = requests.get(url, params=para)
        data= responce.json()
        temperature = data['main']['temp']
        l3= Label(root, text=f"{temperature} Fahrenheit").place(x=50, y=100)
    except Exception as e:
        print(f"{e}")


def Submit():
    abc= ZIP.get()
    get_weather(api_key, abc)

L1= Label(root, text="Check your Weather",fg="red", bg="black", font=('Helvetica bold', 12, 'bold')).pack()
L2= Label(root, text="Enter your Zip code").place(x=30,y=30)
E1= Entry(root, textvariable=ZIP).place(x=150, y=30)
S1= Button(root, text="Submit", command=Submit).place(x=130, y=60)



root.mainloop()
