##Code for distance conversion

def ConvertApptoAbs(app, distance):
    #if distance is in parsecs
    import numpy as np
    abs = app - 5*np.log10(distance) + 5
    return abs

##Code for absolute to apparent magnitiude

def ConvertAbstoApp(abs, distance):
    #if distance is in parsecs
    import numpy as np
    app = 5*np.log10(distance) - 5 + abs
    return app
