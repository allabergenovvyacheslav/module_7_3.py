import string

# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий
# файлов и записывать их в атрибут file_names в виде списка или кортежа.
class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                
            file_name = file_name.lower().strip(',', '.', '=', '!', '?', ';', ':', ' - ').split(' ')
            # s = file_name
            # s.translate(str.maketrans('', '', string.punctuation))

                return all_words


    def find(self, word):
        pass

    def count(self, word):
        pass


