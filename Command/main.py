import Command

beaker1 = Command.Beaker(0,100)
beaker2 = Command.Beaker(100,0)

command1 = Command.AddSaltCommand(beaker1)
command2 = Command.AddWaterCommand(beaker2)

command1.experiment()
command2.experiment()