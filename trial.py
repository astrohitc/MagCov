
print("Yes we know scipy and astropy exist")
def ConvertApptoAbs(app, distance):
    #if distance is in parsecs
    import numpy as np
    abs = app - 5*np.log10(distance) + 5
    return abs


def ConvertAbstoApp(abs, distance):
    #if distance is in parsecs
    import numpy as np
    app = 5*np.log10(distance) - 5 + abs
    return app
