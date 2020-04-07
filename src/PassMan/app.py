import hashlib
from base64 import a85encode
import toga
from toga.style.pack import *

class PassMan(toga.App):
    def startup(self):
        main_box = toga.Box()
        w_box = toga.Box()
        m_box = toga.Box()
        f_box = toga.Box()

        w_input = toga.TextInput()
        m_input = toga.PasswordInput()
        f_input = toga.TextInput(readonly=True)

        w_label = toga.Label('Website:', style=Pack(text_align=CENTER))
        m_label = toga.Label('Master Password:', style=Pack(text_align=CENTER))
        f_label = toga.Label('Your Password:', style=Pack(text_align=CENTER))

        def genPasswd(widget):
            website = w_input.value.encode()
            masterpass = m_input.value.encode()

            salted = website + masterpass
            hash = hashlib.sha256(salted).digest()
            password = a85encode(hash).decode()[:15]

            f_input.value = password

        button = toga.Button('Generate Password', on_press=genPasswd)

        w_box.add(w_label)
        w_box.add(w_input)

        m_box.add(m_label)
        m_box.add(m_input)

        f_box.add(f_label)
        f_box.add(f_input)

        main_box.add(w_box)
        main_box.add(m_box)
        main_box.add(f_box)
        main_box.add(button)

        main_box.style.update(direction=COLUMN, padding_top=10)
        w_box.style.update(direction=ROW, padding=5, padding_bottom=50)
        m_box.style.update(direction=ROW, padding=5, padding_bottom=50)
        f_box.style.update(direction=ROW, padding=5)

        w_input.style.update(flex=1, padding_right=10)
        m_input.style.update(flex=1, padding_right=10)
        f_input.style.update(flex=1, padding_right=10)
        w_label.style.update(flex=1)
        m_label.style.update(flex=1)
        f_label.style.update(flex=1)

        button.style.update(padding=15, flex=1)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(446, 308))
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return PassMan()