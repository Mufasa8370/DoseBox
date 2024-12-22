from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import time
# Adresse I2C, ici on utilise 0x3C
I2C_ADDRESS = 0x3C  # Adresse trouvée avec i2cdetect

# Créer l'interface I2C
serial = i2c(port=1, address=I2C_ADDRESS)

# Initialiser l'écran OLED
try:
    device = ssd1306(serial)
    print("Écran OLED initialisé avec succès.")
except Exception as e:
    print(f"Erreur d'initialisation de l'écran : {e}")

# Utiliser canvas pour dessiner
try:
    with canvas(device) as draw:
        draw.text((0, 0), "Hello Raspberry Pi!", fill="white")
        print("Texte affiché sur l'écran.")
    device.show()
except Exception as e:
    print(f"Erreur lors de l'affichage du texte : {e}")

# Attendez un peu pour voir l'affichage
time.sleep(5)
