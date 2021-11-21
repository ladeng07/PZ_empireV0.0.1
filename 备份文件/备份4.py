import pygame
from pygame.locals import *
import time


pygame.init()

menu_bg='pz.jpg'
start_bg='start_bg.jpg'
start_bg2='start_bg2.jpg'
text_box='text_box.png'
top_label='top_label.png'
study_button='study_button.png'
social_button='social_button.png'
shop_button='shop_button.png'
start_button='start_button.png'
mes_box='mes_box.png'
button='button.png'
xg='xg.png'
start_menu=1
start_game=0
rd=0
l=[]
FINISH =USEREVENT + 1
finish = pygame.event.Event(FINISH,message='g')
study=100
eq=100
rem=100
ima=100
stress=0
energy=100
rod=0
right_list=[]
w,h=size = (1000,600)



screen=pygame.display.set_mode(size,RESIZABLE)
now=pygame.Surface(size)
pygame.display.set_caption('PZ帝国')
clock=pygame.time.Clock()
background=pygame.image.load(menu_bg).convert()
start_bg=pygame.image.load(start_bg).convert()
start_bg2=pygame.image.load(start_bg2).convert()
text_box=pygame.image.load(text_box).convert()
top_label=pygame.image.load(top_label).convert_alpha()
study_button=pygame.image.load(study_button).convert_alpha()
social_button=pygame.image.load(social_button).convert_alpha()
shop_button=pygame.image.load(shop_button).convert_alpha()
start_button=pygame.image.load(start_button).convert()
mes_box=pygame.image.load(mes_box).convert()
button=pygame.image.load(button).convert_alpha()
xg=pygame.image.load(xg).convert_alpha()
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
        #pygame.time.wait(30) #130 
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
        self.blit(screen.subsurface(pygame.Rect(self.position+self.size)),(0,0))
        self.blit(pygame.transform.smoothscale(self.sf,self.size),(0,0))


    def get_rect(self):
        return self.position+self.size

def labelbox(text,position):
    f=pygame.font.SysFont('华文中宋',16)
    heigh=f.get_linesize()
    f= f.render(text,True,(0,0,0))
    return f,position

