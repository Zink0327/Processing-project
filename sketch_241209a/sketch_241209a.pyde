#original blocks
lfu = 0
lfd = 1
rfu = 2
rfd = 3
lbu = 4
lbd = 5
rbu = 6
rbd = 7
#which block lands where 
lfuc = lfu
lfdc = lfd
rfuc = rfu
rfdc = rfd
lbuc = lbu
lbdc = lbd
rbuc = rbu
rbdc = rbd
cube_pos = [[-1,-1,1],
            [-1,1,1],   
            [1,-1,1],
            [1,1,1],
            [-1,-1,-1],
            [-1,1,-1],
            [1,-1,-1],
            [1,1,-1]
        ]
#object to: face vertical horizontal
#color no.,rotateY,rotateX
cube_ratio =  [[[0,0,0],[1,PI/2,0],[2,0,PI/2]],
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]],   
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]],
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]],
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]],
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]],
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]],
            [[0,0,0],[1,PI/2,0],[2,0,PI/2]]
        ]
cube_color = [["#FF7300","#005FFF","#FFF300"],
            ["#FF7300","#005FFF","#FFFFFF"],   
            ["#FF7300","#0BFF00","#FFF300"],
            ["#FF7300","#0BFF00","#FFFFFF"],
            ["#FF0004","#005FFF","#FFF300"],
            ["#FF0004","#005FFF","#FFFFFF"],
            ["#FF0004","#0BFF00","#FFF300"],
            ["#FF0004","#0BFF00","#FFFFFF"]
        ]

def drawcube(cube_id):
    pushMatrix()
    translate(cube_pos[cube_id][0]*30, cube_pos[cube_id][1]*30, cube_pos[cube_id][2]*60)  #up
    fill(cube_color[cube_id][cube_ratio[cube_id][0][0]])
    rotateY(cube_ratio[cube_id][0][1])
    rotateX(cube_ratio[cube_id][0][2])
    rect(0,0,60,60)
    popMatrix()
    
    pushMatrix()
    translate(cube_pos[cube_id][0]*60, cube_pos[cube_id][1]*30, cube_pos[cube_id][2]*30)  #left
    fill(cube_color[cube_id][cube_ratio[cube_id][1][0]])
    rotateY(cube_ratio[cube_id][1][1])
    rotateX(cube_ratio[cube_id][1][2])
    rect(0,0,60,60)
    popMatrix()
    
    pushMatrix()
    translate(cube_pos[cube_id][0]*30, cube_pos[cube_id][1]*60, cube_pos[cube_id][2]*30)  #right
    fill(cube_color[cube_id][cube_ratio[cube_id][2][0]])
    rotateY(cube_ratio[cube_id][2][1])
    rotateX(cube_ratio[cube_id][2][2])
    rect(0,0,60,60)
    popMatrix()
    
def L():
    global lfuc,lfdc,rfuc ,rfdc ,lbuc ,lbdc ,rbuc ,rbdc

    for i in [lfuc,lfdc,lbuc,lbdc]:
        a=cube_pos[i][2]
        cube_pos[i][2]=cube_pos[i][1]*-1
        cube_pos[i][1]=a
        aa=cube_ratio[i][0][0]
        cube_ratio[i][0][0]=cube_ratio[i][2][0]
        cube_ratio[i][2][0]=aa

    zz=lfuc
    lfuc=lbuc
    lbuc=lbdc
    lbdc=lfdc
    lfdc=zz

   
def R():
    global lfuc,lfdc,rfuc ,rfdc ,lbuc ,lbdc ,rbuc ,rbdc

    for i in [rfuc,rfdc,rbuc,rbdc]:
        a=cube_pos[i][1]
        cube_pos[i][1]=cube_pos[i][2]*-1
        cube_pos[i][2]=a
        aa=cube_ratio[i][0][0]
        cube_ratio[i][0][0]=cube_ratio[i][2][0]
        cube_ratio[i][2][0]=aa
    
    zz=rfuc
    rfuc=rfdc
    rfdc=rbdc
    rbdc=rbuc
    rbuc=zz
    
def U():
    global lfuc,lfdc,rfuc ,rfdc ,lbuc ,lbdc ,rbuc ,rbdc

    for i in [rfuc,lfuc,rbuc,lbuc]:
        a=cube_pos[i][0]
        cube_pos[i][0]=cube_pos[i][2]*-1
        cube_pos[i][2]=a
        aa=cube_ratio[i][0][0]
        cube_ratio[i][0][0]=cube_ratio[i][1][0]
        cube_ratio[i][1][0]=aa

    zz=rfuc
    rfuc=rbuc
    rbuc=lbuc
    lbuc=lfuc
    lfuc=zz

 

