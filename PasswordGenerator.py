import string
import random
import pyperclip

class PasswordGenerator:
    def __init__(self):
        self.alphabet_string_lowercase = string.ascii_lowercase
        self.alphabet_string_uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.simbols = string.punctuation

    def generate_password(self, label):
        junction = self.alphabet_string_lowercase + self.alphabet_string_uppercase + self.numbers + self.simbols
        pasword_length = 16
        password = ''.join(random.sample(junction, pasword_length))

        label['text'] = password
    
    def copy_password(self, label):
        pyperclip.copy(label['text'])
