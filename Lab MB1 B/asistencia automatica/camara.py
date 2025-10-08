import cv2

# Inicia la cámara (0 = cámara predeterminada)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ No se puede acceder a la cámara.")
else:
    print("✅ Cámara detectada. Presiona 'q' para cerrar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error al leer el video.")
        break

    # Muestra la imagen de la cámara
    cv2.imshow("Prueba de cámara - Ing. Josué Quijivix", frame)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
