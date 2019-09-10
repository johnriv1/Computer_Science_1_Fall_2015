from Board import *

class Rick(object):
    def __init__(self, rick_info):
        self.curr_boardname = rick_info[0]
        self.prev_boardname = rick_info[0]
        self.first_boardname = rick_info[0]
        self.x0 = int(rick_info[1])
        self.y0 = int(rick_info[2])
        self.size = int(rick_info[3])
        self.dx = float(rick_info[4])
        self.dy = float(rick_info[5])
        self.bool = False
        
    #def __str__(self):
        #return "boardname is %s\nx0 is %s\ny0 is %s\nsize is %s\ndx is %s\ndy is %s" %(self.boardname, self.x0, self.y0, self.size, self.dx, self.dy)
    
    def __str__(self):
        return "Time 0: Rick of %s is in %s board at (%d, %d) with speed (%.1f, %.1f)" %(self.first_boardname, self.curr_boardname, self.x0, self.y0, self.dx, self.dy)
    
    def move(self, board_dict):              ### board --> dictionary of {boardname: correspondant board object}
        
        self.bool = False
        
        for b in board_dict:
            if b == self.curr_boardname:
                board = board_dict[b]
                
        self.x0 += self.dx/(board.gravity)
        self.y0 += self.dy/(board.gravity)
        
        ### Colision Checking ######################################################################################################################################################
        
        for coord in board.obst_tups:
            
            if coord[0] >= self.x0 and coord[0] <= (self.x0 + length) and coord[1] >= self.y0 and coord[1] <= self.y0 + length:  ##if obstacle collids with rick box
            
                self.dx = self.dx*(-1)
                self.dy = self.dy*(-1)
                self.dx = (self.dx)/2
                self.bool = True
                return "Rick of %s crashed into object at (%d, %d) in %s board\n   New speed is (%.1f, %.1f)" %(board.name, self.x0, self.y0, board.name, self.dx, self.dy)
        
        ### Boundary checking ######################################################################################################################################################
        
        if self.y0 <= 0 or self.x0 <= 0 or (self.x0 + self.size) >= 1000 or (self.y0 + self.size) >= 1000:
            
            Past_str = "    Past Location: Rick of %s is in %s at (%d, %d) with (%.1f, %.1f)\n" %(self.first_boardname, self.curr_boardname, self.x0, self.y0, self.dx, self.dy)
            self.prev_boardname = self.curr_boardname
            
            self.bool = True
            
            if self.y0 <= 0 and self.x0 <= 0:
                self.curr_boardname = board.leftboard
            elif (self.x0 + self.size) >= 1000 and (self.y0 + self.size) >= 1000:
                self.curr_boardname = board.rightboard
            elif self.y0 <= 0:
                self.curr_boardname = board.upboard
            elif self.x0 <= 0:
                self.curr_boardname = board.leftboard
            elif (self.x0 + self.size) >= 1000:
                self.curr_boardname = board.rightboard
            elif (self.y0 + self.size) >= 1000:
                self.curr_boardname = board.downboard   
            
            for b in board_dict:
                if b == self.curr_boardname:
                    board = board_dict[b]            
            
            self.x0 = board.portalx
            self.y0 = board.portaly
            
            Moved_str = "Rick of %s moved from %s to %s board\n" %(self.first_boardname, self.prev_boardname, self.curr_boardname)
            
            Curr_str = "    Current location: Rick of %s is in %s board at (%d, %d) with speed (%.1f, %.1f)" %(self.first_boardname, self.curr_boardname, self.x0, self.y0, self.dx, self.dy)
            
            return Moved_str + Past_str + Curr_str
        
        return "Rick of %s is in %s board at (%d, %d) with speed (%.1f, %.1f)" %(self.first_boardname,self.curr_boardname, self.x0, self.y0, self.dx, self.dy)
    
    #def boolean(self):
        #if self.bool == False:
            #return False
        #elif self.bool == True:
            #return True 
        
        #elif self.x0 <= 0:
        #elif (self.x0 + self.size) >= 1000:
        #elif (self.y0 + self.size) >= 1000:
            
            

##f = (open('rick1.txt')).read()
##ricks = f.split('\n')
##rick_info = ricks[0].split('|')
##print Rick(rick_info)