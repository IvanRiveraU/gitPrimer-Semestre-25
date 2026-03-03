#!/bin/bash

# Instala Zenity si no está instalado y paquetes básicos
if ! command -v zenity >/dev/null 2>&1; then
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y zenity gdebi synaptic make automake cmake autoconf git aptitude curl
fi

# =============================================
# FUNCIONES UTILITARIAS
# =============================================

# Función para instalar .deb desde GitHub (última versión)
install_github_deb() {
  local repo_url="$1"
  local version_filter="$2"
  local file_pattern="$3"
  local program_name="$4"

  echo -e "\n\033[1;34mBuscando la última versión de $program_name...\033[0m"

  # Obtener versión más reciente
  LATEST_VERSION=$(curl -sL "$repo_url" | grep -oP "$version_filter" | head -1)

  if [ -z "$LATEST_VERSION" ]; then
    echo -e "\n\033[1;34mNo se pudo obtener la versión de $program_name.\n\nURL usada: $repo_url \033[0m"
    return 1
  fi

  # Construir URL de descarga
  DEB_FILE=$(eval echo "$file_pattern")
  DOWNLOAD_URL="$repo_url/download/$LATEST_VERSION/$DEB_FILE"

  # Descargar e instalar
  echo -e "\n\033[1;34mDescargando $program_name v$LATEST_VERSION...\033[0m"
  if ! wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
    echo -e "\n\033[1;34mError al descargar $program_name.\n\nURL intentada: $DOWNLOAD_URL\033[0m"
    return 1
  fi

  sudo dpkg -i "/tmp/$DEB_FILE"
  sudo apt install -f -y
  rm "/tmp/$DEB_FILE"
  echo -e "\n\033[1;34m✅ ¡$program_name v$LATEST_VERSION instalado correctamente!\033[0m"
}

# Función para instalar desde Flatpak
install_flatpak() {
  local app_id="$1"
  local program_name="$2"

  if ! flatpak list | grep -q "$app_id"; then
    echo -e "\n\033[1;34mInstalando $program_name...\033[0m"
    flatpak install -y flathub "$app_id"
    echo -e "\n\033[1;34m✅ ¡$program_name instalado correctamente!\033[0m"
  else
    echo -e "\n\033[1;34m$program_name ya está instalado.\033[0m"
  fi
}

# Función para seleccionar la versión de Ubuntu
select_debian_version() {
  zenity --list --radiolist --title="Selecciona la versión de Debian" \
    --text="Selecciona la versión de Debian que deseas configurar:" \
    --column="Seleccionar" --column="Versión" --column="Descripción" \
    TRUE "bullseye" "Debian 11 (Bullseye)" \
    FALSE "bookworm" "Debian 12 (Bookworm)" \
    FALSE "trixie" "Debian 13 (Trixie)" \
    --width=500 --height=300
}

# Función para mostrar el menú de selección de secciones
show_section_menu() {
  zenity --list --checklist --title="Selecciona las secciones" \
    --text="Selecciona las secciones que deseas instalar:" \
    --column="Seleccionar" --column="Sección" \
    FALSE "🛠️ Accesorios" \
    FALSE "🎨 Gráficos" \
    FALSE "🌐 Internet" \
    FALSE "🎬 Multimedia" \
    FALSE "🎮 Juegos" \
    FALSE "📄 Oficina" \
    FALSE "🖥️ Escritorios" \
    --separator="|" --width=400 --height=300
}

