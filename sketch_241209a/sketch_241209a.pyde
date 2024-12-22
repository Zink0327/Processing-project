lfu = 0
lfd = 1
rfu = 2
rfd = 3
lbu = 4
lbd = 5
rbu = 6
rbd = 7

cube_pos = [[1,1,1],
            [1,1,-1],   
            [-1,1,1],
            [-1,1,-1],
            [1,-1,1],
            [1,-1,-1],
            [-1,-1,1],
            [-1,-1,-1]
        ]
cube_color = ["0x0000ff",
            "0xff00ff",   
            "0x00ffff",
            "0xffffff",
            "0xff0000",
            "0x00ff00",
            "0xffff00",
            "0x000000"
        ]
def drawcube(cube_id):
    pushMatrix()
    translate(cube_pos[cube_id][0]*30, cube_pos[cube_id][1]*30, cube_pos[cube_id][2]*30)
    fill(cube_color[cube_id])
    box(60)
    popMatrix()
    
def L():
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
def R():
    cube_pos[rfu][0]*=1
    cube_pos[rfu][1]*=-1
    cube_pos[rfu][2]*=1
    
    cube_pos[rfd][0]*=1
    cube_pos[rfd][1]*=-1
    cube_pos[rfd][2]*=1
    
    cube_pos[rbu][0]*=1
    cube_pos[rbu][1]*=-1
    cube_pos[rbu][2]*=1
    
    cube_pos[rbd][0]*=1
    cube_pos[rbd][1]*=-1
    cube_pos[rbd][2]*=1
    
def U():
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
def D():
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
    
    cube_pos[rfd][0]*=1
    cube_pos[rfd][1]*=1
    cube_pos[rfd][2]*=-1
    
    cube_pos[rbu][0]*=1
    cube_pos[rbu][1]*=1
    cube_pos[rbu][2]*=-1
    
    cube_pos[rbd][0]*=1
    cube_pos[rbd][1]*=1
    cube_pos[rbd][2]*=-1
    
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
    global x,y,z,a
    size(800,800,P3D)
    x = width/2
    y = height/2
    z = 0
    a = 0
    translate(x,y,z)
    batch_draw()

def draw():
    global x,y,z,a
    translate(x,y,z)
    if keyPressed
    background(200)
    batch_draw()
