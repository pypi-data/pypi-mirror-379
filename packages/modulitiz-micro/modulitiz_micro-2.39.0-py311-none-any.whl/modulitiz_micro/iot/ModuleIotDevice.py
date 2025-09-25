from modulitiz_micro.ModuloNumeri import ModuloNumeri
from modulitiz_micro.ModuloStringhe import ModuloStringhe
from modulitiz_micro.eccezioni.EccezioneRuntime import EccezioneRuntime
from modulitiz_micro.eccezioni.http.EccezioneHttp import EccezioneHttp
from modulitiz_micro.files.ModuloLogging import ModuloLogging
from modulitiz_micro.iot.beans.IotDeviceBean import IotDeviceBean
from modulitiz_micro.iot.enums.IotOSEnum import IotOSEnum
from modulitiz_micro.iot.espurna.ModuleEspurna import ModuleEspurna
from modulitiz_micro.rete.http.ModuloHttp import ModuloHttp


class ModuleIotDevice(object):
	def __init__(self, logger:ModuloLogging|None, deviceBean:IotDeviceBean):
		self.__logger=logger
		self.__deviceBean=deviceBean
	
	def getRelayStatus(self, relayNum:int)->bool:
		"""
		@param relayNum: Depending on which OS you choose, can be relative (0, 1, ...) or GPIO
		"""
		if self.__deviceBean.os==IotOSEnum.ESPURNA:
			url=ModuleEspurna.URL_GET_RELAY.format(ip=self.__deviceBean.ip,relayNum=relayNum,apiKey=self.__deviceBean.key)
		else:
			raise EccezioneRuntime("Iot os '%s' not known"%(self.__deviceBean.os,))
		return ModuloNumeri.intToBool(ModuloNumeri.strToInt(self.__sendRequest(url)))
	
	def setRelayStatus(self, relayNum:int, status:bool):
		"""
		@param relayNum: Depending on which OS you choose, can be relative (0, 1, ...) or GPIO
		@param status: value to set, can only be false or true
		"""
		if self.__deviceBean.os==IotOSEnum.ESPURNA:
			statusStr=str(ModuloNumeri.boolToInt(status))# TODO check if works or if u have to use value 2 (toggle)
			url=ModuleEspurna.URL_SET_RELAY.format(ip=self.__deviceBean.ip,relayNum=relayNum,apiKey=self.__deviceBean.key,status=statusStr)
		else:
			raise EccezioneRuntime("Iot os '%s' not known"%(self.__deviceBean.os,))
		# TODO: check output
		self.__sendRequest(url)
	
	def __sendRequest(self, url:str)->str:
		http=ModuloHttp(url,self.__logger,False)
		http.setUserAgent()
		bean=http.doGet(0, False)
		if bean.status!=ModuloHttp.STATUS_OK:
			raise EccezioneHttp(bean.status)
		return bean.responseBody.decode(ModuloStringhe.CODIFICA_UTF8)
