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
    koukaton_rect = koukaton_image.get_rect()
    koukaton_rect.center = 300, 200


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        #print(key_lst[pg.K_UP])
        #print(key_lst[pg.K_DOWN])
        #print(key_lst[pg.K_RIGHT])
        #print(key_lst[pg.K_LEFT])

        if key_lst[pg.K_UP]:
            koukaton_rect.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            koukaton_rect.move_ip((0, 100))
        if key_lst[pg.K_RIGHT]:
            koukaton_rect.move_ip((1, 0))
        if key_lst[pg.K_LEFT]:
            koukaton_rect.move_ip((-1, 0))

        x = -(tmr%3200)
        screen.blit(bg_img,  [x, 0])
        screen.blit(bg_img_flipped, [x+1600, 0])
        screen.blit(bg_img,  [x+3200, 0])
        screen.blit(bg_img_flipped, [x+4800, 0])
        #screen.blit(koukaton_image, [300, 200])  # screen Surfaceにこうかとん画像Surfaceを貼り付ける
        screen.blit(koukaton_image, koukaton_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)
        
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()