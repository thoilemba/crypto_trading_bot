import tkinter as tk
import logging
from connectors.binance_futures import BinanceFutureClient
from interface.root_component import Root

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

    binance = BinanceFutureClient("dbc3a01149f0e22c4f038929cf6d02f13686616c5b038842492466a833f7e246",
                                  "8ad3cdc5e5045adb49db2fabf809008f75ee31d691dd4c86f0f05ce645c3d5e9", True)

    root = Root()
    root.mainloop()

