def calcular_estadisticas_globales(sesiones):
    total_sesiones = len(sesiones)
    suma_ping = 0
    suma_duracion = 0
    cantidad_competitivas = 0

    for sesion in sesiones:
        suma_ping = suma_ping + sesion["ping_promedio"]
        suma_duracion = suma_duracion + sesion["duracion_minutos"]

        if sesion["tipo_partida"] == "Competitiva" or sesion["tipo_partida"] == "Torneo":
            cantidad_competitivas = cantidad_competitivas + 1

    ping_promedio = round(suma_ping / total_sesiones, 2)
    duracion_promedio = round(suma_duracion / total_sesiones, 2)
    porcentaje_competitivas = cantidad_competitivas / total_sesiones * 100

    resultados = {
        "total_sesiones": total_sesiones,
        "ping_promedio": ping_promedio,
        "duracion_promedio": duracion_promedio,
        "porcentaje_competitivas": porcentaje_competitivas
    }
    return resultados

def analizar_por_servidor(sesiones):
    servidores = {}

    for sesion in sesiones:
        nombre_servidor = sesion["servidor"]

        if nombre_servidor not in servidores:
            servidores[nombre_servidor] = {
                "cantidad": 0,
                "suma_ping": 0,
                "suma_fps": 0
            }

        servidores[nombre_servidor]["cantidad"] = servidores[nombre_servidor]["cantidad"] + 1
        servidores[nombre_servidor]["suma_ping"] = servidores[nombre_servidor]["suma_ping"] + sesion["ping_promedio"]
        servidores[nombre_servidor]["suma_fps"] = servidores[nombre_servidor]["suma_fps"] + sesion["fps_promedio"]

    for nombre_servidor in servidores:
        datos_servidor = servidores[nombre_servidor]

        ping_promedio = round(datos_servidor["suma_ping"] / datos_servidor["cantidad"], 2)
        fps_promedio = round(datos_servidor["suma_fps"] / datos_servidor["cantidad"], 2)

        servidores[nombre_servidor] = {
            "cantidad": datos_servidor["cantidad"],
            "ping_promedio": ping_promedio,
            "fps_promedio": fps_promedio
        }

    return servidores

def clasificar_incidentes(sesiones):
    resumen = {
        "Normal": 0,
        "Sospechoso": 0,
        "Critico": 0
    }

    eventos_criticos = []

    for sesion in sesiones:
        if sesion["reportes_trampa"] >= 3 or sesion["intentos_fallidos"] >= 4:
            resumen["Critico"] = resumen["Critico"] + 1

            if sesion["reportes_trampa"] >= 3 and sesion["intentos_fallidos"] >= 4:
                motivo = "Exceso de reportes por trampa e intentos fallidos"
            elif sesion["reportes_trampa"] >= 3:
                motivo = "Exceso de reportes por trampa"
            else:
                motivo = "Exceso de intentos fallidos"

            evento = {
                "id_sesion": sesion["id_sesion"],
                "jugador_id": sesion["jugador_id"],
                "servidor": sesion["servidor"],
                "motivo": motivo
            }

            eventos_criticos.append(evento)

        elif (sesion["ping_promedio"] > 200 and sesion["intentos_fallidos"] >= 2) or sesion["reportes_trampa"] == 2:
            resumen["Sospechoso"] = resumen["Sospechoso"] + 1
        else:
            resumen["Normal"] = resumen["Normal"] + 1

    return resumen, eventos_criticos

        
