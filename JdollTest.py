from ursina import *


# update is run every frame
def update():
	#print('test')
	if held_keys['a']:
		cube.x -= 1 * time.dt


app = Ursina()


cube = Entity(model='quad', color=color.orange, scale = (2,5), position = (5,1))






app.run()