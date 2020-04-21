from tkinter import *
from tkinter import filedialog as fd

from tkinter import *
from tkinter import filedialog as fd

def insertText():                      #позволяет выбрать(открыть) документ
    file_name = fd.askopenfilename()
    f = open(file_name)
    global text
    text = f.read()
    f.close()
    
   
def enterText():                       #позволяет написать текст вручную
    
    def getText():
        global text
        text = txt.get('1.0', 'end-1c')
        
    root = Tk()
    
    txt = Text(root,height=25,width=60,font='Arial 14')
    txt.pack()

    b_get = Button(root, text='Загрузить', command = getText)
    b_get.pack(side=LEFT)
    b_dstr = Button(root, text='Завершить', command = root.destroy)
    b_dstr.pack(side=RIGHT)
    
    root.mainloop()


main_root = Tk()                       #главное диалоговое окно

label = Label(width=30, height=15, text='Откройте текстовый документ или \nнапишите текст вручную', font='Arial 12 bold', fg='dark green')
label.grid(row=0, column=0, columnspan=2)

b1 = Button(main_root, text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(main_root, text="Создать", command=enterText)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(main_root, text="Начать", command=main_root.destroy)
b3.grid(row=1,column=1, sticky=E)
 
main_root.mainloop()



from natasha import (
    NamesExtractor,
    AddressExtractor,
    DatesExtractor,
    LocationExtractor
)
from natasha.markup import show_markup, show_json

Name = NamesExtractor()
Add = AddressExtractor()
Dat = DatesExtractor()
Loc = LocationExtractor()

extractors = [
    Name,
    Add,
    Dat,
    Loc
]

spans = []
facts = []

for extractor in extractors:            #выделение сущностей в тексте
    matches = extractor(text)
    spans.extend(_.span for _ in matches)
    facts.extend(_.fact.as_json for _ in matches)
show_markup(text,spans)


#names extraction
Namespans = []
Namefacts = []
Name_matches = Name(text)
Namespans.extend(_.span for _ in Name_matches)
Namefacts.extend(_.fact.as_json for _ in Name_matches)

print('\n\n Names:\n')
show_json(Namefacts)

#addresses&locations extraction
Addspans = []
Addfacts = []
Locspans = []
Locfacts = []
Add_matches = Add(text)
Addspans.extend(_.span for _ in Add_matches)
Addfacts.extend(_.fact.as_json for _ in Add_matches)
Loc_matches = Loc(text)
Locspans.extend(_.span for _ in Loc_matches)
Locfacts.extend(_.fact.as_json for _ in Loc_matches)

print('\n\n Addresses:\n')
show_json(Addfacts)
show_json(Locfacts)

#dates extraction
Datspans = []
Datfacts = []
Dat_matches = Dat(text)
Datspans.extend(_.span for _ in Dat_matches)
Datfacts.extend(_.fact.as_json for _ in Dat_matches)

print('\n\n Dates:\n')
show_json(Datfacts)
