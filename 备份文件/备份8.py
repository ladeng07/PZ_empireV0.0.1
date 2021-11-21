import pygame
from pygame.locals import *
import time
import random


pygame.init()

menu_bg='pz.jpg'
start_bg='start_bg.jpg'
start_bg2='start_bg2.jpeg'
start_bg3='start_bg3.jpg'
text_box='text_box.png'
top_label='top_label.png'
canteen='canteen.jpeg'
study_button='study_button.png'
social_button='social_button.png'
shop_button='shop_button.png'
start_button='start_button.png'
room_button='button.png'
mes_box='mes_box.png'
button='button.png'
next_button='next.png'
goroom='goroom.png'
zzz='button.png'
skip='skip.jpg'
skip2='skip2.jpg'
pe='pe.jpeg'
xkh='xkh.jpeg'
xg='xg.png'
xz='xz.png'
me='me.png'
wx='wx.png'
et='et.png'
fj='gril1.png'
xjh='xjh.png'

p1='p1.jpg'


s1='s1.jpeg'
#s2='s2.jpeg'
#s3='s3.jpeg'

start_game=0
skip_num=0
skip_l=[]

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
name='我'
w,h=size = (1000,600)



screen=pygame.display.set_mode(size,RESIZABLE)
now=pygame.Surface(size)
pygame.display.set_caption('PZ帝国')
clock=pygame.time.Clock()
background=pygame.image.load(menu_bg).convert()
start_bg=pygame.image.load(start_bg).convert()
start_bg2=pygame.image.load(start_bg2).convert()
start_bg3=pygame.image.load(start_bg3).convert()
text_box=pygame.image.load(text_box).convert()
top_label=pygame.image.load(top_label).convert_alpha()
study_button=pygame.image.load(study_button).convert_alpha()
social_button=pygame.image.load(social_button).convert_alpha()
shop_button=pygame.image.load(shop_button).convert_alpha()
start_button=pygame.image.load(start_button).convert()
mes_box=pygame.image.load(mes_box).convert()
skip=pygame.image.load(skip).convert()
skip2=pygame.image.load(skip2).convert()
xkh=pygame.image.load(xkh).convert()
pe=pygame.image.load(pe).convert()
canteen=pygame.image.load(canteen).convert()
button=pygame.image.load(button).convert_alpha()
room_button=pygame.image.load(room_button).convert_alpha()
next_button=pygame.image.load(next_button).convert_alpha()
goroom=pygame.image.load(goroom).convert_alpha()
zzz=pygame.image.load(zzz).convert_alpha()


xg=pygame.image.load(xg).convert_alpha()
xz=pygame.image.load(xz).convert_alpha()
me=pygame.image.load(me).convert_alpha()
wx=pygame.image.load(wx).convert_alpha()
et=pygame.image.load(et).convert_alpha()
fj=pygame.image.load(fj).convert_alpha()
xjh=pygame.image.load(xjh).convert_alpha()


background=pygame.transform.smoothscale(background,size)
now.blit(background,(0,0))
screen.blit(now,(0,0))

pygame.mixer.init()
sound=pygame.mixer.Sound('刘.ogg')
p1=pygame.image.load(p1).convert_alpha()
s1=pygame.image.load(s1).convert_alpha()

