My Morse Code Translator

This is a small Python project I built. It converts normal text into Morse code and also converts Morse code back into text. On top of that, it can read the letters one by one and then say the full word using text-to-speech.


---

Features

Change text to Morse code

Change Morse code back to text

Reads out each character letter by letter

Then speaks the full word

Skips characters that don’t exist in Morse code



---

How to install

1. Clone this project:

git clone https://github.com/johnnie416/My-Morse-Code-Translator.git
cd My-Morse-Code-Translator


2. Install the requirements:

pip install -r requirements.txt




---

How to run

Start the program with:

python main.py

Example:

Enter text to convert to Morse code: Johnson
Morse Code: .--- --- .... -. ... --- -.
Speaking letters...
J O H N S O N
Full word: Johnson


---

Project files

My-Morse-Code-Translator/
│── main.py
│── README.md
│── requirements.txt


---

Things I may add later

A simple GUI version

Option to play Morse code sounds (beeps)

File input and output support

Maybe more languages