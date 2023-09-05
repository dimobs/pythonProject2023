from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):

    def format(self):
        return '\n'.join(['<HTML>', self.text, '</HTML>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):

        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


myml = HTML('Hello, there!')
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myml)
print(email)

