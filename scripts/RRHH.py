'''TPI · Organización Empresarial
Simulación de Solicitud de Vacaciones'''
### Módulo para RRHH

import pandas as pd
from datetime import datetime

def cargar_tramites() -> pd.DataFrame:
    """
    Lee todos los trámites, y
    devuelve sólo los que se encuentran pendientes de evaluación.

    Returns:
        pd.DataFrame: Dataframe con datos del trámite solicitado.
    """
    ruta = "estados/tramites.csv"

    try:
        tramites = pd.read_csv(ruta)
        tramites = tramites.loc[tramites['estado'] == 2].copy()
        return tramites
    except Exception as e:
        raise Exception(f"Error al leer la base de trámites: {e}")

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
            tramites['fecha_inicio'] = tramites['fecha_inicio'].astype(str).str.replace('nan', '')
            tramites.loc[tramites['id_tramite'] == codigo_tramite, 'fecha_inicio'] = fecha_inicio.strftime('%d/%m/%Y')
        if fecha_fin:
            tramites['fecha_fin'] = tramites['fecha_fin'].astype(str).str.replace('nan', '')
            tramites.loc[tramites['id_tramite'] == codigo_tramite, 'fecha_fin'] = fecha_fin.strftime('%d/%m/%Y')
        if nuevo_estado:
            tramites.loc[tramites['id_tramite'] == codigo_tramite, 'estado'] = nuevo_estado
        with open(ruta, 'w', encoding = 'utf-8', newline = '') as archivo:
            archivo.write(tramites.to_csv(index = False, header = True))
    except Exception as e:
        raise Exception(f"Error al actualizar el trámite: {e}")

def main():
    """
    Función principal que simula el bot para RRHH.
    """
    user = "admin"
    password = "admin"

    print("\n" + "="*40)
    print("= SISTEMA DE EVALUACIÓN DE SOLICITUDES =")
    print("="*40 + "\n")
    while True:
        usuario = input("Ingrese su usuario: ").strip()
        contraseña = input("Ingrese su contraseña: ").strip()
        if usuario == user and contraseña == password:
            break
        else:
            print("¡Acceso denegado! Credenciales inválidas.")
    pendientes = cargar_tramites()
    if pendientes.empty:
        print("No hay trámites pendientes de evaluación.")
    else:
        print(f"\nHay {len(pendientes)} trámite/s pendiente/s de evaluación:")
        for tramite in pendientes.itertuples(index = False):
            print("\n")
            print(f"Código de Trámite: {tramite.id_tramite} | Empleado Solicitante: {tramite.id_empleado}")
            print(f"Fecha de Inicio: {tramite.fecha_inicio} | Fecha de Finalización: {tramite.fecha_fin}")
            decision = input("¿Aprobar solicitud? (s/n): ").strip().lower()
            while decision not in ['s', 'n']:
                decision = input("Entrada inválida. Ingrese 's' para aprobarla o 'n' para denegarla: ").strip().lower()
            actualizar_tramite(codigo_tramite = tramite.id_tramite, nuevo_estado = 3 + bool(decision == 'n'))
        print("\nYa no quedan solicitudes pendientes de evaluación.")

if __name__ == "__main__":
    main()