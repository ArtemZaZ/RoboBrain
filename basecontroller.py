import protocan
import struct


class BaseController:
    """ Базовый контроллер """

    def __init__(self, owner, addr, name):
        self._owner = owner  # Handler
        self._addr = addr  # аддресс контроллера
        self._name = name  # имя контроллера
        self._isConnected = False  # подключен ли контроллер

        self._paramDict = {0x00: {"name": "Test connection", type: "B", "activeValue": None}}  # список параметров контроллера
        self._commandDict = {0xC8: {"name": "Send param", type: ""},  # список комманд контроллера
                             0xC9: {"name": 'Send important params', type: ""},
                             0xCA: {"name": 'Write in EEPROM', type: ""},
                             0xCB: {"name": 'Read from EEPROM', type: ""}}

    @property
    def isConnected(self):
        return self._isConnected

    def setParamRequest(self, prmNum, value):
        """ запрос на установку указанного параметра на контроллере """
        if prmNum not in self._paramDict.keys():
            raise ValueError("Параметра " + prmNum.__repr__() + " не существует в данном контроллере")
        fmt = "=2B " + self._paramDict[prmNum][type]  # формат пакета
        prmLen = struct.calcsize(self._paramDict[prmNum][type])  # длина параметра в байтах
        package = struct.pack(fmt, prmNum, prmLen, value)

        msg = protocan.getDefaultMessage(self._addr, package)  # получаем сообщение
        self._owner.send(msg)  # отправляем его

    def sendCommand(self, cmdNum, cmdParam=None):
        """ Отправка комманды на контроллер """
        if cmdNum not in self._paramDict.keys():
            raise ValueError("Комманды " + cmdNum.__repr__() + " не существует в данном контроллере")
        pass
        # TODO: разобраться почему пакет комманды отличается от пакета параметров

    def checkConnectionRequest(self):
        """ запрос - проверка подключения устройства """
        self._isConnected = False
        self._paramDict[0x00]["activeValue"] = None

    def parseMsg(self, msg):
        """ Парсинг сообщения, приходящего на данный контроллер с данным адресом """
        pass    # TODO: ...
