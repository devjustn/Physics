# 2/24/18
# Simulation of atom compression and rareficatoin
dt = 0.01
t = 0
T = 20
numberOfAtoms = 10


# sphere()
# sphere(pos = vector(0,0,0))

# box
h = 1
w = 1
l = 5
box(pos = vector(0, 0, 0), color = color.white, opacity = 0.17, height = h, width = w, length = l)

atoms = []

for i in range(500):
    x = l * random() - l/2
    y = h * random() - h/2
    z = w * random() - w/2
    atoms.append[sphere(pos=vector(x,y,z), radius=0.02, color=color.cyan)]

for i in range(100):
    x = l/8*random() - l/16
    y = h * random() - h/2
    z = w * random() - w/2
    sphere(pos=vector(x,y,z), radius=0.02, color=color.red)


# # Box
# bottom = curve(color = color.cyan, radius = 0.3)
# bottom.append([vector(1,1,1), vector(1,1,1), vector(1,1,1), vector(1,1,1), vector(1,1,1)])

# d = 1/2+00.04
# r = 0.005
# boxbottom = curve(color=color.cyan, radius=r)
# boxbottom.append([ vector(1,-1,1), vector(1,-1,-1)])
# boxtop = curve(color=gray, radius=r)
# boxtop.append([vector(-d,d,-d), vector(-d,d,d), vector(d,d,d), vector(d,d,-d), vector(-d,d,-d)])



# point = arrow(pos=vector(0, 0, 0), axis = vector(0, 0, 10), shaftwidth =1)