rutasGlobal = {
    "AcceptFromEscrow": "api/CashDevice/AcceptFromEscrow",
    "Authenticate": "api/Users/Authenticate",
    "CancelMultiEscrow": "api/CashDevice/CancelMultiEscrow",
    "ClearCashboxLevels": "api/CashDevice/ClearCashboxLevels",
    "ClearNoteCashboxLevels": "api/CashDevice/ClearNoteCashboxLevels",
    "CommitMultiEscrow": "api/CashDevice/CommitMultiEscrow",
    "comPortReadError" : "api/CashDevice/comPortReadError",
    "DisconnectDevice": "api/CashDevice/DisconnectDevice",
    "DisableAcceptor": "api/CashDevice/DisableAcceptor",
    "DisablePayout": "api/CashDevice/DisablePayout",
    "DispenseValue": "api/CashDevice/DispenseValue",
    "EnableAcceptor": "api/CashDevice/EnableAcceptor",
    "EnableCoinMechOrFeeder" : "api/CashDevice/EnableCoinMechOrFeeder",
    "EnablePayout": "api/CashDevice/EnablePayout",
    "EnablePayoutDevice": "api/CashDevice/EnablePayoutDevice",
    "GetAllLevels": "api/CashDevice/GetAllLevels",
    "GetBarcodeData" : "api/CashDevice/GetBarcodeData",
    "GetBarcodeReaderConfiguration" : "api/CashDevice/GetBarcodeReaderConfiguration",
    "GetCashboxLevels": "api/CashDevice/GetCashboxLevels",
    "GetCoinAcceptance" : "api/CashDevice/GetCoinAcceptance",
    "GetCompleteCashDevice": "api/CashDevice/GetCompleteCashDevice",
    "GetCounters": "api/CashDevice/GetCounters",
    "GetCurrencyAssignment": "api/CashDevice/GetCurrencyAssignment",
    "GetDeviceStatus": "api/CashDevice/GetDeviceStatus",
    "GetDownloadStatus" : "api/Download/GetDownloadStatus",
    "GetGlobalErrorCode": "api/CashDevice/GetGlobalErrorCode",
    "GetHopperOptions" : "api/CashDevice/GetHopperOptions",
    "GetLastRejectCode" : "api/CashDevice/GetLastRejectCode",
    "GetLifterStatus" : "api/CashDevice/GetLifterStatus",
    "GetMultiEscrowSize": "api/CashDevice/GetMultiEscrowSize",
    "GetMultiEscrowValue": "api/CashDevice/GetMultiEscrowValue",
    "GetNoteCashboxLevels": "api/CashDevice/GetNoteCashboxLevels",
    "GetPayoutCount": "api/CashDevice/GetPayoutCount",
    "GetRCMode" : "api/CashDevice/GetRCMode",
    "GetServiceInformation" : "api/CashDevice/GetServiceInformation",
    "GetServiceInformationForModule" : "api/CashDevice/GetServiceInformationForModule",
    "GetSmartCurrencyData" : "api/CashDevice/GetSmartCurrencyData",
    "GetSorterRouteAssignment" : "api/CashDevice/GetSorterRouteAssignment",
    "HaltPayout": "api/CashDevice/HaltPayout",
    "LogRawPackets" : "api/CashDevice/LogRawPackets",
    "OpenConnection": "api/CashDevice/OpenConnection",
    "RefillMode": "api/CashDevice/RefillMode",
    "Replenish": "api/CashDevice/Replenish",
    "ResetDevice": "api/CashDevice/ResetDevice",
    "ReturnFromEscrow": "api/CashDevice/ReturnFromEscrow",
    "SendCustomCommand": "api/CashDevice/SendCustomCommand",
    "SetAutoAccept": "api/CashDevice/SetAutoAccept",
    "SetBarcodeReaderConfiguration" : "api/CashDevice/SetBarcodeReaderConfiguration",
    "SetCashboxLevels": "api/CashDevice/SetCashboxLevels",
    "SetCashboxPayoutLimit": "api/CashDevice/SetCashboxPayoutLimit",
    "SetDenominationInhibits": "api/CashDevice/SetDenominationInhibits",
    "SetDenominationLevel" : "api/CashDevice/SetDenominationLevel",
    "SetDenominationRoute": "api/CashDevice/SetDenominationRoute",
    "SetHopperOptions" : "api/CashDevice/SetHopperOptions",
    "SetMultiEscrowSize": "api/CashDevice/SetMultiEscrowSize",
    "SetNoPayinCount" : "api/CashDevice/SetNoPayinCount",
    "SetPayoutLimit": "api/CashDevice/SetPayoutLimit",
    "SetServiceInformationMaintenanceReset" : "api/CashDevice/SetServiceInformationMaintenanceReset",
    "SetSorterRoute" : "api/CashDevice/SetSorterRoute",
    "SetTwinMode" : "api/CashDevice/SetTwinMode",
    "SmartEmpty": "api/CashDevice/SmartEmpty",
    "StartDevice" : "api/CashDevice/StartDevice",
    "StartDownload" : "api/Download/StartDownload",
    "StopDevice" : "api/CashDevice/StopDevice",
    "UpdateCredentials": "api/CashDevice/UpdateCredentials",
    "UpdateSmartCurrencyDataset" : "api/CashDevice/UpdateSmartCurrencyDataset"
}
import requests
import json
import logging
from typing import List, Dict, Any
from dataclasses import asdict, is_dataclass, dataclass
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#---------------------------------------------------------------------------------
#                                                                                   
#           Clase base de usuario para la autenticación
#                       en la API de ITL
#
#---------------------------------------------------------------------------------


#Clase usuario con valores por defecto
@dataclass
class Usuario:
    """
    Clase con credenciales de usuario
    
    Args: 
        Usuario (str) : Usuario con el que se realiza la autenticacion por Token. Por defecto "admin"
        Contrasena (str) : Contraseña correspondiente al usuario. Por defecto "password"
    """
    Usuario: str = "admin"
    Contrasena: str = "password"


#---------------------------------------------------------------------------------
#                                                                                   
#           Clase con los valores de conexion para comunicacion
#                       con la API de ITL
#
#---------------------------------------------------------------------------------

