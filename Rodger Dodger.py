from tkinter import *
from time import *
from math import *
from random import *
root = Tk()
s = Canvas( root, width=600, height=800, background = "white" )
s.pack()

### Image Imports #########
heart1=PhotoImage(file="heart.gif")
heart1=heart1.subsample(20,20)
heart2=PhotoImage(file="heart.gif")
heart2=heart1.subsample(20,20)
heart3=PhotoImage(file="heart.gif")
heart3=heart1.subsample(20,20)
heart4=PhotoImage(file="heart.gif")
heart4=heart1.subsample(20,20)
heart5=PhotoImage(file="heart.gif")
heart5=heart1.subsample(20,20)
plane1=PhotoImage(file="plane.gif")
plane1=plane1.subsample(4,4)
plane2=PhotoImage(file="plane.gif")
plane2=plane2.subsample(1,1)           
missile=PhotoImage(file="missile.gif")
missile=missile.subsample(4,4)
missile2=PhotoImage(file="missile.gif")
missile2=missile2.subsample(3,3)
missile3=PhotoImage(file="missile.gif")
missile3=missile3.subsample(2,2)
missile4=PhotoImage(file="missile.gif")
missile4=missile4.subsample(1,1)
extralife=PhotoImage(file="extralife.gif")
extralife=extralife.subsample(20,20)
plane3=PhotoImage(file="intro plane.gif")
plane3=plane3.subsample(3,3)
plane4=PhotoImage(file="intro plane.gif")
plane4=plane4.subsample(10,10)
flames=PhotoImage(file="flames.gif")
flames=flames.subsample(5,5)
flames2=PhotoImage(file="flames.gif")
flames=flames2.subsample(5,5)
cloud=PhotoImage(file="cloud.gif")

####Initialize Global Variables ####
bonusLife=False
bonuscount=0
bulletcount=0
total=0
Line2=[]
newScore=0


def BlockSetup(): ### Draws initial Blocks ###
    global xBlock,yBlock,xBlockSize,yBlockSize,Block,numblocks,BlockSpeed,total,ResetLife,missilegif
    xBlock=[]
    yBlock=[]
    xBlockSize=[]
    yBlockSize=[]
    Block=[]
    missilegif=[]
    BlockSpeed=[]

    for i in range(numblocks):
        
            NewBlockSpeed=randint(2,8)                                 
            BlockSpeed.append(NewBlockSpeed)
            
            NewxBlock=randint(-5,605)
            NewyBlock=randint(-300,0)

            NewxBlockSize=randint(5,15)
            NewyBlockSize=randint(10,35)

            Block.append(0)
            
            xBlock.append(NewxBlock)
            yBlock.append(NewyBlock)

            xBlockSize.append(NewxBlockSize)
            yBlockSize.append(NewyBlockSize)
            missilegif.append(0)
            
def Blocks(): ### Updates Blocks Every Frame ### 
        global yBlock,xBlock,xBlockSize,yBlockSize,Block,numblocks,BlockSpeed,Line2,total,ResetLife,missilegif,missile,bonuscount,bonusLife,yBullet,xBullet
       
        if total<=5:
            
            for i in range(numblocks):
                
                yBlock[i]=yBlock[i]+BlockSpeed[i]

                if yBlock[i]>750:
                    yBlock[i]=-50
                    
                if yBlockSize[i]>30:
                    missilegif[i]=s.create_image((xBlock[i]+5),(yBlock[i]+5),image=missile3)

                elif 20<=yBlockSize[i]<=30:
                    missilegif[i]=s.create_image((xBlock[i]+5),(yBlock[i]+5),image=missile2)
                

                elif yBlockSize[i]>=10:
                    missilegif[i]=s.create_image((xBlock[i]+5),(yBlock[i]+5),image=missile)                   

                if xPos<=xBlock[i]+xBlockSize[i]<=xPos+xSize and yPos<=yBlock[i]+yBlockSize[i]<=yPos+xSize:
                    if bonusLife==True:
                        bonuscount=1
                        bonusLife=False
                    else:
                        total=total+1
                    LifeCounter()
                                   
                elif xPos<=xBlock[i]<=xPos+xSize and yPos<=yBlock[i]<=yPos+xSize:

                    if bonusLife==True:
                        bonuscount=1
                        bonusLife=False

                    else:
                        total=total+1
                    LifeCounter()
                    
                    
                elif xPos<=xBlock[i]<=xPos+xSize and yPos<=yBlock[i]+yBlockSize[i]<=yPos+xSize:

                    if bonusLife==True:
                        bonuscount=1
                        bonusLife=False                       

                    else:
                        total=total+1                                   
                    LifeCounter()
                    


     
                elif xPos<=xBlock[i]+xBlockSize[i]<=xPos+xSize and yPos<=yBlock[i]<=yPos+xSize:

                    if bonusLife==True:
                        bonuscount=1
                        bonusLife=False

                    else:
                         total=total+1
                    LifeCounter()

            s.update()
            endGame()
            for i in range(numblocks):
                s.delete(missilegif[i])


