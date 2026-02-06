# English to Kannada Translator

A powerful Python application that translates English text to Kannada language using Google Translate API.

## Features

✨ **Core Features:**
- 🔤 Translate single words
- 📝 Translate sentences
- 📄 Translate paragraphs
- 📂 Translate entire files
- 💾 Translation caching for faster retrieval
- 🎯 Accurate translations using Google Translate API
- 🖥️ User-friendly CLI interface

## Project Structure

```
English_to_kannada_translator/
├── translator.py           # Core translation module
├── cli.py                  # Command-line interface
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── sample_text.txt        # Sample file for testing
├── translation_cache.json # Cache file (auto-generated)
└── README.md              # This file
```

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd english_to_kannada_translator
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the CLI Application

Start the interactive command-line interface:
```bash
python cli.py
```

### Menu Options

Once the application is running, you'll see the following options:

1. **Translate a word** - Translate a single word from English to Kannada
2. **Translate a sentence** - Translate a complete sentence
3. **Translate a paragraph** - Translate multiple lines of text
4. **Translate from file** - Translate content from a text file
5. **Clear translation cache** - Remove all cached translations
6. **Exit** - Close the application

### Using the Translator Module in Your Code

You can also import and use the translator in your own Python scripts:

```python
from translator import EnglishToKannadaTranslator

# Initialize the translator
translator = EnglishToKannadaTranslator()

# Translate a word
result = translator.translate_word("Hello")
print(result)  # Output: ಹಲೋ

# Translate a sentence
sentence = "How are you today?"
result = translator.translate_sentence(sentence)
print(result)

# Translate from file
translator.translate_file("input.txt", "output.txt")
```

## Methods Reference

### EnglishToKannadaTranslator Class

#### `translate_text(text: str) -> str`
Translates any English text to Kannada.
- **Parameters:** `text` - The English text to translate
- **Returns:** Translated Kannada text

#### `translate_word(word: str) -> str`
Translates a single word.
- **Parameters:** `word` - The English word
- **Returns:** Translated Kannada word

#### `translate_sentence(sentence: str) -> str`
Translates a sentence.
- **Parameters:** `sentence` - The English sentence
- **Returns:** Translated Kannada sentence

#### `translate_paragraph(paragraph: str) -> str`
Translates a paragraph.
- **Parameters:** `paragraph` - The English paragraph
- **Returns:** Translated Kannada paragraph

#### `translate_file(input_file: str, output_file: str = None) -> bool`
Translates content from a file.
- **Parameters:**
  - `input_file` - Path to the input text file
  - `output_file` - Path to save translated text (optional)
- **Returns:** True if successful, False otherwise

## Example Translations

| English | Kannada |
|---------|---------|
| Hello | ಹಲೋ |
| Goodbye | ಬೈ |
| Thank you | ಧನ್ಯವಾದ |
| Good morning | ಶುಭೋದಯ |
| How are you? | ನೀವು ಹೇಗಿದ್ದೀರಿ? |

## Caching System

The application automatically caches all translations for improved performance:
- Translations are stored in `translation_cache.json`
- Previously translated text is retrieved from cache instantly
- Cache can be manually cleared from the menu

## Troubleshooting

### Issue: Import Error for `translate` module
**Solution:** Ensure you've installed the requirements
```bash
pip install -r requirements.txt
```

### Issue: Encoding errors when reading files
**Solution:** Ensure your input text files are saved with UTF-8 encoding

### Issue: No internet connection
**Solution:** The application requires internet connection to use Google Translate API. Cached translations will still work offline.

## Configuration

Edit `config.py` to customize:
- Source and target languages
- Cache settings
- Output file naming conventions
- Application metadata

## Technical Details

- **Translation Engine:** Google Translate (via googletrans)
- **Language:** Python 3.6+
- **Dependencies:** googletrans library
- **Encoding:** UTF-8 for all text operations
- **Cache Format:** JSON

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## Support

For issues or questions, please create an issue in the repository.

---

**Version:** 1.0.0  
**Last Updated:** January 2026