
from tkinter.constants import RAISED
import requests
import tkinter as tk

def news():
    main_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=39f6ff722b73477391dbf16b9b04934c"
    news=requests.get(main_url).json()
    
    article=news['articles']
    
    news_articles=[]
    my_news=" "
    for i in article:
        news_articles.append(i['title'])

    for i in range(len(news_articles)):
        my_news=my_news + str(i+1) + " . " + news_articles[i] +" \n"

    label.config(text=my_news,bg="pink")    

canvas=tk.Tk()
canvas.geometry("1000x600")
canvas.title("Latest News")
canvas.config(bg="pink")

button=tk.Button(canvas,font=("Time New Roman",24),bg="violet",text="Reload",relief=RAISED,command=news)
button.pack(pady= 20)

label=tk.Label(canvas,font=16,justify="left")
label.pack(pady=20)

news()

canvas.mainloop()




