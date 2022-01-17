from phue import Bridge
from time import sleep
ip = ''
b = Bridge(ip)
b.connect()
# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

b.get_light(1, 'on')
# Prints if light 1 is on or not
b.get_light('light')
lights = b.lights
# Print light names
for l in lights:
    print(l.name)

# Set brightness of each light to 127
for l in lights:
    sas = b.get_light(1, 'on')
    print(sas)

    b.set_light(1, 'on', True)
    l.brightness = 127
start = True
color = 0

b.set_light(1, 'on', True)
while start:
    while color < 65400:
        color = color + 200
        b.set_light(1, 'hue', color)
        print(color)
    if color == 200:
        pass
    else:
        color = 1
        b.set_light(1, 'hue', color)
        print(color)
