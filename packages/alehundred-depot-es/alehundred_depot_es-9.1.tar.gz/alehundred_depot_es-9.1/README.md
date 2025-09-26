# Alehundred-Depot (Versión en Español)

Una herramienta con interfaz de texto (TUI) para facilitar la instalación y gestión de un servidor Perforce Helix Core en hardware de bajo costo como una Raspberry Pi.

# 1. Instalación
Conéctate a tu Raspberry Pi vía SSH

- Reemplaza con tu usuario y hostname/IP real
ssh TuUsuario@NombreDeTuPi.local

# 2. Copia, pega y ejecuta este bloque completo

- Esto actualizará el sistema, instalará las dependencias, instalará el toolkit y configurará el PATH, todo de una sola vez.

sudo apt update && sudo apt install python3-pip -y
pip install --break-system-packages alehundred-depot-es
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
echo "¡Instalación completa! Ejecuta 'alehundred-depot' para empezar."

# 3. Ejecuta el programa

alehundred-depot-es

## 4. Actualizar el Programa

Para asegurarte de tener las últimas características y correcciones, actualiza el toolkit regularmente con el siguiente comando:

pip install --upgrade --break-system-packages alehundred-depot-es

Si el comando anterior no instala la última versión (especialmente en una Raspberry Pi), puede deberse a un caché en el repositorio de `piwheels`. Para forzar la actualización directamente desde PyPI, usa este comando:

pip install --upgrade --index-url https://pypi.org/simple/ --break-system-packages alehundred-depot-es