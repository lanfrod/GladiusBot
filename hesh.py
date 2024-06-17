from PIL import Image, ImageDraw


def board(boa):
    width, height = 920, 920
    im = Image.new("RGB", (width, height))
    size = 300
    drawer = ImageDraw.Draw(im)
    h, w = 0, 0
    drawer.rectangle(((w, h), (width, height)), '#FFFFFF')
    for i in range(2):
        #w = 0
        #drawer.rectangle(((0, h), (lines, lines)), '#000000')
        drawer.line(((w + size, 0), (w + size, height)), '#000000', width=10)
        drawer.line(((0, h + size), (width, h + size)), '#000000', width=10)
        #drawer.rectangle(((w, 0), (lines, lines)), "#FFFFFF")
        w += size
        h += size
    boa = boa.split("/")
    size = 305
    count = 1



    for i in boa:
        print(i)
        #count += 1
        coh = count // 4 + 1
        if count == 7:
            coh += 1
        cow = count % 3
        if cow == 0:
            cow = 3
        if i == "x":
            drawer.line((((cow - 1) * (size + 5), (coh - 1) * size), ((cow) * (size - 5), coh * size - 5)), '#000000', width=10)
            drawer.line((((cow) * (size - 5), (coh - 1) * size), ((cow - 1) * (size + 5), coh * size - 15)), '#000000', width=10)


    im.save('img/res.png')

board("?/?/?/?/?/?/?/?/?")