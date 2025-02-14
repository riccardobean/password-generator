from tkinter import *
from tkinter import colorchooser
from constants import *
import random
import pyperclip


def generate_upper(length):
    const_len = len(UPPER)
    return_string = ""
    for value in range(length):
        index = random.randrange(0, const_len)
        return_string += UPPER[index]
    return return_string


def generate_lower(length):
    const_len = len(LOWER)
    return_string = ""
    for value in range(length):
        index = random.randrange(0, const_len)
        return_string += LOWER[index]
    return return_string


def generate_nums(length):
    const_len = len(NUMS)
    return_string = ""
    for value in range(length):
        index = random.randrange(0, const_len)
        return_string += NUMS[index]
    return return_string


def generate_symbols(length):
    const_len = len(SYMBOLS)
    return_string = ""
    for value in range(length):
        index = random.randrange(0, const_len)
        return_string += SYMBOLS[index]
    return return_string


def show_error_window(message):
    error_window = Toplevel()
    error_window.title("Error")
    error_window.geometry("300x150")
    error_window.configure(bg="#FFCCCC")

    error_label = Label(error_window, text="An error occurred", font=A18B, fg="red", bg="#FFCCCC")
    error_label.pack(pady=10)

    message_label = Label(error_window, text=message, font=A14, bg="#FFCCCC", wraplength=250, justify="center")
    message_label.pack(pady=5)

    error_window.grab_set()


