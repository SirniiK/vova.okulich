# Створення калькулятору схожого на калькулятор Android

![image](https://user-images.githubusercontent.com/86946026/125194680-02b13000-e25b-11eb-8681-a29e568456e5.png)

#import tkinter as tk - "імпорт відповідної бібліотеки Tkinter"

#"Стилі для рамки, кнопок, полів..."
LARGE_FONT_STYLE = ("Arial", 40, "bold")

SMALL_FONT_STYLE = ("Arial", 16)

DIGITS_FONT_STYLE = ("Arial", 24, "bold")

DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"

WHITE = "#FFFFFF"

LIGHT_BLUE = "#CCEDFF"

LIGHT_GRAY = "#F5F5F5"

LABEL_COLOR = "#25265E"

#"характеристика вікна"

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        
#"характеристика полів введення та виводу"

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

#"основні операції з DIVISION SIGN кодом"

    self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    
#"характеристика кнопок"

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
#"кнопка очищення та її характеристика"
    
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
#"оновлення полів"

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])
        
#"запуск калькулятора"

    def run(self):
        self.window.mainloop()
