"""
Command Line Interface for English to Kannada Translator
Provides a user-friendly CLI for translation operations
"""

import sys
from translator import EnglishToKannadaTranslator


def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print("   ENGLISH TO KANNADA TRANSLATOR")
    print("="*60 + "\n")


def print_menu():
    """Print main menu options"""
    print("\nChoose an option:")
    print("1. Translate a word")
    print("2. Translate a sentence")
    print("3. Translate a paragraph")
    print("4. Translate from file")
    print("5. Clear translation cache")
    print("6. Exit")
    print()


def translate_word(translator):
    """Handle word translation"""
    word = input("Enter the word to translate: ").strip()
    if word:
        result = translator.translate_word(word)
        print(f"\n✓ English:  {word}")
        print(f"✓ Kannada:  {result}\n")
    else:
        print("Please enter a valid word!\n")


def translate_sentence(translator):
    """Handle sentence translation"""
    sentence = input("Enter the sentence to translate: ").strip()
    if sentence:
        result = translator.translate_sentence(sentence)
        print(f"\n✓ English:  {sentence}")
        print(f"✓ Kannada:  {result}\n")
    else:
        print("Please enter a valid sentence!\n")


def translate_paragraph(translator):
    """Handle paragraph translation"""
    print("Enter the paragraph (press Enter twice to finish):")
    lines = []
    empty_count = 0
    
    while empty_count < 2:
        line = input()
        if line == "":
            empty_count += 1
        else:
            empty_count = 0
            lines.append(line)
    
    paragraph = " ".join(lines)
    if paragraph.strip():
        result = translator.translate_paragraph(paragraph)
        print(f"\n✓ English:\n{paragraph}")
        print(f"\n✓ Kannada:\n{result}\n")
    else:
        print("Please enter a valid paragraph!\n")


def translate_from_file(translator):
    """Handle file translation"""
    input_file = input("Enter the input file path: ").strip()
    output_file = input("Enter the output file path (press Enter to auto-generate): ").strip()
    
    output_file = output_file if output_file else None
    
    if translator.translate_file(input_file, output_file):
        print(f"✓ File translated successfully!\n")
    else:
        print("✗ Failed to translate file!\n")


def clear_cache(translator):
    """Clear translation cache"""
    translator.cache.clear()
    translator._save_cache()
    print("✓ Translation cache cleared!\n")


def main():
    """Main CLI loop"""
    translator = EnglishToKannadaTranslator()
    print_header()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            translate_word(translator)
        elif choice == "2":
            translate_sentence(translator)
        elif choice == "3":
            translate_paragraph(translator)
        elif choice == "4":
            translate_from_file(translator)
        elif choice == "5":
            clear_cache(translator)
        elif choice == "6":
            print("\nThank you for using English to Kannada Translator!")
            print("Goodbye!\n")
            sys.exit(0)
        else:
            print("✗ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user. Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ An error occurred: {str(e)}\n")
        sys.exit(1)
