import time
import sys

lyrics = [
"Baitha phookne toh kitna hai maal ni puchda",
"Karu hinsa toh kaunsa hai gaal ni puchda",
"Rap school ke hain wahi hum bigde bachche",
"Jinse koi master sawaal ni puchda\n",

"Re dekhunga aaj tujhe ankhiyan bharke",
"Bata kitne mar gaye teri zulfa karke",
"Tu atharah ki hoyi abbe barah padhke",
"Tere karke satrah mere parche chadh ga\n",

"Love letters ke tere varke padhke",
"Ure ladke lad gaye chori ghar mein badhke",
"Faadu parde kaan ke baje gun ke khadke",
"Mere ghar wale tang ho rahe mere karke\n",

"Are koi bhi ho disa chale apna hi kissa",
"Hum dono ek gaane mein toh lage mota paisa",
"Jab pen chaku Leonardo da Vinci banke",
"Bol kagaz pe likhe hue lage Mona Lisa\n",

"Koi sadiyon mein paida hove ek mhare jaisa",
"Mujhe GOAT reflect hove dekhun jab sheesha",
"Main Kim Jong baitha apni saltanat ka",
"Main US–Iran wali war ka nahi hissa\n\n"
]

def type_text(text, speed=0.043):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

print("Boom Shaka By KR$NA\n\n")

# Print lyrics with delay
for i in range(len(lyrics)):
    type_text(lyrics[i])   # typing animation
