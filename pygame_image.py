import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#surfaceクラスのインスタンス
    bg_img_flipped = pg.transform.flip(bg_img, True, False)
    koukaton_image = pg.image.load("fig/3.png")
    koukaton_image = pg.transform.flip(koukaton_image, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr%3200)
        screen.blit(bg_img,  [x, 0])
        screen.blit(bg_img_flipped, [x+1600, 0])
        screen.blit(bg_img,  [x+3200, 0])
        screen.blit(bg_img_flipped, [x+4800, 0])
        screen.blit(koukaton_image, [300, 200])  # screen Surfaceにこうかとん画像Surfaceを貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)
        
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()