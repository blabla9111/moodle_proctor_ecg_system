import TKinterModernThemes as TKMT
import tkinter as tk
import requests
from take_ecg import *
from threading import Thread
from config import *


class App(TKMT.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(APP_NAME, theme, mode,
                         usecommandlineargs=usecommandlineargs, useconfigfile=usethemeconfigfile)
        self.frame = self.addLabelFrame("")
        self.label = self.frame.Label(APP_TEXT_DICT["enter_code"])
        self.entry = self.frame.Entry(tk.Variable)
        self.proctor_start = 0
        self.button = self.frame.AccentButton(APP_TEXT_DICT["enter_code_button"], self.handleSendCodeButtonClick)
        self.run()
        self.proctor_start = 2
        self.close()

    def handleSendCodeButtonClick(self):
        url = ECG_PROCTOR_SERVER_URL+FIND_CODE_URL
        data = {REQUEST_RARAMS_DICT["code"]: self.entry.get()}
        r = requests.post(url, json=data)
        global id_transaction
        id_transaction = r.text
        if r.text != "None":
            print(r.text)
            self.label.configure(text=APP_TEXT_DICT["start_ecg"])
            self.entry.destroy()
            self.button.destroy()
            self.button = self.frame.AccentButton(APP_TEXT_DICT["start_ecg_button"], self.handleStartECGButtonClick)

    def handleStartECGButtonClick(self):
        url = ECG_PROCTOR_SERVER_URL+SEND_INIT_ECG_URL
        ecg = take_ecg()
        if ecg is None:  # убрали с порта
            self.proctor_start = 2
            self.button.destroy()
        else:
            data = {REQUEST_RARAMS_DICT["id_transaction"]: id_transaction,
                    REQUEST_RARAMS_DICT["ecg_data"]: ecg}
            r = requests.post(url, json=data)
            self.label.configure(text=APP_TEXT_DICT["ecg_in_progress"])
            self.button.destroy()
        # Страрт непрерывной идентификации
        Thread(target=self.ecg).start()

    def ecg(self):
        text = ""
        while text != APP_END_CODE and self.proctor_start != 2:
            time.sleep(10)
            url = ECG_PROCTOR_SERVER_URL+CHECK_ECG_URL
            ecg = take_ecg()
            if ecg is None:  # убрали с порта
                self.proctor_start = 2
            else:
                data = {REQUEST_RARAMS_DICT["id_transaction"]: id_transaction,
                        REQUEST_RARAMS_DICT["ecg_data"]: ecg}
                r = requests.post(url, json=data)
                print(r.text)
                text = r.text
        self.close(id_transaction)
        self.label.configure(text=APP_TEXT_DICT["ecg_end"])

    def close(self, id_transaction="None"):
        url = ECG_PROCTOR_SERVER_URL+CLOSE_DESKTOP_URL
        data = {REQUEST_RARAMS_DICT["id_transaction"]: id_transaction}
        requests.post(url, json=data)


if __name__ == "__main__":
    App(APP_THEME[0], APP_THEME[1])