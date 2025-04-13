import tkinter as tk
from customtkinter import *
import alg


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        bg_color = self._apply_appearance_mode(self.cget("background"))

        name = CTkLabel(self, text="Проверка сообщения на спам")
        name.pack(padx=10, pady=10, anchor="n")


        main_frame = CTkFrame(self, fg_color=bg_color)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)



        vvod_frame = CTkFrame(main_frame, fg_color=bg_color, border_color="gray", border_width=2, corner_radius=10)
        vvod_frame.grid(row=1, column=0, padx=10, pady=10)


        l = CTkLabel(vvod_frame, text="Введите сообщение для проверки")  # Указываем родителя
        l.grid(row=0, column=0, padx=5, pady=5)  # Указываем позицию

        input_text = CTkTextbox(vvod_frame)
        input_text.grid(row=1, padx=10)

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
            else:
                ans_text.delete(0.0, 'end')
                ans_text.configure(border_color="green")
                ans_text.insert(END, "\nТекст безопасен, спам-фраз не обнаружено.")

        btn = CTkButton(vvod_frame, text="Ввод", command=print_text)
        btn.grid(row=2, padx=10, pady=10)

        ans_frame = CTkFrame(main_frame)
        ans_frame.grid(row=1, column=1, padx=10, pady=10)

        ans_text = CTkTextbox(main_frame, border_width=2, border_color="gray", corner_radius=10)
        ans_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


app = App()
app.resizable(False, False)
app.mainloop()