g1=[[p1,['日常  挤饭堂','智商+5 情商+10 ','想象力-5'],'在晚饭的时候,你选择打铁碗在饭堂吃，结果人山人海。',(5,10,0,-5,0,0)],
    [p1,['日常  搬课本','智商-5 情商-5 ','想象力-5  记忆力-5 压力+5'],'晚自习的时候,你们班的男生被叫去尚学楼搬书，你搬完回来发现准备下课了。',(-5,-5,-5,-5,5,0)],
    [p1,['日常  去六六','智商+10 情商+10 ','想象力+10 记忆力-10  压力-10'],'在一个难得的周日下午，你被几个同学带去了一条什么的小巷子里，上到二楼发现这是一个叫66的网吧，你和同学打了一下午LOL。',(10,10,-10,10,-10,0)],
    [p1,['日常  体育课','智商-5 情商-5 ','想象力-5 记忆力-5'],'上体育课的时候，你尝试和本班一千米冠军赛跑，结果扭伤了脚。',(-5,-5,-5,-5,0,0)],
    [p1,['日常  鸳鸯鞋','智商+5 情商-5 ','想象力-5'],'你在宿舍洗衣服的时候用力过猛，导致你的一只鞋湿了，于是你机智的穿着一只运动鞋一只拖鞋去教室，路上能听到其他人的切切私语。',(5,-5,0,5,0,0)],
    [p1,['日常  英语课','情商+2 记忆力+10',''],'上英语课的时候，你在一秒钟内回答出了五个短语，获得了同学们的一致赞扬',(0,2,10,0,0,0)],
    [p1,['日常  生物晚自习','智商-5 情商-5','记忆力-5 想象力-5'],'生物晚自习的时候，你和生物老师的儿子在隔壁休息室打了一节课架，你输得很惨。',(-5,-5,-5,-5,0,0)],
    [p1,['日常  晚自习唱歌','智商-5 情商-5','记忆力-2 想象力-3'],'你听说边唱歌边写作业可以提高效率，于是你在晚自习的时候轻轻唱出了歌，结果被路过的领导给听到了。',(-5,-5,-2,-3,0,0)],
    [p1,['日常  吹泡泡','智商-2 情商+5','想象力-5'],'同学买了泡泡水，你在课间吹起了泡泡，导致整栋教学楼围观，造成了不好的影响，被老师教育了',(-2,5,0,5,0,0)],
    [p1,['日常  拾金不昧','情商-5','记忆力+5 想象力+3'],'你在教室走廊捡到了98块钱，于是拾金不昧，交给政教处，获得了夸奖，虽然后来被证明这个钱是你们班同学掉的。',(0,-5,5,3,0,0)],
    [p1,['日常  数学题','智商-1 情商+3','记忆力+2 想象力+1'],'同桌昆哥问了你一道很难的数学题，你非常轻松的做错了。',(-1,3,2,1,0,0)],
    [p1,['日常  K歌Praty','','记忆力+5 想象力+5'],'一个难得的月假，你参加了你们班富二代同学的k歌Party，你们玩的很开心。',(0,0,5,5,0,0)],
    [p1,['日常  英语课giao屎','情商+10','记忆力+10'],'英语课上老师出去接电话，你跑到了门后面想要吓英语老师，英语老师回来后识破了你的诡计，说你giao屎。你学英语的兴趣提高了。',(0,10,10,0,0,0)],
    [p1,['日常  语文课','智商-5 情商+10','记忆力+10 想象力+5'],'在语文课上，语文老师破天荒的给你们讲了两节课古代故事，学习语文的兴趣提高了。',(-5,10,10,5,0,0)],
    [p1,['日常  化学课','智商-5 情商-5','记忆力-3 想象力-4'],'化学课上化学老师打了一个响嗝，你和你同桌一直在憋笑，结果被发现了。',(-5,-5,-3,-4,0,0)],
    [p1,['日常  校园恶霸','智商-10 情商-5','记忆力-10 想象力-5'],'你的洗衣粉被宿舍的恶霸强占了，你气不过与之硬拼，结果打不过受伤了。',(-10,-5,-10,-5,0,0)],
    [p1,['日常  恶作剧','智商-10 情商+5','想象力-2'],'你的同桌把一封情书给你让你转交，结果你在人家班门口等了一个课间都不见人，然而你并不知道情书是同桌收到的。',(-10,5,0,-2,0,0)],
    [p1,['日常  小黑真的黑','智商-10 情商-10','记忆力+10'],'小黑老板趁你不注意，打多了你两块钱。',(-10,-10,10,0,0,0)],
    
    
    ]
print('目前一共有=',len(g1))
g2=[]
g3=[]



rightroom_l=[]

def textbox(target,size):
    global text_box,label
    y=size[1]//4
    tbox=pygame.transform.smoothscale(text_box,(size[0],y))
    target.blit(tbox,(0,size[1]-y))
    print(target.get_rect())
    label.append((0,size[1]-y,size[0],y))
    print(label)


def textlabel(text,position,disp,size,num=0,line=0):
    f=pygame.font.SysFont('华文中宋',16)
    for i in range(0,len(text)):
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
        textlabel(text[i:],position,[now],size,line)
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

def labelbox(text,position,font_size=16,size=(0,0),line=0,color=(0,0,0)):
    f=pygame.font.SysFont('华文中宋',font_size)
    if line:
        for i in range(0,len(text)):
           # print(text,'zhijiushi')
            #print(f.size(text[:i]))
            if f.size(text[:i])[0] > size[0]:
                break
        t=f.render(text[:i],True,(0,0,0))
        screen.blit(f.render(text[:i+1],True,color),position)
        
        if i <len(text)-1:
            #line+=1
            position=position[0],position[1]+f.get_linesize()
            labelbox(text[i+1:],position,font_size,size,line,color)
        return 1,1
    
    else:
        f= f.render(text,True,color)
        return f,position

