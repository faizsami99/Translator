import tkinter
from tkinter.ttk import Combobox
import tkinter.messagebox as tmg
from translate import Translator
########  language
Lang = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

#######Fucntions
def Click():
    ll = Lang[languges.get()]
    text = var1.get()
    translator = Translator(to_lang=ll)
    translation = translator.translate(text)
    # print (translation)
    var2.set(translation)

def Reset():
    var1.set("")
    var2.set("")

def want_exit():
    ext = tmg.askyesno("Notification", "are you sure?")
    if ext == True:
        quit()
    


main_frame = tkinter.Tk()
main_frame.geometry("550x400")
main_frame.resizable(False, False)
main_frame.title("Translator")
main_frame.config(background="light green")

########### Entry Boxes

var1 = tkinter.StringVar()
entry1 = tkinter.Entry(main_frame, textvariable=var1, font="times 16 bold", width=30) 
entry1.place(x=170, y=50)

var2 = tkinter.StringVar()
entry2 = tkinter.Entry(main_frame, textvariable=var2, font="times 16 bold", width=30) 
entry2.place(x=170, y=110)

########Labels

Enter_value = tkinter.Label(main_frame, text="Enter Text:", bg="light green", font="lucida 16 bold italic")
Enter_value.place(x=20, y=50)

Translated_value = tkinter.Label(main_frame, text="Translated:", bg="light green", font="lucida 16 bold italic")
Translated_value.place(x=20, y=110)

############################Buttons

click_button = tkinter.Button(main_frame,width=5, text="Click",font="lucida 15 italic", command=Click, bd=2, activebackground="red")
click_button.place(x=80, y=200)
# click_button.bind("<Enter>", "on_enterentry")
# click_button.bind("<Leave>", "on_leaveentry")

Reset_button = tkinter.Button(main_frame,width=5, text="Reset",font="lucida 15 italic", command=Reset, bd=2,activebackground="red")
Reset_button.place(x=220, y=200)

Exit_button = tkinter.Button(main_frame,width=5, text="Exit",font="lucida 15 italic", command=want_exit, bd=2,activebackground="red")
Exit_button.place(x=360, y=200)

#####Scroll bar
languges = tkinter.StringVar()
select_lang = Combobox(main_frame, textvariable=languges, state="readonly")
select_lang['values'] = [i for i in Lang.keys()]
select_lang.current(37)
select_lang.place(x = 0, y=0)

main_frame.mainloop()