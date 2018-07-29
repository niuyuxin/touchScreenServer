#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt5.QtNetwork import *
from PyQt5.QtCore import *
from config import  *
import ast
import json
import random

class TcpServer(QObject):
    Modal = "Modal"
    getAllSubDev = pyqtSignal(str, list)
    selectedDevice = pyqtSignal(list)
    Call = 2
    CallResult = 3
    CallError = 4
    ForbiddenDevice = "ForbiddenDevice"
    SetScreen = "setScreen"
    SetScreenValue = "value"
    MonitorName = "MonitorName"
    MonitorDevice = "MonitorDevice"
    MonitorSocket = "Socket"
    MonitorId = "MonitorId"
    MonitorRecBuf = "RecBuf"
    MonitorDeviceCount = "MonitorDeviceCount"
    UpdateDevice = "UpdateDevice"
    def __init__(self):
        super().__init__()
        self.tcpServer = QTcpServer(self) # should have parent
        self.sendCount = 0
        self.socketList = []
        if not self.tcpServer.listen(QHostAddress.AnyIPv4, 5000):
            print("listen error")
            return
        else:
            self.tcpServer.newConnection.connect(self.onNewConnection)
            print("listen successful")
    @pyqtSlot()
    def onNewConnection(self):
        while self.tcpServer.hasPendingConnections():
            socket = self.tcpServer.nextPendingConnection()
            socket.readyRead.connect(self.onReadyToRead)
            socket.disconnected.connect(self.onSocketDisconnect)
            socketDict = {TcpServer.MonitorSocket:socket,
                          TcpServer.MonitorId:None,
                          TcpServer.MonitorDevice:[],
                          TcpServer.MonitorName:None,
                          TcpServer.MonitorDeviceCount:0}
            self.socketList.append(socketDict)
            print("socket accpet ", socketDict)
            b = QByteArray(bytes(r"Hello, New tcpSocket... [socket IpV4 = {}]".format(socket.peerAddress().toString()), encoding="UTF-8"))
            socket.write(b)
    @pyqtSlot()
    def onSocketDisconnect(self):
        socket = self.sender()
        count = 0
        for s in self.socketList:
            if s[TcpServer.MonitorSocket] == socket:
                self.socketList.pop(count)
                print("delete socket name", socket)
            count += 1
        socket.deleteLater()
    @pyqtSlot()
    def onReadyToRead(self):
        try:
            socket = self.sender()
            socketDict = {}
            for s in self.socketList:
                if s[TcpServer.MonitorSocket] == socket:
                    socketDict = s
                    break
            if not socketDict:
                print("socket {} is not in socketList".format(socketDict))
                return
            while socket.bytesAvailable():
                allData = str(socket.readAll(), encoding='UTF-8')
                dataList = allData.split('\0')
                print("Received: ", len(dataList), dataList)
                for data in dataList:
                    if len(data) == 0: continue
                    dataJson = json.loads(data)
                    if len(dataJson) == 4 and dataJson[0] == TcpServer.Call:
                        if socketDict[TcpServer.MonitorName] == None or socketDict[TcpServer.MonitorId] == None:
                            dataDict = dataJson[3]
                            if isinstance(dataDict, dict):
                                socketDict[TcpServer.MonitorId] = int(dataDict.get(TcpServer.MonitorId))
                                socketDict[TcpServer.MonitorDeviceCount] = dataDict.get(TcpServer.MonitorDeviceCount)
                                socketDict[TcpServer.MonitorName] = dataDict.get(TcpServer.MonitorName)
                                message = [TcpServer.CallResult, dataJson[1], dataJson[2], {}]
                                socket.write(bytes(json.dumps(message, ensure_ascii='UTF-8'), encoding='utf-8'))
                                socket.waitForBytesWritten()
                            else:
                                socket.disconnectFromHost()
                        elif len(socketDict[TcpServer.MonitorDevice]) != socketDict[TcpServer.MonitorDeviceCount]:
                            if dataJson[2] == TcpServer.UpdateDevice:
                                if isinstance(dataJson[3], dict) and isinstance(dataJson[3][TcpServer.MonitorDevice], list):
                                    socketDict[TcpServer.MonitorDevice].extend(dataJson[3][TcpServer.MonitorDevice])
                                if len(socketDict[TcpServer.MonitorDevice]) == socketDict[TcpServer.MonitorDeviceCount]:
                                    self.getAllSubDev.emit(socketDict[TcpServer.MonitorName], socketDict[TcpServer.MonitorDevice])
                                message = [TcpServer.CallResult, dataJson[1], dataJson[2], {}]
                                socket.write(bytes(json.dumps(message, ensure_ascii='UTF-8'), encoding='utf-8'))
                                socket.waitForBytesWritten()
                        else:
                            self.analysisData(dataJson[1], dataJson[2], dataJson[3])
        except Exception as e:
            tempDict = {"Error:{}".format(str(e)): data}
            b = QByteArray(bytes(str(tempDict), encoding="UTF-8")).append("\n")
            socket.write(b)

    def analysisData(self, unionId, action, dataDict):
        if action == "SelectedDevice":
            self.selectedDevice.emit(dataDict["Device"])
        elif action == "helloworld":
            pass
        elif action == ".....":
            pass
        else:
            print("Unknow request!")

    def onDataToSend(self, name, id, messageList): # messageTypeId, action, data
        try:
            message = []
            if len(messageList) == 4:
                message = messageList
            else:
                message = [messageList[0], self.createUnionId(messageList[1]), messageList[1], messageList[2]]
            self.sendDataToSocket(name, id, bytes(json.dumps(message, ensure_ascii='UTF-8'), encoding='utf-8'))
        except Exception as e:
            print("onDataToSend", str(e))

    def sendDataToSocket(self, name, id, data): # 选择要发给的设备
        sendSocket = None
        try:
            for socket in self.socketList:
                if socket[TcpServer.MonitorName] == name and \
                    socket[TcpServer.MonitorId] == id and \
                    socket[TcpServer.MonitorSocket].state() == QAbstractSocket.ConnectedState:
                    sendSocket = socket[TcpServer.MonitorSocket]
                    sendSocket.write(data)
                    sendSocket.waitForBytesWritten()
        except Exception as e:
            print("onsendData", str(e))

    def createUnionId(self, type):
        time = QDateTime.currentDateTime().toString("yyMMddhhmmsszzz")
        self.sendCount += 1
        return str(type) + '-' + time + '-' + str(self.sendCount)