import tkinter as tk
from doctest import master
import datetime

from customtkinter import *
from PIL import Image, ImageTk
from uritemplate import expand

import alg


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        bg_color = self._apply_appearance_mode(self.cget("background"))

        name = CTkLabel(self, text="Проверка сообщения на спам", font=("Arial",20, "bold"))
        name.pack(padx=10, pady=10, anchor="n")

        # Основной фрейм
        main_frame = CTkFrame(self, fg_color=bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


        # Фрейм для вводо сообщения
        vvod_frame = CTkFrame(main_frame, fg_color=bg_color, border_color="gray", border_width=2, corner_radius=10)
        vvod_frame.grid(row=1, column=0, padx=10, pady=10)


        l = CTkLabel(vvod_frame, text="Введите сообщение для проверки")  # Указываем родителя
        l.grid(row=0, column=0, padx=5, pady=5)  # Указываем позицию

        input_text = CTkTextbox(vvod_frame)
        input_text.grid(row=1, padx=10)

        # Проверка сообщения и вывод результата
        def print_text():
            spam_phrases = alg.load_spam_phrases()
            spam_words = alg.load_spam_words()
            text = input_text.get("1.0", "end-1c")
            detected_phrases = alg.check_spam(text, spam_phrases, spam_words)
            if detected_phrases:
                a = '------\n'
                for phrase in detected_phrases:
                    a += f"- {phrase}\n"
                    ans_text.delete(0.0, 'end')
                a += "------"
                ans_text.configure(border_color="red")
                ans_text.insert(END, f"\nОбнаружены спам-фразы:\n\n{a}\n\nРекомендуется пометить как спам!")
                with open("spam_history.txt", "a") as file:
                    file.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")};{text[:10]}...;true\n")
            else:
                ans_text.delete(0.0, 'end')
                ans_text.configure(border_color="green")
                ans_text.insert(END, "\nТекст безопасен, спам-фраз не обнаружено.")
                with open("spam_history.txt", "a") as file:
                    file.write(f"{datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")};{text[10]}...;false\n")

        # Кнопка ввода
        btn_frame = CTkFrame(vvod_frame, width=200)
        btn_frame.grid(row=2, padx=10, pady=10)

        btn = CTkButton(btn_frame, text="Ввод", command=print_text, width=135, height=35)
        btn.grid(row=0, column=1, padx=5, pady=5)

        # Загрузка текста из файла
        def load_from_file():
            file_path = filedialog.askopenfilename(title="Выберите файл", filetypes=[('Text Files', '*.txt')])
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                input_text.delete(0.0, 'end')
                input_text.insert(END, text)
                spam_phrases = alg.load_spam_phrases()
                spam_words = alg.load_spam_words()
                detected_phrases = alg.check_spam(text, spam_phrases, spam_words)
                if detected_phrases:
                    a = '------\n'
                    for phrase in detected_phrases:
                        a += f"- {phrase}\n"
                        ans_text.delete(0.0, 'end')
                    a += "------"
                    ans_text.configure(border_color="red")
                    ans_text.insert(END, f"\nОбнаружены спам-фразы:\n\n{a}\n\nРекомендуется пометить как спам!")
                else:
                    ans_text.delete(0.0, 'end')
                    ans_text.configure(border_color="green")
                    ans_text.insert(END, "\nТекст безопасен, спам-фраз не обнаружено.")


        # Кнопка выбора файла
        icon = tk.PhotoImage(file="../AntiSpam/img/icn1.png")
        btn_file = CTkButton(btn_frame, width=35, image=icon, text='', command=load_from_file)
        btn_file.grid(row=0, column=0, padx=5, pady=5)


        # Фрейм с выбором файла
        ans_frame = CTkFrame(main_frame)
        ans_frame.grid(row=1, column=1, padx=10, pady=10)

        ans_text = CTkTextbox(main_frame, border_width=2, border_color="gray", corner_radius=10)
        ans_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        


app = App()
app.resizable(False, False)
app.title("AntiSpam")
app.mainloop()