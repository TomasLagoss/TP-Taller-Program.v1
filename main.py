from carga import cargar_telemetria
from procesamiento import calcular_estadisticas_globales
from procesamiento import analizar_por_servidor
from procesamiento import clasificar_incidentes

def exportar_reporte(sesiones, ruta_salida="reporte_gamesec.txt"):
    estadisticas = calcular_estadisticas_globales(sesiones)
    servidores = analizar_por_servidor(sesiones)
    resumen, eventos_criticos = clasificar_incidentes(sesiones)
    fecha = input("Ingrese la fecha del reporte (DD/MM/AAAA): ")
    conclusion_1 = input("Primera conclusion del grupo: ")
    conclusion_2 = input("Segunda conclusion del grupo: ")
    conclusion_3 = input("Tercera conclusion del grupo: ")


    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE DE AUDITORIA Y TELEMETRIA\n")
        archivo.write("=====================\n")
        archivo.write("\n[1] RESUMEN GLOBAL\n")
        archivo.write(f"Total de sesiones: {estadisticas['total_sesiones']}\n")
        archivo.write(f"Ping promedio global: {estadisticas['ping_promedio']:.2f} ms\n")
        archivo.write(f"Duracion media de partida: {estadisticas['duracion_promedio']:.2f} min\n")
        archivo.write(f"Partidas Competitiva o Torneo: {estadisticas['porcentaje_competitivas']:.2f} %\n")
        archivo.write("\n[2] RENDIMIENTO REGIONAL POR SERVIDOR\n")
        archivo.write("Servidor | Sesiones | Ping promedio | FPS promedio\n")

        for nombre_servidor in servidores:
            datos_servidor = servidores[nombre_servidor]

            archivo.write(f"{nombre_servidor} | {datos_servidor['cantidad']} | {datos_servidor['ping_promedio']:.2f} ms | {datos_servidor['fps_promedio']:.2f} fps\n")
        archivo.write("\n[3] AUDITORIA DE SEGURIDAD E INCIDENTES\n")

        for estado in resumen:
            cantidad = resumen[estado]
            porcentaje = cantidad / len(sesiones) * 100

            archivo.write(f"{estado}: {cantidad} sesiones ({porcentaje:.2f} %)\n")
        archivo.write("\nDetalle de sesiones criticas detectadas:\n")

        for evento in eventos_criticos:
            archivo.write(f"Sesion #{evento['id_sesion']} | Jugador: {evento['jugador_id']} | Servidor: {evento['servidor']}\n")
            archivo.write(f"Motivo: {evento['motivo']}\n\n")
        archivo.write(f"Fecha de generacion: {fecha}\n")
        archivo.write("\n[4] CONCLUSIONES TECNICAS DEL EQUIPO\n")
        archivo.write(f"1. {conclusion_1}\n")
        archivo.write(f"2. {conclusion_2}\n")
        archivo.write(f"3. {conclusion_3}\n")
        archivo.write("\n========================================\n")
        archivo.write("FIN DEL REPORTE\n")









def main():
    sesiones = []
    opcion = ""
    while opcion != "6":
        print("\n GAMESEC MONITOR")
        print("1. Cargar y validar dataset")
        print("2. Ver estadisticas globales")
        print("3. Ver rendimiento por servidor")
        print("4. Ver incidentes de seguridad")
        print("5. Exportar reporte consolidado")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            try:
                sesiones = cargar_telemetria("gamesec_logs.csv")
                print("Sesiones cargadas:", len(sesiones))
            except FileNotFoundError as error:
                print(error)
            except ValueError as error:
                print(error)
        elif opcion == "2":
            if len(sesiones) ==  0:
                print("Primero debe cargar los datos con la opcion 1.")
            else:
                estadisticas = calcular_estadisticas_globales(sesiones)
                print(estadisticas)
        elif opcion == "3":
            if len(sesiones) == "0":
                print("Primero debe cargar los datos con la opcion 1.")
            else:
                servidores = analizar_por_servidor(sesiones)
                for nombre_servidor in servidores:
                    print(nombre_servidor, servidores[nombre_servidor])
        elif opcion =="4":
            if len(sesiones) =="0":
                print("Primero debe cargar los datos con la opcion 1.")
            else:
                resumen, eventos_criticos = clasificar_incidentes(sesiones)
                print("Resumen de seguridad", resumen)
                print("Detalle de sesiones criticas:")

                for evento in eventos_criticos:
                    print(evento)
        elif opcion == "5":
            if len(sesiones) == 0:
                print("Primero debe cargar el dataset con la opción 1.")
            else:
                exportar_reporte(sesiones)
                print("Reporte guardado en reporte_gamesec.txt")
        elif opcion == "6":
            print("Programa Finalizado.")
        else:
            print("¡Seleccione una opcion de la lista!.")

main()
