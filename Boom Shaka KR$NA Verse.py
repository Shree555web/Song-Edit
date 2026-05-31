import time
import sys

lyrics = [
"Main bolun Boom Shaka Laka",
"Ye bole hukum mere AKA",
"Thoda sa teda tu jhaka",
"Toh mathe beech baje pataka\n",

"Bolo ab Boom Shaka Laka, Kare Bandook Shaka Laka",
"Chilla rahe Boom Shaka Laka, hilade room Shaka Laka\n",

"Bolo Boom Shaka Laka, Kare Bandook Shaka Laka",
"Chilla rahe Boom Shaka Laka, hilade room Shaka Laka\n",

"Bolo Boom Shaka Laka, Kare Bandook Shaka Laka",
"Chilla rahe Boom Shaka Laka, hilade room Shaka Laka\n\n"
]

def type_text(text, speed=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

print("Boom Shaka By KR$NA\n\n")

# Print lyrics with delay
for i in range(len(lyrics)):
    type_text(lyrics[i])   # typing animation
