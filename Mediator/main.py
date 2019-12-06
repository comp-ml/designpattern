import mediator

saito = mediator.Saito()

nitta  = mediator.Collegue('Nitta', saito)
ayumi  = mediator.Collegue('Ayumi', saito)
tomoko = mediator.Collegue('Tomoko', saito)
kenta  = mediator.Collegue('Kenta', saito)

nitta.set_secretlover(ayumi)
ayumi.set_secretlover(nitta)
tomoko.set_secretlover(nitta)
kenta.set_secretlover(tomoko)

saito.add_collegue(nitta)
saito.add_collegue(ayumi)
saito.add_collegue(tomoko)
saito.add_collegue(kenta)


print(nitta.need_advice())
print(ayumi.need_advice())
print(tomoko.need_advice())
print(kenta.need_advice())