class Button(pygame.Surface):
    def __init__(self,sf,size,position,text=None,c=1,power=(0,0,0,0,0,0),ima=None):
        self.sf=sf
        self.size=size
        self.position=position
        self.status=0
        self.c=0
        self.ima=ima
        self.power=power
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
study_list=[Button(button,(lw,lh),((w-int(w//1.4)+lw//14,(h-int(h//1.4))//2+lh//6)),['练习  导学案','智商+2  情商+1','记忆力+2  行动力-10'],c=0,power=(2,1,2,0,0,-10),ima=s1),
            Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw,(h-int(h//1.4))//2+lh//6)),['练习  语文测评','情商+3  记忆力+3','想象力+2  行动力-15'],c=0,power=(0,3,3,2,0,-15),ima=s1),
            Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*2,(h-int(h//1.4))//2+lh//6)),['练习  数学活页','智商+5  情商+1','想象力+4  行动力-20'],c=0,power=(5,1,0,4,0,-20),ima=s1)]


room_l=[Button(button,(lw,lh),((w-int(w//1.4)+lw//14,(h-int(h//1.4))//2+lh//6)),['娱乐 睡觉','智商+5  情商+3','记忆力+10  行动力+50'],c=0,power=(5,3,10,0,0,50),ima=s1)]

def choice(w,h,n=3,right=False,event=None,power=None,ima=None):
    global study_list,right_list
    lw,lh=w//6,h//12
    if not right:
        row,line=len(study_list) % n,len(study_list) // n
        if event:
            study_list.append(Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*row,(h-int(h//1.4))//2+lh//6+lh*line)),event,c=0,power=power,ima=ima))
        for i in range(len(study_list)):
            study_list[i].__init__(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*(i%n),(h-int(h//1.4))//2+lh//6+lh*(i//n))),study_list[i].text,c=0,power=study_list[i].power,ima=study_list[i].ima)
        return study_list
    else:
        for i in range(len(right_list)):
            right_list[i].__init__(button,(lw,lh),(w-lw,(h-int(h//1.4))//2+lh//6+lh*i),right_list[i].text,c=0,power=right_list[i].power,ima=right_list[i].ima)
            screen.blit(right_list[i],right_list[i].get_rect()[:2])

def room_choice(w,h,n=3,right=False,event=None,power=None,ima=None):
    lw,lh=w//6,h//12
    if not right:
        row,line=len(room_l) % n,len(room_l) // n
        if event:
            room_l.append(Button(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*row,(h-int(h//1.4))//2+lh//6+lh*line)),event,c=0,power=power,ima=ima))
        for i in range(len(room_l)):
            room_l[i].__init__(button,(lw,lh),((w-int(w//1.4)+lw//14+lw*(i%n),(h-int(h//1.4))//2+lh//6+lh*(i//n))),room_l[i].text,c=0,power=room_l[i].power,ima=room_l[i].ima)
        return room_l
    else:
        for i in range(len(rightroom_l)):
            rightroom_l[i].__init__(button,(lw,lh),(w-lw,(h-int(h//1.4))//2+lh//6+lh*i),rightroom_l[i].text,c=0,power=rightroom_l[i].power,ima=rightroom_l[i].ima)
            screen.blit(rightroom_l[i],rightroom_l[i].get_rect()[:2])


def talk_box(sf,text,name,me=False):
    global w,h
    f,p=labelbox(name,(0,0))
    lh=f.get_rect()[3]
    flush(l)
    sf=pygame.transform.smoothscale(sf,(300,400))
    if me:
        screen.blit(sf,(w-sf.get_rect()[2],h-sf.get_rect()[3]))
        temp=pygame.Surface((f.get_rect()[2],f.get_rect()[3]))
        temp.fill((255,255,255))
        temp.blit(f,(0,0))
        screen.blit(temp,(w*0.9-f.get_rect()[2],h-h//5-f.get_rect()[3]))
        textlabel(text,(w//7.5,h-h//5.5),[l[1]],(w//1.4,h//1.2),0,0)
    else:
        screen.blit(sf,(0,h-sf.get_rect()[3]))
        temp=pygame.Surface((f.get_rect()[2],f.get_rect()[3]))
        temp.fill((255,255,255))
        temp.blit(f,(0,0))
        screen.blit(temp,(w//10,h-h//5-f.get_rect()[3]))
        textlabel(text,(w//7.5,h-h//5.5),[l[1]],(w//1.4,h//1.2),0,0)


def skipfun(a):
    skip.get_rect()
    skip_l=list([[pygame.transform.smoothscale(z.ima,(skip.get_rect()[2]//2,skip.get_rect()[3])),z.text,z.power] for z in right_list])
    for z in range(4):
        r=random.randint(0,len(a)-1)
        print(a[r][0])
        a[r][0]=pygame.transform.smoothscale(a[r][0],(skip.get_rect()[2]//2,skip.get_rect()[3]))
        skip_l.insert(z+4,a[r])
        g1.pop(r)
    return skip_l
        

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
            social_b=Button(social_button,(w//6,h//12),(0,h//2-h//15+h//12))
            shop_b=Button(shop_button,(w//6,h//12),(0,h//2-h//15+h//6))
            start_b=Button(start_button,(w//4,h//10),((w-w//4)//2,int(h//1.5)))
            room_b=Button(room_button,(w//6,h//12),(0,h//2-h//15))
            zzz_b=Button(zzz,(w//6,h//12),(0,h//2-h//15+h//12))
            flush(l)
            if not start_game:
                screen.blit(start_b,start_b.get_rect()[:2])
        
                    


        if event.type == MOUSEBUTTONUP:
            mouse_pos=pygame.mouse.get_pos()
            lh=pygame.font.SysFont('华文中宋',16).get_linesize()
            
            if skip_l ==[] and not start_game and rd > 0:
                skip_num = 0
                start_game = 1
                rod += 1
                rd += 1
                screen.blit(pygame.transform.smoothscale(start_bg3,size),(0,0))
                l=[Label(start_bg3,(w,h),(0,0)),
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


            if zzz_b.c and not zzz_b.status and start_game and rod>0 and b.get_rect()[0]<mouse_pos[0] and b.get_rect()[1] < mouse_pos[1] < b.get_rect()[1]+b.get_rect()[3]:
                lw,lh=w//6,h//12
                row=mouse_pos[0]-(w-int(w//1.4)+lw//14)
                line=mouse_pos[1]-((h-int(h//1.4))//2+lh//6)
                row=row//lw
                line=line//lh
                if 0<=row < 3 and 0<=line<8 and row+line*3 < len(room_l) and len(rightroom_l) < 4:
                    rightroom_l.append(room_l[row+line*3])
                row=mouse_pos[0]-w+lw
                line=mouse_pos[1]-((h-int(h//1.4))//2+lh//6)
                line=line//lh
                if  mouse_pos[0]>w-lw and 0 <= line < 4 and line < len(rightroom_l):
                    rightroom_l.pop(line)
                    print(rightroom_l)
                    screen.blit(b,b.get_rect()[:2])
                    for z in room_choice(w,h):
                        screen.blit(z,z.get_rect()[:2])
                choice(w,h,right=True)
                pygame.display.update()




            if zzz_b.status and zzz_b.get_range()[0] < mouse_pos[0] < zzz_b.get_range()[2] and zzz_b.get_range()[1] < mouse_pos[1] < zzz_b.get_range()[3]:
                b=Label(mes_box,(int(w//1.4),int(h//1.4)),(w-int(w//1.4),(h-int(h//1.4))//2))
                print('???')
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   room_b,
                   ]
                l.append(b)
                screen.blit(b,b.get_rect()[:2])
                for z in room_choice(w,h):
                    screen.blit(z,z.get_rect()[:2])
                room_choice(w,h,right=True)
                flush(l[:-2],num=True)
                zzz_b.c=1
                zzz_b.status=0
                pygame.display.update()
                


            if not room_b.status and  room_b.c and room_b.get_range()[0] < mouse_pos[0] < room_b.get_range()[2] and room_b.get_range()[1] < mouse_pos[1] < room_b.get_range()[3]:
                room_b.status=1
                room_b.c=0
                
            if room_b.status and  room_b.c and room_b.get_range()[0] < mouse_pos[0] < room_b.get_range()[2] and room_b.get_range()[1] < mouse_pos[1] < room_b.get_range()[3]:
                canteen=pygame.transform.smoothscale(canteen,size)
                screen.blit(canteen,(0,0))
                screen.blit(pygame.transform.smoothscale(goroom,(w//6,h//12)),(0,h//2-h//15))
                room_b.status=0



            if room_b.status and not room_b.c and  rd >40:
                screen.blit(pygame.transform.smoothscale(start_bg,size),(0,0))
                room_b=Button(room_button,(w//6,h//12),(0,h//2-h//15))
                zzz_b=Button(zzz,(w//6,h//12),(0,h//2-h//15+h//12))
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(top_label,(int(w//5),int(h//2.5)),(0,0)),
                   labelbox('智商   %d'% study,(0,0)),
                   labelbox('情商      %d'% eq,(0,lh)),
                   labelbox('记忆力   %d'% rem,(0,lh*2)),
                   labelbox('想象力   %d'% ima,(0,lh*3)),
                   labelbox('行动力   %d'% energy,(0,lh*4)),
                   labelbox('回合   %d'% rod,(0,int(h//2.5-4*lh))),
                   room_b,
                   zzz_b,]
                room_b.c=1
                room_b.status=1
                zzz_b.status=1
                flush(l)


            if shop_b.status and study_b.status and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4 and 19 < rd< 21:
                flush(l)
                print(l[-1])
                shop_b.status=0

            if  study_b.status and shop_b.get_range()[0] < mouse_pos[0] < shop_b.get_range()[2] and shop_b.get_range()[1] < mouse_pos[1] < shop_b.get_range()[3] and start_game == 1 and 19< rd < 21:
                t='商店功能功能暂未开放，敬请期待'
                textlabel(t,(w//7.5,h-h//5.5),[Label(text_box,(w//5*4,h//5),(w//10,h-h//5))],(w//1.4,h//1.2),0,0)
                shop_b.status=1


            if  study_b.status and social_b.status and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4 and 19 < rd< 21:
                flush(l)
                print(l[-1])
                print('ile')
                social_b.status=0


            if  study_b.status and social_b.get_range()[0] < mouse_pos[0] < social_b.get_range()[2] and social_b.get_range()[1] < mouse_pos[1] < social_b.get_range()[3] and start_game == 1 and 19< rd < 21:
                t='社交功能暂未开放，敬请期待'
                print('dierci')
                textlabel(t,(w//7.5,h-h//5.5),[Label(text_box,(w//5*4,h//5),(w//10,h-h//5))],(w//1.4,h//1.2),0,0)
                social_b.status=1


            
            if not social_b.status and study_b.c and not study_b.status and start_game and rod>0 and b.get_rect()[0]<mouse_pos[0] and b.get_rect()[1] < mouse_pos[1] < b.get_rect()[1]+b.get_rect()[3]:
                lw,lh=w//6,h//12
                row=mouse_pos[0]-(w-int(w//1.4)+lw//14)
                line=mouse_pos[1]-((h-int(h//1.4))//2+lh//6)
                row=row//lw
                line=line//lh
                if 0<=row < 3 and 0<=line<8 and row+line*3 < len(study_list) and len(right_list) < 8:
                    right_list.append(study_list[row+line*3])
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
                


            if  not social_b.status and not shop_b.status and study_b.c and not study_b.status and start_game and rod>0:
                if  b.get_rect()[0] > mouse_pos[0] or b.get_rect()[1] > mouse_pos[1]  or mouse_pos[1] >  b.get_rect()[1]+b.get_rect()[3]:
                    if study_b.get_range()[0] < mouse_pos[0] < study_b.get_range()[2] and study_b.get_range()[1] < mouse_pos[1] < study_b.get_range()[3]:
                        skip=Label(skip,(int(w//1.8),int(h//2.5)),(w//2-int(w//3.6),h//2-h//6))
                        screen.blit(pygame.transform.smoothscale(skip2,size),(0,0))
                        screen.blit(skip,skip.get_rect()[:2])
                        start_game=0
                        study_b.c=0
                    elif  mouse_pos[0] > social_b.get_range()[3] or mouse_pos[1] < social_b.get_range()[1] or mouse_pos[1] > social_b.get_range()[3]+social_b.get_rect()[3]:
                        screen.blit(Label(start_bg3,(w,h),(0,0)),(0,0))
                        l=[Label(start_bg3,(w,h),(0,0)),
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
                        study_b.c=0


            if not start_game and rd >0:
                screen.blit(skip,skip.get_rect()[:2])
                if not skip_l:
                    print(rd)
                    skip_l=skipfun(g1)
                    right_list=[]
                screen.blit(skip_l[skip_num][0],(w//2-int(w//3.6),h//2-h//6))
                f,p=labelbox(skip_l[skip_num][1][0],(skip.get_rect()[0]+skip.get_rect()[2]//2,h//2-h//7),font_size=25,color=(255,255,255))
                screen.blit(f,p)
                f,p=labelbox(skip_l[skip_num][1][1],(skip.get_rect()[0]+skip.get_rect()[2]//2+skip.get_rect()[3]//20,skip.get_rect()[1]+skip.get_rect()[3]-int(f.get_rect()[3]*1.5)),color=(255,255,255))
                screen.blit(f,p)
                f,p=labelbox(skip_l[skip_num][1][2],(skip.get_rect()[0]+skip.get_rect()[2]//2+skip.get_rect()[3]//20,skip.get_rect()[1]+skip.get_rect()[3]-int(f.get_rect()[3]*1.5)),color=(255,255,255))
                screen.blit(f,p)
                study += skip_l[skip_num][-1][0]
                eq += skip_l[skip_num][-1][1]
                rem += skip_l[skip_num][-1][2]
                ima += skip_l[skip_num][-1][3]
                stress += skip_l[skip_num][-1][4]
                energy += skip_l[skip_num][-1][5]
                
                if len(skip_l[skip_num]) > 3:
                    labelbox(skip_l[skip_num][2],(skip.get_rect()[0]+skip.get_rect()[2]//2+f.get_rect()[3]//4,h//2-h//8+f.get_rect()[3]),16,(int(skip.get_rect()[2]//2.5),skip.get_rect()[3]),line=1,color=(255,255,255))
                if skip_num >= len(skip_l)-1:
                    skip_l=[]
                skip_num += 1
                
            
            
            if  not social_b.status and not shop_b.status and study_b.get_range()[0] < mouse_pos[0] < study_b.get_range()[2] and study_b.get_range()[1] < mouse_pos[1] < study_b.get_range()[3] and start_game == 1 and study_b.status:
                b=Label(mes_box,(int(w//1.4),int(h//1.4)),(w-int(w//1.4),(h-int(h//1.4))//2))
                l=[Label(start_bg3,(w,h),(0,0)),
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
                l.append(b)
                screen.blit(b,b.get_rect()[:2])
                study_b.c=1
                study_b.status=0
                for z in choice(w,h):
                    screen.blit(z,z.get_rect()[:2])
                choice(w,h,right=True)
                flush(l[:-2],num=True)
                screen.blit(pygame.transform.smoothscale(next_button,(w//6,h//12)),(0,h//2-h//15))


            if event.button == 1 and rd==20 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                screen.blit(pygame.transform.smoothscale(start_bg3,size),(0,0))
                study_b=Button(study_button,(w//6,h//12),(0,h//2-h//15))
                social_b=Button(social_button,(w//6,h//12),(0,h//2-h//15+h//12))
                shop_b=Button(shop_button,(w//6,h//12),(0,h//2-h//15+h//6))
                l=[Label(start_bg3,(w,h),(0,0)),
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
                rod=1                                                                                             #############################################################################

            
            if event.button == 1 and rd==52 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.post(finish)
                screen.blit(pygame.transform.smoothscale(start_bg3,size),(0,0))
                l=[Label(start_bg3,(w,h),(0,0)),
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
                rd += 1
            


            if event.button == 1 and rd==50 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='哎，吃得苦中苦，方为人上人，不跟你聊了，我衣服还没晾呢。'
                room_b.status=1
                talk_box(fj,t,'FJ')
                rd += 1

            
            if event.button == 1 and rd==49 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='这么爽的吗，早生两年就爽多了，唉，按这个作息时间，每天的睡眠总量也就八小时左右，太难了'
                talk_box(me,t,name,me=True)
                rd += 1


            if event.button == 1 and rd==48 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='蛤，这学校的确是一天比一天苦了，想当年我们九年级的时候，还没有课后讨论这种东西，甚至周六下午就可以回家了，不像现在只有周日下午的黄金六小时。'
                talk_box(fj,t,'FJ')
                rd += 1


            if event.button == 1 and rd==47 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='上了一天课，累死我了，感觉以后每天这样上下去我就累死了，FJ你说是不是吧'
                talk_box(me,t,name,me=True)
                rd += 1

                
            if event.button == 1 and rd==46 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
                    ]
                flush(l)
                t='(半夜22:40 E栋701宿舍 )'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1

            if event.button == 1 and rd==45 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='(新增社交选项，你现在可以和别人交庞友了)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==44 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='哈哈哈哈，我可是咱浦中最正派的体委啊，怎么会与你同流合污呢，哈哈哈哈哈'
                talk_box(xjh,t,'壕哥')
                rd += 1


            if event.button == 1 and rd==43 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='呼哈~呼哈~，我太难了，你以为每个人都像你这么能跑么，呼哈~呼哈~，要不你帮我随便填个成绩得了，及格就行'
                talk_box(me,t,name,me=True)
                rd += 1
                
            if event.button == 1 and rd==42 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='你再不跑快点，就要吊车尾了，哈哈哈蛤'
                talk_box(xjh,t,'壕哥')
                rd += 1


            if event.button == 1 and rd==41 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                t='(这时，一个风一样的男子从你身边冲出来)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==40 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='哎哟妈呀，中考那时候都没这么累啊，咋现在感觉举步维艰啊，呼哈~呼哈~'
                talk_box(me,t,name,me=True)
                rd += 1

            if event.button == 1 and rd==39 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(pe,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
                    ]
                t='(星期三下午，第二节体育课上，烈日当空，大家都在测一千米)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==38 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='那以后我们就一起进步了（他那个笑容透露出一丝...）。'
                talk_box(me,t,name,me=True)
                rd += 1


            if event.button == 1 and rd==37 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='hbb?? 哈哈哈，哪里哪里，我觉得你英语才是好棒棒呢（坏笑），'
                talk_box(fj,t,'FJ')
                rd += 1


            if event.button == 1 and rd==36 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='FJ,你的英语口语真的好棒棒啊，可以教教我嘛QAQ。'
                talk_box(me,t,name,me=True)
                rd += 1


            if event.button == 1 and rd==35 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(xkh,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
                    ]
                t='(下课后)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==34 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='好，同学们这节课上到这里，厦阔。'
                talk_box(et,t,'英语老师')
                rd += 1

            
            if event.button == 1 and rd==33 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='酱紫念起来像一个和尚一样了喔'
                talk_box(et,t,'英语老师')
                rd += 1

                
            if event.button == 1 and rd==32 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                sound.play()
                pygame.event.set_blocked([MOUSEBUTTONUP])
                t='(@#$$%$@@#^%$^%^#&#@">}:^&%$#@%#$#@%$^$^$$%#@$#%$^%^>">}{&%%#&%$#@$%$^&%$@#$%^&@#$%^&&&^%$#@#$%^&^%$@#$%^&@@#$%^*%@%*%#$%&%@@#%&%@^*^&*(_(^#!!#%^&*()_+_)(*&^%$+}{"?}"?><!#$@#">"@$#$%^&*&*^%^$@#$%^^&*^&%^$%^^%&^%$#@#$%^%$#@@#$%^^%?":{*^#":&%##@$%^&^%$#%^&*^%$%#@%^$%^)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                pygame.time.wait(4500)
                print('jj')
                rd += 1
                
            if event.button == 1 and rd==31 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='有些同学怎么读啊~。'
                talk_box(et,t,'英语老师')
                rd += 1

                
            if event.button == 1 and rd==30 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='一些同学不是我的水平喔。~呵~。'
                talk_box(et,t,'英语老师')
                rd += 1

                
            if event.button == 1 and rd==29 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='现在我示范一些同学的读法啊。'
                talk_box(et,t,'英语老师')
                rd += 1


            if event.button == 1 and rd==28 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='有些同学读的是什么样捏？~'
                talk_box(et,t,'英语老师')
                rd += 1



            if event.button == 1 and rd==27 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='哦~这就对了嘛，我们英语读起来就是要有感觉'
                talk_box(et,t,'英语老师')
                rd += 1

            if event.button == 1 and rd==26 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='(哇，这人也太屌了吧，看来我得多向他学习学习。)'
                talk_box(me,t,name,me=True)
                rd += 1

                
            if event.button == 1 and rd==25 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                t='(eui~eui~,四面八方响起了一股赞扬的声音，)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


                
            if event.button == 1 and rd==24 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='咕噜咕噜咕噜~~~，(他以迅雷不及掩耳的速度读完了...你的脑海里只留下了一股标准的腔调。)'
                talk_box(fj,t,'符X',)
                rd += 1


            if event.button == 1 and rd==23 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                t='(这是，坐在你后面的一个肤色稍深的靓仔笑嘻嘻的站了起来，)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1

            if event.button == 1 and rd==22 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='It was when Asimov was eleven years old that his talent for writing...接下来我们找一个同学来读一下这句话，那就부정FJ同学来读吧，'
                talk_box(et,t,'英语老师',)
                rd += 1


            
            if event.button == 1 and rd==21 and start_game == 1:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg3,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
                    ]
                study_b.status=0
                study_b.c=0
                t='(在一节英语课上...)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==19 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='规范自己,追求卓越，成就辉煌，我失望同学们能做到这几个字的内容，那好，现在我们开始上阔。'
                talk_box(wx,t,'班主任',)
                rod=1
                rd += 1

                
            if event.button == 1 and rd==18 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='(刷~刷~刷，12个漂亮的大字出现在了黑板上...)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1
            
            if event.button == 1 and rd==17 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='嗯~，在这里我送给同学们12个字...'
                talk_box(wx,t,'班主任',)
                rd += 1
            
            if event.button == 1 and rd==16 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='(不知道从哪里传出一个奇怪的声音，只见第一排的一个同学把头埋进了抽屉里)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1
            
            if event.button == 1 and rd==15 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='算了，先自我介绍一下,从今天开始，我就是你们的班主任了，我姓*，叫我*老师就好~隔~...'
                talk_box(wx,t,'班主任',)
                rd += 1
            
            if event.button == 1 and rd==14 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='喂~？，我们同学怎么回事，老远就听到同学们讲话了，一条走廊过来就你们班最吵了，你们看看隔壁人家8班，班主任没来都安静在呢学习，'
                talk_box(wx,t,'班主任',)
                rd += 1


            if event.button == 1 and rd==13 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='(只见一个身材伟岸的男人径直走上讲台，把夹在腋下的化学书重重仍在桌面上，双手叉着讲台...)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1

                
            if event.button == 1 and rd==12 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='(教室里同学们的交谈声不绝于耳，大家都在聊着暑假里面发生的种种趣事，只有少数几个同学默默的在埋头写题,这时，教室的门被推开...)'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1

    
            if event.button == 1 and rd==11 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='呀，真是有点期待我的新班主任和新同学呢！！'
                talk_box(me,t,'我',me=True)
                rd += 1



            if event.button == 1 and rd==10 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg3,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
                    ]
                flush(l)
                t='（回到教室后。）'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==9 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='诶！！！(高二高三的同学们叽叽喳喳讨论起来)。'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1

                
            if event.button == 1 and rd==8 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='在周六日的时候，结核我校实际，给大家适当的来点娱乐，'
                talk_box(xz,t,'陈校长')
                rd += 1

                
            if event.button == 1 and rd==7 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                flush(l)
                t='同学们哟，欢迎来到浦北中学，从今天起大家就是我们浦J的一员，希望大家有无需提醒的自觉。'
                talk_box(xz,t,'陈校长')
                rd += 1


            if event.button == 1 and rd==6 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                '''screen.blit(pygame.transform.smoothscale(start_bg2,size),(0,0))
                study_b=Button(study_button,(w//6,h//12),(0,h//2-h//15))
                social_b=Button(social_button,(w//6,h//12),(0,h//2-h//15+h//12))
                shop_b=Button(shop_button,(w//6,h//12),(0,h//2-h//15+h//6))'''
                l=[Label(start_bg2,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
                    ]
                flush(l)
                t='20XX年9月1日 早上6:51，进城广场大阶梯处，开学典礼上。'
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==5 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
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
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
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
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),]
                t='底下那个是回合数,到一定的回合后，游戏结束。'
                flush(l)
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1



            if event.button == 1 and rd==3 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),
                   Label(text_box,(w//5*4,h//5),(w//10,h-h//5)),
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
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and rd==2 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4 :
                l=[Label(start_bg,(w,h),(0,0)),Label(text_box,(w//5*4,h//5),(w//10,h-h//5))]
                for z in l:
                    p=z.get_rect()
                    screen.blit(z,p[:2])
                textlabel('些啥呢？？',(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1

            
                    
            if event.button == 1 and start_game == 1 and mouse_pos[0] > 0 and mouse_pos[1] > h-h//4 and rd==1:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),Label(text_box,(w//5*4,h//5),(w//10,h-h//5))]
                t='这是一个类似于中国式家长的策略游戏，虽然没写好，没事，总会写好的'
                for z in l:
                    p=z.get_rect()
                    screen.blit(z,p[:2])
                textlabel(t,(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1


            if event.button == 1 and start_game==0 and start_b.get_range()[0] < mouse_pos[0] <start_b.get_range()[2] and start_b.get_range()[1] < mouse_pos[1] < start_b.get_range()[3] and rd==0:
                pygame.event.set_blocked([MOUSEBUTTONUP])
                l=[Label(start_bg,(w,h),(0,0)),Label(text_box,(w//5*4,h//5),(w//10,h-h//5))]
                start_g(l,size)
                textlabel('欢迎来到浦中帝国！！本游戏没有一丝丝教程，大家伙凑合这玩吧哈哈哈哈哈哈哈哈哈',(w//7.5,h-h//5.5),l,(w//1.4,h//1.2),0,0)
                rd += 1
                rd = 49


            
        




    pygame.display.update()
