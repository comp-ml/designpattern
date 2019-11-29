import Builder
import Director

builder = Builder.SaltWaterBuilder()
director = Director.SaltDirector(builder)
status = director.get_status()
print(status.salt, status.water)

director.construct()

status = director.get_status()
print(status.salt, status.water)

director.construct()

status = director.get_status()
print(status.salt, status.water)
