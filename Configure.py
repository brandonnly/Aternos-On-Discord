import tkinter as tk
import re

def launch_config():
    window = tk.Tk()

    window.title("Configure Aternos Bot")
    window.geometry('300x300')

    # label = tk.Label(window, text="Hello, this is the configuration window for your Aternos discord bot.")
    # label.grid(column=0, row=0)

    bot_token_label = tk.Label(window, text="Bot token")
    bot_token_label.place(x=80/1.5, y=130/1.5)
    bot_token_entry = tk.Entry(window, width=15)
    bot_token_entry.place(x=240/1.5, y=130/1.5)

    server_uri_label = tk.Label(window, text="Server link")
    server_uri_label.place(x=80/1.5, y=160/1.5)
    server_uri_entry = tk.Entry(window, width=15)
    server_uri_entry.place(x=240/1.5, y=160/1.5)

    save_button = tk.Button(window, text="Save configuration", bg="#1a6600", fg="white")
    save_button['command'] = lambda : save_configuration(server_uri_entry, bot_token_entry, window)
    save_button.place(x=160/1.5, y=210/1.5)

    window.mainloop()

def save_configuration(uri_entry, token_entry, window):
    if uri_entry.get().endswith(".aternos.me"):
        bot_token = "BOT_TOKEN= {}".format(token_entry.get())
        uri_entry = "\nSERVER_STATUS_URI= {}".format(uri_entry.get())
        with open(".env", "w") as f:
            f.write(bot_token)
            f.write(uri_entry)
        window.destroy()
    else:
        error = tk.Label(window, text="Server link has to match <YourServerName>.aternos.me", )
        error.place(x=0, y=0)
if __name__ == "__main__":
    launch_config()