def setInitialValues(): ### draws plane in  a specific location after a life ###
    global xSpeed,ySpeed,xPos,yPos,xSize,ResetLife,Line1,ScoreText
    xPos=300
    yPos=660
    xSize=20
    xSpeed=0
    ySpeed=0
    ResetLife=False
    colour="black"
    
def drawIntroScreen(): ### Intro buttons and animations ###
    global playButton, line1,line2,easyButton, normalButton,introcloud,RodgerText,DodgerText,TopLine,BottomLine,introplane1,introplane2,intromissile1,intromissile2,intromissile3,intromissile4,instructionsButton, hardButton,bolt1,bolt2,bolt3,bolt4,bgpic2,bgpic4,bgpic5,bgpic6,bgpic7,intropong1,intropong2,line3, line4,introBall1,introBall2

    introcloud=s.create_image(300,400,image=cloud)
    
    RodgerText=s.create_text(200,300,text="RODGER", font="Times 40",fill="black",anchor=W)
    DodgerText=s.create_text(240,330,text="DODGER", font="Times 40",fill="gold",anchor=W)

    TopLine=s.create_rectangle(200,278,400,285,fill="wheat")
    BottomLine=s.create_rectangle(200,343,400,350,fill="wheat")

    introplane1=s.create_image(100,500,image=plane3)
    introplane2=s.create_image(510,500,image=plane3)

    intromissile1=s.create_image(70,80,image=missile4)
    intromissile2=s.create_image(130,150,image=missile4)

    intromissile3=s.create_image(470,80,image=missile4)
    intromissile4=s.create_image(530,150,image=missile4)
    
    easyButton = Button(root, text="EASY",font="Times 20", command=easyButtonPressed, anchor=CENTER)
    easyButton.pack()
    easyButton.place(x=250, y=500)

    normalButton = Button(root, text= "MEDIUM",font="Times 20", command=normalButtonPressed, anchor=CENTER)
    normalButton.pack()
    normalButton.place(x=230, y=575)

    hardButton = Button(root, text="HARD",font="Times 20", command=hardButtonPressed, anchor=CENTER)
    hardButton.pack()
    hardButton.place(x=250, y=650)
    
#### Runs game on three difficulties based on what was pressed by user ###
def easyButtonPressed():
    global yBallSpeed2,numblocks,playButton, line1,line2,easyButton, normalButton, hardButton,xBallSpeed,easySpeed,bgpic2,bgpic4,bgpic5,bgpic6,bgpic7,intropong1,intropong2,line3, line4,introBall1,introBall2
    numblocks=45
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    s.delete(RodgerText,DodgerText,TopLine,BottomLine,introplane1,introplane2,intromissile1,intromissile2,intromissile3,intromissile4)
    s.update()
    runGame()
    
def normalButtonPressed():
    global numblocks
    numblocks=75
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    s.delete(RodgerText,DodgerText,TopLine,BottomLine,introplane1,introplane2,intromissile1,intromissile2,intromissile3,intromissile4)
    s.update()
    runGame()

def hardButtonPressed():
    global numblocks
    numblocks=100
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    s.delete(RodgerText,DodgerText,TopLine,BottomLine,introplane1,introplane2,intromissile1,intromissile2,intromissile3,intromissile4)
    s.update()
    runGame()


def LifeCounter(): ### and keep track of lives lost and deals with Bonus heart### 
    global total,heart1Draw,heart2Draw,heart3Draw,heart4Draw,extraheartDraw,heart5Draw,ResetLife,score,EndGame,newLine2,bonuscount2,Line1,newScore,colour,ScoreText,Block,bonuscount,extraheartDraw

    if bonuscount==1:
            s.delete(extraheartDraw)
            bonuscount=0
            bonuscount2=bonuscount2-1
            ResetLife=True
            
    else:
        if total==1:
            ResetLife=True
            s.delete(heart5Draw)
        
        if total==2:
            ResetLife=True
            s.delete(heart4Draw)
            
        if total==3:
            ResetLife=True
            s.delete(heart3Draw)
            
        if total==4:
            ResetLife=True
            s.delete(heart2Draw)
            
            
        if total==5:
            s.delete(Line1,ScoreText,heart1Draw)
            colour="white"
                
