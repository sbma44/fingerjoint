from fingerjoint import *

MATERIAL_WIDTH = 5.7
MATERIAL_VARIANCE = 0.1
KERF = 0.2


def main():
	width = 150
	height = 150
	depth = 75
	top_panel_FJM = FingerJointMaker(width, height, MATERIAL_WIDTH, (MATERIAL_WIDTH * (1.0 + MATERIAL_VARIANCE)), (2,2,2,2), KERF)
	top_panel_FJM.make()
	top_panel_FJM.svg(filename='top.svg')

	side_panel_FJM = FingerJointMaker(width, depth, MATERIAL_WIDTH, (MATERIAL_WIDTH * (1.0 + MATERIAL_VARIANCE)), (5,3,5,5), KERF)
	side_panel_FJM.make()
	side_panel_FJM.svg(filename='side.svg')


if __name__ == '__main__':
	main()