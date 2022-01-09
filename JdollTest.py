from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


window.fps_counter.enabled = False
window.exit_button.visible = False


class Voxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			#color = color.color(0,0,random.uniform(0.20,1)),
			scale = 0.5)


class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			scale = 150,
			double_sided = True)


for z in range(40):
	for x in range(40):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()


app.run()