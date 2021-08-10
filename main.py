import tkinter as tk
import logging
from connectors.binance_futures import BinanceFutureClient

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

    binance = BinanceFutureClient(True)
    print(binance.get_historical_candles("BTCUSDT", "1h"))

    root = tk.Tk()
    root.mainloop()
