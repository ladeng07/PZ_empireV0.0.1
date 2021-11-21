import pygame
from pygame.locals import *
import time


pygame.init()

menu_bg='pz.jpg'
start_bg='start_bg.jpg'
text_box='text_box.png'
print(pygame.display.list_modes())
start_menu=1
start_game=0
label=[]
size = (800,600)



screen=pygame.display.set_mode(size,RESIZABLE)
now=pygame.Surface(size)
pygame.display.set_caption('PZ帝国')

background=pygame.image.load(menu_bg).convert()
start_bg=pygame.image.load(start_bg).convert()
text_box=pygame.image.load(text_box).convert()
background=pygame.transform.smoothscale(background,size)
now.blit(background,(0,0))

print(pygame.font.get_fonts())
font=pygame.font.SysFont('华文中宋',16)
line_height=font.get_linesize()
position=0
screen.blit(now,(0,0))


def textbox(target,size):
    global text_box,label
    y=size[1]//4
    tbox=pygame.transform.smoothscale(text_box,(size[0],y))
    target.blit(tbox,(0,size[1]-y))
    print(target.get_rect())
    
    label.append((0,size[1]-y,size[0],y))
    print(label)


def textlabel(text,position,disp,size,num,line):
    f=pygame.font.SysFont('华文中宋',16)
    for i in range(num,len(text)):
        if f.size(text[:i])[0] > size[0]:
            print(f.size(text[:i])[0],size[0])
            break
        screen.blit(disp,(0,0))
        screen.blit(f.render(text[:i],True,(0,0,0)),position)
        pygame.time.wait(180) 
        pygame.display.update()
    if i <len(text)-1:
        line+=1
        print(f.size(text[i:]))
        now.blit(screen,(0,0))
        position=position[0],position[1]+f.get_linesize()
        textlabel(text[i:],position,now,size,0,line)
    


def start_g(background,size):
    global start_game
    temp=pygame.Surface((background.get_width(),background.get_height()))
    bd=pygame.transform.smoothscale(background,size)
    temp.blit(bd,(0,0))
    textbox(temp,size)
    screen.blit(temp,(0,0))
    now.blit(screen,(0,0))
    start_game=1
    
    
#textlabel('hhhhhhh',(100,100),0,0,0)
while 1:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == QUIT:
            exit()

        if event.type == VIDEORESIZE:
            size=event.size
            #print(size)
            screen=pygame.display.set_mode(size,RESIZABLE)
            now=pygame.transform.smoothscale(now,size)
            bd=pygame.transform.smoothscale(now,size)
            screen.blit(bd,(0,0))
            now.blit(screen,(0,0))

        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        position+=line_height

        if position > size[1]:
            if start_game:
                position=0
                start_g(start_bg,size)
            else:
                position=0
                screen.blit(pygame.transform.smoothscale(now,size),(0,0))
                now.blit(screen,(0,0))

        if event.type == MOUSEBUTTONUP:
            mouse_pos=pygame.mouse.get_pos()
            if event.button == 1 and start_game==0 and mouse_pos[0] >0 and mouse_pos[1] > 0:
                start_g(start_bg,size)
                textlabel('我嗄嘎存在于疼痛要求非常有手感一飞冲天阿姨擦防晒惩罚她衣服vv动人心弦',(label[0][0]+label[0][2]//10,label[0][1]+label[0][3]//5),now,(200,100),0,0)
                

            
        




    pygame.display.update()