# Función para mostrar el menú de selección de programas en una sección específica
show_program_menu() {
  local section=$1
  case $section in
    "🛠️ Accesorios")
      zenity --list --checklist --title="🛠️ Accesorios" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        TRUE "Fuentes y codecs" "Instalará algunos codecs y fuentes"\
        FALSE "Impresoras" "Instalar driver de multiples impresoras"\
        FALSE "instalador-flatpak" "Instalador para paquetes Flatpak"\
        TRUE "Compilación de software" "Herramientas de compilación y gestión."\
        TRUE "Compresores" "Basico para comprimir o Descomprimir paquetes"\
        FALSE "PeaZip" "Herramienta de compresión de archivos"\
        FALSE "Wine" "permite ejecutar aplicaciones de Windows"\
        TRUE "GParted y más" "Múltiples herramientas para el disco duro"\
        FALSE "BalenaEtcher" "Crea una USB o SD booteable"\
        FALSE "htop" "Monitor de sistema interactivo"\
        FALSE "Mission Center - flatpak" "Supervise el uso de CPU, memoria y GPU"\
        FALSE "CPU-X" "Visualiza la información sobre CPU y más"\
        FALSE "Warehouse - flatpak" "Administra los Flatpaks instalados"\
        FALSE "BleachBit" "Libera rápidamente espacio en disco"\
        FALSE "Fondo - flatpak" "Cambia los fondos de pantalla"\
        FALSE "Geany" "Editor de texto ligero"\
        FALSE "Atom" "Editor de texto moderno, accesible"\
        FALSE "Sublime Text" "Editor de texto y editor de código fuente"\
        --separator="|" --width=600 --height=520
      ;;
    "🎨 Gráficos")
      zenity --list --checklist --title="🎨 Graficos" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        TRUE "Gimp" "Editor de imágenes"\
        FALSE "inkscape" "Editor de gráficos vectoriales"\
        FALSE "Synfig" "Editor de gráficos vectoriales de animación"\
        FALSE "Blender" "programa de modelado, renderizado, la animación en 3D"\
        FALSE "Photoshop" "Editor de imágenes"\
        FALSE "Illustrator" "Editor de gráficos vectoriales"\
        FALSE "LibreSprite - flatpak" "Crea animaciones 2D para videojuegos"\
        FALSE "Pixelorama - flatpak" "Editor de sprites 2D gratuito y de código abierto"\
        FALSE "Krita" "Estudio de arte digital completo para diseñar y pintar"\
        FALSE "Darktable" "Programa de procesamiento fotográfico en formato raw"\
        --separator="|" --width=600 --height=350
      ;;
    "🌐 Internet")
      zenity --list --checklist --title="🌐 Internet" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        TRUE "Google Chrome" "Navegador web Chrome de Google"\
        FALSE "Brave-browser" "Navegador web Brave"\
        FALSE "Vivaldi" "Navegador web potente, personal y privado"\
        FALSE "Microsoft Edge - flatpak" "Navegador web desarrollado por Microsoft"\
        FALSE "Opera - flatpak" "Navegador web rápido, seguro y fácil de usar"\
        FALSE "Firefox - flatpak" "Navegador web gratuito respaldado por Mozilla"\
        FALSE "LibreWolf" "Navegador web y un fork de Firefox"\
        FALSE "Tor Browser Launcher - flatpak" "Navegador web Tor"\
        FALSE "Midori" "Navegador web ligero"\
        FALSE "WhatsApp Desktop - flatpak" "Cliente no oficial de WhatsApp Web Desktop"\
        FALSE "Telegram Desktop - flatpak" "Plataforma de mensajería y VOIP"\
        FALSE "Signal Desktop" "Aplicación gratuita de mensajería y llamadas"\
        FALSE "teams-for-linux - flatpak" "Cliente no oficial de Microsoft Teams"\
        FALSE "Discord - flatpak" "Servicio de mensajería y chat de voz VolP"\
        FALSE "JDownloader - flatpak" "Gestor de descargas"\
        --separator="|" --width=600 --height=460
      ;;
    "🎬 Multimedia")
      zenity --list --checklist --title="🎬 Multimedia" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        TRUE "vlc" "Reproductor multimedia"\
        FALSE "Spotify" "Servicio de música digital"\
        FALSE "Audacity" "Editor de audio"\
        TRUE "Codecs multimedia" "Codecs multimedia y librerías"\
        FALSE "Obs Studio" "Software de grabación y transmisión en vivo"\
        FALSE "Soundconverter" "Conversor de audio"\
        FALSE "Kdenlive" "Editor de video"\
        FALSE "Kodi" "Reproduce vídeos, música, podcasts y otros archivos"\
        FALSE "Video Downloader - flatpak" "Descargue videos de sitios web"\
        FALSE "FreeTube" "Reproductor de YouTube de escritorio"\
        FALSE "HandBrake - flatpak" "Herramienta para convertir vídeos"\
        FALSE "Stremio" "Servicio de streaming para ver películas, series y tv"\
        FALSE "Plex - flatpak" "Convertir tu ordenador en un centro multimedia"\
        FALSE "Shortwave - flatpak" "Reproductor de radio por Internet"\
        FALSE "Bitwig Studio - flatpak" "Estudio de audio digital (DAW)"\
        FALSE "Mixxx DJ" "Software de DJ gratuito"\
        FALSE "Flameshot" "Captura de pantalla potente y fácil"\
        --separator="|" --width=600 --height=500
      ;;
    "🎮 Juegos")
      zenity --list --checklist --title="🎮 Juegos" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        FALSE "steam" "Plataforma de juegos"\
        FALSE "Lutris" "Acceder a tu biblioteca de Steam, Epic Games Store y GOG"\
        FALSE "Heroic Games Launcher" "Acceder a tu biblioteca de Steam, Epic Games Store y GOG"\
        FALSE "Minecraft - flatpak"  "videojuego de construcción de tipo mundo abierto"\
        FALSE "Dolphin" "Emulador para GameCube y Wii"\
        FALSE "Lime3DS - flatpak" "Emulador de 3DS"\
        FALSE "Cemu" "Emulador para WiiU"\
        FALSE "yuzu - flatpak" "Emulador de nintendo switch"\
        FALSE "Ryujinx - flatpak" "Emulador de nintendo switch"\
        FALSE "DuckStation - flatpak" "Emulador de Playstation"\
        FALSE "PPSSPP - flatpak" "Emulador de PSP"\
        FALSE "PCSX2 - flatpak" "Emulador de PS2"\
        FALSE "RPCS3 - flatpak" "Emulador de PS3"\
        FALSE "Flycast - flatpak" "Emulador de Sega Dreamcast, Naomi y Atomiswave"\
        FALSE "RetroArch - flatpak" "Plataforma multiplataforma para emuladores"\
        FALSE "VICE - flatpak" "Emulador de computadoras Commodore's 8-bit"\
        FALSE "Amiberry - flatpak" "Emulador de computadoras Amiga"\
        FALSE "DOSBox-X - flatpak" "Emulador de computadoras IBM PC y DOS"\
        FALSE "Pack Juegos Retro" "Plataforma de juegos"\
        --separator="|" --width=600 --height=500
      ;;
    "📄 Oficina")
      zenity --list --checklist --title="📄 Oficina" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        FALSE "LibreOffice" "Alternativa de Microsoft Office"\
        FALSE "ONLYOFFICE Desktop - flatpak" "Edite documentos, hojas de cálculo y más"\
        FALSE "Calligra" "Otra suite de ofimática"\
        FALSE "Dropbox" "Servicio de alojamiento de archivo en la nube"\
        FALSE "MEGASync" "Servicio de alojamiento de archivo en la nube"\
        FALSE "Insync" "Gestiona servicios en OneDrive, Google Drive y Dropbox"\
        FALSE "calibre - flatpak" "Herramienta de gestión de libros electrónicos"\
        FALSE "Foliate - flatpak" "Aplicación de lectura de libros electrónicos"\
        FALSE "Adobe Reader - flatpak" "Lector de PDF gratuito con Adobe"\
        FALSE "Master PDF Editor - flatpak" "Ver, crear, modificar, firmar, escanear PDF"\
        FALSE "FreeCAD - flatpak" "Modelador 3D paramétrico de código abierto"\
        FALSE "UltiMaker Cura - flatpak" "Aplicación diseñada para impresoras 3D"\
        FALSE "KiCad - flatpak" "Software para diseño electrónico"\
        FALSE "Fritzing - flatpak" "Aplicación de automatización de diseño electrónico"\
        FALSE "Arduino IDE - flatpak" "Programa para escribir y cargar programas en placas"\
        FALSE "DL: language lessons - flatpak" "Cliente para escritorio de Duolingo"\
        FALSE "GnuCash" "Administre sus finanzas, cuentas e inversiones"\
        FALSE "AnyDesk" "Conéctese a un ordenador de forma remota"\
        FALSE "VNC Viewer" "Conéctese a un ordenador de forma remota"\
        --separator="|" --width=600 --height=550
      ;;
    "🖥️ Escritorios")
      zenity --list --checklist --title="🖥️ Escritorios" --text="Selecciona los programas que deseas instalar:"\
        --column="Marcar" --column="Programa" --column="Descripción"\
        FALSE "Gnome" "Escritorio Gnome"\
        FALSE "Cinnamon" "Escritorio Cinnamon"\
        FALSE "Budgie" "Escritorio Budgie"\
        FALSE "KDE Plasma" "Escritorio Kubuntu"\
        FALSE "Mate" "Escritorio mate"\
        FALSE "XFCE 4" "Escritorio XFCE4"\
        FALSE "LXQt" "Escritorio LXQt"\
        FALSE "LXDE" "Escritorio LXDE"\
        --separator="|" --width=600 --height=440
      ;;
  esac
}

