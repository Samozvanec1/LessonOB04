# class Report():
#     def __init__(self,title, content):
#         self.title = title
#         self.content = content
#     def docprint(self):
#         print(self.title,"\n",self.content)
#
# rep = Report("Moy Taytle", "moy cantet")

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormated(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HTMLFormated(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}<h1/>")
        print(f"<p>{report.content}<p/>")

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)

report = Report("заголовок", " это текст отчёта, его тут много", TextFormated())
#report = Report("заголовок", " это текст отчёта, его тут много", HTMLFormated())

report.docPrinter()