def KeyPressedHandler(event):
    global ySpeed, xSpeed
    if event.keysym== "Up":
        ySpeed=-5
    if event.keysym=="Down":
        ySpeed=5
    if event.keysym=="Right":
        xSpeed=5
    if event.keysym=="Left":
        xSpeed=-5
        
    if event.keysym=="space":
        ShootMechanic()
      
def KeyUpHandler(event):
    global ySpeed,xSpeed
    ySpeed=0
    xSpeed=0
    
def drawBody(): ## Draws Plane ###
    global xSpeed,ySpeed,xPos,yPos,body,NorthLine,SouthLine,EastLine,WestLine,bodygif

    bodygif=s.create_image(xPos+8,yPos+20,image=plane4)
    
def updateBody(): ## updates plane every frame ##
    global xSpeed,ySpeed,xPos,yPos
    if xPos>600:
        xPos=0
    if xPos<0:
        xPos=600
    if yPos>650:
        yPos=650
    if yPos<0:
        yPos=0
    yPos=yPos+ySpeed
    xPos=xPos+xSpeed
    
def DrawHearts():
    global heart1Draw,heart2Draw,heart3Draw,heart4Draw,heart5Draw,Line1,ScoreText
    
    heart1Draw=s.create_image(130,100,image=heart1)
    heart2Draw=s.create_image(150,100,image=heart1)
    heart3Draw=s.create_image(170,100,image=heart1)
    heart4Draw=s.create_image(190,100,image=heart1)
    Line1 = s.create_text(50, 100, text= "Lives:",font="Times 25", fill="black", anchor=W)
    heart5Draw=s.create_image(210,100,image=heart1)
    ScoreText=s.create_text(475,100,text="Score:", font="Times 25",fill="black",anchor=W)

def drawScore(): 
    global newLine2

    newLine2=s.create_text(900,100,text=score, font="Times 25",fill="white",anchor=W)
    
def endGame(): 
    global total,TryAgain,FinalScore,FinalScoreText,extraheartDraw
    
    if total==6:
            GameOverText=s.create_text(130,300,text="GAME OVER!",font="Times 50",fill="black", anchor=W)
            
            FinalScoreText = s.create_text(100,400,text="Your final score was:",font = "Times 40", fill="black", anchor=W) 
            FinalScore = s.create_text(450,400,text=score,font = "Times 40", fill="black", anchor=W) 
                       
            TryAgain = Button(root, text = "Back To Main Menu", font = "Times 40", command = TryAgainPressed, anchor=CENTER)
            TryAgain.pack()
            TryAgain.place(x = 120, y = 500)
            
def TryAgainPressed(): ### Restarts game stats and life counter ####
    global total,score,TryAgain,FinalScore,FinalScoreText,bonusLife,bonuscount
    
    TryAgain.destroy()
    drawIntroScreen()
    s.delete(FinalScore,FinalScoreText)
    total=0
    bonusLife=False
    bonuscount=0
    LifeCounter()
    score=0

def runGame(): ## Main loop of game and keeps everything running in a for loop ##
    global score,Line2,newScore,colour,xSize,missile,total,extraheartDraw,bonusLife,bonuscount2
    
    setInitialValues()
    BlockSetup()
    DrawHearts()
    score=0
    colour="black"
    bonuscount2=0
        
    for t in range(10000):

        if t%20==0:
            s.delete(newScore)
            score = score+1

            if score%40==0:
                bonusLife=True
                bonuscount2=bonuscount2+1
                extraheartDraw=s.create_image(240,100,image=extralife)

                if total==6:
                    s.delete(extraheartDraw)                                    
            newScore = s.create_text(560,100,text=score,font = "Times 25", fill=colour, anchor=W)

        drawBody()
        Blocks()
        updateBody()
        s.delete(bodygif)

        for i in range(numblocks):
            if ResetLife==True:
                s.delete(Block[i])
                setInitialValues() 
                BlockSetup()
                s.update()



root.after(0,drawIntroScreen)
s.bind("<Key>", KeyPressedHandler)
s.bind("<KeyRelease>", KeyUpHandler)
s.pack()
s.focus_set()
root.mainloop()
