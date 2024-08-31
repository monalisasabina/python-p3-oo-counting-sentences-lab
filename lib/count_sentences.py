#!/usr/bin/env python3

class MyString:
    
    def __init__(self,value = ""):
        self.value = value


    # checking if the string is a string
    def get_value(self):
        return self._value    
    
    def set_value(self,str_value):
        if(type(str_value) == str):
            self._value =str_value

        else:
            print("The value must be a string.")

    value=(property(get_value,set_value))    

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")  
    
    def is_exclamation(self):
        return self._value.endswith("!") 
    
    def count_sentences(self):
      value = self.value
      for punc in ['!','?']:
        value = value.replace(punc, '.')
    
      sentences = [s for s in value.split('.') if s]
    
      return len(sentences)
    

# checking if a string
checker = MyString()
checker.set_value("Hello, world!")  # Output: Value has been set to: Hello, world!
print(checker.get_value())  # Output: Hello, world!

checker.set_value(123)  # Output: The value must be a string.
print(checker.get_value())  # Output: Hello, world! (unchanged)


#checking the sentence it has '.' 
sentence = MyString("Hello world.")
print(sentence.is_sentence())
sentence = MyString("Hello world")
print(sentence.is_sentence())


#checking the sentence it has '?' 
sentence = MyString("Hello world?")
print(sentence.is_question())
sentence = MyString("Hello world")
print(sentence.is_question())

# count_sentences
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())
# => 3          







