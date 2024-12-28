lfu = 0
lfd = 1
rfu = 2
rfd = 3
lbu = 4
lbd = 5
rbu = 6
rbd = 7

cube_pos = [[-1,-1,-1],
            [-1,1,-1],   
            [1,-1,-1],
            [1,1,-1],
            [-1,-1,1],
            [-1,1,1],
            [1,-1,1],
            [1,1,1]
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
    a=cube_pos[lfu][2]
    cube_pos[lfu][2]=cube_pos[lfu][1]*-1
    cube_pos[lfu][1]=a
    if cube_ratio[lfu][0][0] == 0:
        cube_ratio[lfu][0][0]=2
        cube_ratio[lfu][2][0]=0
    else:
        cube_ratio[lfu][0][0]=0
        cube_ratio[lfu][2][0]=2

    b=cube_pos[lfd][2]
    cube_pos[lfd][2]=cube_pos[lfd][1]*-1
    cube_pos[lfd][1]=b
    if cube_ratio[lfd][0][0] == 0:
        cube_ratio[lfd][0][0]=2
        cube_ratio[lfd][2][0]=0
    else:
        cube_ratio[lfd][0][0]=0
        cube_ratio[lfd][2][0]=2

    c=cube_pos[lbu][2]
    cube_pos[lbu][2]=cube_pos[lbu][1]*-1
    cube_pos[lbu][1]=c
    if cube_ratio[lbu][0][0] == 0:
        cube_ratio[lbu][0][0]=2
        cube_ratio[lbu][2][0]=0
    else:
        cube_ratio[lbu][0][0]=0
        cube_ratio[lbu][2][0]=2

    d=cube_pos[lbd][2]
    cube_pos[lbd][2]=cube_pos[lbd][1]*-1
    cube_pos[lbd][1]=d
    if cube_ratio[lbd][0][0] == 0:
        cube_ratio[lbd][0][0]=2
        cube_ratio[lbd][2][0]=0
    else:
        cube_ratio[lbd][0][0]=0
        cube_ratio[lbd][2][0]=2

    
def R():
    a=cube_pos[rfu][1]
    cube_pos[rfu][1]=cube_pos[rfu][2]*-1
    cube_pos[rfu][2]=a
    if cube_ratio[rfu][0][0] == 0:
        cube_ratio[rfu][0][0]=2
        cube_ratio[rfu][2][0]=0
    else:
        cube_ratio[rfu][0][0]=0
        cube_ratio[rfu][2][0]=2

    b=cube_pos[rfd][1]
    cube_pos[rfd][1]=cube_pos[rfd][2]*-1
    cube_pos[rfd][2]=b
    if cube_ratio[rfd][0][0] == 0:
        cube_ratio[rfd][0][0]=2
        cube_ratio[rfd][2][0]=0
    else:
        cube_ratio[rfd][0][0]=0
        cube_ratio[rfd][2][0]=2

    c=cube_pos[rbu][1]
    cube_pos[rbu][1]=cube_pos[rbu][2]*-1
    cube_pos[rbu][2]=c
    if cube_ratio[rbu][0][0] == 0:
        cube_ratio[rbu][0][0]=2
        cube_ratio[rbu][2][0]=0
    else:
        cube_ratio[rbu][0][0]=0
        cube_ratio[rbu][2][0]=2

    d=cube_pos[rbd][1]
    cube_pos[rbd][1]=cube_pos[rbd][2]*-1
    cube_pos[rbd][2]=d
    if cube_ratio[rbd][0][0] == 0:
        cube_ratio[rbd][0][0]=2
        cube_ratio[rbd][2][0]=0
    else:
        cube_ratio[rbd][0][0]=0
        cube_ratio[rbd][2][0]=2
    
def U():
    a=cube_pos[rfu][1]
    cube_pos[rfu][1]=cube_pos[rfu][0]*-1
    cube_pos[rfu][0]=a
    if cube_ratio[rfu][0][0] == 0:
        cube_ratio[rfu][0][0]=1
        cube_ratio[rfu][1][0]=0
    else:
        cube_ratio[rfu][0][0]=0
        cube_ratio[rfu][1][0]=1
    
    b=cube_pos[lfu][1]
    cube_pos[lfu][1]=cube_pos[lfu][0]*-1
    cube_pos[lfu][0]=b
    if cube_ratio[lfu][0][0] == 0:
        cube_ratio[lfu][0][0]=1
        cube_ratio[lfu][1][0]=0
    else:
        cube_ratio[lfu][0][0]=0
        cube_ratio[lfu][1][0]=1
    
    c=cube_pos[rbu][1]
    cube_pos[rbu][1]=cube_pos[rbu][0]*-1
    cube_pos[rbu][0]=c
    if cube_ratio[rbu][0][0] == 0:
        cube_ratio[rbu][0][0]=1
        cube_ratio[rbu][1][0]=0
    else:
        cube_ratio[rbu][0][0]=0
        cube_ratio[rbu][1][0]=1
    
    d=cube_pos[lbu][1]
    cube_pos[lbu][1]=cube_pos[lbu][0]*-1
    cube_pos[lbu][0]=d
    if cube_ratio[lbu][0][0] == 0:
        cube_ratio[lbu][0][0]=1
        cube_ratio[lbu][1][0]=0
    else:
        cube_ratio[lbu][0][0]=0
        cube_ratio[lbu][1][0]=1
def D():
    cube_pos[rfu][0]*=-1
    cube_pos[rfu][1]*=1
    cube_pos[rfu][2]*=1
    
    cube_pos[rfd][0]*=-1
    cube_pos[rfd][1]*=1
    cube_pos[rfd][2]*=1
    
    cube_pos[rbu][0]*=-1
    cube_pos[rbu][1]*=1
    cube_pos[rbu][2]*=1
    
    cube_pos[rbd][0]*=-1
    cube_pos[rbd][1]*=1
    cube_pos[rbd][2]*=1
def F():
    cube_pos[rfu][0]*=1
    cube_pos[rfu][1]*=1
    cube_pos[rfu][2]*=-1
    
    cube_pos[rfd][0]*=1
    cube_pos[rfd][1]*=1
    cube_pos[rfd][2]*=-1
    
    cube_pos[rbu][0]*=1
    cube_pos[rbu][1]*=1
    cube_pos[rbu][2]*=-1
    
    cube_pos[rbd][0]*=1
    cube_pos[rbd][1]*=1
    cube_pos[rbd][2]*=-1
def B():
    cube_pos[rfu][0]*=1
    cube_pos[rfu][1]*=1
    cube_pos[rfu][2]*=-1
    
    cube_pos[rfd][0]*=-1
    cube_pos[rfd][1]*=1
    cube_pos[rfd][2]*=1
    
    cube_pos[rbu][0]*=-1
    cube_pos[rbu][1]*=1
    cube_pos[rbu][2]*=1
    
    cube_pos[rbd][0]*=-1
    cube_pos[rbd][1]*=1
    cube_pos[rbd][2]*=1
    
def batch_draw():
    drawcube(lfu)
    drawcube(lfd)
    drawcube(rfu)
    drawcube(rfd)
    drawcube(lbu)
    drawcube(lbd)
    drawcube(rbu)
    drawcube(rbd)
    
def setup():
    global x,y,z,a,cx,cy,cz,r,aa,bb
    size(800,800,P3D)
    x = width/2
    y = height/2
    z = 0
    a = 0
    cx=0 #theta x-z
    cy=0 #theta y-z
    r=y/tan(PI/6)
    cz=PI/2
    aa=mouseY
    bb=mouseX
    rectMode(CENTER)
    translate(x,y,z)
    frameRate(60)
    rect(0,0,20,20)
    batch_draw()

def draw():
    global x,y,z,a,cx,cy,cz,r,aa,bb
    
    translate(x,y,z)
    if mousePressed:
        aa=mouseY
        bb=mouseX
    lz=0.001*PI*(mouseX-bb)
    lz+=0.001*PI*(mouseY-aa)
    lx=0.001*PI*(mouseX-bb)
    ly=0.001*PI*(mouseY-aa)
    cz=lz
    cx=lx
    cy=ly
    
    camera(r*cos(cx),r*cos(cy),r*sin(cz),x,y,0,0,1,0)
    translate(x,y,z)
    if keyPressed:
        if (key=="r" or key=="R"):
            R()
            delay(100)
        if (key=="l" or key=="L"):
            L()
            delay(100)
        if key=="f" or key=="F":
            F()
            delay(100)
        if key=="b" or key=="B":
            B()
            delay(100)
        if key=="u" or key=="U":
            U()
            delay(100)
        if key=="d" or key=="D":
            D()
            delay(100)
        
        
    background(200)
    batch_draw()
