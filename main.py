from smart_home import SmartHome
from devices.device_factory import DeviceFactory

def get_status_devices(home):
    return [ device.current_status() for device in home.devices]

def main():
    print("Bem vindo ao sistema casa inteligente")


    home = SmartHome()
    factory = DeviceFactory()
    system = True


    while system:
        print("**** MENU DE ESCOLHA DA CASA INTELIGENTE ****\n"
              "[1] BUSCAR O ESTADO DOS DISPOSITIVOS \n"
              "[2] ADC DISPOSITIVO \n"
              "Para sair digite uma letra:\n")
        choice = input()
        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                print(get_status_devices(home))
            elif choice == 2:
                device_type = input("Digite o tipo de dispositivo (light, thermostat, security_system): ")
                try:
                    device = factory.create_device(device_type)
                    home.add_device(device)
                    print(f"{device_type} adicionado com sucesso.")
                except ValueError as e:
                    print(e)

        else:
            print('Saindo do programa')
            system = False

if __name__ == "__main__":
    main()