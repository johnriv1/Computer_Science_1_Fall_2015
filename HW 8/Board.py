class Board(object):
    def __init__(self, board_info):
        self.name = board_info[0]
        self.gravity = int(board_info[1])
        self.portalx = int(board_info[2])
        self.portaly = int(board_info[3])
        self.rightboard = board_info[4]
        self.upboard = board_info[5]
        self.leftboard = board_info[6]
        self.downboard = board_info[7]
        
        self.obst_tups = []
        if len(board_info) > 8:
            obst_sep = board_info[8:]
            for k in range(len(obst_sep)):
                obst_sep[k] = int(obst_sep[k])
            for i in range(len(obst_sep)/2):
                self.obst_tups.append((obst_sep[2*i:(2*i+2)][0],obst_sep[2*i:(2*i+2)][1])) 
    
    #def __str__(self):
        #return 'name is %s\ngravity is %s\nportalx is %s\nportaly is %s\nrightboard is %s\nupboard is %s\nleftboard is %s\ndownboard is %s\nObstacles are %s' %(self.name, self.gravity, self.portalx, self.portaly, self.rightboard, self.upboard, self.leftboard, self.downboard,self.obst_tups)
    
    def __str__(self):
        return "Board %s: Portal location: (%d, %d), Gravity: %d\n    Obstacles at: %s\n    Portals to: right: %s, up: %s, left: %s, down: %s" %(self.name, self.portalx, self.portaly, self.gravity, str(self.obst_tups), self.rightboard, self.upboard, self.leftboard, self.downboard)

#f = (open('board2.txt')).read()
#boards = f.split('\n')
#board_info = boards[0].split('|')
#print Board(board_info)

##Board(board_info).name