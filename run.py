# %%
import tkinter as tk


def translate(text, lang_dict=None):
    if not lang_dict:
        lang_dict = define_lang(text)
    result = ''
    for letter in text:
        tr_letter = lang_dict.get(letter, letter)
        result += tr_letter
    return result


def define_lang(text):
    """
    Returns appropriate dict for translation
    """
    text_set = set(text)
    eng_len = len(text_set.intersection(engrus.keys()))
    rus_len = len(text_set.intersection(ruseng.keys()))
    result = engrus if eng_len > rus_len else ruseng
    return result


def check_translate():
    global old_text
    text = input_box.get('1.0', tk.END)
    if text != old_text:
        translation = translate(text)
        output_box.delete('1.0', tk.END)
        output_box.insert('1.0', translation)
        old_text = text
    window.after(1000, check_translate)


def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")

    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

# -------- define dictionaries ---------------------------

eng = "`~@#$%^&qwertyuiop[{}]|asdfghjkl;:'\"zxcvbnm,<.>/?"
rus = "ёЁ\"№;%:?йцукенгшщзхХъЪ/фывапролджЖэЭячсмитьбБюЮ.,"
engrus = {key: val for key, val in zip(eng, rus)}
ruseng = {key: val for key, val in zip(rus, eng)}
engrus.update({key.upper(): val.upper() for key, val in engrus.items()
              if key != key.upper()})
ruseng.update({key.upper(): val.upper() for key, val in ruseng.items()
               if key != key.upper()})

# --------- tkinter -----------------------------------

WIDTH = 700
HEIGHT = 500
window = tk.Tk()
window.title('Text converter')
window.geometry(f'{WIDTH}x{HEIGHT}')
window.bind_all("<Key>", _onKeyRelease, "+")
input_box = tk.Text(height=10, font=16)
output_box = tk.Text(font=16)

input_box.pack()
output_box.pack()
old_text = ''
check_translate()
window.mainloop()
