from tkinter import *
from tkinter import messagebox, Menu
import requests
import json
import sqlite3

crypto = Tk()
crypto.title("My Crypto Portfolio - Using SQLite DB")
crypto.iconbitmap('favicon.ico')
con = sqlite3.connect('coin_data.db')
cursorObj = con.cursor()
con.commit()

def close_app():
    crypto.destroy()    
    menu = Menu(crypto)
    file_item = Menu(menu)
    file_item.add_command(label='Close App', command=close_app)
    menu.add_cascade(label="File", menu=file_item)
    crypto.config(menu=menu)
    
def insert_coin():
    cursorObj.execute("DROP TABLE IF EXISTS coin_data")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS coin_data(id INTEGER PRIMARY KEY, symbol TEXT unique, price REAL, market_cap REAL, volume_24h REAL)")
    con.commit()

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=1e6c18b1-d19e-47e0-bf94-c2df617ba16d")
    api = json.loads(api_request.content)
    for i in range(0, 199):
        symbol = api['data'][i]['symbol']
        current_price = api['data'][i]['quote']['USD']['price']
        market_cap = api['data'][i]['quote']['USD']['market_cap']
        volume_24h = api['data'][i]['quote']['USD']['volume_24h']
        cursorObj.execute("INSERT INTO coin_data(symbol, price, market_cap, volume_24h) VALUES(?, ?, ?, ?)", (symbol, current_price, market_cap, volume_24h))
        con.commit()

def query_coin():
    coin_row = 1
    cursorObj.execute("SELECT * FROM coin_data order by price DESC")
    coins_price = cursorObj.fetchall()
    cursorObj.execute("SELECT * FROM coin_data order by market_cap DESC")
    coins_market_cap = cursorObj.fetchall()
    cursorObj.execute("SELECT * FROM coin_data order by volume_24h DESC")
    coins_volume_24h = cursorObj.fetchall()

#     print(str(coins_price) + '\n\n\n' + str(coins_market_cap) + '\n\n\n' + str(coins_volume_24h))
    Header = Label(crypto, text=" ", bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    Header.grid(row=coin_row, column=0, sticky=N+S+E+W)

    Header = Label(crypto, text="Price", bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    Header.grid(row=coin_row, column=0, sticky=N+S+E+W)
    
    coin_row += 2
    
    #1
    for i in range(0,5):
        portfolio_id = Label(crypto, text=coins_price[i][0], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        portfolio_id.grid(row=coin_row, column=0, sticky=N+S+E+W)
    
        name = Label(crypto, text=coins_price[i][1], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        name.grid(row=coin_row, column=1, sticky=N+S+E+W)
    
        price = Label(crypto, text="${0:.2f}".format(float(coins_price[i][2])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        price.grid(row=coin_row, column=2, sticky=N+S+E+W)
    
        market_cap = Label(crypto, text="${0:.2f}".format(float(coins_price[i][3])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        market_cap.grid(row=coin_row, column=3, sticky=N+S+E+W)

        volume = Label(crypto, text="${0:.2f}".format(float(coins_price[i][4])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        volume.grid(row=coin_row, column=4, sticky=N+S+E+W)
        
        coin_row += 1
        
    Header2 = Label(crypto, text=" ", bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    Header2.grid(row=coin_row, column=0, sticky=N+S+E+W)

    Header2 = Label(crypto, text="Market Cap", bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    Header2.grid(row=coin_row, column=0, sticky=N+S+E+W)
        
    coin_row += 2

#2: coins_market_cap   

    for i in range(0,5):
        portfolio_id = Label(crypto, text=coins_market_cap[i][0], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        portfolio_id.grid(row=coin_row, column=0, sticky=N+S+E+W)

        name = Label(crypto, text=coins_market_cap[i][1], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        name.grid(row=coin_row, column=1, sticky=N+S+E+W)

        price = Label(crypto, text="${0:.2f}".format(float(coins_market_cap[i][2])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        price.grid(row=coin_row, column=2, sticky=N+S+E+W)

        market_cap = Label(crypto, text="${0:.2f}".format(float(coins_market_cap[i][3])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        market_cap.grid(row=coin_row, column=3, sticky=N+S+E+W)

        volume = Label(crypto, text="${0:.2f}".format(float(coins_market_cap[i][4])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        volume.grid(row=coin_row, column=4, sticky=N+S+E+W)

        coin_row += 1
        
    Header = Label(crypto, text=" ", bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    Header.grid(row=coin_row, column=0, sticky=N+S+E+W)

    Header = Label(crypto, text="Volume", bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    Header.grid(row=coin_row, column=0, sticky=N+S+E+W) 
        
    coin_row += 2

#3 : coins_volume_24h
    
    for i in range(0,5):
        portfolio_id = Label(crypto, text=coins_volume_24h[i][0], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        portfolio_id.grid(row=coin_row, column=0, sticky=N+S+E+W)

        name = Label(crypto, text=coins_volume_24h[i][1], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        name.grid(row=coin_row, column=1, sticky=N+S+E+W)

        price = Label(crypto, text="${0:.2f}".format(float(coins_volume_24h[i][2])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        price.grid(row=coin_row, column=2, sticky=N+S+E+W)

        market_cap = Label(crypto, text="${0:.2f}".format(float(coins_volume_24h[i][3])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        market_cap.grid(row=coin_row, column=3, sticky=N+S+E+W)

        volume = Label(crypto, text="${0:.2f}".format(float(coins_volume_24h[i][4])), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
        volume.grid(row=coin_row, column=4, sticky=N+S+E+W)

        coin_row += 1
        

def app_header():
    portfolio_id = Label(crypto, text="Portfolio ID", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    portfolio_id.grid(row=0, column=0, sticky=N+S+E+W)
    
    name = Label(crypto, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=1, sticky=N+S+E+W)
    
    price = Label(crypto, text="Price", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    price.grid(row=0, column=2, sticky=N+S+E+W)
    
    market_cap = Label(crypto, text="Market Cap", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    market_cap.grid(row=0, column=3, sticky=N+S+E+W)
    
    volume = Label(crypto, text="Volume", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    volume.grid(row=0, column=4, sticky=N+S+E+W)
        
app_header()
insert_coin()
query_coin()
crypto.mainloop()
cursorObj.close()
con.close()
