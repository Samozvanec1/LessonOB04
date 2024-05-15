# class Book():
#     def read(self):
#       print ("Чтение интересных историй")
#
# class StoryReader(): # стори_ридер сильно завистит от класса Бук, а согласно принципу инверсии зависимости,
#                      # этого быть не должно, ОНИ ДОЛЖНЫ ЗАВИСИТЬ НЕ ОТ ДРУГ ДРУГА,
#                      # А ОТ АБСТРАКЦИЙ - АБСТРАКТНОГО КЛАССА
#     def __init__(self):
#         self.Book =  Book()
#
#     def tell_story(self):
#         self.book.read() #Используем функцию read  из класса Book




from  abc import ABC, abstractmethod

class StorySource (ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение интересных историй")

class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересных историй вслух")


class StoryReader():
     def __init__(self, story_source: StorySource):
         self.story_source = story_source

     def tell_story(self):
         self.story_source.get_story()  #Используем функцию get_story  из класса AudioBook(StorySource):

book = Book()
audiobook = AudioBook()

readerBook = StoryReader(book) #В круглых скобках прописывается объект класса который будет передоваться, сейчас это book

readerAudioBook = StoryReader(audiobook)

readerBook.tell_story()
readerAudioBook.tell_story()
