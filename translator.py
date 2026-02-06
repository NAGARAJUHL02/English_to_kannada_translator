"""
English to Kannada Translator
A simple translator that converts English text to Kannada using Google Translate API
"""

from googletrans import Translator
import json
from pathlib import Path


class EnglishToKannadaTranslator:
    """Class to handle English to Kannada translation"""
    
    def __init__(self):
        """Initialize the translator"""
        self.translator = Translator()
        self.cache_file = Path('translation_cache.json')
        self.cache = self._load_cache()
    
    def _load_cache(self):
        """Load translation cache from file"""
        if self.cache_file.exists():
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_cache(self):
        """Save translation cache to file"""
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def translate_text(self, text):
        """
        Translate English text to Kannada
        
        Args:
            text (str): English text to translate
            
        Returns:
            str: Translated Kannada text
        """
        if not text.strip():
            return ""
        
        # Check cache first
        if text in self.cache:
            return self.cache[text]
        
        try:
            result = self.translator.translate(text, src_language='en', dest_language='kn')
            translated = result['text'] if isinstance(result, dict) else result.text
            # Cache the translation
            self.cache[text] = translated
            self._save_cache()
            return translated
        except Exception as e:
            return f"Error in translation: {str(e)}"
    
    def translate_file(self, input_file, output_file=None):
        """
        Translate text from a file
        
        Args:
            input_file (str): Path to input file
            output_file (str): Path to output file (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            translated_content = self.translate_text(content)
            
            if output_file is None:
                output_file = input_file.replace('.txt', '_kannada.txt')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            
            return True
        except Exception as e:
            print(f"Error translating file: {str(e)}")
            return False
    
    def translate_word(self, word):
        """
        Translate a single word
        
        Args:
            word (str): Single word to translate
            
        Returns:
            str: Translated word
        """
        return self.translate_text(word.strip())
    
    def translate_sentence(self, sentence):
        """
        Translate a sentence
        
        Args:
            sentence (str): Sentence to translate
            
        Returns:
            str: Translated sentence
        """
        return self.translate_text(sentence.strip())
    
    def translate_paragraph(self, paragraph):
        """
        Translate a paragraph
        
        Args:
            paragraph (str): Paragraph to translate
            
        Returns:
            str: Translated paragraph
        """
        return self.translate_text(paragraph.strip())


if __name__ == "__main__":
    # Example usage
    translator = EnglishToKannadaTranslator()
    
    # Test with a simple word
    word = "Hello"
    print(f"English: {word}")
    print(f"Kannada: {translator.translate_word(word)}")
    print()
    
    # Test with a sentence
    sentence = "Hello, how are you today?"
    print(f"English: {sentence}")
    print(f"Kannada: {translator.translate_sentence(sentence)}")