class Button(pygame.Surface):
    def __init__(self,sf,size,position,text=None,c=1,power=(0,0,0,0,0,0)):
        self.sf=sf
        self.size=size
        self.position=position
        self.status=0
        self.c=0
        self.text=text
        pygame.Surface.__init__(self,size)
        self.blit(screen.subsurface(pygame.Rect(self.position+self.size)),(0,0))
        self.blit(pygame.transform.smoothscale(self.sf,self.size),(0,0))
        if self.text:
            f=pygame.font.SysFont('华文中宋',12)
            fh=f.get_linesize()
            if c:
                posi=(self.size[1]-f.get_linesize())//2
                f= f.render(text[0],True,(0,0,0))
                self.blit(f,((self.size[0]-f.get_rect()[2])//2,(self.size[1]-f.get_rect()[3])//2))
            else:
                posi=fh//8
                for i in text:
                    fo=f.render(i,True,(0,0,0))
                    self.blit(fo,((self.size[0]-fo.get_rect()[2])//2,posi))
                    posi += int(fh*0.8)

    def get_rect(self):
        return self.position+self.size

    def get_range(self):
        return self.position+(self.position[0]+self.size[0],self.position[1]+self.size[1])

    
        
    
    def choice(self,text,c=1):
        f=pygame.font.SysFont('华文中宋',12)
        fh=f.get_linesize()
        if c:
            posi=(self.size[1]-f.get_linesize())//2
            f= f.render(text[0],True,(0,0,0))
            self.blit(f,((self.size[0]-f.get_rect()[2])//2,(self.size[1]-f.get_rect()[3])//2))
        else:
            posi=fh//6
            for i in text:
                fo=f.render(i,True,(0,0,0))
                self.blit(fo,((self.size[0]-fo.get_rect()[2])//2,posi))
                posi += int(fh*0.8)
            

def flush(l,num=False):
    for z in l:
        print(type(z))
        if num and type(z)==Label and z.get_rect()[2:] != size:
            #print('hhh')
            screen.blit(z,z.get_rect()[:2])
        elif type(z) == tuple:
            screen.blit(z[0],z[1])
        elif not num:
            screen.blit(z,z.get_rect()[:2])

lw,lh=w//6,h//12
study_list=[Button(button,(lw,lh),((w-int(w//1.4)+lw//14,(h-int(h//1.4))//2+lh//6)),['导学案','智商+2 情商+1','记忆力+2 行动力-10'],c=0,power=(2,1,2,0,0,-10)),
            Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw,(h-int(h//1.4))//2+lh//6)),['语文测评','情商+3 记忆力+3','想象力+2 行动力-15'],c=0,power=(0,3,3,2,0,-15)),
            Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*2,(h-int(h//1.4))//2+lh//6)),['数学活页','智商+5 情商+1','想象力+4 行动力-20'],c=0,power=(5,1,0,4,0,-20))]


def choice(w,h,n=3,right=False,event=None):
    global study_list,right_list
    lw,lh=w//6,h//12
    if not right:
        row,line=len(study_list) % n,len(study_list) // n
        if event:
            study_list.append(Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*row,(h-int(h//1.4))//2+lh//6+lh*line)),event,c=0))
        for i in range(len(study_list)):
            study_list[i].__init__(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*(i%n),(h-int(h//1.4))//2+lh//6+lh*(i//n))),study_list[i].text,c=0)
        return study_list
    else:
        for i in range(len(right_list)):
            right_list[i].__init__(button,(lw,lh),(w-lw,(h-int(h//1.4))//2+lh//6+lh*i),right_list[i].text,c=0)
            screen.blit(right_list[i],right_list[i].get_rect()[:2])

def talk_box(sf,text,name,me=False):
    global w,h
    f,p=labelbox(name,(0,0))
    lh=f.get_rect()[3]
    flush(l)
    sf=pygame.transform.smoothscale(sf,(200,300))
    if me:
        screen.blit(sf,(w-sf.get_rect()[2],h-sf.get_rect()[3]-h//4))
        temp=pygame.Surface((f.get_rect()[2],f.get_rect()[3]))
        temp.fill((255,255,255))
        temp.blit(f,(0,0))
        screen.blit(temp,(w-100-(f.get_rect()[2])//2,h-h//4-f.get_rect()[3]))
        textlabel(text,(w//10,h-h//4+h//20),[l[1]],(w//1.3,h//1.2),0,0)
    else:
        screen.blit(sf,(0,h-sf.get_rect()[3]-h//4))
        temp=pygame.Surface((f.get_rect()[2],f.get_rect()[3]))
        temp.fill((255,255,255))
        temp.blit(f,(0,0))
        screen.blit(temp,((200-f.get_rect()[2])//2,h-h//4-f.get_rect()[3]))
        textlabel(text,(w//10,h-h//4+h//20),[l[1]],(w//1.3,h//1.2),0,0)



while 1:
    time_pass=clock.tick(30)
    for event in pygame.event.get():
        #print(event.type)
        if event.type == QUIT:
            exit()

        if event.type == FINISH:
            pygame.event.set_allowed([MOUSEBUTTONUP])


        if event.type == VIDEORESIZE:
            size=w,h=event.size
            #print(size)
            #l=[Label(screen,size,(0,0))]
            screen=pygame.display.set_mode(size,RESIZABLE)
            now=pygame.transform.smoothscale(now,size)
            bd=pygame.transform.smoothscale(now,size)
            screen.blit(bd,(0,0))
            now.blit(screen,(0,0))
            study_b=Button(study_button,(w//6,h//12),(0,h//2-h//15))
            start_b=Button(start_button,(w//4,h//10),((w-w//4)//2,int(h//1.5)))
            flush(l)
            if not start_game:
                screen.blit(start_b,start_b.get_rect()[:2])
        
    
                


        if event.type == MOUSEBUTTONUP:
            mouse_pos=pygame.mouse.get_pos()
            lh=pygame.font.SysFont('华文中宋',16).get_linesize()

                
            if study_b.c and not study_b.status and start_game and rod>0 and b.get_rect()[0]<mouse_pos[0] and b.get_rect()[1] < mouse_pos[1] < b.get_rect()[1]+b.get_rect()[3]:
                print('我裂开了')
                lw,lh=w//6,h//12
                row=mouse_pos[0]-(w-int(w//1.4)+lw//14)
                line=mouse_pos[1]-((h-int(h//1.4))//2+lh//6)
                row=row//lw
                line=line//lh
                print(row,line)
                if 0<=row < 3 and 0<=line<8 and row+line*3 < len(study_list) and len(right_list) < 8:
                    right_list.append(study_list[row+line*3])
                    print(right_list)
                #print(b.get_rect())
                #print(mouse_pos)
                row=mouse_pos[0]-w+lw
                line=mouse_pos[1]-((h-int(h//1.4))//2+lh//6)
                line=line//lh
                if  mouse_pos[0]>w-lw and 0 <= line < 8 and line < len(right_list):
                    right_list.pop(line)
                    print(right_list)
                    screen.blit(b,b.get_rect()[:2])
                    for z in choice(w,h):
                        screen.blit(z,z.get_rect()[:2])

                choice(w,h,right=True)
                pygame.display.update()
                


            if study_b.c and not study_b.status and start_game and rod>0:
                if not b.get_rect()[0]<mouse_pos[0] or not b.get_rect()[1] < mouse_pos[1] < b.get_rect()[1]+b.get_rect()[3]:
                    print('好的')
                    screen.blit(Label(start_bg,(w,h),(0,0)),(0,0))
                    flush(l)
                    study_b.status=1


            if  study_b.get_range()[0] < mouse_pos[0] < study_b.get_range()[2] and study_b.get_range()[1] < mouse_pos[1] < study_b.get_range()[3] and start_game == 1 and study_b.status:
                b=Label(mes_box,(int(w//1.4),int(h//1.4)),(w-int(w//1.4),(h-int(h//1.4))//2))
                l=[Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   study_b,
                   social_b,
                   shop_b,]
                screen.blit(b,b.get_rect()[:2])
                study_b.c=1
                study_b.status=0
                for z in choice(w,h):
                    screen.blit(z,z.get_rect()[:2])


                choice(w,h,right=True)
                flush(l,num=True)


            if event.button == 1 and rd==12 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   study_b,
                   social_b,
                   shop_b,]
                flush(l)
                study_b.status=1
                rod=1
                rd += 1
            if event.button == 1 and rd==11 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='呀，真是有点期待我的新班主任和新同学呢！！'
                talk_box(xg,t,'我',me=True)
                rd += 1



            if event.button == 1 and rd==10 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='（回到教室后。）'
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==9 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='诶！！！(高二高三的同学们叽叽喳喳讨论起来)。'
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1

                
            if event.button == 1 and rd==8 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='在周六日的时候，结核我校实际，给大家适当的来点娱乐，'
                talk_box(xg,t,'陈校长')
                rd += 1

                
            if event.button == 1 and rd==7 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='同学们哟，欢迎来到浦北中学，从今天起大家就是我们浦J的一员，希望大家有无需提醒的自觉。'
                talk_box(xg,t,'陈校长')
                rd += 1


            if event.button == 1 and rd==6 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                '''screen.blit(pygame.transform.smoothscale(start_bg2,size),(0,0))
                study_b=Button(study_button,(w//6,h//12),(0,h//2-h//15))
                social_b=Button(social_button,(w//6,h//12),(0,h//2-h//15+h//12))
                shop_b=Button(shop_button,(w//6,h//12),(0,h//2-h//15+h//6))'''
                l=[Label(start_bg2,(w,h),(0,0)),
                   Label(text_box,(w,h//4),(0,h-h//4)),
                    ]
                flush(l)
                t='20XX年9月1日 早上6:51，进城广场大阶梯处，开学典礼上。'
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==5 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w,h//4),(0,h-h//4)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   social_b,
                   shop_b,
                   study_b]
                t='最后，祝你游戏愉快！'
                flush(l)
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1




            if event.button == 1 and rd==4 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                study_b=Button(study_button,(w//6,h//12),(0,h//2-h//15))
                social_b=Button(social_button,(w//6,h//12),(0,h//2-h//15+h//12))
                shop_b=Button(shop_button,(w//6,h//12),(0,h//2-h//15+h//6))
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   study_b,
                   social_b,
                   shop_b,
                   Label(text_box,(w,h//4),(0,h-h//4)),]
                t='底下那个是回合数,到一定的回合后，游戏结束。'
                flush(l)
                textlabel(t,(w//10,h-h//4+h//20),l,(w//1.3,h//1.2),0,0)
                rd += 1



            if event.button == 1 and rd==3 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w,h//4),(0,h-h//4)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4))
                   ]
                t='最上面那个是状态栏，上面有学习力，魅力，执行力和行动力四个参数，这四个参数决定了你的高中生涯，'
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
