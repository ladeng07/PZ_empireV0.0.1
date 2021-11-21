from function import Button
import pygame
from pygame.locals import *
pygame.init()

def get_study_list(size,screen,button,pic):
    w,h=size
    lw,lh=w//6,h//12
    return [Button(button,(lw,lh),((w-int(w//1.4)+lw//14,(h-int(h//1.4))//2+lh//6)),screen,\
                   ['练习  导学案','智商+2  情商+1','记忆力+2  行动力-10'],c=0,power=(2,1,2,0,0,-10),ima=pic[0]),
            Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw,(h-int(h//1.4))//2+lh//6)),screen,\
                   ['练习  语文测评','情商+3  记忆力+3','想象力+2  行动力-15'],c=0,power=(0,3,3,2,0,-15),ima=pic[0]),
            Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*2,(h-int(h//1.4))//2+lh//6)),screen,\
                   ['练习  数学活页','智商+5  情商+1','想象力+4  行动力-20'],c=0,power=(5,1,0,4,0,-20),ima=pic[0])]

def get_room_list(size,screen,button,pic):
    w,h=size
    lw,lh=w//6,h//12
    return [Button(button,(lw,lh),((w-int(w//1.4)+lw//14,(h-int(h//1.4))//2+lh//6)),screen,\
                   ['娱乐 睡觉','智商+5  情商+3','记忆力+10  行动力+50'],c=0,power=(5,3,10,0,0,50),ima=pic[0])]
