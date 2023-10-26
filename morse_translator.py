# Define dictionaries for mapping characters to Morse code and vice versa
text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

morse_to_text = {v: k for k, v in text_to_morse.items()}

def text_to_morse_code(text):
    morse_code = ' '.join(text_to_morse.get(char.upper(), char) for char in text)
    return morse_code

def morse_code_to_text(morse_code):
    text = ''.join(morse_to_text.get(code, code) for code in morse_code.split())
    return text

while True:
    print("Morse Code Converter")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        input_text = input("Enter the text to convert to Morse code: ")
        morse_code = text_to_morse_code(input_text)
        print("Morse Code: " + morse_code)
    elif choice == '2':
        input_morse_code = input("Enter the Morse code to convert to text: ")
        text = morse_code_to_text(input_morse_code)
        print("Text: " + text)
    elif choice == '3':
        print("Exiting the Morse Code Converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