@dataclass
class Conexion:
    """
    Clase con los datos basicos de conexion con la API
    
    Args:
        puerto (str) : Puerto de comunicación (COM3, ttyUSB0, etc...) 
        nombre_dispositivo (str) : Nombre del dispositivo ITL a conectar
        direccionSSP (int) : Numero del puerto SSP donde se comunica el dispositivo
        url_base (str) : Direccion base donde se ejecuta la API para posteriormente concatenarla con las rutas de los diferentes endpoints
        token (str) : Token de autenticación para la conexión con los diferentes endpoints de la API
        denominacion (str) : Denominacion de la moneda, según país (Ej. COP, MXN)
        id_dispositivo (str) : Identificador del dispositivo (Obtenido automaticamente al realizar la conexion)
    """
    puerto: str = ""                            # Puerto de comunicación
    nombre_dispositivo: str = ""                # Nombre del dispositivo
    direccionSSP: int = 0                       # Dirección SSP
    url_base: str = ""                          # URL base
    token: str = ""                             # Token de autenticación
    denominacion: str = ""                      # Moneda (COP)
    id_dispositivo: str = ""                    # ID del dispositivo

    
    def __post_init__(self):
        self.puerto = self.puerto.upper() if self.puerto != "" else ""
        self.nombre_dispositivo = self.nombre_dispositivo.upper() if self.nombre_dispositivo != "" else ""
        self.denominacion = self.denominacion.upper() if self.denominacion != "" else ""
        
    
#---------------------------------------------------------------------------------
#                                                                                  
#           Clase con los valores de configuración iniciales
#                   para NV4000 y SCS de ITL
#
#---------------------------------------------------------------------------------

@dataclass
class Configuracion:
    """
    Clase con los valores de configuración iniciales para NV4000 y SCS de 
    
    Args: 
        ComPort (str, opcional) : Puerto de Comunicación del dispositivo (Asignado automaticamente al realizar conexion)
        LogFilePath (str) : Ruta donde se guardarán los Loggings de la conexión o aplicacion. Por defecto "C:/Temp/"
        SetRoutes (Dict, opcional) : Diccionario con las denominaciones y rutas en recicladores del dispositivo. Por defecto None
        SetInhibits (Dict, opcional) : Denominaciones que el dispositivo debe rechazar/aceptar automaticamente. Por defecto None
        SetCoin
    """
    ComPort: str = ""                                  # Puerto de comunicación
    LogFilePath: str = "C:/Temp/"                      # Ruta para guardar los logs
    SetRoutes: Dict = None                             # Configuracion :(que denominacion se guarda en que recicladora / hopper)
    SetInhibits: Dict = None                           # Denominaciones a deshabilitar aceptacion (ej. {"25": True})


#---------------------------------------------------------------------------------
#                                                                                   
#           Clase para iniciar la comunicacion entre el dispositivo
#                       con la API de ITL
#
#---------------------------------------------------------------------------------
class Device():

    def __init__(self, conexion: Conexion, usuario: Usuario, configuracion: Configuracion):
        
        self.configuracion = configuracion
        self.conexion = conexion
        self.usuario = usuario
        self.rutas = rutasGlobal
        self.Authenticate()
        self.reintentos = 3  #  Número de reintentos para solicitar nuevos tokens
        

