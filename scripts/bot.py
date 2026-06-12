#!/usr/bin/env python3
"""TPI de Organización Empresarial
Simulación de Solicitud de Vacaciones"""

from csv import writer
import pandas as pd
from datetime import datetime

def obtener_siguiente_codigo_tramite() -> str:
    """
    Genera el siguiente código de trámite único.
    
    Returns:
        Código de trámite generado
    """
    ruta = "estados/contador.csv"

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            numero = int(archivo.read().strip() or "0")
        numero += 1
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(str(numero))
        codigo = f"VAC{numero:03d}"
        return codigo
    except Exception as e:
        raise Exception(f"Error al generar código de trámite: {e}")

def cargar_empleados() -> pd.DataFrame:
    """
    Carga el dataframe de empleados desde CSV.
    
    Returns:
        pd.DataFrame: Dataframe con empleados
    """
    ruta = "datos/empleados.csv"

    empleados = pd.read_csv(ruta)
    return empleados

def cargar_tramite(codigo_tramite: str) -> pd.DataFrame:
    """
    Carga el registro del trámite solicitado.
    
    Args:
        codigo_tramite: string con el código del trámite.
    Returns:
        pd.DataFrame: Dataframe con datos del trámite solicitado.
    """
    ruta = "estados/tramites.csv"

    try:
        tramites = pd.read_csv(ruta)
        tramite = tramites.loc[tramites["id_tramite"] == codigo_tramite].copy()
        if not tramite.empty:
            return tramite
        else:
            raise ValueError(f"No se encontró el trámite: {codigo_tramite}")
    except Exception as e:
        raise Exception(f"Error al encontrar el código de trámite: {e}") 

def validar_empleado_existe(id_empleado: str, empleados: list) -> bool:
    """
    Valida si un empleado existe en el sistema.
    
    Args:
        id_empleado: ID del empleado a validar
        empleados: Dataframe (pandas) con empleados
    Returns:
        True si existe, False en caso contrario
    """
    return id_empleado in empleados

def pedir_DNI() -> int:
    """
    Solicita al usuario su número de DNI.

    Returns:
        DNI como número entero
    """
    while True:
        try:
            DNI = input("Ingrese su DNI (sólo numeros): ").strip()
            if DNI.isdigit():
                return int(DNI)
            else:
                raise ValueError("Sólo puede ingresar números (sin puntos, etc.)")
        except ValueError as e:
            print(f"Error en el ingreso de DNI: {e}")

def pedir_fechas() -> tuple[datetime, datetime]:
    """
    Solicita al usuario las fechas de inicio y finalización de vacaciones.

    Returns:
        Tupla con dos datetimes (fecha de inicio y fecha de finalización)
    Raises:
        ValueError: Si el formato es inválido o las fechas incompatibles
    """
    while True:
        while True:
            try:
                fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio de vacaciones (formato DD/MM/AAAA): ").strip(), "%d/%m/%Y")
                break
            except ValueError:
                print("Error en el ingreso de fecha: Formato de fecha inválido.")
        while True:
            try:
                fecha_fin = datetime.strptime(input("Ingrese la fecha de finalización de vacaciones (formato DD/MM/AAAA): ").strip(), "%d/%m/%Y")
                break
            except ValueError:
                print("Error en el ingreso de fecha: Formato de fecha inválido.")
        if fecha_inicio > fecha_fin:
            print("La fecha de inicio no puede ser posterior a fecha de fin.")
        elif fecha_inicio < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
            print("La fecha de inicio no puede ser en el pasado.")
        else:
            return [fecha_inicio, fecha_fin]

def calcular_dias_solicitados(fecha_inicio: datetime, fecha_fin: datetime) -> int:
    """
    Calcula la cantidad de días entre dos fechas (inclusive).
    
    Args:
        fecha_inicio: Fecha de inicio
        fecha_fin: Fecha de fin
    Returns:
        int: Cantidad de días
    """
    diferencia = fecha_fin - fecha_inicio
    dias = diferencia.days + 1
    return dias

def actualizar_tramite(codigo_tramite: str, fecha_inicio: bool|datetime = False, fecha_fin: bool|datetime = False, nuevo_estado: bool|int = False):
    """
    Actualiza el registro del trámite solicitado,
    modificando el estado o agregando fechas.
    
    Args:
        codigo_tramite: string con el código del trámite.
        fecha_inicio: False si está vacío, o datetime con la fecha de inicio.
        fecha_fin: False si está vacío, o datetime con la fecha de finalización.
        nuevo_estado: False si está vacío, número entero con el nuevo estado del trámite.
    """
    ruta = "estados/tramites.csv"

    try:
        tramites = pd.read_csv(ruta)
        if fecha_inicio:
            tramites["fecha_inicio"] = tramites["fecha_inicio"].astype(str).str.replace("nan", "")
            tramites.loc[tramites["id_tramite"] == codigo_tramite, "fecha_inicio"] = fecha_inicio.strftime("%d/%m/%Y")
        if fecha_fin:
            tramites["fecha_fin"] = tramites["fecha_fin"].astype(str).str.replace("nan", "")
            tramites.loc[tramites["id_tramite"] == codigo_tramite, "fecha_fin"] = fecha_fin.strftime("%d/%m/%Y")
        if nuevo_estado:
            tramites.loc[tramites["id_tramite"] == codigo_tramite, "estado"] = nuevo_estado
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(tramites.to_csv(index=False))
    except Exception as e:
        raise Exception(f"Error al actualizar el trámite: {e}")

