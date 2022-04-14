import os


class PlayerStat:                         # Player Class Creation
  def __init__(self, Endurance, Strength):
    self.Endurance = Endurance
    self.Strength = Strength

  def Endurancefunc(self):                       # Defining Possible Functions
    print("Endurance = " + str(self.Endurance))
  def Strengthfunc(self):
    print("Strength = " + str(self.Strength))
  def sentancefun(self):
      arrayValue = [str(self.Endurance), " ", str(self.Strength)]
      print(''.join(arrayValue))


p1 = PlayerStat(40, 36)                     #Dataset grabbed by functions
p2 = PlayerStat(80, 50)

#print("Player 1 Stats")

#p1.namefunc()                               #Player1 Function Sequence
#p1.agefunc()

#print("Player 2 Stats")

#p2.namefunc()                               #Player2 Function Sequence
#p2.agefunc()

#p1.sentancefun()


Stats.p2.Endurancefunc()