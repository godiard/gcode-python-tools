# get min and max valu from a gcode file
import sys

gcode_file_name = sys.argv[1]
z_delta = float(sys.argv[2])
print(f'Opening { gcode_file_name }')

with open(gcode_file_name) as gcode_file:
    for line in gcode_file.readlines():
        if line.startswith('('):
            # gcode comment
            print(line)
            continue
        coords = line.split()
        for coord in coords:
            value = float(coord[1:])
            if coord.startswith('Z'):
                new_z = value + z_delta
                new_coord = 'Z%f' % new_z
                line = line.replace(coord, new_coord)
                break
        print(line.strip())
