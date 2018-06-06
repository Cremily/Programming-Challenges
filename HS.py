class Player():
    def __init__(self,battlefield,mana):
        self.battlefield = battlefield
        self.mana = mana
player_1 = Player([],0)
player_2 = Player([],0)
class Minion:
    def __init__(self,name,attack,health,cost,desc,tribe):
        self.name = name
        self.attack = attack
        self.health = health
        self.cost = cost    
        self.desc = desc
    def control(self,player):
        self.owner = player
class Imp_Master(Minion):
    def summon_imp(self):
        Imp = Minion("Imp",1,1,1,"","Demon")
        Imp.control(self.owner)
        self.owner.battlefield.append(Imp)
        self.health -= 1
    def end_of_turn(self):
        self.summon_imp()
ID_1 = Imp_Master("Imp Master",1,5,3,"At the end of each turn, summon a 1/1 Demon and lose one health.",None)
ID_1.owner = player_1
curr_player = player_1
curr_player.battlefield.append(ID_1)
def end_of_turn():
    for minion in curr_player.battlefield:
        try:
            minion.end_of_turn()
        except:
            pass
end_of_turn()
print(curr_player.battlefield)