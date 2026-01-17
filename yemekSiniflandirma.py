# -*- coding: utf-8 -*-
import time

def color_sorting_python():
    # Simulate the array of green channel intensities
    COLOR_DATA = [120, 210, 50, 240, 15, 200, 90, 220]
    GREEN_THRESHOLD = 150  # Define the sorting threshold
    actuator_count = 0     # Initialize counter for items sorted (actuator usage)
    
    start_time = time.perf_counter() # Start timer
    
    # Iterate through each simulated item
    for color_intensity in COLOR_DATA:
        # Decision logic (Assembly: CMP/JLE/INC)
        if color_intensity > GREEN_THRESHOLD:
            # GREEN APPLE: Action needed (Simulate triggering the actuator)
            actuator_count += 1
        else:
            # RED APPLE: No action (Simulate letting it pass)
            pass
            
    end_time = time.perf_counter()  # Stop timer
    duration_ms = (end_time - start_time) * 1000
    
    return duration_ms

color_sorting_python()
