from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


window.fps_counter.enabled = False
window.exit_button.visible = False
mansion = Entity(model="assets/Mansion.obj", texture = "assets/Mansion")



class Voxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			scale = 0.5)


for z in range(40):
	for x in range(40):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()


app.run()