def D():
    global lfuc,lfdc,rfuc ,rfdc ,lbuc ,lbdc ,rbuc ,rbdc

    for i in [rfdc,lfdc,rbdc,lbdc]:
        a=cube_pos[i][2]
        cube_pos[i][2]=cube_pos[i][0]*-1
        cube_pos[i][0]=a
        aa=cube_ratio[i][0][0]
        cube_ratio[i][0][0]=cube_ratio[i][1][0]
        cube_ratio[i][1][0]=aa

    zz=rfdc
    rfdc=lfdc
    lfdc=lbdc
    lbdc=rbdc
    rbdc=zz
 
def F():
    global lfuc,lfdc,rfuc ,rfdc ,lbuc ,lbdc ,rbuc ,rbdc

    for i in [rfdc,lfdc,rfuc,lfuc]:
        a=cube_pos[i][0]
        cube_pos[i][0]=cube_pos[i][1]*-1
        cube_pos[i][1]=a
        aa=cube_ratio[i][2][0]
        cube_ratio[i][2][0]=cube_ratio[i][1][0]
        cube_ratio[i][1][0]=aa

    zz=rfuc
    rfuc=lfuc
    lfuc=lfdc
    lfdc=rfdc
    rfdc=zz

def B():
    global lfuc,lfdc,rfuc ,rfdc ,lbuc ,lbdc ,rbuc ,rbdc

    for i in [rbdc,lbdc,rbuc,lbuc]:
        a=cube_pos[i][1]
        cube_pos[i][1]=cube_pos[i][0]*-1
        cube_pos[i][0]=a
        aa=cube_ratio[i][2][0]
        cube_ratio[i][2][0]=cube_ratio[i][1][0]
        cube_ratio[i][1][0]=aa

    zz=rbuc
    rbuc=rbdc
    rbdc=lbdc
    lbdc=lbuc
    lbuc=zz

    
def batch_draw():
    drawcube(lfu)
    drawcube(lfd)
    drawcube(rfu)
    drawcube(rfd)
    drawcube(lbu)
    drawcube(lbd)
    drawcube(rbu)
    drawcube(rbd)
    
def drawcoord():
    line(0,0,100,0,0,200)
    line(0,0,100,-20,0,120)
    line(0,0,100,20,0,120)
    line(-20,0,210,-20,0,250)
    line(-20,0,230,20,0,230)
    line(-20,0,210,20,0,210)
    
def randomprocess():
    for i in range(10):
        index = int(random(6))
        if (index==0):
            R()
        if (index==1):
            L()
        if index==2:
            F()
        if index==3:
            B()
        if index==4:
            U()
        if index==5:
            D()

def setup():
    global x,y,z,a,cx,cy,cz,r,aa,bb,istri,isstart,tt,isend
    size(800,800,P3D)
    x = width/2
    y = height/2
    z = 0
    a = 0
    cx=PI/2 #theta x-z
    cy=0 #theta y-z
    r=y*2
    cz=0
    aa=400
    bb=400
    istri=1
    isstart=False
    isend=False
    tt="not started"
    rectMode(CENTER)
    textSize(40)
    translate(x,y,z)
    frameRate(60)
    rect(0,0,20,20)
    randomprocess()
    batch_draw()

def keyPressed():
    global istri,isstart,mmm,sss,isend
    if isstart==False and isend == False:
        mmm=minute()
        sss=second()
        isstart=True
    if (key=="r" or key=="R"):
        for i in range(istri):
            R()
    if (key=="l" or key=="L"):
        for i in range(istri):
            L()
    if key=="f" or key=="F":
        for i in range(istri):
            F()
    if key=="b" or key=="B":
        for i in range(istri):
            B()
    if key=="u" or key=="U":
        for i in range(istri):
            U()
    if key=="d" or key=="D":
        for i in range(istri):
            D()
    if key=="'":
        if istri == 1:
            istri=3
        else:
            istri=1
    if key == " ":
        isend = True
    delay(110)

def draw():
    global x,y,z,a,cx,cy,cz,r,aa,bb,isstart,tt,mmm,sss,isend
    
    translate(x,y,z)
    if mousePressed:
        aa=mouseY
        bb=mouseX
    lz=0.002*PI*(mouseX-bb)
    lz+=0.002*PI*(mouseY-aa)
    lx=0.002*PI*(mouseX-bb)
    ly=0.002*PI*(mouseY-aa)
    cz=lz
    cx=lx
    cy=ly
    if isstart and (not isend):
        ss=str(second()-sss+(minute()-mmm)*60)
        tt=ss+"s"
    camera(r*cos(cx),r*cos(cy),r*sin(cz),x,y,0,0,1,0)
    translate(x,y,z)

        
    background(200)
    fill(0)
    text(tt, 172, 175, 0)
    batch_draw()
    drawcoord()
