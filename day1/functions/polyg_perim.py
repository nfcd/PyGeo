# import numpy library
import numpy as np

def polyg_perim(polyg,step):
    """
    calculate the perimeter of a polygon
    from the polygon points (n x 2 array) and the
    average length of the segments as represented
    by step: 1 (all points), 2 (every two points), etc.
    Note: points must be in sequential order
    """
    npoints = polyg.shape[0] # number of points
    perimeter = 0.0 # initialize perimeter to 0.0
    
    # calculate polygon´s perimeter
    for i in range(0,npoints,step):
        # current point
        point_1 = polyg[i,:]
        # next point:
        # if i is last point, connect to first point
        # this closes the polygon
        if i >= npoints-step:
            point_2 = polyg[0,:]
        # else use next point, i +  step
        else:
            point_2 = polyg[i+step,:]
        # add the segment to the perimeter
        perimeter += np.sqrt((point_1[0]-point_2[0])**2 + \
                             (point_1[1]-point_2[1])**2)
    
    return perimeter