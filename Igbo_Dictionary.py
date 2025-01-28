import tkinter as tk
from tkinter import StringVar

window = tk.Tk()
window.geometry("500x500")
window.title("The General Dictionary")

igbo_dictionary = {
    'aka': "hand",
    'anya': "eye",
    'azu': "back",
    'kwusi': "stop",
    'nwa': "child",
    'bia': "come",
    'gawa': "go",
    'imi': "nose",
    'nti': "ear",
    'ukwu': "leg",
    'isi': "head",
    'onu': "mouth",
    'eze': "teeth",
    'ire': "tongue",
    'ngwu': "shoulder",
    'otu': "one",
    'abuo': "two",
    'ato': "three",
    'ano': "four",
    'ise': "five",
    'asato': "seven",
}

yoruba_dictionary = {
    'owo': "hand",
    'oju': "eye",
    'ati': "ear",
    'ori': "head",
    'ajika': "shoulder",
    'wa': "come",
    'gba': "take",
    'ese': "leg",
    'enu': "mouth",
    'sara': "run",
    'jada': "out",
    'odabor': "goodbye",
    'maji': "two",
    'metar': "three",
    'shibi': "spoon",
    'abour': "plate",
    'omi': "water",
    'oko': "tree",
    'ojen': "food",
    'aja': "dog",
}

nupe_dictionary = {
    'dzuko': "market",
    'be': "come",
    'emi': "home",
    'ede': "cloth",
    'ebi': "knife",
    'esa': "chair",
    'bichi': "leg",
    'soku': "broom",
    'layam': "give me",
    'ewugi': "spoon",
    'kubelazi': "good morning",
    'kubegidi': "good afternoon",
    'yeshi': "night",
    'azo': "beans",
    'asibiti': "hospital",
    'pati': "mountain",
    'misu': "mouth",
    'egwalo': "right hand",
    'eyi': "guinea corn",
    'kubelozu': "good evening",
}

french_dictionary = {
    'bonjour': "Good Morning",
    'merci': "Thank you",
    'oui': "Yes",
    'non': "No",
    'excuse-moi': "Excuse me",
    'pardon': "Sorry",
    'comment': "How",
    'pourquoi': "Why",
    'quand': "When",
    'qui': "Who",
    'je': "I",
    'tu': "You",
    'il': "He",
    'elle': "She",
    'nous': "We",
    'et': "And",
    'bon': "Good",
    'chaud': "Hot",
    'froid': "Cold",
    'bonsoir': "Good evening",
}

spanish_dictionary = {
    'hola': "hello",
    'buenas dias': "good morning",
    'buenas tardes': "good afternoon",
    'buenas noches': "good evening",
    'me llamo': "my name is",
    'como estas': "how are you",
    'soy': "I am",
    'estoy bien': "I'm fine",
    'izquierda': "left",
    'derecha': "right",
    'adelante': "forward",
    'atras': "backward",
    'uno': "one",
    'dos': "two",
    'tres': "three",
    'cuatro': "four",
    'pollo': "chicken",
    'leche': "milk",
    'yogur': "yogurt",
    'pan': "bread",
}

current_language = None


def translate_word(word, language):
    word = word.lower()
    dictionary_map = {
        "igbo": igbo_dictionary,
        "yoruba": yoruba_dictionary,
        "nupe": nupe_dictionary,
        "french": french_dictionary,
        "spanish": spanish_dictionary,
    }

    if language not in dictionary_map:
        translation.set("Invalid Language")
        return

    dictionary = dictionary_map[language]

    if word in dictionary:
        translation.set(dictionary[word])
    else:
        translation.set("Word not found")


def handle_navigate_forward(target_language):
    global current_language
    current_language = target_language
    button_frame.pack_forget()
    sub_heading.pack_forget()
    translation_frame.pack()
    word_entry.pack()
    translation_label.pack()
    translate_button.pack()
    back_button.pack()


def handle_navigate_back():
    translation.set("")
    word_entry.delete(0, tk.END)
    translation_frame.pack_forget()
    pack_first_page()


heading = tk.Label(window, text="Welcome to the Multi-language Dictionary", font=("Times New Roman", 20), pady=20)
sub_heading = tk.Label(window, text="Select a language to translate", font=("Times New Roman", 15), pady=10)

button_frame = tk.Frame(window)
yoruba_button = tk.Button(button_frame, text="Yoruba", width=20, pady=5,command=lambda: handle_navigate_forward("yoruba"))
igbo_button = tk.Button(button_frame, text="Igbo", width=20, pady=5, command=lambda: handle_navigate_forward("igbo"))
french_button = tk.Button(button_frame, text="French", width=20, pady=5,command=lambda: handle_navigate_forward("french"))
nupe_button = tk.Button(button_frame, text="Nupe", width=20, pady=5, command=lambda: handle_navigate_forward("nupe"))
spanish_button = tk.Button(button_frame, text="Spanish", width=20, pady=5,
                           command=lambda: handle_navigate_forward("spanish"))


def pack_first_page():
    button_frame.pack()
    yoruba_button.pack()
    igbo_button.pack()
    french_button.pack()
    nupe_button.pack()
    spanish_button.pack()


translation = StringVar()
translation_frame = tk.Frame(window)
word_entry = tk.Entry(translation_frame, width=30, font=("Arial", 14))
translate_button = tk.Button(translation_frame, text="Translate", width=20,command=lambda: translate_word(word_entry.get(), current_language))
translation_label = tk.Label(translation_frame, textvariable=translation, font=("Arial", 14), pady=10)
back_button = tk.Button(translation_frame, text="Back", width=20, command=handle_navigate_back)

heading.pack()
sub_heading.pack()
pack_first_page()

window.mainloop()

