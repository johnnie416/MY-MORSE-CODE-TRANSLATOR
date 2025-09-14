from colorama import init, Fore
import time
import pyttsx3
import platform

# Initialize colorama
init(autoreset=True)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Platform check for sound playback
if platform.system() == "Windows":
    import winsound

# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/',  # space between words
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    ':': '---...', ';': '-.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', "'": '.----.', '@': '.--.-.'
}

reverse_morse_dict = {value: key for key, value in morse_code_dict.items()}

# Encode text to Morse
def encode_to_morse(text):
    text = text.upper()
    morse_text = ''
    for char in text:
        morse_text += morse_code_dict.get(char, '?') + ' '
    return morse_text.strip()

# Decode Morse to text
def decode_from_morse(morse_code):
    words = morse_code.split(' / ')
    decoded_text = ''
    for word in words:
        letters = word.split()
        for letter in letters:
            decoded_text += reverse_morse_dict.get(letter, '?')
        decoded_text += ' '
    return decoded_text.strip()

# Save output to file
def save_to_file(output, filename="morse_output.txt"):
    with open(filename, "a") as f:
        f.write(output + "\n")
    print(Fore.GREEN + f"Output saved to {filename}")

# Play Morse code as beeps
def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            beep(200)
        elif symbol == '-':
            beep(600)
        elif symbol == ' ' or symbol == '/':
            time.sleep(0.2)

# Cross-platform beep function
def beep(duration):
    if platform.system() == "Windows":
        winsound.Beep(800, duration)
    else:
        # For Linux/Mac, you can use os.system('play -nq -t alsa synth {} sine 800'.format(duration/1000))
        time.sleep(duration/1000)  # Fallback silent wait

# Speak text using TTS
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main program
def main():
    print(Fore.CYAN + "=== Ultimate Interactive Morse Code Converter ===")

    while True:
        print(Fore.YELLOW + "\nChoose an option:")
        print("1. Encode text to Morse Code")
        print("2. Decode Morse Code to text")
        print("3. Exit")

        choice = input(Fore.CYAN + "Enter 1, 2, or 3: ").strip()

        if choice == '1':
            text = input(Fore.CYAN + "Enter text to convert: ")
            morse = encode_to_morse(text)
            print(Fore.MAGENTA + "Morse Code: " + Fore.WHITE + morse)

            if input(Fore.CYAN + "Play Morse code as sound? (y/n): ").lower() == 'y':
                play_morse(morse)

            if input(Fore.CYAN + "Save output to file? (y/n): ").lower() == 'y':
                save_to_file(morse)

        elif choice == '2':
            morse = input(Fore.CYAN + "Enter Morse Code to decode (use / for spaces): ")
            decoded = decode_from_morse(morse)
            print(Fore.MAGENTA + "Decoded Text: " + Fore.WHITE + decoded)

            if input(Fore.CYAN + "Speak decoded text? (y/n): ").lower() == 'y':
                speak_text(decoded)

            if input(Fore.CYAN + "Save output to file? (y/n): ").lower() == 'y':
                save_to_file(decoded)

        elif choice == '3':
            print(Fore.GREEN + "Goodbye! Thanks for using the converter.")
            break

        else:
            print(Fore.RED + "Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()