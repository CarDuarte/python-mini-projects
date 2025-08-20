import string

def caesar_econde(text: str, shift: int) -> str:
    resut = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            resut.append(shifted_char)
        else:
            resut.append(char)
    return ''.join(resut)

def caesar_decode(text: str, shift: int) -> str:
    return caesar_econde(text, -shift)

def main():
    text = input("Enter text: ")
    shift = int(input("Enter shift value (integer): "))
    mode = input("Choose mode (encode/decode): ").strip().lower()

    if mode == 'encode':
        output = caesar_econde(text, shift)
    elif mode == 'decode':
        output = caesar_decode(text, shift)
    else:
        print("Invalid mode selected. Please choose 'encode' or 'decode'.")
        return
    
    print(f"Output: {output}")


if __name__ == "__main__":
    main()