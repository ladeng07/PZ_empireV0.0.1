import pygame

class Button(pygame.Surface):
    def __init__(self,sf,size,position,screen,text=None,c=1,power=(0,0,0,0,0,0),ima=None):
        self.sf=sf
        self.size=size
        self.position=position
        self.status=0
        self.c=0
        self.ima=ima
        self.power=power
        self.text=text
        self.screen=screen
        pygame.Surface.__init__(self,size)
        self.blit(self.screen.subsurface(pygame.Rect(self.position+self.size)),(0,0))
        print(self.sf)
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
            

