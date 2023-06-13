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
    kaiten= pg.transform.rotozoom(koukaton,10,1.0)
    #こうかとん回転
    kkflip=[koukaton,kaiten]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [(0-tmr%1600),0])
        #screen.blit(bg_img, [(1600-tmr%1600),0])
        #こうかとんが羽ばたく
        screen.blit(kkflip[tmr%2],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()