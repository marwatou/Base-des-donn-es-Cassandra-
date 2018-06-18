import csv
from tkinter import filedialog, Tk, Label, Button
import itertools
import shimpparser

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.geometry = '600x400'
        label = Label(self, text="SHIMP Database", foreground="#892222", background="#FFAAAA", padx="300",
                      pady="100")
        label.grid()
        button = Button(self, text="Choose TXT file", command=self.__choose__)
        button.grid()

    def __choose__(self):
        filename = filedialog.askopenfilename(initialdir="~/PycharmProjects/untitled/ascii.txt",
                                              title="Choose TXT file")
        self.__load_data(filename)



    def __load_data(self, filename):
#      lecture de la fichier et ouvrir le fichier qui a le nom dans la varibale filename
       # cr = csv.reader(open(filename, 'r'), delimiter=';')
#lecture ligne par ligne
        #row1 = next(cr)
        #row1 = next(cr)
 #affiher la deuxiéme ligne
        #print('deuxieme ligne analysee: ', row1)
#afficher les valeursde la deuxiéme ligne correspond a la premiere colonne ,la troisieme colonne ,la quatriéme colonne
       # print(row1[0], row1[3], row1[4])
# créé une instance du ShimpParserme)
        shimp_parser = shimpparser.ShimpParser()
#analyser le fichier selectionné par l'utilusateur et les résultats ira dans dans la variable shimp_data
        shimp_data = shimp_parser.parse(filename)




main_window = MainWindow()

main_window.mainloop()