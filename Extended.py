import sys
import time

lyrics=[
   (0.05, "Ab yeh kaise main man lu ki"),
   (0.10, "Rehta hun tere dil mai kahin"),
   (0.15, "Aaise khoya tune muzko"),
   (0.19, "Jaisay main tera kuch bhi nahi"),
   (0.24, "Meri yaadon ke is sheher me"),
   (0.29, "Aaj bhi hai teri kami"),
   (0.34, "Raah tune jo chuni thi"),
   (0.39, "Phir tu usme kyu khush nahi"),
   (0.44, "Tum raho ab ajanabi"),
   (0.49, "Mai bhi ab waisa nahi"),
   (0.54, "Jaise mai tanha ji rha tha"),
   (0.59, "Tu bhi ji ,Tu bhi ji"),
   (1.04, "Mai bekhabar tha ,Befikar tha"),
   (1.08, "Ke tu tha mera\n\n")
]

def convert_time(t):
    minutes = int(t)
    seconds = round((t - minutes) * 100)

    return minutes * 60 + seconds

def type_text(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

print("\nExtended...\n")

previous_time = 0

for timestamp, line in lyrics:

    current_time = convert_time(timestamp)

    duration = current_time - previous_time
    previous_time = current_time

    speed = duration / max(len(line), 1)

    type_text(line, speed)