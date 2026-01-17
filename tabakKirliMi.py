# -*- coding: utf-8 -*-
import time

def plate_classification_python(stain_density=80, weight_val=15):
    # Sonuçlar: 1=Kirli, 0=Temiz, 2=Tekrar Kontrol
    result = None
    
    start_time = time.perf_counter()
    
    # KURAL 1: Leke Yoğunluğu > 75 ise -> Kirli
    if stain_density > 75:
        result = 1
    
    # KURAL 2: Leke <= 75 VE Ağırlık > 20 ise -> Kirli
    elif weight_val > 20:
        result = 1
        
    # KURAL 3: Leke <= 75 VE Ağırlık <= 20 VE Leke > 30 ise -> Tekrar Kontrol
    elif stain_density > 30:
        result = 2
        
    # KURAL 4: Geri Kalan -> Temiz
    else:
        result = 0
        
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    
    print(f"Python Sınıflandırma Süresi: {duration_ms:.6f} ms. Sonuç: {result}")
    return duration_ms

plate_classification_python()
