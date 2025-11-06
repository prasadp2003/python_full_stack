class StringManipulationSuite:
    def __init__(self, text):
        self.text = text

    # 1️⃣ Reverse the string
    def reverse_string(self):
        return self.text[::-1]

    # 2️⃣ Convert to uppercase
    def to_uppercase(self):
        return self.text.upper()

    # 3️⃣ Convert to lowercase
    def to_lowercase(self):
        return self.text.lower()

    # 4️⃣ Count vowels and consonants
    def count_vowels_consonants(self):
        vowels = 'aeiouAEIOU'
        v_count = sum(1 for c in self.text if c in vowels)
        c_count = sum(1 for c in self.text if c.isalpha() and c not in vowels)
        return {"vowels": v_count, "consonants": c_count}

    # 5️⃣ Check if palindrome
    def is_palindrome(self):
        s = ''.join(c.lower() for c in self.text if c.isalnum())
        return s == s[::-1]

    # 6️⃣ Remove punctuation
    def remove_punctuation(self):
        import string
        return ''.join(c for c in self.text if c not in string.punctuation)

    # 7️⃣ Find frequency of each character
    def char_frequency(self):
        from collections import Counter
        return dict(Counter(self.text))

    # 8️⃣ Replace substring
    def replace_substring(self, old, new):
        return self.text.replace(old, new)

    # 9️⃣ Title case conversion
    def to_title_case(self):
        return self.text.title()

    # 🔟 Remove extra spaces
    def remove_extra_spaces(self):
        return ' '.join(self.text.split())

