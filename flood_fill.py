import matplotlib.pyplot as plt

def flood_fill(img, x, y):

    #podminka navratu
    if x < 0 or x >= img.shape[0] or y < 0 or y >= img.shape[0]: # souradnice 0,0 je posledni, resp prvni kterou se zacina
        return img
    # kontrola, jestli v celem obrazci neni volna seda, nebo whatever

    #abychom se nezacyklili
    if img[x, y] == 2 or img[x, y] == 0:
        return img
    img[x, y] = 2

    plt.imshow(img, cmap="gray") # okno obrazku
    plt.show(block=False) #blokace vypisu
    plt.pause(0.05) # at vidime zmenu, tak pauza 5ms
    plt.clf()

    #ulozeni do img a rekurze
    img = flood_fill(img, x+1, y) # doprava
    img = flood_fill(img, x, y+1) # nahoru
    img = flood_fill(img, x - 1, y) # doleva
    img = flood_fill(img, x, y - 1) # dolu

    return img


def main():
    # img = plt.imread("files/img0.png")[:, :, 0] #nacteni obrazku
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    # zobrazeni
    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
