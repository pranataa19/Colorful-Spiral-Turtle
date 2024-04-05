import turtle as tur
import colorsys as cs

tur.setup(800, 800)
tur.speed(0)
tur.width(2)
tur.bgcolor('black')
tur.tracer(100)

# Mengatur jumlah iterasi untuk menghasilkan gambar yang lebih kompleks
iterations = 100

for j in range(iterations):
    for i in range(30):
        hue = (i / 30 + j / iterations) % 1
        saturation = 1 - (j / iterations) * 0.6
        value = 1
        tur.color(cs.hsv_to_rgb(hue, saturation, value))

        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(2, 54)

tur.hideturtle()
tur.update()
tur.done()
