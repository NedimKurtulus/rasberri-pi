

# -*- coding: utf-8 -*-
import time

def sensor_threshold_python():
    # Assembly'deki veri dizisini ve byte yapısını taklit et
    SENSOR_DATA = [32, 21, 48, 18, 64, 10, 37, 26, 80, 5] 
    THRESHOLD = 48
    count_high = 0
    
    start_time = time.perf_counter()
    
    for reading in SENSOR_DATA:
        # Karşılaştırma ve Sayım
        if reading > THRESHOLD:
            count_high += 1
            
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    
    print(f"Python Sensör Kontrol Süresi: {duration_ms:.6f} ms. Eşiği Aşan: {count_high}")
    return duration_ms

sensor_threshold_python()