def iniciar_tramite(id_empleado: int) -> str:
    """
    Registra el inicio del trámite, asignándole un código único.

    Args:
        id_empleado: ID del empleado
    Returns:
        Código del trámite asignado
    """
    ruta = "estados/tramites.csv"

    try:
        id_tramite = obtener_siguiente_codigo_tramite()
        with open(ruta, "a", encoding="utf-8", newline="") as archivo:
            writer(archivo).writerow([id_tramite, id_empleado, "", "", 1])
        return id_tramite
    except Exception as e:
        raise Exception(f"Error al registrar el inicio de trámite: {e}")

def seguir_tramite(codigo: str) -> None:
    """
    Recupera el trámite desde su último punto guardado

    Args:
        codigo: ID del trámite
    """
    tramite = cargar_tramite(codigo)
    if tramite.iloc[0]["estado"] == 1:
        empleados = cargar_empleados()
        print(empleados)
        empleado = empleados.loc[empleados["DNI"] == tramite.iloc[0]["id_empleado"]].copy()
        print(empleado)
        if empleado.iloc[0]["dias_disponibles"] == 0:
            print("No quedan días disponibles para tomarse.
Solicitud de vacaciones denegada.")
            actualizar_tramite(tramite.iloc[0]["id_tramite"], nuevo_estado=66)
        else:
            print(f"Usted posee {empleado.iloc[0]["dias_disponibles"]} días disponibles para tomarse.")
            while True:
                fecha_inicio, fecha_fin = pedir_fechas()
                dias_solicitados = calcular_dias_solicitados(fecha_inicio, fecha_fin)
                if dias_solicitados <= empleado.iloc[0]["dias_disponibles"]:
                    break
                else:
                    print(f"Se solicitan "{dias_solicitados}" días, pero sólo dispone de {empleado.iloc[0]["dias_disponibles"]} días.")
            actualizar_tramite(tramite.iloc[0]["id_tramite"], fecha_inicio, fecha_fin, 2)
            print(f"Solicitud de Vacaciones enviada a RRHH, con N° de Trámite: {tramite.iloc[0]["id_tramite"]}.")
    if tramite.iloc[0]["estado"] == 2:
        print(f"Su solicitud de Vacaciones, para las fechas {tramite.iloc[0]["fecha_inicio"]}-{tramite.iloc[0]["fecha_fin"]} se encuentra en evaluación por parte de RRHH.")
    if tramite.iloc[0]["estado"] == 66:
        print("Su solicitud de Vacaciones fue denegada por falta de días disponibles.")

def pedir_tramite() -> str:
    """
    Solicita al usuario su código de trámite.

    Returns:
        codigo como string
    """
    while True:
        try:
            codigo = input("Ingrese su código de trámite: ").strip().upper()
            if codigo.isalnum():
                return codigo
            else:
                raise ValueError("Sólo puede ingresar letras y números (sin guiones, etc.)")
        except ValueError as e:
            print(f"Error en el ingreso de DNI: {e}")

def main():
    """
    Función principal que simula el bot.
    """
    
    opcion_menu = 0
    while opcion_menu != 3:
        print("
" + "="*40)
        print("="*2 + " SISTEMA DE SOLICITUD DE VACACIONES " + "="*2)
        print("="*40)
        print("1. Inicio de Trámite")
        print("2. Seguimiento de Trámite")
        print("3. Salir")
        print("="*40)
        try:
            opcion_menu = int(input("Seleccione una opción: "))
            if opcion_menu == 1:
                empleados = cargar_empleados()
                while True:
                    DNI = pedir_DNI()
                    if validar_empleado_existe(DNI, empleados.DNI.tolist()):
                        break
                    else:
                        print(f"Empleado "{DNI}" no encontrado.")
                codigo_tramite = iniciar_tramite(DNI)
                print(f"Solicitud de Vacaciones iniciada, con N° de Trámite: {codigo_tramite}.")
                seguir_tramite(codigo_tramite)
            elif opcion_menu == 2:
                codigo_tramite = pedir_tramite()
                seguir_tramite(codigo_tramite)
            elif opcion_menu == 3: print("Finalizando la ejecución del sistema.")
            else: raise ValueError
        except ValueError as e:
            print("Error: Entrada no válida. Debe ingresar un número entero entre 1 y 3.")

if __name__ == "__main__":
    main()
