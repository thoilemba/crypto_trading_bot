import tkinter as tk
import logging
from binance_futures import get_contract

logger = logging.getLogger()

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance_contracts = get_contract()

    root = tk.Tk()
    root.configure(bg='grey12')

    font1 = ("Calibri", 12, "normal")

    i = 0
    j = 0

    for contract in binance_contracts:
        label_widget = tk.Label(root, text=contract, bg="grey12", fg="SteelBlue1", font=font1, width=13)
        label_widget.grid(row=i, column=j, sticky="ew")

        if i == 7:
            j += 1
            i = 0
        else:
            i += 1

    root.mainloop()
