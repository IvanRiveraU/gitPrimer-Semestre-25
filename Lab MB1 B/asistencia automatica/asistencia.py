import cv2
from pyzbar import pyzbar
import pandas as pd
from datetime import datetime
import os

# Ruta del archivo Excel
archivo_excel = r"D:\Ubicacion C a D\Documentos\gitPrimer-Semetre-25\Lab MB1 B\asistencia automatica\asistenciamacro.xlsm"

# Si no existe, crear el archivo base
if not os.path.exists(archivo_excel):
    df = pd.DataFrame(columns=["Código", "Nombre", "Carnet", "Asistencia", "Fecha", "Hora"])
    df.to_excel(archivo_excel, index=False)

# Función para leer el Excel existente
def leer_datos():
    return pd.read_excel(archivo_excel)

# Función para guardar asistencia
def registrar_asistencia(codigo):
    df = leer_datos()

    # Evitar duplicados (si ya marcó asistencia)
    if codigo in df["Código"].values:
        print(f"{codigo} ya registrado.")
        return

    try:
        nombre, carnet = codigo.split("_")
    except:
        nombre, carnet = codigo, ""

    nueva_fila = {
        "Código": codigo,
        "Nombre": nombre,
        "Carnet": carnet,
        "Asistencia": "Presente",
        "Fecha": datetime.now().strftime("%Y-%m-%d"),
        "Hora": datetime.now().strftime("%H:%M:%S")
    }

    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_excel(archivo_excel, index=False)
    print(f"Asistencia registrada: {nombre} ({carnet})")

# Iniciar cámara
print("📸 Iniciando cámara... (presiona 'q' para salir)")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar códigos QR en el cuadro
    qrcodes = pyzbar.decode(frame)
    for qr in qrcodes:
        data = qr.data.decode("utf-8")
        (x, y, w, h) = qr.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        registrar_asistencia(data)

    cv2.imshow("Asistencia QR - Ing. Josué Quijivix", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
