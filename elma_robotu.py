import cv2
import RPi.GPIO as GPIO
import time

# =============================
# RASPBERRY PI SERVO KURULUMU
# =============================
SERVO_PIN = 18   # BCM pin numarası
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM sinyali
servo.start(0)

def servo_hareket(duty):
    """Servo motoru istenen duty cycle’a götür."""
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    time.sleep(0.2)

# =============================
# KAMERA AÇILIYOR
# =============================
kamera = cv2.VideoCapture(0)
time.sleep(2)  # kamera ısınma süresi


# =============================
# RENK ALGILAMA FONKSİYONU
# =============================
def renk_algila(frame):
    """Görüntüdeki elmanın rengini tespit eder."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # YEŞİL elma HSV aralığı
    lower_green = (40, 70, 70)
    upper_green = (80, 255, 255)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # KIRMIZI elma HSV aralığı (iki bölge)
    lower_red1 = (0, 70, 50)
    upper_red1 = (10, 255, 255)
    lower_red2 = (170, 70, 50)
    upper_red2 = (180, 255, 255)
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)

    if cv2.countNonZero(mask_green) > 800:
        return "green"
    elif cv2.countNonZero(mask_red) > 800:
        return "red"
    else:
        return "none"


# =============================
# ROBOT KOLU HAREKETLERİ
# =============================
def kol_al_ve_kutuya_koy():
    """Yeşil elmayı alıp kutuya koyan hareket dizisi."""
    print("Yeşil elma tespit edildi → alınıyor ve kutuya bırakılıyor.")

    # Kol aşağı in → elmayı al
    servo_hareket(7)

    # Kol yukarı çık
    servo_hareket(12)

    # Kutunun olduğu pozisyona git
    servo_hareket(5)

    # Elmayı bırak (hafif geri çekil)
    servo_hareket(10)


def kol_birak():
    """Kırmızı elmaya dokunma."""
    print("Kırmızı elma tespit edildi → banda devam.")


# =============================
# ANA DÖNGÜ
# =============================
print("Sistem çalışıyor... CTRL+C ile durdurabilirsin.")

try:
    while True:
        ret, frame = kamera.read()
        if not ret:
            continue

        renk = renk_algila(frame)

        if renk == "green":
            kol_al_ve_kutuya_koy()
            time.sleep(0.5)

        elif renk == "red":
            kol_birak()
            time.sleep(0.5)

        # Kamerayı kapatmadan önce ufak gecikme
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program durduruldu.")

finally:
    kamera.release()
    servo.stop()
    GPIO.cleanup()
