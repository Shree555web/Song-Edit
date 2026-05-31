import time
import sys

lyrics = [
"Agar karun baat toh wo aam baat (nahi)",
"Aur yaar kare bas baatein, jaise kaam-kaaj nahi",
"Jo bol rahe the jyada, unka naam aaj nahi",
"Mujhse bhidna dubara tu koi jaanbaaz nahi\n",

"Main na gayab hota bro, just quiet on the low",
"And if I ever go, main retire hora G.O.A.T",
"Mujhe kheenche ye neeche, the higher up I go",
"Main waha se hoon aaya, where they fire up the stove\n",

"Chalata main b’m, the 5 series be Me",
"Jo rakhti thi blocked, kare slide in my DM",
"Har subah bheje GM, milna hai TN",
"Kyunki chahiye usse chahiye mo’ D – jaise PM \n",

"Bol mera aura hua kab tabah?",
"Yahan aaj bhi hai kayam mera dabdabah",
"Kai saal baad iska haar ke na mann bhara",
"Dekho kaise naache meri dhun pe yahan apsara\n\n",
]


# Typing effect function
def type_text(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

print("Boom Shaka By KR$NA\n\n")
# Print lyrics with delay
for i in range(len(lyrics)):
    type_text(lyrics[i])   # typing animation
