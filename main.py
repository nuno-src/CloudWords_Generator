from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image


def o1():

    text = open('text.txt', 'r').read()

    wc = WordCloud(stopwords=STOPWORDS).generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()



def o2():

    print("NOTE: ")

    text = open('text.txt', 'r').read()

    img = np.array(PIL.Image.open(""))

    #colormap = ImageColorGenerator(img)

    wc = WordCloud(stopwords=STOPWORDS,
                   mask=img,
                   background_color="black",
                   contour_color="white",
                   contour_with=3,
                   min_font_size=3,
                   max_words=400).generate(text)

    #wc.recolor(color_func=colormap)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()



opc = ""
while opc != "exit":

    print("\n==============================================================")
    print("                      MENU PRINCIPAL")
    print("==============================================================")
    print("[1] - Gerar CloudWord")
    print("[2] - Gerar CloudWord com imagem")
    print("[exit] - Sair")
    print("==============================================================")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        o1()
    elif opc == "000":
        exit()
    elif opc == "2":
        o2()
    elif opc == "exit":
        print("\nA sair...")
    else:
        print("\nERRO! - Opção inválida")