class PasswordGeneratorApp:
    def __init__(self):
        self.upper_status = True
        self.lower_status = True
        self.nums_status = True
        self.symbols_status = True
        self.bg_color = BG
        self.fg_color = FG
        self.copy_to_clipboard_status = True if COPY_TO_CLIPBOARD == "True" else False

        self.pwrd = Tk()
        self.pwrd.title("Password Generator")
        self.photo = PhotoImage(file="assets/logo.png")
        self.pwrd.iconphoto(True, self.photo)
        self.pwrd.geometry("570x570")
        self.pwrd.config(bg=BG)

        self.on = PhotoImage(file="assets/on.png")
        self.off = PhotoImage(file="assets/off.png")

        self.create_widgets()
        self.pwrd.mainloop()

    # Password App
    def create_widgets(self):
        # Pass Frame W
        # Pass Frame A
        #   Pass Frame 1
        #   Pass Frame 2
        # Pass Frame B
        #   Pass Frame 3
        #   Pass Frame 4
        #   Pass Frame 5

        self.Pass_Frame_W = Frame(self.pwrd, bg=BG)
        self.Pass_FrameA = Frame(self.pwrd, bg=BG)
        self.Pass_Frame1 = Frame(self.Pass_FrameA, bg=BG)
        self.Pass_Frame2 = Frame(self.Pass_FrameA, bg=BG)
        self.Pass_FrameB = Frame(self.pwrd, bg=BG)
        self.Pass_Frame3 = Frame(self.Pass_FrameB, bg=BG)
        self.Pass_Frame4 = Frame(self.Pass_FrameB, bg=BG)
        self.Pass_Frame5 = Frame(self.Pass_FrameB, bg=BG)
        self.Pass_Welcome_Label = Label(self.Pass_Frame_W, text="Welcome to the Password Generator!", font=A18B, bg=BG,
                                        fg=FG)
        self.Pass_Frame_W.pack(side="top", pady=20)
        self.Pass_FrameA.pack(side="top")
        self.Pass_Frame1.pack(side="left", padx=50)
        self.Pass_Frame2.pack(side="left", padx=40)
        self.Pass_FrameB.pack(side="top", pady=10)
        self.Pass_Frame3.pack(side="top", pady=10)
        self.Pass_Frame4.pack(side="top", pady=10)
        self.Pass_Frame5.pack(side="top", pady=10)
        self.Pass_Welcome_Label.pack(side="top")

        self.Pass_Length_Label = Label(self.Pass_Frame1, text="Length", font=A18B, bg=BG, fg=FG)
        self.Pass_Length_Label.pack(side="top", pady=10)
        self.Pass_Length_Text = Text(self.Pass_Frame2, width=6, height=1, font=A18)
        self.Pass_Length_Text.pack(side="top", pady=7)

        self.Pass_Uppercase_label = Label(self.Pass_Frame1, text="Uppercase Letters", font=A18, bg=BG, fg=FG)
        self.Pass_Uppercase_label.pack(side="top", pady=10)
        self.Pass_Uppercase_button = Button(self.Pass_Frame2, image=self.on, bd=0, bg=BG, activebackground=BG,
                                            command=lambda: self.switch("Uppercase"))
        self.Pass_Uppercase_button.pack(side='top', pady=7)

        self.Pass_Lowercase_label = Label(self.Pass_Frame1, text="Lowercase Letters", font=A18, bg=BG, fg=FG)
        self.Pass_Lowercase_label.pack(side="top", pady=10)
        self.Pass_Lowercase_button = Button(self.Pass_Frame2, image=self.on, bd=0, bg=BG, activebackground=BG,
                                            command=lambda: self.switch("Lowercase"))
        self.Pass_Lowercase_button.pack(side='top', pady=7)

        self.Pass_Numbers_label = Label(self.Pass_Frame1, text="Numbers", font=A18, bg=BG, fg=FG)
        self.Pass_Numbers_label.pack(side="top", pady=10)
        self.Pass_Numbers_button = Button(self.Pass_Frame2, image=self.on, bd=0, bg=BG, activebackground=BG,
                                          command=lambda: self.switch("Numbers"))
        self.Pass_Numbers_button.pack(side='top', pady=7)

        self.Pass_Symbols_label = Label(self.Pass_Frame1, text="Special Characters", font=A18, bg=BG, fg=FG)
        self.Pass_Symbols_label.pack(side="top", pady=10)
        self.Pass_Symbols_button = Button(self.Pass_Frame2, image=self.on, bd=0, bg=BG, activebackground=BG,
                                          command=lambda: self.switch("Symbols"))
        self.Pass_Symbols_button.pack(side='top', pady=7)

        self.Pass_Generate_Button = Button(self.Pass_Frame3, text="Generate", font=A18, width=10, bg="skyblue",
                                           activebackground=FG, activeforeground=BG, command=self.output)
        self.Pass_Generate_Button.pack(side="left", padx=20)

        self.Pass_Settings_Button = Button(self.Pass_Frame3, text="Settings", font=A18, width=10, bg="skyblue",
                                           activebackground=FG, activeforeground=BG,
                                           command=lambda: self.open_settings())
        self.Pass_Settings_Button.pack(side="right", padx=20)

        self.Pass_Password_Text = Text(self.Pass_Frame4, font=C18, width=40, height=1)
        self.Pass_Password_Text.pack(side="top", pady=10)

        self.Pass_Copied_Label = Label(self.Pass_Frame5, text="Copied to Clipboard!", fg="green", font=A12B)

    def switch(self, option):
        if option == "Uppercase":
            if self.upper_status:
                self.Pass_Uppercase_button.config(image=self.off)
                self.upper_status = False
            else:
                self.Pass_Uppercase_button.config(image=self.on)
                self.upper_status = True
        if option == "Lowercase":
            if self.lower_status:
                self.Pass_Lowercase_button.config(image=self.off)
                self.lower_status = False
            else:
                self.Pass_Lowercase_button.config(image=self.on)
                self.lower_status = True
        if option == "Numbers":
            if self.nums_status:
                self.Pass_Numbers_button.config(image=self.off)
                self.nums_status = False
            else:
                self.Pass_Numbers_button.config(image=self.on)
                self.nums_status = True
        if option == "Symbols":
            if self.symbols_status:
                self.Pass_Symbols_button.config(image=self.off)
                self.symbols_status = False
            else:
                self.Pass_Symbols_button.config(image=self.on)
                self.symbols_status = True
        return self.upper_status, self.lower_status, self.nums_status, self.symbols_status

    def output(self):
        text, code = self.validate()
        self.Pass_Password_Text.delete("1.0", END)
        self.Pass_Password_Text.insert(END, text)
        self.Pass_Password_Text.config(fg="red" if code == 1 else "black")
        if code == 0 and COPY_TO_CLIPBOARD == "True":
            pyperclip.copy(text)
            self.show_badge()

    def how_many_are_checked(self):
        count = 0
        if self.upper_status:
            count += 1
        if self.lower_status:
            count += 1
        if self.nums_status:
            count += 1
        if self.symbols_status:
            count += 1
        return count

    def validate(self):
        length_str = self.Pass_Length_Text.get("1.0", "end-1c")
        if length_str.strip() and length_str != "0":
            try:
                length = int(length_str)
            except ValueError:
                return "ERROR: Password length must be a number", 1
        else:
            return "ERROR: Password length cannot be zero", 1

        options_checked = self.how_many_are_checked()
        if length < options_checked:
            return "ERROR: Deselect at least one option", 1
        if options_checked == 0:
            return "ERROR: Select at least one option", 1

        return self.generate_password(length), 0

    def generate_password(self, length):
        max_quantity = [1, 1, 1, 1]
        available = [1, 1, 1, 1]
        remaining = length - 4
        while remaining > 0:
            add_to = random.randint(0, 3)
            max_quantity[add_to] += 1
            remaining -= 1
        if not self.upper_status:
            available[0] = 0
        if not self.lower_status:
            available[1] = 0
        if not self.nums_status:
            available[2] = 0
        if not self.symbols_status:
            available[3] = 0
        if not self.upper_status:
            for i in range(max_quantity[0]):
                index = 0
                while available[index] == 0:
                    index = random.randint(0, 3)
                max_quantity[index] += 1
            max_quantity[0] = 0
        if not self.lower_status:
            for i in range(max_quantity[1]):
                index = 1
                while available[index] == 0:
                    index = random.randint(0, 3)
                max_quantity[index] += 1
            max_quantity[1] = 0
        if not self.nums_status:
            for i in range(max_quantity[2]):
                index = 2
                while available[index] == 0:
                    index = random.randint(0, 3)
                max_quantity[index] += 1
            max_quantity[2] = 0
        if not self.symbols_status:
            for i in range(max_quantity[3]):
                index = 3
                while available[index] == 0:
                    index = random.randint(0, 3)
                max_quantity[index] += 1
            max_quantity[3] = 0
        upper = generate_upper(max_quantity[0])
        lower = generate_lower(max_quantity[1])
        nums = generate_nums(max_quantity[2])
        symbols = generate_symbols(max_quantity[3])
        ordered_password = (list(upper)) + (list(lower)) + (list(nums)) + (list(symbols))
        random.shuffle(ordered_password)
        password = "".join(ordered_password)
        return password

    def show_badge(self):
        self.Pass_Copied_Label.pack()
        self.Pass_Frame5.after(3000, self.Pass_Copied_Label.pack_forget)

    # Settings Screen
    def copy_switch(self, button):
        if self.copy_to_clipboard_status:
            button.config(image=self.off)
            self.copy_to_clipboard_status = False
        else:
            button.config(image=self.on)
            self.copy_to_clipboard_status = True

    def choose_bg_color(self, widget_c, widget_t):
        code = colorchooser.askcolor(title="Choose Color")[1]
        if code:
            widget_c.config(bg=code)
            widget_t.config(text=code)
            self.bg_color = code

    def choose_fg_color(self, widget_c, widget_t):
        code = colorchooser.askcolor(title="Choose Color")[1]
        if code:
            widget_c.config(bg=code)
            widget_t.config(text=code)
            self.fg_color = code

    def reboot_program(self, new_window):
        message = write_constants()
        if message == "Settings updated successfully":
            global BG, FG, UPPER, LOWER, NUMS, SYMBOLS, COPY_TO_CLIPBOARD
            BG, FG, UPPER, LOWER, NUMS, SYMBOLS, COPY_TO_CLIPBOARD = read_constants()
            new_window.destroy()
            self.pwrd.destroy()
            self.__init__()
        else:
            show_error_window(message)

    def update(self, new_window, upper_input, lower_input, nums_input,
               symbols_input):

        global BG, FG, UPPER, LOWER, NUMS, SYMBOLS, COPY_TO_CLIPBOARD
        bg = self.bg_color
        fg = self.fg_color
        upper = upper_input.get("1.0", "end-1c")
        lower = lower_input.get("1.0", "end-1c")
        nums = nums_input.get("1.0", "end-1c")
        symbols = symbols_input.get("1.0", "end-1c")
        copy_to_clipboard = "True" if self.copy_to_clipboard_status else "False"
        message = write_constants(bg, fg, upper, lower, nums, symbols, copy_to_clipboard)
        if message == "Settings updated successfully":
            BG, FG, UPPER, LOWER, NUMS, SYMBOLS, COPY_TO_CLIPBOARD = read_constants()
            new_window.destroy()
            self.pwrd.destroy()
            self.__init__()
        else:
            show_error_window(message)

    def open_settings(self):

        #   Title Section
        #   Customize
        #       Left Section
        #       Right Section
        #           Right Section BG
        #               Right Section Color Section BG
        #               Right Section Label Section BG
        #               Right Section Button Section BG
        #           Right Section FG
        #               Right Section Color Section FG
        #               Right Section Label Section FG
        #               Right Section Button Section FG
        #   Copy Section
        #   Buttons Section

        settings = Toplevel(self.pwrd)
        settings.config(bg=BG)
        settings.title("Settings")
        settings.geometry("800x470")

        title_section = Frame(settings)
        title_section.config(bg=BG)
        title_section.pack(side='top')
        title = Label(title_section, text="Customize the app!", font=A18B, fg=FG, bg=BG)
        title.pack(pady=20)

        customize = Frame(settings)
        customize.config(bg=BG)
        customize.pack(side='top')

        left_section = Frame(customize)
        left_section.config(bg=BG)
        left_section.pack(side='left')

        right_section = Frame(customize)
        right_section.config(bg=BG)
        right_section.pack(side='right')

        right_section_bg = Frame(right_section)
        right_section_bg.config(bg=BG)
        right_section_bg.pack(side='top')

        right_section_color_section_bg = Frame(right_section_bg)
        right_section_color_section_bg.config(bg=BG)
        right_section_color_section_bg.pack(side='left')

        right_section_label_section_bg = Frame(right_section_bg)
        right_section_label_section_bg.config(bg=BG)
        right_section_label_section_bg.pack(side='left')

        right_section_button_section_bg = Frame(right_section_bg)
        right_section_button_section_bg.config(bg=BG)
        right_section_button_section_bg.pack(side='right')

        right_section_fg = Frame(right_section)
        right_section_fg.config(bg=BG)
        right_section_fg.pack(side='top')

        right_section_color_section_fg = Frame(right_section_fg)
        right_section_color_section_fg.config(bg=BG)
        right_section_color_section_fg.pack(side='left')

        right_section_label_section_fg = Frame(right_section_fg)
        right_section_label_section_fg.config(bg=BG)
        right_section_label_section_fg.pack(side='left')

        right_section_button_section_fg = Frame(right_section_fg)
        right_section_button_section_fg.config(bg=BG)
        right_section_button_section_fg.pack(side='right')

        copy_section = Frame(settings)
        copy_section.config(bg=BG)
        copy_section.pack(side='top')

        buttons_section = Frame(settings)
        buttons_section.config(bg=BG)
        buttons_section.pack(side='top')

        background_label = Label(left_section, text="Background Color", font=A14, bg=BG, fg=FG)
        background_label.pack(side="top", padx=15, pady=8)
        color_bg = Label(right_section_color_section_bg, text="Preview", bg=BG, fg=FG, width=17, height=1, font=A14)
        color_bg.pack(side="top", padx=(15, 6), pady=8)
        background_text = Label(right_section_label_section_bg, font=C14, text=BG, width=16, height=1)
        background_text.pack(side="top", padx=7, pady=8)
        button_bg = Button(right_section_button_section_bg, width=16, height=1, text="Select", font=A12B, bg="skyblue",
                           activebackground=FG, activeforeground=BG,
                           command=lambda: self.choose_bg_color(color_bg, background_text))
        button_bg.pack(side="top", padx=6, pady=8)

        foreground_label = Label(left_section, text="Text Color", font=A14, bg=BG, fg=FG)
        foreground_label.pack(side="top", padx=15, pady=8)
        color_fg = Label(right_section_color_section_fg, text="Preview", bg=FG, fg=BG, width=17, height=1, font=A14)
        color_fg.pack(side="top", padx=(15, 6), pady=8)
        foreground_text = Label(right_section_label_section_fg, font=C14, text=FG, width=16, height=1)
        foreground_text.pack(side="top", padx=7, pady=8)
        button_fg = Button(right_section_button_section_fg, width=16, height=1, text="Select", font=A12B, bg="skyblue",
                           activebackground=FG, activeforeground=BG,
                           command=lambda: self.choose_fg_color(color_fg, foreground_text))
        button_fg.pack(side="top", padx=6, pady=8)

        upper_label = Label(left_section, text="Uppercase Letters", font=A14, bg=BG, fg=FG)
        upper_label.pack(side="top", padx=15, pady=8)
        upper_text = Text(right_section, font=C14, width=55, height=1)
        upper_text.pack(side="top", padx=15, pady=8)
        upper_text.insert(END, UPPER)

        lower_label = Label(left_section, text="Lowercase Letters", font=A14, bg=BG, fg=FG)
        lower_label.pack(side="top", padx=15, pady=8)
        lower_text = Text(right_section, font=C14, width=55, height=1)
        lower_text.pack(side="top", padx=15, pady=8)
        lower_text.insert(END, LOWER)

        nums_label = Label(left_section, text="Numbers", font=A14, bg=BG, fg=FG)
        nums_label.pack(side="top", padx=15, pady=8)
        nums_text = Text(right_section, font=C14, width=55, height=1)
        nums_text.pack(side="top", padx=15, pady=8)
        nums_text.insert(END, NUMS)

        symbols_label = Label(left_section, text="Symbols", font=A14, bg=BG, fg=FG)
        symbols_label.pack(side="top", padx=15, pady=8)
        symbols_text = Text(right_section, font=C14, width=55, height=1)
        symbols_text.pack(side="top", padx=15, pady=8)
        symbols_text.insert(END, SYMBOLS)

        clipboard_label = Label(copy_section, text="Automatically copy to clipboard", font=A14, bg=BG, fg=FG)
        clipboard_label.pack(side="left", padx=25, pady=8)
        clipboard_button = Button(copy_section, image=self.on if self.copy_to_clipboard_status else self.off, bd=0,
                                  bg=BG, activebackground=BG,
                                  command=lambda: self.copy_switch(clipboard_button))
        clipboard_button.pack(side='right', padx=25, pady=8)

        reset_button = Button(buttons_section, text="Reset", font=A14, width=10, bg="skyblue", activebackground=FG,
                              activeforeground=BG, command=lambda: self.reboot_program(settings))

        reset_button.pack(side="left", padx=15, pady=8)
        update_button = Button(buttons_section, text="Update", font=A14, width=10, bg="skyblue", activebackground=FG,
                               activeforeground=BG,
                               command=lambda: self.update(settings, upper_text,
                                                           lower_text, nums_text, symbols_text))
        update_button.pack(side="left", padx=15, pady=8)
        settings.grab_set()


App = PasswordGeneratorApp()