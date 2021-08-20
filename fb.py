"""Import regexp library"""
import re


class FizzBuzzDetector:
    """FizzBuzzDetector implementation"""
    def __init__(self, string):
        self.string = string

    def validate_string(self):
        """Validate input string"""
        pattern = '^[a-z ]{7,100}$'
        if not re.search(pattern, self.string):
            raise ValueError('Invalid input please try again')

    def get_over_lappings(self):
        """Replace words and letters to Fizz or Buzz"""
        self.validate_string()
        fb_result = []
        list_string = self.string.split()
        for index, word in enumerate(list_string):
            if (index+1) % 3 == 0:
                fb_result.append('F')
            elif len(word) >= 5:
                new_list = []
                for i, letter in enumerate(word):
                    if (i+1) % 5 == 0:
                        new_list.append('B')
                    else:
                        new_list.append(letter)
                fb_result.append(''.join(new_list))
            else:
                fb_result.append(word)
            result_string = ''.join(fb_result)
            result = {
                'F': result_string.count('F'),
                'B': result_string.count('B')
            }
        return result
