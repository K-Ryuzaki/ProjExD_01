import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton = pg.image.load("ex01/fig/3.png")
    #こうかとんの画像読み込み
    koukaton = pg.transform.flip(koukaton, True, False)
    #こうかとん反転
    kaiten= pg.transform.rotozoom(koukaton,0,1.0)
    #こうかとん回転
    kkflip=[koukaton,kaiten]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if 10<=tmr%100<20 or 30<=tmr%100<40 or 50<=tmr%100<60 or 70<=tmr%100<80 or 90<=tmr%100<100:  
            kaiten= pg.transform.rotozoom(koukaton,10-tmr%10,1.0)
        else:
            kaiten = pg.transform.rotozoom(koukaton,tmr%10,1.0)
        screen.blit(bg_img, [-tmr,0])
        if tmr%1600 == 0:
            hanten= pg.transform.flip(bg_img, True, False)
        screen.blit(hanten, [(1600-tmr),0])
        screen.blit(bg_img, [3200-tmr,0])
        #こうかとんが羽ばたく
        screen.blit(kaiten,[300,200])
        pg.display.update()
        if tmr == 3200:
            tmr = 0
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()