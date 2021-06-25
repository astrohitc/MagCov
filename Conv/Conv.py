
print("Yes we know scipy and astropy exist")


def ApptoAbs(app, distance):
    #if distance is in parsecs
    import numpy as np
    abs = app - 5*np.log10(distance) + 5
    return abs


def AbstoApp(abs, distance):
    #if distance is in parsecs
    import numpy as np
    app = 5*np.log10(distance) - 5 + abs
    return app


def LyrtoPc(lyr):
    import numpy as np
    pc = np.divide(lyr, 3.2612)
    return pc


def PctoLyr(pc):
    import numpy as np
    lyr = np.multiply(pc, 3.2612)
    return lyr


def CarttoSph(x = 0, y = 0, z = 0):
    import numpy as np
    if z == 0:
        theta = np.arctan(y/x)
        r = np.sqrt(x**2 + y**2)
        print("({},{}) in Polar form is ({},{})".format(x,y,r,theta))
    elif z != 0:
        theta = np.arctan(y/x)
        r = np.sqrt(x**2 + y**2 + z**2)