# Función para instalar los programas seleccionados
install_selected_programs() {
  local programs_to_install=("$@")

  # Confirmación antes de instalar
  ##zenity --question --title="Confirmación" --text="¿Deseas instalar los programas seleccionados?" --width=350
  #if [[ $? -ne 0 ]]; then
  #  exit 1
  #fi

  sudo apt update
  for program in "${programs_to_install[@]}"; do
    case $program in
      "Fuentes y codecs")
        echo -e "\033[1;33mInstalando Fuentes y codecs\033[0m"
        sleep 2
        sudo apt install -y ubuntu-restricted-extras libavcodec-extra curl ttf-mscorefonts-installer mtp-tools ipheth-utils ideviceinstaller ifuse
        echo -e "\033[1;32mFuentes y codecs instalado correctamente\033[0m"
        sleep 2
        ;;
      "Impresoras")
        echo -e "\033[1;33mInstalando Impresoras\033[0m"
        sleep 2
        sudo apt -y install printer-driver-all
        echo -e "\033[1;32mImpresoras instalado correctamente\033[0m"
        sleep 2
        ;;
      "instalador-flatpak")
        echo -e "\033[1;33mInstalando flatpak\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        echo -e "\033[1;32mflatpak instalado correctamente\033[0m"
        sleep 2
        ;;
      "Compilación de software")
        echo -e "\033[1;33mInstalando Compilación de software\033[0m"
        sleep 2
        sudo apt install -y build-essential make automake cmake autoconf git wget
        echo -e "\033[1;33mInstalando build-essential make automake cmake autoconf git wget\033[0m"
        sleep 2
        ;;
      "Compresores")
        echo -e "\033[1;33mInstalando Compresores\033[0m"
        sleep 2
        sudo apt install -y p7zip-full p7zip-rar rar unrar zip unzip unace bzip2 arj lzip lzma gzip unar
        echo -e "\033[1;33mInstalando p7zip-full p7zip-rar rar unrar zip unzip unace bzip2 arj lzip lzma gzip unar\033[0m"
        sleep 2
        ;;
      "PeaZip")
        REPO_URL="https://github.com/peazip/PeaZip/releases"
        echo -e "\n\033[1;33mInstalando PeaZip...\033[0m"
        sleep 2
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'PeaZip \K[0-9]+\.[0-9]+\.[0-9]+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          echo -e "\033[1;31mError: No se pudo detectar la última versión\033[0m"
          return 1
        fi
        DEB_FILE="peazip_${LATEST_VERSION}.LINUX.GTK2-1_amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/$LATEST_VERSION/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mPeaZip $LATEST_VERSION instalado correctamente\033[0m"
          sleep 2
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "Wine")
        echo -e "\033[1;33mInstalando Wine\033[0m"
        sleep 2
        sudo dpkg --add-architecture i386
        sudo mkdir -pm755 /etc/apt/keyrings
        sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
        sudo wget -NP /etc/apt/sources.list.d/ "https://dl.winehq.org/wine-builds/ubuntu/dists/$ubuntu_version/winehq-$ubuntu_version.sources"
        sudo apt update
        sudo apt install --install-recommends winehq-stable -y
        echo -e "\033[1;33mInstalando Wine\033[0m"
        sleep 2
        ;;
      "GParted y más")
        echo -e "\033[1;33mInstalando GParted y más\033[0m"
        sleep 2
        sudo apt install -y gparted exfat-fuse hfsplus hfsutils ntfs-3g
        echo -e "\033[1;33mInstalando gparted exfat-fuse hfsplus hfsutils ntfs-3g\033[0m"
        sleep 2
        ;;
      "BalenaEtcher")
        echo -e "\033[1;33mInstalando BalenaEtcher\033[0m"
        sleep 2
        REPO_URL="https://github.com/balena-io/etcher/releases"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'Etcher \Kv[0-9]+\.[0-9]+\.[0-9]+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v2.1.0"
        fi
        VERSION_NUMBER=${LATEST_VERSION#v}
        DEB_FILE="balena-etcher_${VERSION_NUMBER}_amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mBalena Etcher $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "htop")
        echo -e "\033[1;33mInstalando Htop\033[0m"
        sleep 2
        sudo apt install -y htop btop
        echo -e "\033[1;33mInstalando Htop Btop\033[0m"
        sleep 2
        ;;
      "Geany")
        echo -e "\033[1;33mInstalando Geany\033[0m"
        sleep 2
        sudo apt install -y geany
        echo -e "\033[1;33mInstalando Geany\033[0m"
        sleep 2
        ;;
      "Mission Center - flatpak")
        echo -e "\033[1;33mInstalando Mission Center\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub io.missioncenter.MissionCenter
        echo -e "\033[1;33mInstalando Mission Center\033[0m"
        sleep 2
        ;;
      "CPU-X")
        echo -e "\033[1;33mInstalando CPU-X\033[0m"
        sleep 2
        sudo apt install -y cpu-x
        echo -e "\033[1;33mInstalando CPU-X\033[0m"
        sleep 2
        ;;
      "Warehouse - flatpak")
        echo -e "\033[1;33mInstalando Warehouse\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub io.github.flattool.Warehouse
        echo -e "\033[1;33mInstalando Warehouse\033[0m"
        sleep 2
        ;;
      "BleachBit")
        echo -e "\033[1;33mInstalando BleachBit\033[0m"
        sleep 2
        cd /tmp/
        wget https://download.bleachbit.org/bleachbit_4.6.0-0_all_ubuntu2310.deb
        sudo dpkg -i bleachbit_4.6.0-0_all_ubuntu2310.deb
        sudo apt install -y -f
        rm bleachbit_4.6.0-0_all_ubuntu2310.deb
        echo -e "\033[1;33mInstalando BleachBit\033[0m"
        sleep 2
        ;;
      "Fondo - flatpak")
        echo -e "\033[1;33mInstalando Fondo\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.github.calo001.fondo
        echo -e "\033[1;33mInstalando Fondo\033[0m"
        sleep 2
        ;;
      "Atom")
        REPO_URL="https://github.com/atom/atom/releases"
        echo -e "\n\033[1;33mInstalando Atom Editor...\033[0m"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'Atom \Kv[0-9]+\.[0-9]+\.[0-9]+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v1.60.0"
        fi
        DEB_FILE="atom-amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mAtom Editor $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "Sublime Text")
        echo -e "\033[1;33mInstalando Sublime Text\033[0m"
        sleep 2
        wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
        echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
        sudo apt-get update
        sudo apt-get install sublime-text
        echo -e "\033[1;33mInstalando Sublime Text\033[0m"
        sleep 2
        ;;
      "Gimp")
        echo -e "\033[1;35mInstalando Gimp\033[0m"
        sleep 2
        sudo apt install -y gimp
        echo -e "\033[1;33mInstalando Gimp\033[0m"
        sleep 2
        ;;
      "Inkscape")
        echo -e "\033[1;35mInstalando Inkscape\033[0m"
        sleep 2
        sudo apt install -y inkscape
        echo -e "\033[1;33mInstalando Inkscape\033[0m"
        sleep 2
        ;;
      "Synfig")
       echo -e "\033[1;35mInstalando Synfig\033[0m"
       sleep 2
        sudo apt install -y synfig
        echo -e "\033[1;33mInstalando Synfig\033[0m"
        sleep 2
        ;;
      "Blender")
        echo -e "\033[1;35mInstalando Blender\033[0m"
        sleep 2
        sudo apt install -y blender
        echo -e "\033[1;33mInstalando Blender\033[0m"
        sleep 2
        ;;
      "Photoshop")
        echo -e "\033[1;35mInstalando Photoshop\033[0m"
        sleep 2
        sudo apt update && sudo apt upgrade -y
        sudo apt install -y zenity gdebi synaptic make automake cmake autoconf git aptitude synaptic curl
        cd /tmp/
        git clone https://gitlab.com/csmarckitus1/photoshop.git
        cd photoshop
        make
        ./Photoshop2020
        echo -e "\033[1;33mInstalando Photoshop\033[0m"
        sleep 2
        ;;
      "Illustrator")
        echo -e "\033[1;35mInstalando Illustrator\033[0m"
        sleep 2
        sudo apt update && sudo apt upgrade -y
        sudo apt install -y zenity gdebi synaptic make automake cmake autoconf git aptitude synaptic curl
        cd /tmp/
        wget https://github.com/LinSoftWin/Illustrator-CC-2021-Linux/releases/download/1.0.0/install-illustrator-2021.sh
        chmod +x install-illustrator-2021.sh
        sh install-illustrator-2021.sh
        echo -e "\033[1;33mInstalando Illustrator\033[0m"
        sleep 2
        ;;
      "LibreSprite - flatpak")
        echo -e "\033[1;35mInstalando LibreSprite\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.github.libresprite.LibreSprite
        echo -e "\033[1;33mInstalando LibreSprite\033[0m"
        sleep 2
        ;;
      "Pixelorama - flatpak")
        echo -e "\033[1;35mInstalando Pixelorama\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.orama_interactive.Pixelorama
        echo -e "\033[1;33mInstalando Pixelorama\033[0m"
        sleep 2
        ;;
      "Krita")
        echo -e "\033[1;35mInstalando Krita\033[0m"
        sleep 2
        sudo apt install -y krita
        echo -e "\033[1;33mInstalando Krita\033[0m"
        sleep 2
        ;;
      "Darktable")
        echo -e "\033[1;35mInstalando Darktable\033[0m"
        sleep 2
        sudo apt install -y darktable
        echo -e "\033[1;33mInstalando Darktable\033[0m"
        sleep 2
        ;;
      "vlc")
        echo -e "\033[1;36mInstalando Darktable\033[0m"
        sleep 2
        sudo apt install -y vlc
        echo -e "\033[1;33mInstalando Darktable\033[0m"
        sleep 2
        ;;
      "Spotify")
        echo -e "\033[1;36mInstalando Spotify\033[0m"
        sleep 2
        curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
        echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
        sudo apt-get update && sudo apt-get install spotify-client
        echo -e "\033[1;33mInstalando Spotify\033[0m"
        sleep 2
        ;;
      "Audacity")
        echo -e "\033[1;36mInstalando Audacity\033[0m"
        sleep 2
        sudo apt install -y audacity
        echo -e "\033[1;33mInstalando Audacity\033[0m"
        sleep 2
        ;;
      "Codecs multimedia")
        echo -e "\033[1;36mInstalando Codecs multimedia\033[0m"
        sleep 2
        sudo apt install -y w64codecs libdvdcss2 gstreamer1.0-libav
        echo -e "\033[1;33mInstalando Codecs multimedia\033[0m"
        sleep 2
        ;;
      "kdenlive")
        echo -e "\033[1;36mInstalando kdenlive\033[0m"
        sleep 2
        sudo apt install -y kdenlive mediainfo
        echo -e "\033[1;33mInstalando kdenlive\033[0m"
        sleep 2
        ;;
      "Obs Studio")
        echo -e "\033[1;36mInstalando Obs Studio\033[0m"
        sleep 2
        sudo add-apt-repository -y ppa:obsproject/obs-studio
        sudo apt update
        sudo apt install -y obs-studio
        echo -e "\033[1;33mInstalando Obs Studio\033[0m"
        sleep 2
        ;;
      "Soundconverter")
        echo -e "\033[1;36mInstalando Soundconverter\033[0m"
        sleep 2
        sudo apt install -y soundconverter
        echo -e "\033[1;33mInstalando Soundconverter\033[0m"
        sleep 2
        ;;
      "Kdenlive")
        echo -e "\033[1;36mInstalando Kdenlive\033[0m"
        sleep 2
        sudo apt install -y kdenlive
        echo -e "\033[1;33mInstalando Kdenlive\033[0m"
        sleep 2
        ;;
      "Kodi")
        echo -e "\033[1;36mInstalando Kodi\033[0m"
        sleep 2
        sudo apt install -y kodi
        echo -e "\033[1;33mInstalando Kodi\033[0m"
        sleep 2
        ;;
      "Video Downloader - flatpak")
        echo -e "\033[1;36mInstalando Video Downloader\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.github.unrud.VideoDownloader
        echo -e "\033[1;33mInstalando Video Downloader\033[0m"
        sleep 2
        ;;
      "FreeTube")
        echo -e "\033[1;36mInstalando FreeTube\033[0m"
        sleep 2
        REPO_URL="https://github.com/FreeTubeApp/FreeTube/releases"
        echo -e "\n\033[1;34mInstalando FreeTube...\033[0m"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'FreeTube \Kv[0-9]+\.[0-9]+\.[0-9]+(-beta)?' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v0.23.3-beta"
        fi
        VERSION_NUMBER=$(echo "$LATEST_VERSION" | sed 's/^v//;s/-beta//')
        DEB_FILE="freetube_${VERSION_NUMBER}_amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mFreeTube $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "HandBrake - flatpak")
        echo -e "\033[1;36mInstalando HandBrake\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub fr.handbrake.ghb
        echo -e "\033[1;33mInstalando HandBrake\033[0m"
        sleep 2
        ;;
      "Stremio")
        echo -e "\033[1;36mInstalando Stremio\033[0m"
        sleep 2
        BASE_URL="https://dl.strem.io/shell-linux"
        echo -e "\n\033[1;34mInstalando Stremio...\033[0m"
        LATEST_VERSION=$(curl -sL "$BASE_URL" | grep -oP 'v\d+\.\d+\.\d+' | sort -V | tail -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v4.4.168"
        fi
        VERSION_NUMBER=${LATEST_VERSION#v}
        DEB_FILE="stremio_${VERSION_NUMBER}-1_amd64.deb"
        DOWNLOAD_URL="$BASE_URL/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mStremio $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "Plex - flatpak")
        echo -e "\033[1;36mInstalando Plex\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub tv.plex.PlexDesktop
        echo -e "\033[1;33mInstalando Plex\033[0m"
        sleep 2
        ;;
      "Shortwave - flatpak")
        echo -e "\033[1;36mInstalando Shortwave\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub de.haeckerfelix.Shortwave
        echo -e "\033[1;33mInstalando Shortwave\033[0m"
        sleep 2
        ;;
      "Bitwig Studio - flatpak")
        echo -e "\033[1;36mInstalando Bitwig Studio\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.bitwig.BitwigStudio
        echo -e "\033[1;33mInstalando Bitwig Studio\033[0m"
        sleep 2
        ;;
      "Mixxx DJ")
        echo -e "\033[1;36mInstalando Mixxx DJ\033[0m"
        sleep 2
        sudo add-apt-repository -y ppa:mixxx/mixxx
        sudo apt update
        sudo apt install mixxx
        echo -e "\033[1;33mInstalando Mixxx DJ\033[0m"
        sleep 2
        ;;
      "Flameshot")
        echo -e "\033[1;36mInstalando Flameshot\033[0m"
        sleep 2
        REPO_URL="https://github.com/flameshot-org/flameshot/releases"
        UBUNTU_VERSION="22.04"
        echo -e "\n\033[1;34mInstalando Flameshot...\033[0m"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'Flameshot \Kv\d+\.\d+\.\d+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v12.1.0"
        fi
        VERSION_NUMBER=${LATEST_VERSION#v}
        DEB_FILE="flameshot-${VERSION_NUMBER}-1.ubuntu-${UBUNTU_VERSION}.amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mFlameshot $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        echo -e "\033[1;33mInstalando Flameshot\033[0m"
        sleep 2
        ;;
      "Google Chrome")
        echo -e "\033[1;43mInstalando Google Chrome\033[0m"
        sleep 2
        cd /tmp/
        wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo dpkg -i google-chrome-stable_current_amd64.deb
        sudo apt install -f -y
        rm google-chrome-stable_current_amd64.deb
        echo -e "\033[1;33mInstalando Google Chrome\033[0m"
        sleep 2
        ;;
      "Brave-browser")
        echo -e "\033[1;43mInstalando Brave-browser\033[0m"
        sleep 2
        sudo apt install -y curl
        sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
        echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg  arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
        sudo apt update
        sudo apt install -y brave-browser
        echo -e "\033[1;33mInstalando Brave-browser\033[0m"
        sleep 2
        ;;
      "Vivaldi")
        echo -e "\033[1;43mInstalando Vivaldi\033[0m"
        sleep 2
        BASE_URL="https://downloads.vivaldi.com/stable"
        echo -e "\n\033[1;34mInstalando Vivaldi Browser...\033[0m"
        VERSION_FILE=$(curl -sL "$BASE_URL/" | grep -oP 'vivaldi-stable_\K\d+\.\d+\.\d+\.\d+-\d+_amd64\.deb' | head -n 1)
        LATEST_VERSION=$(echo "$VERSION_FILE" | grep -oP '\d+\.\d+\.\d+\.\d+-\d+')
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="7.3.3635.9-1"
        fi
        DEB_FILE="vivaldi-stable_${LATEST_VERSION}_amd64.deb"
        DOWNLOAD_URL="$BASE_URL/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mVivaldi $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "Microsoft Edge - flatpak")
        echo -e "\033[1;43mInstalando Microsoft Edge\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.microsoft.Edge
        echo -e "\033[1;33mInstalando Microsoft Edge\033[0m"
        sleep 2
        ;;
      "Opera - flatpak")
        echo -e "\033[1;43mInstalando Opera\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.opera.Opera
        echo -e "\033[1;33mInstalando Opera\033[0m"
        sleep 2
        ;;
      "Firefox - flatpak")
        echo -e "\033[1;43mInstalando Firefox\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.mozilla.firefox
        echo -e "\033[1;33mInstalando Firefox\033[0m"
        sleep 2
        ;;
      "LibreWolf")
        echo -e "\033[1;43mInstalando LibreWolf\033[0m"
        sleep 2
        sudo apt update && sudo apt install extrepo -y
        sudo extrepo enable librewolf
        sudo apt update && sudo apt install librewolf -y
        echo -e "\033[1;33mInstalando LibreWolf\033[0m"
        sleep 2
        ;;
      "Tor Browser Launcher - flatpak")
        echo -e "\033[1;43mInstalando Tor Browser Launcher\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.github.micahflee.torbrowser-launcher
        echo -e "\033[1;33mInstalando Tor Browser Launcher\033[0m"
        sleep 2
        ;;
      "Midori")
        echo -e "\033[1;43mInstalando Midori\033[0m"
        sleep 2
        REPO_URL="https://github.com/goastian/midori-desktop/releases"
        echo -e "\n\033[1;34mInstalando Midori Browser...\033[0m"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'Midori \Kv\d+\.\d+\.\d+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v11.5.2"
        fi
        VERSION_NUMBER=${LATEST_VERSION#v}
        DEB_FILE="midori_${VERSION_NUMBER}-1_amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mMidori $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "WhatsApp Desktop - flatpak")
        echo -e "\033[1;43mInstalando Midori\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.rtosta.zapzap
        echo -e "\033[1;33mInstalando Tor Browser Launcher\033[0m"
        sleep 2
        ;;
      "Telegram Desktop - flatpak")
        echo -e "\033[1;43mInstalando Telegram Desktop\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.telegram.desktop
        echo -e "\033[1;33mInstalando Telegram Desktop\033[0m"
        sleep 2
        ;;
      "Signal Desktop")
        echo -e "\033[1;43mInstalando Signal Desktop\033[0m"
        sleep 2
        wget -O- https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor > signal-desktop-keyring.gpg
        cat signal-desktop-keyring.gpg | sudo tee /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null
        echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] https://updates.signal.org/desktop/apt xenial main' |\
        sudo tee /etc/apt/sources.list.d/signal-xenial.list
        sudo apt update && sudo apt install signal-desktop
        echo -e "\033[1;33mInstalando Signal Desktop\033[0m"
        sleep 2
        ;;
      "teams-for-linux - flatpak")
        echo -e "\033[1;43mInstalando teams-for-linux\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.github.IsmaelMartinez.teams_for_linux
        echo -e "\033[1;33mInstalando teams-for-linux\033[0m"
        sleep 2
        ;;
      "Discord - flatpak")
        echo -e "\033[1;43mInstalando teams-for-linux\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.discordapp.Discord
        echo -e "\033[1;33mInstalando teams-for-linux\033[0m"
        sleep 2
        ;;
      "JDownloader - flatpak")
        echo -e "\033[1;43mInstalando JDownloader\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.jdownloader.JDownloader
        echo -e "\033[1;33mInstalando JDownloader\033[0m"
        sleep 2
        ;;
      "steam")
        echo -e "\033[1;44mInstalando steam\033[0m"
        sleep 2
        cd /tmp/
        wget https://cdn.akamai.steamstatic.com/client/installer/steam.deb
        sudo dpkg --add-architecture i386
        sudo apt install -y libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 python-apt libgl1-nvidia-glx
        sudo apt update
        sudo dpkg -i steam.deb
        sudo apt install -y -f
        rm steam.deb
        echo -e "\033[1;33mInstalando steam\033[0m"
        sleep 2
        ;;
      "Lutris")
        echo -e "\033[1;44mInstalando Lutris\033[0m"
        sleep 2
        REPO_URL="https://github.com/lutris/lutris/releases"
        echo -e "\n\033[1;34mInstalando Lutris...\033[0m"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'Lutris \Kv\d+\.\d+\.\d+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="v0.5.18"
        fi
        VERSION_NUMBER=${LATEST_VERSION#v}
        DEB_FILE="lutris_${VERSION_NUMBER}_all.deb"
        DOWNLOAD_URL="$REPO_URL/download/${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mLutris $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "Heroic Games Launcher")
        echo -e "\033[1;44mInstalando Heroic Games Launcher\033[0m"
        sleep 2
        REPO_URL="https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases"
        echo -e "\n\033[1;34mInstalando Heroic Games Launcher...\033[0m"
        LATEST_VERSION=$(curl -sL "$REPO_URL" | grep -oP 'Release v\K\d+\.\d+\.\d+' | head -n 1)
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="2.16.1"
        fi
        DEB_FILE="Heroic-${LATEST_VERSION}-linux-amd64.deb"
        DOWNLOAD_URL="$REPO_URL/download/v${LATEST_VERSION}/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mHeroic Games Launcher v$LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        echo -e "\033[1;33mInstalando Heroic Games Launcher\033[0m"
        sleep 2
        ;;
      "Minecraft - flatpak")
        echo -e "\033[1;44mInstalando Minecraft\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.mojang.Minecraft
        echo -e "\033[1;33mInstalando Minecraft\033[0m"
        sleep 2
        ;;
      "Dolphin")
        echo -e "\033[1;44mInstalando Dolphin\033[0m"
        sleep 2
        sudo apt-add-repository ppa:dolphin-emu/ppa
        sudo apt update
        sudo apt install -y dolphin-emu
        echo -e "\033[1;33mInstalando Dolphin\033[0m"
        sleep 2
        ;;
      "Lime3DS - flatpak")
        echo -e "\033[1;44mInstalando Dolphin\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y io.github.lime3ds.Lime3DS
        echo -e "\033[1;33mInstalando Dolphin\033[0m"
        sleep 2
        ;;
      "Cemu - flatpak")
        echo -e "\033[1;44mInstalando Cemu\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub info.cemu.Cemu
        echo -e "\033[1;33mInstalando Cemu\033[0m"
        sleep 2
        ;;
      "yuzu - flatpak")
        echo -e "\033[1;44mInstalando yuzu\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.yuzu_emu.yuzu
        echo -e "\033[1;33mInstalando yuzu\033[0m"
        sleep 2
        ;;
      "Ryujinx - flatpak")
        echo -e "\033[1;44mInstalando Ryujinx\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.ryujinx.Ryujinx
        echo -e "\033[1;33mInstalando Ryujinx\033[0m"
        sleep 2
        ;;
      "DuckStation - flatpak")
        echo -e "\033[1;44mInstalando DuckStation\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.duckstation.DuckStation
        echo -e "\033[1;33mInstalando DuckStation\033[0m"
        sleep 2
        ;;
      "PPSSPP - flatpak")
        echo -e "\033[1;44mInstalando PPSSPP\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.ppsspp.PPSSPP
        echo -e "\033[1;33mInstalando PPSSPP\033[0m"
        sleep 2
        ;;
      "PCSX2 - flatpak")
        echo -e "\033[1;44mInstalando PCSX2\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub net.pcsx2.PCSX2
        echo -e "\033[1;33mInstalando PCSX2\033[0m"
        sleep 2
        ;;
      "RPCS3 - flatpak")
        echo -e "\033[1;44mInstalando RPCS3\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y net.rpcs3.RPCS3
        echo -e "\033[1;33mInstalando RPCS3\033[0m"
        sleep 2
        ;;
      "Flycast - flatpak")
        echo -e "\033[1;44mInstalando Flycast\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y org.flycast.Flycast
        echo -e "\033[1;33mInstalando Flycast\033[0m"
        sleep 2
        ;;
      "RetroArch - flatpak")
        echo -e "\033[1;44mInstalando RetroArch\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.libretro.RetroArch
        echo -e "\033[1;33mInstalando RetroArch\033[0m"
        sleep 2
        ;;
      "VICE - flatpak")
        echo -e "\033[1;44mInstalando VICE\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub net.sf.VICE
        echo -e "\033[1;33mInstalando VICE\033[0m"
        sleep 2
        ;;
      "Amiberry - flatpak")
        echo -e "\033[1;44mInstalando Amiberry\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.blitterstudio.amiberry
        echo -e "\033[1;33mInstalando Amiberry\033[0m"
        sleep 2
        ;;
      "DOSBox-X - flatpak")
        echo -e "\033[1;44mInstalando Amiberry\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.dosbox_x.DOSBox-X
        echo -e "\033[1;33mInstalando Amiberry\033[0m"
        sleep 2
        ;;
      "Pack Juegos Retro")
        echo -e "\033[1;44mInstalando Pack Juegos Retro\033[0m"
        sleep 2
        sudo apt -y install alienblaster boswars enigma freedoom gweled hedgewars neverball njam pingus pipenightdreams pokerth pychess seahorse-adventures supertux supertuxkart vodovod xmoto xgalaga
        echo -e "\033[1;33mInstalando Pack Juegos Retro\033[0m"
        sleep 2
        ;;
      "LibreOffice")
        echo -e "\033[1;45mInstalando LibreOffice\033[0m"
        sleep 2
        sudo apt install -y libreoffice libreoffice-l10n-es
        echo -e "\033[1;33mInstalando LibreOffice\033[0m"
        sleep 2
        ;;
      "ONLYOFFICE Desktop - flatpak")
        echo -e "\033[1;45mInstalando ONLYOFFICE Desktop\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.onlyoffice.desktopeditors
        echo -e "\033[1;33mInstalando ONLYOFFICE Desktop\033[0m"
        sleep 2
        ;;
      "Calligra")
        echo -e "\033[1;45mInstalando Calligra\033[0m"
        sleep 2
        sudo apt install -y calligra
        echo -e "\033[1;33mInstalando Calligra\033[0m"
        sleep 2
        ;;
      "MEGASync")
        echo -e "\033[1;45mInstalando MEGASync\033[0m"
        sleep 2
        cd /tmp/
        wget https://mega.nz/linux/repo/xUbuntu_22.04/amd64/megasync-xUbuntu_22.04_amd64.deb
        sudo dpkg -i megasync-xUbuntu_22.04_amd64.deb
        sudo apt install -y -f
        rm megasync-xUbuntu_22.04_amd64.deb
        echo -e "\033[1;33mInstalando MEGASync\033[0m"
        sleep 2
        ;;
        "Insync")
            # Configuración básica
            BASE_URL="https://cdn.insynchq.com/builds/linux"
            VERSION="3.9.5.60024"
            echo -e "\n\033[1;34mInstalando Insync para Ubuntu $UBUNTU_VERSION...\033[0m"

            # Descargar e instalar
            DEB_FILE="insync_${VERSION}-${ubuntu_version}_amd64.deb"
            DOWNLOAD_URL="$BASE_URL/$VERSION/$DEB_FILE"

            echo "Descargando desde: $DOWNLOAD_URL"

            if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
                sudo dpkg -i "/tmp/$DEB_FILE"
                sudo apt install -f -y
                rm "/tmp/$DEB_FILE"
                echo -e "\033[1;32m✓ Insync $VERSION instalado correctamente.\033[0m"
            else
                echo -e "\033[1;31m✗ Error: No se pudo descargar el paquete.\033[0m"
                echo "Intenta manualmente con:"
                echo "wget $DOWNLOAD_URL && sudo dpkg -i $DEB_FILE"
            fi
            ;;
      "calibre - flatpak")
        echo -e "\033[1;45mInstalando calibre\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.calibre_ebook.calibre
        echo -e "\033[1;33mInstalando calibre\033[0m"
        sleep 2
        ;;
      "Foliate - flatpak")
        echo -e "\033[1;45mInstalando Foliate\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.github.johnfactotum.Foliate
        echo -e "\033[1;33mInstalando Foliate\033[0m"
        sleep 2
        ;;
      "Adobe Reader - flatpak")
        echo -e "\033[1;45mInstalando Adobe Reader\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.adobe.Reader
        echo -e "\033[1;33mInstalando Adobe Reader\033[0m"
        sleep 2
        ;;
      "Master PDF Editor - flatpak")
        echo -e "\033[1;45mInstalando Adobe Reader\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub net.codeindustry.MasterPDFEditor
        echo -e "\033[1;33mInstalando Adobe Reader\033[0m"
        sleep 2
        ;;
      "FreeCAD - flatpak")
        echo -e "\033[1;45mInstalando FreeCAD\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.freecadweb.FreeCAD
        echo -e "\033[1;33mInstalando FreeCAD\033[0m"
        sleep 2
        ;;
      "UltiMaker Cura - flatpak")
        echo -e "\033[1;45mInstalando UltiMaker Cura\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub com.ultimaker.cura
        echo -e "\033[1;33mInstalando UltiMaker Cura\033[0m"
        sleep 2
        ;;
      "KiCad - flatpak")
        echo -e "\033[1;45mInstalando KiCad\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.kicad.KiCad
        echo -e "\033[1;33mInstalando KiCad\033[0m"
        sleep 2
        ;;
      "Fritzing - flatpak")
        echo -e "\033[1;45mInstalando Fritzing\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub org.fritzing.Fritzing
        echo -e "\033[1;33mInstalando Fritzing\033[0m"
        sleep 2
        ;;
      "Arduino IDE - flatpak")
        echo -e "\033[1;45mInstalando Arduino IDE\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub cc.arduino.arduinoide
        echo -e "\033[1;33mInstalando Arduino IDE\033[0m"
        sleep 2
        ;;
      "DL: language lessons - flatpak")
        echo -e "\033[1;45mInstalando DL: language lessons\033[0m"
        sleep 2
        sudo apt install -y flatpak
        sudo apt install -y gnome-software-plugin-flatpak
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install -y flathub ro.go.hmlendea.DL-Desktop
        echo -e "\033[1;33mInstalando DL: language lessons\033[0m"
        sleep 2
        ;;
      "GnuCash")
        echo -e "\033[1;45mInstalando UltiMaker Cura\033[0m"
        sleep 2
        sudo apt install -y gnucash
        echo -e "\033[1;33mInstalando DL: language lessons\033[0m"
        sleep 2
        ;;
      "AnyDesk")
        echo -e "\033[1;45mInstalando AnyDesk\033[0m"
        sleep 2
        BASE_URL="https://download.anydesk.com/linux"
        echo -e "\n\033[1;34mInstalando AnyDesk...\033[0m"
        VERSION_INFO=$(curl -sL "https://anydesk.com/es/downloads/thank-you/linux" | grep -oP 'anydesk_\K\d+\.\d+\.\d+-\d+_amd64\.deb' | head -n 1)
        LATEST_VERSION=$(echo "$VERSION_INFO" | grep -oP '\d+\.\d+\.\d+-\d+')
        if [ -z "$LATEST_VERSION" ]; then
          LATEST_VERSION="6.4.3-1"
        fi
        DEB_FILE="anydesk_${LATEST_VERSION}_amd64.deb"
        DOWNLOAD_URL="$BASE_URL/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mAnyDesk $LATEST_VERSION instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "VNC Viewer")
        echo -e "\033[1;45mInstalando VNC Viewer\033[0m"
        sleep 2
        BASE_URL="https://downloads.realvnc.com/download/file/viewer.files"
        echo -e "\n\033[1;34mInstalando VNC Viewer...\033[0m"
        VERSION_INFO=$(curl -sL "https://www.realvnc.com/en/connect/download/viewer/linux/" | grep -oP 'VNC-Viewer-\K\d+\.\d+\.\d+' | head -n 1)
        if [ -z "$VERSION_INFO" ]; then
          VERSION_INFO="7.13.1"
        fi
        DEB_FILE="VNC-Viewer-${VERSION_INFO}-Linux-x64.deb"
        DOWNLOAD_URL="$BASE_URL/$DEB_FILE"
        if wget -q --show-progress "$DOWNLOAD_URL" -O "/tmp/$DEB_FILE"; then
          sudo dpkg -i "/tmp/$DEB_FILE"
          sudo apt install -f -y
          rm "/tmp/$DEB_FILE"
          echo -e "\033[1;32mVNC Viewer $VERSION_INFO instalado correctamente\033[0m"
        else
          echo -e "\033[1;31mError al descargar el paquete\033[0m"
        fi
        ;;
      "Gnome")
        echo -e "\033[1;46mInstalando Gnome\033[0m"
        sleep 2
        sudo apt install -y ubuntu-gnome-desktop
        echo -e "\033[1;33mInstalando Gnome\033[0m"
        sleep 2
        ;;
      "Cinnamon")
        echo -e "\033[1;46mInstalando Cinnamon\033[0m"
        sleep 2
        sudo apt install -y cinnamon
        echo -e "\033[1;33mInstalando Cinnamon\033[0m"
        sleep 2
        ;;
      "Budgie")
        echo -e "\033[1;46mInstalando Budgie\033[0m"
        sleep 2
        sudo apt install -y budgie-core budgie-screensaver lightdm indicator-applet
        echo -e "\033[1;33mInstalando Budgie\033[0m"
        sleep 2
        ;;
      "KDE Plasma")
        echo -e "\033[1;46mInstalando KDE Plasma\033[0m"
        sleep 2
        sudo apt install -y kde-full
        echo -e "\033[1;33mInstalando KDE Plasma\033[0m"
        sleep 2
        ;;
      "Mate")
        echo -e "\033[1;46mInstalando mate\033[0m"
        sleep 2
        sudo apt install -y mate mate-extra lightdm
        echo -e "\033[1;33mInstalando mate\033[0m"
        sleep 2
        ;;
      "XFCE 4")
        echo -e "\033[1;46mInstalando XFCE 4\033[0m"
        sleep 2
        sudo apt install -y xfce4
        echo -e "\033[1;33mInstalando XFCE 4\033[0m"
        sleep 2
        ;;
      "LXQt")
        echo -e "\033[1;46mInstalando LXQt\033[0m"
        sleep 2
        sudo apt install -y task-lxqt-desktop
        echo -e "\033[1;33mInstalando LXQt\033[0m"
        sleep 2
        ;;
      "LXDE")
        echo -e "\033[1;46mInstalando LXDE\033[0m"
        sleep 2
        sudo apt install -y task-lxde-desktop
        echo -e "\033[1;33mInstalando LXDE\033[0m"
        sleep 2
        ;;
      *)
        echo -e "\033[1;33mPrograma no reconocido: $program\033[0m"
        ;;
    esac
  done
}

