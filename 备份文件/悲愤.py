import pygame
from pygame.locals import *
import time


pygame.init()

menu_bg='pz.jpg'
start_bg='start_bg.jpg'
text_box='text_box.png'
top_label='top_label.png'
study_button='study_button.png'
start_button='start_button.png'
start_menu=1
start_game=0
rd=0
l=[]
FINISH =USEREVENT + 1
finish = pygame.event.Event(FINISH,message='g')
study=500
charm=500
power=500
rod=1
w,h=size = (800,600)



screen=pygame.display.set_mode(size,RESIZABLE)
now=pygame.Surface(size)
pygame.display.set_caption('PZ帝国')

background=pygame.image.load(menu_bg).convert()
start_bg=pygame.image.load(start_bg).convert()
text_box=pygame.image.load(text_box).convert()
top_label=pygame.image.load(top_label).convert()
study_button=pygame.image.load(study_button).convert()
start_button=pygame.image.load(start_button).convert()
background=pygame.transform.smoothscale(background,size)
now.blit(background,(0,0))
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
            break
        for z in disp:
            if type(z) == tuple:
                screen.blit(z[0],z[1])
            else:
                screen.blit(z,z.get_rect()[:2])
                        
        t=f.render(text[:i],True,(0,0,0))
        print(t.get_rect(),'gg')
        screen.blit(f.render(text[:i+1],True,(0,0,0)),position)
        pygame.time.wait(30) #130 
        pygame.display.update()

    now.blit(screen,(0,0))
    if i <len(text)-1:
        line+=1
        position=position[0],position[1]+f.get_linesize()
        textlabel(text[i:],position,[now],size,0,line)
    pygame.event.post(finish)
    print('我好了')


def start_g(l,size):
    global start_game
    for z in l:
        p=z.get_rect()
        print(p[:2])
        screen.blit(z,p[:2])
    start_game=1
    


class Label(pygame.Surface):
    def __init__(self,sf,size,position):
        self.size=size
        self.position=position
        self.sf=sf
        pygame.Surface.__init__(self,size)
        self.blit(pygame.transform.smoothscale(self.sf,self.size),(0,0))


    def get_rect(self):
        return self.position+self.size

def labelbox(text,position):
    f=pygame.font.SysFont('华文中宋',16)
    heigh=f.get_linesize()
    f= f.render(text,True,(0,0,0))
    return f,position

class Button(pygame.Surface):
    def __init__(self,sf,size,position):
        self.sf=sf
        self.size=size
        self.position=position
        self.status=0
        pygame.Surface.__init__(self,size)
        self.blit(pygame.transform.smoothscale(self.sf,self.size),(0,0))

    def get_rect(self):
        return self.position+self.size

    def get_range(self):
        return self.position+(self.position[0]+self.size[0],self.position[1]+self.size[1])

def flush(l,num=False):
    for z in l:
        print(type(z))
        if num and type(z)==Label and z.get_rect()[2:] != size:
            print('hhh')
            screen.blit(z,z.get_rect()[:2])
        elif type(z) == tuple:
            screen.blit(z[0],z[1])
        elif not num:
            screen.blit(z,z.get_rect()[:2])

study_b=Button(study_button,(w//7,h//12),(w-w//7,h//4-h//12))
print(study_b.get_range())
start_b=Button(start_button,(w//5,h//10),((w-w//5)//2,int(h//1.5)))

    
        

while 1:
    
    for event in pygame.event.get():
        #print(event.type)
        if event.type == QUIT:
            exit()

        if event.type == FINISH:
            pygame.event.set_allowed([MOUSEBUTTONUP])


        if event.type == VIDEORESIZE:
            size=w,h=event.size
            #print(size)
            l=[Label(screen,size,(0,0))]
            screen=pygame.display.set_mode(size,RESIZABLE)
            now=pygame.transform.smoothscale(now,size)
            bd=pygame.transform.smoothscale(now,size)
            screen.blit(bd,(0,0))
            now.blit(screen,(0,0))
            if not start_game:
                screen.blit(start_b,start_b.get_rect()[:2])
        
    
                


        if event.type == MOUSEBUTTONUP:
            mouse_pos=pygame.mouse.get_pos()
            lh=pygame.font.SysFont('华文中宋',16).get_linesize()
            if study_b.get_range()[0]<mouse_pos[0]<study_b.get_range()[2] and study_b.get_range()[1] < mouse_pos[1] < study_b.get_range()[3] and start_game == 1 and study_b.status:
                charm += 1
                l=[Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('学习力   %d'% study,(0,0)),
                   labelbox('魅力      %d'% charm,(0,int(lh*1.5))),
                   labelbox('执行力   %d'% power,(0,lh*3)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh)))]
                print('龙怡广牛逼！！')
                flush(l,num=True)

                
            if event.button == 1 and rd==5 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w,h//4),(0,h-h//4)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('学习力   %d'% study,(0,0)),
                   labelbox('魅力      %d'% charm,(0,int(lh*1.5))),
                   labelbox('执行力   %d'% power,(0,lh*3)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   study_b]
                t='最后，祝你游戏愉快！'
                flush(l)
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                study_b.status=1
                #rd += 1









            if event.button == 1 and rd==4 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w,h//4),(0,h-h//4)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('学习力   %d'% study,(0,0)),
                   labelbox('魅力      %d'% charm,(0,int(lh*1.5))),
                   labelbox('执行力   %d'% power,(0,lh*3)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   study_b]
                t='底下那个是回合数,到一定的回合后，游戏结束。'
                flush(l)
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1



            if event.button == 1 and rd==3 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w,h//4),(0,h-h//4)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('学习力   %d'% study,(0,0)),
                   labelbox('魅力      %d'% charm,(0,int(lh*1.5))),
                   labelbox('执行力   %d'% power,(0,lh*3)),]
                t='最上面那个是状态栏，上面有学习力，魅力，执行力三个参数，这三个参数决定了你的高中生涯，也影响着你毕业后的工作，'
                for z in l:
                    print(type(z))
                    if type(z) == tuple:
                        screen.blit(z[0],z[1])
                    else:
                        screen.blit(z,z.get_rect()[:2])
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==2 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4 :
                l=[Label(start_bg,(w,h),(0,0)),Label(text_box,(w,h//4),(0,h-h//4))]
                for z in l:
                    p=z.get_rect()
                    screen.blit(z,p[:2])
                textlabel('些啥呢？？',(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1

            
                    
            if event.button == 1 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4 and rd==1:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),Label(text_box,(w,h//4),(0,h-h//4))]
                t='这是一个类似于中国式家长的策略游戏，虽然没写好，没事，总会写好的'
                for z in l:
                    p=z.get_rect()
                    screen.blit(z,p[:2])
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1


            if event.button == 1 and start_game==0 and start_b.get_range()[0] < mouse_pos[0] <start_b.get_range()[2] and start_b.get_range()[1] < mouse_pos[1] < start_b.get_range()[3] and rd==0:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),Label(text_box,(w,h//4),(0,h-h//4))]
                start_g(l,size)
                textlabel('欢迎来到浦中帝国！！本游戏没有一丝丝教程，大家伙凑合这玩吧哈哈哈哈哈哈哈哈哈',(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1


            
        




    pygame.display.update()
