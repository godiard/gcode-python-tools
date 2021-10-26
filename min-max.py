# get min and max valu from a gcode file
import sys

gcode_file_name = sys.argv[1]

print(f'Opening { gcode_file_name }')

min_x = None
min_y = None
max_x = None
max_y = None
min_z = None
max_z = None
with open(gcode_file_name) as gcode_file:
    for line in gcode_file.readlines():
        if line.startswith('G1'):
            coords = line.split()
            for coord in coords:
                try:
                    value = float(coord[1:])
                    if coord.startswith('X'):
                        if min_x is None or value < min_x:
                            min_x = value
                        if max_x is None or value > max_x:
                            max_x = value
                    if coord.startswith('Y'):
                        if min_y is None or value < min_y:
                            min_y = value
                        if max_y is None or value > max_y:
                            max_y = value
                    if coord.startswith('Z'):
                        if min_z is None or value < min_z:
                            min_z = value
                        if max_z is None or value > max_z:
                            max_z = value

                except Exception:
                    print(f'Exception on line "{ line }" part { coord }')

print('Min X: %f' % min_x)
print('Max X: %f' % max_x)
print('Min Y: %f' % min_y)
print('Max Y: %f' % max_y)
print('Min Z: %f' % min_z)
print('Max Z: %f' % max_z)
