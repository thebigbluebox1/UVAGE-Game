import uvage
camera = uvage.Camera(800,800)

a = uvage.from_image(400, 400, "C:\\Users\\rchha\\Downloads\\image000000.jpg")
camera.draw(a)

def tick():
    camera.display()


ticks_per_second = 60
uvage.timer_loop(ticks_per_second, tick)