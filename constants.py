def read_constants():
    try:
        file = open("assets/constants.txt", "r")
        file.readline()
        bg = file.readline().strip()
        fg = file.readline().strip()
        upper = file.readline().strip()
        lower = file.readline().strip()
        nums = file.readline().strip()
        symbols = file.readline().strip()
        copy_to_clipboard = file.readline().strip()
        file.close()
    except:
        bg = "#191970"
        fg = "#ffffff"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        nums = "1234567890"
        symbols = "-?@$€*/&+£%"
        copy_to_clipboard = True
    finally:
        return bg, fg, upper, lower, nums, symbols, copy_to_clipboard


def write_constants(bg="#191970", fg="#ffffff", upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ", lower="abcdefghijklmnopqrstuvwxyz",
                    nums="1234567890", symbols="!@#$%^&*()-+", copy_to_clipboard="True"):
    text = "DO NOT CHANGE OR DELETE THIS FILE"
    try:
        file = open("assets/constants.txt", "w")
        file.write(text + '\n' +
            bg + '\n' + fg + '\n' + upper + '\n' + lower + '\n' + nums + '\n' + symbols + '\n' + copy_to_clipboard)
        file.close()
        message = "Settings updated successfully"
    except:
        message = "Unable to update settings"
    finally:
        return message



BG, FG, UPPER, LOWER, NUMS, SYMBOLS, COPY_TO_CLIPBOARD = read_constants()

A12B = ("Arial", 12, "bold")
A14B = ("Arial", 14, "bold")
A18B = ("Arial", 18, "bold")
A18 = ("Arial", 18)
A14 = ("Arial", 14)
C18 = ("Consolas", 18)
C14 = ("Consolas", 14)
