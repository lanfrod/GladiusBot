from PIL import Image, ImageDraw


def board(boa):
    width, height = 920, 920
    im = Image.new("RGB", (width, height))
    size = 300
    drawer = ImageDraw.Draw(im)
    h, w = 0, 0
    drawer.rectangle(((w, h), (width, height)), '#FFFFFF')
    for i in range(2):
        drawer.line(((w + size, 0), (w + size, height)), '#000000', width=10)
        drawer.line(((0, h + size), (width, h + size)), '#000000', width=10)
        w += size
        h += size
    boa = boa.split("/")
    size = 305
    count = 0
    for i in boa:
        count += 1
        coh = count // 4 + 1
        if count == 7:
            coh += 1
        cow = count % 3
        if cow == 0:
            cow = 3
        if i == "x":
            drawer.line((((cow - 1) * (size + 5), (coh - 1) * size),
                         ((cow) * (size - 5), coh * size - 5)), 'black', width=10)
            drawer.line((((cow) * (size - 5), (coh - 1) * size),
                         ((cow - 1) * (size + 5), coh * size - 15)), 'black', width=10)
        elif i == "o":
            drawer.ellipse((((cow - 1) * (size), (coh - 1) * (size - 2)),
                        ((cow) * (size) - 10, coh * (size - 8))), 'white', outline="black", width=15)

    im.save('img/res.png')


#board("?/?/?/?/?/?/?/?/?")