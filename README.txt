MOTU PATLU CLOUD PHONE — TEST PACKAGE

IMPORTANT:
This ZIP is a safe diagnostics test, NOT an Android operating system or emulator.
Your current Pterodactyl container showed no /dev/kvm, no QEMU in PATH, and no root access.
This package lets you test that a Python web page can run and view container capability checks.

PTERODACTYL SETUP
1. Upload and extract this ZIP into your server's Files tab.
2. In Startup, set the startup command to:
   python3 app.py
3. Set the server's allocation / primary port to the port provided by your panel.
   The app uses SERVER_PORT, then PORT, and defaults to 8080.
4. Start the server.
5. Open the allocation address shown by your Pterodactyl panel in your phone browser.

If the panel provides a port variable such as SERVER_PORT, it should be passed automatically.
If your panel uses a different port variable, change the final line in app.py to use that variable.

NEXT STEP FOR REAL ANDROID
A diagnostics webpage is not a cloud phone. To run full Android, the host must provide a compatible
Android runtime/VM and required privileges. Ask the provider/admin whether Android-x86/Waydroid/QEMU
or an Android container is supported. Do not try to install Docker or modify host permissions from
inside an unprivileged Pterodactyl container.