# Main program flow

# Seleccionar versión de Ubuntu
ubuntu_version=$(select_debian_version)
if [[ -z "$ubuntu_version" ]]; then
  zenity --error --text="No se seleccionó ninguna versión de Ubuntu. Saliendo..."
  exit 1
fi

echo -e "\n\033[1;34mHas seleccionado Debian $ubuntu_version. Esto se usará para configurar los repositorios.\033[0m"

# Seleccionar secciones
selected_sections=$(show_section_menu)
if [[ -z "$selected_sections" ]]; then
  zenity --error --text="No se seleccionó ninguna sección. Saliendo..."
  exit 1
fi

# Array para almacenar todos los programas seleccionados
declare -a all_selected_programs

# Procesar cada sección seleccionada
IFS='|' read -ra sections <<< "$selected_sections"
for section in "${sections[@]}"; do
  # Seleccionar programas en esta sección
  selected_programs=$(show_program_menu "$section")
  if [[ -n "$selected_programs" ]]; then
    IFS='|' read -ra programs <<< "$selected_programs"
    for program in "${programs[@]}"; do
      all_selected_programs+=("$program")
    done
  fi
done

# Si no se seleccionó ningún programa, salir
if [[ ${#all_selected_programs[@]} -eq 0 ]]; then
  zenity --error --text="No se seleccionó ningún programa para instalar. Saliendo..."
  exit 1
fi

# Mostrar resumen de programas seleccionados
summary="Programas seleccionados para instalar:\n\n"
for program in "${all_selected_programs[@]}"; do
  summary+="- $program\n"
done

zenity --info --title="Resumen de instalación" --text="$summary" --width=500 --height=400

# Instalar los programas seleccionados
install_selected_programs "${all_selected_programs[@]}"

# Configuración final
sudo apt autoremove -y
zenity --info --text="¡Instalación completada!\n\nReinicia tu sistema para aplicar todos los cambios." --width=300