#----------------------------------------------- Funciones Recurrentes -----------------------------------------------------------

    # Carga un archivo JSON y lo convierte a un diccionario dada su ruta
    def cargar_json(self,ruta_archivo: str) -> Dict:
        """
        Carga un archivo JSON y lo convierte a un diccionario dada su ruta
        
        Args:
            ruta_archivo (str) : Ruta desde la cual se desea cargar el archivo JSON y deserializar a Diccionario
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = json.load(archivo)
                if not isinstance(contenido, dict):
                    logger.error("El JSON no representa un diccionario")
                    raise ValueError("El JSON no representa un diccionario")
                logger.info(f"Archivo JSON cargado correctamente: {ruta_archivo}")
                return contenido
        except FileNotFoundError:
            logger.exception("Archivo no encontrado")
            raise ValueError(f"El archivo no fue encontrado: {ruta_archivo}")
        except json.JSONDecodeError as e:
            logger.exception("Error al decodificar JSON")
            raise ValueError(f"Error al decodificar JSON: {e}")
    
    # Determina las rutas y denominaciones a configurar en el dispositivo
    def SetDenominations(self, denominaciones: List[int], rutas: List[int]) -> List[Dict[str, Any]]:
        """
        
        Configura las denominaciones y rutas para el dispositivo.
        Devuelve una lista de diccionarios con formato:
        [
        {"Denomination": "500", "Route": 2},
        {"Denomination": "1000", "Route": 3},
        ...
        ]
        Args:
            denominaciones (List[int]) : Las denominaciones o valores de dinero con los que trabajará el . Ej: [100,200,500,1000]
            rutas (List[int]) : La posicion en los recicladores del dispositivo. Ej: [2,3,4,5]
        """
        if len(denominaciones) != len(rutas):
            logger.error("Los arrays deben tener la misma longitud")
            
            raise ValueError("Los arrays deben tener la misma longitud")

        resultado: List[Dict[str, Any]] = []
        for d, r in zip(denominaciones, rutas):
            resultado.append({
                "Denomination": f"{d if self.conexion.denominacion != "COP" else d * 100} {self.conexion.denominacion}",  #  por ejemplo "1000 COP"
                "Route": r
            })
        self.configuracion.SetRoutes = resultado

    # Concatena la ruta base con la ruta del modulo a utilizar
    def GetPath(self, modulo:str, key_device:bool = False) -> str:
        """
        Crea la ruta para el modulo indicado, concatenandola con la ruta base

        Args:
            modulo (string): Modulo al que se desea conectar.
            key_device (bool, opcional): Decide si incluye el ID del dispositivo en la URL 
        """
        ruta_modulo = self.rutas[modulo]
        if not ruta_modulo:
            logger.error(f"Módulo '{modulo}' no encontrado en las rutas.")
            raise ValueError(f"Módulo '{modulo}' no encontrado en las rutas.")
        
        url_completa = f"{self.conexion.url_base}{ruta_modulo}"
        if key_device:
            url_completa = f"{url_completa}?deviceID={self.conexion.id_dispositivo}"
        logger.debug(f"Ruta completa para el módulo '{modulo}': {url_completa}")
        return url_completa
    
    #  Obtiene los encabezados para las solicitudes HTTP
    def GetHeaders(self,autenticado: bool = False, json: bool = False) -> Dict[str, str]:
        """
        Obtiene los encabezados para las solicitudes HTTP.
        
        Args:
            autenticado (bool, opcional): Indica si se incluye en el encabezado el Token de autenticacion. Por defecto False
            json (bool, opcional): Indica si se va a incluir un cuerpo en formato JSON. Por defecto False
        """
        headers = {}
        # print(self.conexion.token)
        if autenticado:
            if not self.conexion.token:
                logger.error("Token de autenticación no disponible. Autentícate primero.")
                raise ValueError("Token de autenticación no disponible. Autentícate primero.")
            headers["Authorization"] = f"Bearer {self.conexion.token}"
        
        if json:
            headers["Content-Type"] = "application/json"
            
        return headers
# ----------------------------------------------------- ENDPOINTS ----------------------------------------------------------------- 

    # Obtiene el token de autenticación
    def Authenticate(self) -> str:
        """
        Método para Authenticate y obtener un token de acceso.
        """
        # Endpoint a utilizar
        url = self.GetPath("Authenticate")
        logger.info(f"URL de autenticación: {url}")
        
        # Cuerpo y Headers de la solicitud [Estructura definida en la doc de Postman API ITL]
        body = {
            "Username": self.usuario.Usuario,
            "Password": self.usuario.Contrasena
        }
        
        headers = self.GetHeaders(autenticado=False,json=True)
        
        # Obtenemos respuesta de la API
        respuesta = requests.post(url, json=body, headers=headers)
        
        
        if respuesta.status_code == 200:
            self.reintentos = 3
            self.reintentos = 3
            token = respuesta.json().get("token")
            logger.info("Autenticación exitosa.")
            self.conexion.token = token
            return True
        else:
            logger.error(f"Error en la autenticación: {respuesta.status_code}")
            return False
    
    #  Establece la conexion inicial con el dispositivo ITL.
    def OpenConnection(self):
        """
        Establece la conexion inicial con el dispositivo ITL.
        """
        self.configuracion.ComPort = self.conexion.puerto
        
        # print(self.configuracion)          # ----> Impresion para verificar que las configuraciones se limpiaron correctamente.
        
        url = self.GetPath("OpenConnection")
        
        # print(self.conexion.token)
        headers = self.GetHeaders(autenticado=True, json=True)
        
        # Si el objeto es un dataclass, se convierte a diccionario, si no, se usa tal cual.
        body = asdict(self.configuracion) if is_dataclass(self.configuracion) else self.configuracion
        
        respuesta = requests.post(url, json=body, headers=headers)
        if respuesta.status_code == 200:
            self.conexion.id_dispositivo = respuesta.json().get("deviceID")
            self.reintentos = 3
            logger.info("Conexión establecida exitosamente.")
            
            # print(respuesta.json())   # ----> Impresion para verificar que la conexion se establecio correctamente.
            
        elif respuesta.status_code == 401 and self.reintentos > 0:
            
            logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
            self.reintentos -= 1
            self.Authenticate()
            self.OpenConnection()  
        else:
            logger.error(f"Error al abrir la conexión: {respuesta.status_code} - {respuesta.text}")
            raise ValueError("Error al abrir la : {respuesta.status_code} - {respuesta.text}")

    # Cierra la conexión con el dispositivo ITL.
    def DisconnectDevice(self):
        """
        Cierra la conexión con el dispositivo ITL.
        """
        url = self.GetPath("DisconnectDevice", key_device=True)
        
        headers = self.GetHeaders(autenticado=True, json=False)
        
        respuesta = requests.post(url, headers=headers)
        if respuesta.status_code == 200:
            self.reintentos = 3
            logger.info("Conexión cerrada exitosamente.")
        else:
            logger.error(f"Error al cerrar la conexión: {respuesta.status_code} - {respuesta.text}")
            raise ValueError("Error al cerrar la conexión: {respuesta.status_code} - {respuesta.text}")
    
    # Obtiene el estado actual del dispositivo y sus ultimas acciones
    def GetDeviceStatus(self):
        """Obtiene el estado actual del dispositivo ITL.
        """
        url = self.GetPath("GetDeviceStatus", key_device=True)

        headers = self.GetHeaders(autenticado=True, json=False)

        respuesta = requests.get(url, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetDeviceStatus()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
        
    # Obtiene los estados actuales dce los cashbox
    def GetAllLevels(self):
        """
        Obtiene el estado de los niveles del cash
        """
        url = self.GetPath("GetAllLevels", key_device=True)
        headers = self.GetHeaders(autenticado=True)

        respuesta = requests.get(url, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetAllLevels()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Devuelve informacion de las denominaciones
    def GetCurrencyAssignment(self):
        """
        Devuelve la asignación actual de denominaciones (route, si está inhibida, si es reciclable, canal, etc.).
        """
        url = self.GetPath("GetCurrencyAssignment", key_device=True)
        headers = self.GetHeaders(autenticado=True)

        respuesta = requests.get(url, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetCurrencyAssignment()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Obtiene la información completa de los cash del dispositivo 
    def GetCompleteCashDevice(self):
        """
        Devuelve todas las variables públicas del objeto CashDevice (seriales, firmware, estados, counters, etc.).
        """
        url = self.GetPath("GetCompleteCashDevice", key_device=True)
        headers = self.GetHeaders(autenticado=True)

        respuesta = requests.get(url, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetCompleteCashDevice()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Obtiene los contadores de la maquina (cantidad dispensada, rechazada, etc)
    def GetCounters(self):
        """
        Obtiene contadores (stacked, stored, dispensed, rejected, etc.).
        """
        url = self.GetPath("GetCounters", key_device=True)
        headers = self.GetHeaders(autenticado=True)
        respuesta = requests.get(url,headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return respuesta.content
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetCounters()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Habilita la función de pago (permitir que el equipo entregue billetes/monedas).
    def EnablePayout(self):
        """
        Habilita la función de pago (permitir que el equipo entregue billetes/monedas).
        """
        url = self.GetPath("EnablePayout", True)
        headers = self.GetHeaders(True)
        respuesta = requests.post(url,headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.EnablePayout()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Deshabilita la función de pago (permitir que el equipo entregue billetes/monedas).
    def DisablePayout(self):
        """
        Deshabilita la función de pago (permitir que el equipo entregue billetes/monedas).
        """
        url = self.GetPath("DisablePayout", True)
        headers = self.GetHeaders(True)
        respuesta = requests.post(url,headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.DisablePayout()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Habilita el validador para aceptar dinero
    def EnableAcceptor(self):
        """
        Habilita el validador para recibir dinero
        """
        url = self.GetPath("EnableAcceptor", True)
        headers = self.GetHeaders(True)
        respuesta = requests.post(url,headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.EnableAcceptor()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Deshabilita el validador para aceptar dinero
    def DisableAcceptor(self):
        """
        Deshabilita el validador para recibir dinero
        """
        url = self.GetPath("DisableAcceptor", True)
        headers = self.GetHeaders(True)
        respuesta = requests.post(url,headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.DisableAcceptor()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Modifica si el dispositivo acepta automanticamente el dinero en ESCROW
    def SetAutoAccept(self, habilitado : bool = True):
        """
        Activa/desactiva la aceptación automática de notas que estén en escrow (booleano).
        
        Args: 
            habilitado (bool) : Decide si activa o desactiva la aceptacion automatica. True = activar, False = desactivar
        """
        dato = "false"
        url = self.GetPath("SetAutoAccept",True)
        headers = self.GetHeaders(autenticado=True,json=True)
        if habilitado:
            dato = "true"
        respuesta = requests.post(url=url,data=dato,headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetAutoAccept()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Permite aceptar el dinero que está en escrow o espera
    def AcceptFromEscrow(self):
        """
        Acepta el dinero en ESCROW
        """
        url = self.GetPath("AcceptFromEscrow",True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.post(url=url, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.AcceptFromEscrow()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # permite devolver el dinero que está en escrow o espera
    def ReturnFromEscrow(self):
        """
        Rechaza o devuelve el dinero en ESCROW
        """
        url = self.GetPath("ReturnFromEscrow",True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.post(url=url, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.ReturnFromEscrow()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Actualiza (activar/desactivar) las inhibiciones por denominación (aceptar o rechazar billetes).
    def SetDenominationInhibits(self, valores: List[int] = [], inhibir: bool = True):
        """
        Actualiza (activar/desactivar) las inhibiciones por denominación (solo SCS).

        Args:
            valores (List[int]): Valores de dinero a inhibir.
            inhibir (bool, opcional): Acepta/Rechaza la lista. Por defecto en True.

        """
        url = self.GetPath("SetDenominationInhibits",True)
        
        denominaciones = []
        
        for valor in valores:
            dato = f"{valor if self.conexion.denominacion != "COP" else valor * 100} {self.conexion.denominacion}"
            denominaciones.append(dato)
            
        body = {
            "ValueCountryCodes" : denominaciones,
            "Inhibit": "true" if inhibir else "false"
        }
        
        headers = self.GetHeaders(autenticado=True,json=True)
        
        respuesta = requests.post(url=url, json=body, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetDenominationInhibits(inhibir)
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Reinicia el dispositivo a sus configuraciones iniciales
    def ResetDevice(self):
        """
        Permite reiniciar el dispositivo conlas configuraciones por defecto
        """
        
        ruta = self.GetPath("ResetDevice", True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.post(url=ruta, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.ResetDevice()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Actualiza el usuario y contraseña en la autenticación por token
    def UpdateCredentials(self, usuario_actual : Usuario, usuario_nuevo : Usuario):
        """
        Actualiza las credenciales de conexion con el dispositivo
        
        Args:
            usuario_actual (dataclass Usuario): Objeto con credenciales de conexion actuales
            usuario_nuevo (dataclass Usuario) : Objeto con las nuevas credenciales de acceso
            """
        ruta = self.GetPath("UpdateCredentials", key_device=False)
        headers = self.GetHeaders(autenticado=True,json=True)
        
        body = {
            "CurrentUsername": usuario_actual.Usuario,
            "CurrentPassword": usuario_actual.Contrasena,
            "NewUsername": usuario_nuevo.Usuario,
            "NewPassword": usuario_nuevo.Contrasena
        }
        
        respuesta = requests.post(url=ruta, headers=headers, json=body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.UpdateCredentials(usuario_actual,usuario_nuevo)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    
    
    # Consulta los niveles actuales de la caja (cantidad por denominación).
    def GetCashboxLevels(self):
        """
        Consulta los niveles actuales de la caja (cantidad por denominación).
        
        """
        
        ruta = self.GetPath("GetCashboxLevels",True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.get(url=ruta, headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetCashboxLevels()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Configura cuantos billetes se pueden mantener simultaneamente en multi-escrow
    def SetMultiEscrowSize(self, tamano : int = 2):
        """
        Configura cuántos billetes se pueden mantener simultáneamente en multi-escrow.
        
        Args:
            tamano (int) : Cantidad de billetes que se pueden almacenar de manera simultanea en escrow. Por defecto 2
        """
        
        ruta = self.GetPath("SetMultiEscrowSize", True)
        
        headers = self.GetHeaders(autenticado=True)
        
        dato = str(tamano)
        
        respuesta = requests.post(url=ruta, headers=headers, data=dato)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetMultiEscrowSize(tamano)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Obtiene el tamaño de cuantos billetes se pueden mantener en mutiescrow
    def GetMultiEscrowSize(self):
        """Obtiene cuántos billetes se pueden mantener simultáneamente en multi-escrow."""
        
        ruta = self.GetPath("GetMultiEscrowSize", True)
        
        headers = self.GetHeaders(autenticado=True)
    
        respuesta = requests.get(url=ruta, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetMultiEscrowSize()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Obtiene la cantidad de dinero retenido en multi-escrow y su denominacion
    def GetMultiEscrowValue(self):
        """Obtiene cuántos billetes se encuentran actualmente en multi-escrow y su denominacion."""
        
        ruta = self.GetPath("GetMultiEscrowValue", True)
        
        headers = self.GetHeaders(autenticado=True)
    
        respuesta = requests.get(url=ruta, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetMultiEscrowValue()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Obtiene la cantidad de dinero retenido en multi-escrow y su denominacion
    def CommitMultiEscrow(self):
        """Confirma todos los billetes retenidos en multi-escrow (los almacena)."""
        
        ruta = self.GetPath("CommitMultiEscrow", True)
        
        headers = self.GetHeaders(autenticado=True)
    
        respuesta = requests.post(url=ruta, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.CommitMultiEscrow()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Obtiene la cantidad de dinero retenido en multi-escrow y su denominacion
    def CancelMultiEscrow(self):
        """Devuelve todos los billetes retenidos en multi-escrow"""
        
        ruta = self.GetPath("CancelMultiEscrow", True)
        
        headers = self.GetHeaders(autenticado=True)
    
        respuesta = requests.post(url=ruta, headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.CancelMultiEscrow()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Devuelve la cantidad de dinero ingresado
    def DispenseValue(self, valor : int = 0):
        """
        Ordena al dispositivo que entregue una cantidad especificada de dinero (payout).
        
        Args:
            valor (int): Valor en dinero de la denominación establecida la cual se desea dispensar del dispositivo
        """
        ruta = self.GetPath("DispenseValue", True)
        logger.info("...Dispensando...")
        headers = self.GetHeaders(autenticado=True,json=True)
        dinero = valor
        body = {
            "Value" : dinero,
            "CountryCode" : self.conexion.denominacion
        }
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.DispenseValue(valor)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Establece el limite de pago valido por modulo
    def SetCashboxPayoutLimit(self,valores: List[int] = []):
        """representa el número máximo de billetes que se pueden pagar por cada denominación. Cada índice corresponde a una denominación específica en la matriz de asignación de moneda.
        Permite al host especificar un nivel máximo de monedas/billetes, por denominación, que se pueden dejar en la tolva/reciclador. El valor predeterminado después de encender/reiniciar la unidad es 0 (sin límite).
        
        Args:
            vaores (List[int]) : Lista de valores (de tamaño n según la cantidad de recicladores) donde se indica la cantidad de billetes que puede tener cada reciclador
        """
        
        ruta = self.GetPath("SetCashboxPayoutLimit", True)
        headers = self.GetHeaders(autenticado=True)
        datos = str(valores)
        
        respuesta = requests.post(url = ruta, headers = headers, data = datos)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetCashboxPayoutLimit(valores)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Vacia el modulo ingresado
    def SmartEmpty(self, numero_modulo : int):
        """
        Vacía inteligentemente (según reglas) el contenido de la caja/recycler.
        
        Args:
            numero_modulo (int) : Numero del modulo que se desea vaciar
        """
        
        ruta = self.GetPath("SmartEmpty", True)
        headers = self.GetHeaders(autenticado=True,json=True)
        body = {
            "ModuleNumber" : numero_modulo
        }
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SmartEmpty(numero_modulo)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Detiene inmediatamente cualquier pago en curso
    def HaltPayout(self):
        """Cancela cualquier pago en proceso"""
        ruta = self.GetPath(modulo="HaltPayout", key_device=True)
        headers = self.GetHeaders(autenticado=True)
        respuesta = requests.post(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.HaltPayout()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Número de billetes que se repondrán desde el RC a los módulos de pago.
    def Replenish(self,cantidad : int):
        """
        Número de billetes que se repondrán desde el RC a los módulos de pago.
        
        Args:
            cantidad (int): Cantidad de billetes que se repondran desde el RC a los modulos de pago    
        """    
        ruta = self.GetPath(modulo="Replenish", key_device=True)
        headers = self.GetHeaders(autenticado=True)
        dato = str(cantidad)
        
        respuesta = requests.post(url = ruta, data = dato, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.Replenish(cantidad)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Configura en modo de rellenado
    def RefillMode(self, estado = True):
        """
        Cambiael modo de rellenado (para recargas).
        
        Args:
            estado (bool) : Habilita o deshabilita el modo rellenado de la maquina. Por defecto True
        """
        ruta = self.GetPath(modulo="RefillMode", key_device=True)
        headers = self.GetHeaders(autenticado=True)
        dato = "true" if estado else "false"
        
        respuesta = requests.post(url = ruta, data = dato, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.RefillMode(estado)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Configura los niveles actuales de la caja (cantidad por denominación).
    def SetCashboxLevels(self, cantidad_dinero: int = 0, valor_dinero: int = 0):
        """
        Configura los niveles actuales de la caja (cantidad por denominación).
        
        Args:
            cantidad_dinero (int) : Numero de billetes o monedas a configurar. Por defecto 0
            valor_dinero (int) : Valor del billete o moneda a configurar. Por defecto 0
        """
        
        ruta = self.GetPath("SetCashboxLevels",True)
        headers = self.GetHeaders(autenticado=True, json = True)
        body = {
            "NumCoinsToAdd" : cantidad_dinero,
            "Denomination" : valor_dinero if self.conexion.denominacion != "COP" else valor_dinero * 100,
            "CountryCode" : self.conexion.denominacion
        }
        respuesta = requests.post(url=ruta, headers=headers, json = body)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetCashboxLevels(cantidad_dinero,valor_dinero)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            


    # Limpia los niveles actuales de la caj (cantidad por denominación).
    def ClearCashboxLevels(self):
        """
        Limpia los niveles actuales de la caja. Vaciado de cashbox
        """
        
        ruta = self.GetPath("ClearCashboxLevels",True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.post(url=ruta, headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.ClearCashboxLevels()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Consulta niveles de billetes específicamente en la cashbox.
    def GetNoteCashboxLevels(self):
        """
        Consulta niveles de billetes específicamente en la cashbox.
        """
        
        ruta = self.GetPath("GetNoteCashboxLevels",True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.get(url=ruta, headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetNoteCashboxLevels()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Segunda version para limpiar los billetes del cashbox
    def ClearNoteCashboxLevels(self):
        """
        Limpia los niveles actuales de la caja. Vaciado de cashbox
        """
        
        ruta = self.GetPath("ClearNoteCashboxLevels",True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.post(url=ruta, headers=headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.ClearNoteCashboxLevels()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Define un límite máximo que puede pagarse en una operación.
    def SetPayoutLimit(self, cantidad_monedas : int = 0):
        """
        Limita la cantidad de monedas que se pueden dispensar en una transacción
        
        Args:
            cantidad_monedas (int) : Limite de monedas que puede dispensar el dispositivo. Por defecto 0    
        """
        ruta = self.GetPath("SetPayoutLimit", True)
        headers = self.GetHeaders(autenticado=True)
        dato = str(cantidad_monedas)
        respuesta = requests.post(url = ruta, headers = headers, data = dato)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetPayoutLimit()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Devuelve cuántos pagos se han hecho (contador).
    def GetPayoutCount(self):
        """Devuelve cuántos pagos se han hecho (contador)."""
        ruta = self.GetPath("GetPayoutCount",key_device=True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetPayoutCount()
            case __:    
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Obtiene errores globale y generales del dispositivo
    def GetGlobalErrorCode(self):
        """Devuelve códigos de error globales del dispositivo (para diagnóstico)."""
        ruta = self.GetPath("GetGlobalErrorCode", True)
        headers = self.GetHeaders(autenticado=True)
        
        respuesta = requests.get(url = ruta, headers = headers) 
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetGlobalErrorCode()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Envía un comando personalizado de bajo nivel al dispositivo
    def SendCustomCommand(self, comando: str = ""):
        """
        Envía un comando personalizado de bajo nivel al dispositivo
        
        Args:
            comando (str) : Cadena de texto que contiene el comando en bajo nivel que se enviará al dispositivo. Por defecto vacío  
        """
        
        ruta = self.GetPath("SendCustomCommand", True)
        headers = self.GetHeaders(autenticado = True, json = True)
        body = {
            "CommandData": comando
        }
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SendCustomCommand(comando)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    # Habilita un módulo o dispositivo específico para realizar pagos
    def EnablePayoutDevice(self):
        """
        Habilita un módulo o dispositivo específico para realizar pagos.
        """
        url = self.GetPath("EnablePayoutDevice", True)
        headers = self.GetHeaders(True)
        respuesta = requests.post(url,headers=headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {url}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.EnablePayoutDevice()
            case __:
                logger.error(f"Error en : {url} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Configura la ruta de destino de un valor de billete o moneda específico
    def SetDenominationRoute(self, valor_dinero: int = 0, ruta: int = 0):
        """
        Configura la ruta de destino de un valor de billete o moneda específico
        Args:
            valor_dinero (int) : Valor de la moneda o billete al cual se desea asignar la ruta. Por defecto 0
            ruta (int) : Dirección de Cash o Reciclador a donde se asignará el billete o moneda enviada. Por defecto 0
        """
        url = self.GetPath("SetDenominationRoute", key_device= True)
        headers = self.GetHeaders(autenticado = True, json = True)
        body = {
            "Value" : valor_dinero if self.conexion.denominacion != "COP" else valor_dinero * 100,
            "CountryCode": self.conexion.denominacion,
            "Route" : ruta
        }
        
        respuesta = requests.post(url = url, headers= headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetDenominationRoute(valor_dinero,ruta)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    # Inicia el proceso/servicio que mantiene al dispositivo funcionando y escuchando eventos.
    def StartDevice(self):
        """
        Inicia el proceso/servicio que mantiene al dispositivo funcionando y escuchando eventos.
        """
        ruta = self.GetPath(key_device=True,modulo="StartDevice")
        
        headers = self.GetHeaders(autenticado = True, json = False)
        
        respuesta = requests.post(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.StartDevice()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Detiene el proceso que gestiona el dispositivo, pero deja el puerto abierto
    def StopDevice(self):
        """
        Detiene el proceso que gestiona el dispositivo, pero deja el puerto abierto.
        """
        ruta = self.GetPath(key_device=True,modulo="StopDevice")
        
        headers = self.GetHeaders(autenticado = True, json = False)
        
        respuesta = requests.post(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.StopDevice()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    # Activa el registro de los mensajes brutos que intercambia el dispositivo (para depuración).
    def LogRawPackets(self, activar : bool = True):
        """
        Activa el registro de los mensajes brutos que intercambia el dispositivo (para depuración).
        
        Args:
            activar (bool) : valor que decide si activa o desactiva el registro de los mensajes. Por defecto True
        """
        ruta = self.GetPath(key_device=True,modulo="LogRawPackets")
        data = "true" if activar else "false"
        headers = self.GetHeaders(autenticado = True, json = False)
        
        respuesta = requests.post(url = ruta, headers = headers, data = data)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.LogRawPackets()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
        
    #Ajusta manualmente el conteo/reportado de una denominación concreta.
    def SetDenominationLevel(self, valor_dinero : int = 0, cantidad_dinero : int = 0):
        """
        Ajusta manualmente el conteo/reportado de una denominación concreta.
        
        Args:
            valor_dinero (int) : Valor de la denominacion que se desea ajustar. Por defecto 0
            cantidad_dinero (int) : Unidades de billete o moneda del valor solicitado. Por defecto 0
        """
        ruta = self.GetPath(key_device=True, modulo = "SetDenominationLevel")
        headers = self.GetHeaders(autenticado = True, json = True)
        body = {
            "Value" : valor_dinero if self.conexion.denominacion != "COP" else valor_dinero * 100,
            "CountryCode" : self.conexion.denominacion,
            "NumCoinsToAdd" : cantidad_dinero
        }
        
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetDenominationLevel(valor_dinero,cantidad_dinero)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    #Consulta la configuración del lector de códigos de barra (si existe).
    def GetBarcodeReaderConfiguration(self):
        """Consulta la configuración del lector de códigos de barra (si existe)."""
        ruta = self.GetPath(key_device= True)
        headers = self.GetHeaders(autenticado = True)
        respuesta = requests.get(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetBarcodeReaderConfiguration()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    #Ajusta la configuración del lector de códigos de barra.
    def SetBarcodeReaderConfiguration(self,habilitar : int = 0, formato_codigo : int = 0, numero_caracteres : int = 0):
        """
        Ajusta la configuración del lector de códigos de barra.
        
        Args:
            habilitar (int) : Indica los lectores a habilitar. Por defecto 0
            formato_codigo (int) : Formato del QR. Por defecto 0
            numero_caracteres (int) : Define el numero de caracteres que contendrá el QR. Por defecto 0
        """
        ruta = self.GetPath("SetBarcodeReaderConfiguration",key_device = True)
        headers = self.GetHeaders(autenticado = True, json = True)
        body = {
            "EnableReaders": habilitar,
            "BarCodeFormat": formato_codigo,
            "NumberOfCharacters": numero_caracteres
        }
        
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetBarcodeReaderConfiguration(habilitar,formato_codigo,numero_caracteres)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    #Obtiene el último código de barra válido leído (p. ej. ticket).
    def GetBarcodeData(self):
        """Obtiene el último código de barra válido leído (p. ej. ticket)."""
        ruta = self.GetPath("GetBarcodeData", key_Device = True)
        headers = self.GetHeaders(autenticado = True, json = False)
        respuesta = requests.get(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetBarcodeData()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            

    #Habilita el mecanismo de monedas o alimentador (si el equipo tiene módulo de monedas).
    def EnableCoinMechOrFeeder(self, activar : bool = True):
        """
        Habilita el mecanismo de monedas o alimentador (si el equipo tiene módulo de monedas).
        
        Args:
            activar (bool) : Activa/Desactiva el mecanismo de monedas. Por defecto True
        """
        ruta = self.GetPath(key_device=True,modulo="EnableCoinMechOrFeeder")
        data = "true" if activar else "false"
        headers = self.GetHeaders(autenticado = True, json = False)
        
        respuesta = requests.post(url = ruta, headers = headers, data = data)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.EnableCoinMechOrFeeder(activar)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    #Consulta el modo del cassette de reposición (replenishment cassette).
    def GetRCMode(self):
        """Consulta el modo del cassette de reposición (replenishment cassette)."""
        
        ruta = self.GetPath("GetRCMode", key_device = True)
        headers = self.GetHeaders(autenticado = True, json = False)
        
        respuesta = requests.get(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetRCMode()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    
    #Obtiene opciones/configuración del hopper (mecanismo de monedas).
    def GetHopperOptions(self):
        """Obtiene opciones/configuración del hopper (mecanismo de monedas)."""
        
        ruta = self.GetPath("GetHopperOptions", key_device = True)
        headers = self.GetHeaders(autenticado = True, json = False)
        
        respuesta = requests.get(url = ruta, headers = headers)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetHopperOptions()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
    
    #Ajusta opciones del hopper.
    def SetHopperOptions(self, reg0 : int = 0, reg1 : int = 0):
        """Ajusta opciones del hopper"""
        
        ruta = self.GetPath("SetHopperOptions", key_device= True)
        headers = self.GetHeaders(True,True)
        body = {
            "Reg0" : reg0,
            "Reg1" : reg1
        }
        
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetHopperOptions(reg0, reg1)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
    
    #Obtiene informacion del servicio general
    def GetServiceInformation(self, byte : int = 1):
        """
        Obtiene información de servicio general (texto/instrucciones para mantenimiento).
        Args:
            byte (int) : El subcomando para especificar el tipo de información de servicio a recuperar.
                Posibles valores:
                    - 1 : Extrae el número de notas desde diversos eventos, como el restablecimiento de mantenimiento, la última descarga, el encendido y el último atasco
                    - 2 : Extrae el número de notas aceptadas desde el restablecimiento de mantenimiento, la última descarga y el encendido.
                    - 3 : Extrae el número de atascos desde el restablecimiento de mantenimiento, la última descarga y en los últimos 1000 billetes.
                    - 4 : Devuelve el estado actual del indicador de servicio.
        """
        ruta = self.GetPath("GetServiceInformation", key_device = True)
        headers = self.GetHeaders(True, False)
        dato = str(byte)
        
        respuesta = requests.get(url = ruta, headers = headers, data = dato)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetServiceInformation()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
    
    #Obtiene la información de servicio específica de un módulo concreto.
    def GetServiceInformationForModule(self, modulo : int = 0, subcomando : int = 0):
        """
        Recupera información de servicio del dispositivo según el módulo y el subcomando proporcionados, y formatea la información en una cadena legible.
        
        Args:
            modulo (int) : El identificador del módulo que especifica el tipo de módulo del que se recuperará la información.
            subcomando (int) :  El subcomando que especifica el tipo de información de servicio que se recuperará   
        """
        ruta = self.GetPath("GetServiceInformationForModule", key_device = True)
        headers = self.GetHeaders(True,True)
        body = {
            "Module" : modulo,
            "SubCommand" : subcomando
        }
    
        respuesta = requests.get(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetServiceInformationForModule()
            case __:
                logger.error(f"Error al obtener: {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
            
    #Resetea la información de mantenimiento (marcar que se hizo mantenimiento).
    def SetServiceInformationMaintenanceReset(self, semana : str = "00", anio : str = "25"):
        """
        Resetea la información de mantenimiento (marcar que se hizo mantenimiento).
        
        Args:
            semana (str) : Dos digitos de la semana del reseteo de  en formato "ww". Por defecto "00"
            anio (str) : Dos ultimos digitos del año del reseteo de mantenimiento en formato "YY". Por defecto "25"
        """
        if len(semana) != 2 or len(anio) != 2:
            raise ValueError("La semana y el año deben tener solo dos digitos")
        
        datos = [semana[0], semana[1], anio[0], anio[1]]
        datos_convertidos = []
        
        try:
            for numero in datos:
                datos_convertidos.append(int(numero))
        except ValueError:
            raise ValueError("Error al digitar la fecha. Formato string invalido")
        
        ruta = self.GetPath("SetServiceInformationMaintenanceReset",True)
        headers = self.GetHeaders(True,True)
        body = {
            "WeekNumber1AsciiByte" : datos_convertidos[0],
            "WeekNumber2AsciiByte" : datos_convertidos[1],
            "YearNumber1AsciiByte" : datos_convertidos[2],
            "YearNumber2AsciiByte" : datos_convertidos[3]
        }
        
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetServiceInformationMaintenanceReset(semana,anio)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
    
    #Consulta qué monedas están aceptadas por el equipo.
    def GetCoinAcceptance(self, byte_dispositivo : int = 0):
        """
        Consulta qué monedas están aceptadas por el equipo.
        
        Args:
            byte_dispositivo (int) : El byte que representa el componente específico del dispositivo desde el cual se recuperará el estado de aceptación de monedas.
        """
        ruta = self.GetPath("GetCoinAcceptance",True)
        headers = self.GetHeaders(autenticado=True)
        dato = str(byte_dispositivo)
        
        respuesta = requests.get(url = ruta, headers = headers, data = dato)
        
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetCoinAcceptance(byte_dispositivo)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                self.DisconnectDevice()
                
    # Establece la ruta para que la denominación especificada vaya a la tolva PRINCIPAL o SECUNDARIA del sistema de monedas Twin SMART.
    def SetSorterRoute(self, valor : int = 0, ruta_sorter : int = 0):
        """
        Establece la ruta para que la denominación especificada vaya a la tolva PRINCIPAL o SECUNDARIA del sistema de monedas Twin SMART.
        
        Args:
            valor (int) : representa el valor del dinero en su respectivo codigo de país
            ruta_sorter (int) : La ruta de clasificación que se establecerá para la denominación especificada. Use 0 para la tolva PRINCIPAL y 1 para la tolva SECUNDARIA.
        """
        ruta = self.GetPath("SetSorterRoute", True)
        headers = self.GetHeaders(autenticado = True, json = True)
        body = {
            "Value" : valor,
            "CountryCode" : self.conexion.denominacion,
            "SorterRoute" : ruta_sorter
        }
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetSorterRoute(valor,ruta_sorter)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
    
    # Consulta cómo están asignadas actualmente las rutas del sorter.
    def GetSorterRouteAssignment(self):
        """Consulta cómo están asignadas actualmente las rutas del sorter."""
        ruta = self.GetPath("GetSorterRouteAssignment", True)
        headers = self.GetHeaders(autenticado=True)
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetSorterRouteAssignment()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                
    # Ajusta el modo "twin" (relacionado con configuración de dispositivos dobles).
    def SetTwinMode(self, modo : int = 0):
        """
        Ajusta el modo "twin" (relacionado con configuración de dispositivos dobles).
        
        Args:
            modo (int) : Modo de operación. Actualmente hay 4 modos disponibles
                Posibles Valores:
                - 0 : Sistema de Monedas Inteligentes Normal
                - 1 : Sistema de Monedas Inteligentes Doble
                - 2 : Sistema de Monedas Inteligentes Doble Simple
                - 3 : Modo Twin 1ec Equilibrado
        """
        ruta = self.GetPath("SetTwinMode", True)
        headers = self.GetHeaders(True,False)
        respuesta = requests.post(url = ruta, headers = headers, data = str(modo))
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.SetTwinMode(modo)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
    
    # Comprueba si hay algún error de lectura en el puerto COM
    def ComPortReadError(self):
        """Comprueba si hay algún error de lectura en el puerto COM"""
        ruta = self.GetPath("comPortReadError", True)
        headers = self.GetHeaders(autenticado=True, json=False)
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.ComPortReadError()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")

    # Consulta el estado del lifter (mecanismo que mueve billetes dentro del equipo).
    def GetLifterStatus(self):
        """Consulta el estado del lifter (mecanismo que mueve billetes dentro del equipo)."""
        ruta = self.GetPath("GetLifterStatus", True)
        headers = self.GetHeaders(autenticado=True, json=False)
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetLifterStatus()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
    
    # Devuelve la razón por la que se rechazó el último billete.
    def GetLastRejectCode(self):
        """Devuelve la razón por la que se rechazó el último billete."""
        ruta = self.GetPath("GetLastRejectCode", True)
        headers = self.GetHeaders(autenticado = True, json = False)
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetLastRejectCode()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                
    # Muestra los ficheros de moneda disponibles en Smart Currency (tarjeta SD).
    def GetSmartCurrencyData(self):
        """Muestra los ficheros de moneda disponibles en Smart Currency (tarjeta SD)."""
        ruta = self.GetPath("GetSmartCurrencyData", True)
        headers = self.GetHeaders(autenticado = True, json = False)
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return respuesta.json()
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetLastRejectCode()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                
    # Establece el conjunto de datos para la moneda que desea aceptar de la tarjeta SD insertada en el Smart Currency NV200 Spectral
    def UpdateSmartCurrencyDataset(self, codigo_dataset : str = ""):
        """
        Establece el conjunto de datos para la moneda que desea aceptar de la tarjeta SD insertada en el Smart Currency NV200 Spectral
        
        Args:
            codigo_dataset (str) : El código del conjunto de datos para el archivo de moneda que desea aceptar.
        """
        ruta = self.GetPath("UpdateSmartCurrencyDataset",key_device = True)
        headers = self.GetHeaders(autenticado = True, json = False)
        respuesta = requests.post(url = ruta, headers = headers, data = codigo_dataset)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.UpdateSmartCurrencyDataset(codigo_dataset)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
    
    # Inicia la descarga de un dataset/firmware al dispositivo.
    def StartDownload(self, ruta_Archivo : str = "C:/IT_EXAMPLE.bv1", puerto : str = "", direccionSSP : str = ""):
        """Inicia la descarga de un dataset/firmware al dispositivo.
        
        Args:
            ruta_archivo (str) : ruta de archivo con el firmware o dataset. La ruta debe contener el directorio, el nombre y la extension de archivo.
            puerto (str) : Puerto donde se encuentra localizado el dispositivo ITL
            direccionSSP (str) : Direccion SSP de la comunicacion con el dispositivo ITL"""
            
        ruta = self.GetPath("StartDownload", key_device = False)
        headers = self.GetHeaders(autenticado = True, json =True)
        body = {
            "DownloadFileName" : ruta_Archivo,
            "ComPort" : puerto,
            "SspAddress" : direccionSSP
        }
        respuesta = requests.post(url = ruta, headers = headers, json = body)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.StartDownload(ruta_Archivo,puerto,direccionSSP)
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")   
                
    # Consulta el progreso/estado de una descarga iniciada.
    def GetDownloadStatus(self):
        """Consulta el progreso/estado de una descarga iniciada."""
        ruta = self.GetPath("GetDownloadStatus", key_device = False)
        headers = self.GetHeaders(autenticado = True, json = False)
        respuesta = requests.get(url = ruta, headers = headers)
        match respuesta.status_code:
            case 200:
                self.reintentos = 3
                logger.info(f"OK desde : {ruta}")
                return True
            
            case 401:
                if self.reintentos > 0:
                    logger.error(f"Acceso denegado: {respuesta.status_code} - {respuesta.text}, obteniendo un nuevo token.")
                    self.reintentos -= 1
                    self.Authenticate()
                    self.GetDownloadStatus()
            case __:
                logger.error(f"Error en : {ruta} : {respuesta.status_code} - {respuesta.text}")
                
    

    def ReceiveUntilAmount(self, monto_objetivo: int, timeout: int = 120, poll_interval: float = 1.0, set_multi_size: int = 20, auto_accept: bool = False) -> Dict[str, Any]:
        """
        Espera y acumula notas en ESCROW hasta que el valor retenido sea >= monto_objetivo.
        Solo para dispositivos con multi-escrow (MNE: Spectral Payout, NV4000...).

        Args:
            monto_objetivo (int): Monto objetivo en la misma unidad que devuelve GetMultiEscrowValue.
            timeout (int): Tiempo máximo en segundos para esperar. Default 120s.
            poll_interval (float): Intervalo de sondeo en segundos. Default 1s.
            set_multi_size (int): Tamaño multi-escrow a configurar (por defecto 20, máximo documentado).
            auto_accept (bool): Si True activa SetAutoAccept(True) (aceptación automática).
                                Si False se mantiene auto-accept desactivado y se usa CommitMultiEscrow.

        Returns:
            dict: {
                "success": bool,
                "collected": int,            # valor en escrow al momento de retorno
                "message": str,
                "committed": bool            # True si se hizo CommitMultiEscrow
            }
        """
        inicio = time.time()
        try:
            # 1) Asegurar acceptor activo
            try:
                self.EnableAcceptor()
            except Exception as e:
                logger.warning(f"EnableAcceptor devolvió error (continuando): {e}")

            # 2) Configurar multi-escrow size si el dispositivo lo soporta
            try:
                self.SetMultiEscrowSize(set_multi_size)
            except Exception as e:
                logger.warning(f"No se pudo setear multi-escrow size: {e} (puede que el dispositivo no soporte SetMultiEscrowSize)")

            # 3) Configurar auto-accept según parámetro
            try:
                self.SetAutoAccept(auto_accept)
            except Exception as e:
                logger.warning(f"SetAutoAccept devolvió error (continuando): {e}")

            # 4) Bucle de sondeo
            collected = 0
            committed = False
            while True:
                # Comprobar timeout
                if time.time() - inicio > timeout:
                    return {
                        "success": False,
                        "collected": collected,
                        "message": f"Timeout alcanzado ({timeout}s). Valor en escrow: {collected}",
                        "committed": committed
                    }

                # Intentar leer valor en multi-escrow
                try:
                    respuesta = self.GetMultiEscrowValue()
                except Exception as e:
                    # No es multi-escrow o fallo al consultar
                    logger.error(f"Error consultando GetMultiEscrowValue: {e}")
                    return {
                        "success": False,
                        "collected": 0,
                        "message": "GetMultiEscrowValue no disponible o falló. Dispositivo puede no soportar multi-escrow.",
                        "committed": False
                    }

                # respuesta esperada: {"multiEscrowValue": 1000, "multiEscrowCurrency": "EUR"}
                if not respuesta:
                    collected = 0
                else:
                    # Normalizar estructura segura
                    if isinstance(respuesta, dict):
                        collected = respuesta.get("multiEscrowValue", 0)
                        currency = respuesta.get("multiEscrowCurrency", None)
                    else:
                        # Si tu método devuelve JSON/str, intenta parsear de forma robusta
                        try:
                            collected = int(respuesta)
                            currency = self.conexion.denominacion
                        except Exception:
                            collected = 0
                            currency = None

                logger.info(f"Valor en escrow: {collected} {currency if currency else ''} (objetivo: {monto_objetivo})")

                # Si ya alcanzó o sobrepasó el objetivo: commitear y salir
                if collected >= monto_objetivo:
                    try:
                        self.CommitMultiEscrow()
                        committed = True
                        return {
                            "success": True,
                            "collected": collected,
                            "message": f"Objetivo alcanzado. Se committearon {collected} {currency if currency else ''}.",
                            "committed": True
                        }
                    except Exception as e:
                        logger.error(f"CommitMultiEscrow falló: {e}")
                        return {
                            "success": False,
                            "collected": collected,
                            "message": f"Objetivo alcanzado pero CommitMultiEscrow falló: {e}",
                            "committed": False
                        }

                # Sino: esperar y volver a consultar
                time.sleep(poll_interval)

        except Exception as e:
            logger.exception("ReceiveUntilAmount fallo inesperadamente")
            return {
                "success": False,
                "collected": 0,
                "message": f"Error inesperado: {e}",
                "committed": False
            }

        