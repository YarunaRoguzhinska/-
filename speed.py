from pygame import*
window= display.set_mode((700,500))
display.set_caption("доганялки")
background = transform.scale(image.load("kichen.jpg"),(700,500))


clock=time.Clock()
FPS=60

x1=100
y1=300

x2=300
y2=300

sprite1 = transform.scale(image.load("knife.png"),(100,100))
sprite2 = transform.scale(image.load("cheese.png"),(100,100))

run = True
while run:

    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x2 > 5:
        x2 -=15
    if keys_pressed[K_RIGHT] and x2 < 595:
        x2 +=15
    if keys_pressed[K_UP] and y2 > 5:
        y2 -=15
    if keys_pressed[K_DOWN] and y2 < 395:
        y2 +=15
    
    
    if keys_pressed[K_a] and x1 > 5:
        x1 -=15
    if keys_pressed[K_d] and x1 < 595:
        x1 +=15
    if keys_pressed[K_w] and y1 > 5:
        y1 -=15
    if keys_pressed[K_s] and y1 < 395:
        y1 +=15


    display.update()
    clock.tick(FPS)