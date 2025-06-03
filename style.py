class Colors:
    magenta = '\033[95m'
    yellow = '\033[93m'
    cyan = '\033[96m'
    reset = '\033[0m'

def header(title):
    print("\n" + "~"*115)
    print(f"{Colors.cyan}{title.center(60)}{Colors.reset}")
    print("~"*115)

def footer():
    print("\n" + "~"*60)
    print(f"{Colors.cyan}{'Gracias por usar el sistema'.center(60)}{Colors.reset}")
    print("~"*60)

def start():
    header("Bienvenido: Belardita, Berón, Ortega, Ruiz Canaza & Sandoval les agradecen el pago y uso de éste Sistema de Gestión")
