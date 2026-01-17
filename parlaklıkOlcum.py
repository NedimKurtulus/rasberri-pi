# -*- coding: utf-8 -*-
import time

def image_brightness_python():
    # Assembly'deki piksel dizisini taklit et
    PIXEL_DATA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
    DATA_COUNT = len(PIXEL_DATA)
    
    start_time = time.perf_counter()
    
    sum_val = 0
    for pixel in PIXEL_DATA:
        sum_val += pixel
        
    # Ortalama Hesaplama
    average_val = sum_val / DATA_COUNT
    
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    
    print(f"Python Ortalama Parlaklık Süresi: {duration_ms:.6f} ms. Ortalama: {average_val}")
    return duration_ms

image_brightness_python()

