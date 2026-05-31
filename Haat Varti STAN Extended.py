import time
import sys

lyrics = [
"Yeah",
"Haath warti",
"Teri item mekochh kyu jhadti", 
"Fir Kya botta garad aaj bangyela marad",
"Teko bayko Ki garaj meko kayko ni garaj",
"Me akela baras ma saras me charas",
"Me barsenga tu meko milne Ko 10 time tarsenga",
"Turkey me bajenga ghayi chhap me",
"Khaye to kaise kya hagega sajega to sajana ke liye",
"Par sajana ko Kissne Kis kisne diye",
"Teko malum hal ander Ki baat Ghaat\n",

"Ghaate to bhaate to raydo", 
"To bhaag jaate aas paas karawayi bhurte",
"Idhar bhai ban jaate",
"Tap tup me ekda vaar Fir banner pe",
"Yo banner pe",
"Banner pe banner pe bhau log ki photo",
"Bitch imma loco deti kya Choco",
"Meko kon tobi roko ma meko photo",
"Bura mat maan meri hil gayeli taar",
"Meko dikhrele chaar",
"Saysab ki mat le re haath pe tere vaar",
"Akhirkaar jaakar hua me tadipaar",
"Fuck",
"Yo"
]
delay = [0.6,0.7,1.0,0,0,0,0,0,0,0,0,0,0,0,0,0.5,0,0,0,0,0,0,0,0.4,0]

def type_text(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

print("Haath Varti By STAN\n\n")

# Print lyrics with delay
for i in range(len(lyrics)):
    type_text(lyrics[i])   # typing animation
    time.sleep(delay[i])  # wait before next line
