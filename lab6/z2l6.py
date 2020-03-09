class Player:
    def __init__(self,score,stacksAvailable):
        self.score=score
        self.stacksAvailable=stacksAvailable
class Node:
    def __init__(self,stacks,playerMove,player1 : Player,player2 : Player,prevTaken):
        self.stacks=stacks
        self.children=[]
        self.playerMove=playerMove
        self.player1=player1
        self.player2=player2
        self.prevTaken=prevTaken
        
    def checkMovesPossibility(self):
        stacksAvailableSum=self.player1.stacksAvailable + list(set(self.player2.stacksAvailable)-set(self.player1.stacksAvailable))
        for s in stacksAvailableSum:
            if(self.stacks[s]>0):
                return True
        return False
    
    def createTree(self):
        if self.playerMove:
            availableStacks = self.player1.stacksAvailable
        else:
            availableStacks = self.player2.stacksAvailable
        
        if(self.prevTaken==0):
            maxCoins=1
        else:
            maxCoins=2*self.prevTaken

        moveMade = False
        
        for stack in availableStacks:
            for coinsTaken in range(1, min(self.stacks[stack]+1, maxCoins+1)):
                coins_stacks = self.stacks.copy()
                coins_stacks[stack] -= coinsTaken
                moveMade = True
                if self.playerMove:
                    playerStacks = self.player1.stacksAvailable.copy()
                    score=self.player1.score + coinsTaken
                    playerStacks.remove(stack)
                    self.children.append(Node(coins_stacks,not self.playerMove,Player(score,playerStacks),Player(self.player2.score,self.player2.stacksAvailable),coinsTaken))
                else:
                    playerStacks = self.player2.stacksAvailable.copy()
                    score=self.player2.score + coinsTaken
                    playerStacks.remove(stack)
                    self.children.append(Node(coins_stacks,not self.playerMove,Player(self.player1.score,self.player1.stacksAvailable),Player(score,playerStacks),coinsTaken))
         
        if not moveMade:
            if (self.checkMovesPossibility()):
                self.children.append(Node(self.stacks.copy(),not self.playerMove,Player(self.player1.score,self.player1.stacksAvailable),Player(self.player2.score,self.player2.stacksAvailable),self.prevTaken))

    def start(self):
        self.createTree()
        for child in self.children:
            child.start()
            
def game(root):
    scores=[]
    if root.children == []:
        return(root.player1.score-root.player2.score)
    elif root.playerMove:
        for child in root.children:
            scores.append(game(child))
        return(max(scores))
    else :
        for child in root.children:
            scores.append(game(child))
        return(min(scores))

def simulate(stacks):
    tree = Node(stacks,True,Player(0,[0,1,2]),Player(0,[0,1,2]),0)
    tree.start()
    score = game(tree)
    print(stacks, 'Player 1: ', score, 'Player2: ', -score)

stacks = [[2,2,2],[3,3,3],[1,2,6]]

for stackx in stacks:
    simulate(stackx)
    
        