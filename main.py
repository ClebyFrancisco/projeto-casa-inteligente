from smart_home import SmartHome
from devices.device_factory import DeviceFactory
from devices.light import Light
from devices.thermostat import Thermostat
from devices.security_system import SecuritySystem
from functools import reduce


def get_status_devices(home):
    return [device.current_status() for device in home.devices]

def list_devices(home):
    for index, device in enumerate(home.devices):
        print(f"{index}: {device.__class__.__name__} - {device.current_status()}")

def turn_off_all_lights(home):
    lights = filter(lambda device: isinstance(device, Light), home.devices)
    list(map(lambda light: light.turnOff(), lights))
    print("Todas as luzes foram desligadas.")

def get_on_devices(home):
    on_devices = filter(lambda device: device.current_status() in ['on', 'heating', 'cooling', 'armed_home', 'armed_away'], home.devices)
    return list(on_devices)

def count_on_devices(home):
    on_devices = get_on_devices(home)
    return reduce(lambda count, _: count + 1, on_devices, 0)

def main():
    print("Bem-vindo ao sistema de casa inteligente\n")

    home = SmartHome()
    factory = DeviceFactory()
    system = True

    while system:
        print("**** MENU DE ESCOLHA DA CASA INTELIGENTE ****\n\n"
              "[1] BUSCAR O ESTADO DOS DISPOSITIVOS \n"
              "[2] ADICIONAR DISPOSITIVO \n"
              "[3] MUDAR O ESTADO DE UM DISPOSITIVO \n"
              "[4] MUDAR O ESTADO DE VÁRIOS DISPOSITIVOS DO MESMO TIPO \n"
              "[5] DESLIGAR TODAS AS LUZES \n"
              "[6] LISTAR DISPOSITIVOS LIGADOS \n"
              "[7] CONTAR DISPOSITIVOS LIGADOS \n"
              "[8] REMOVER DISPOSITIVO \n\n"


              "Para sair digite 'exit'.\n")
        choice = input()
        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                print(f'{get_status_devices(home)} \n')
            elif choice == 2:
                device_type = input("Digite o tipo de dispositivo (light, thermostat, security_system): ")
                try:
                    device = factory.create_device(device_type)
                    home.add_device(device)
                    print(f"{device_type} adicionado com sucesso. \n")
                except ValueError as e:
                    print(e)
            elif choice == 3:
                list_devices(home)
                device_index = int(input("Digite o índice do dispositivo que deseja alterar: "))
                if 0 <= device_index < len(home.devices):
                    device = home.devices[device_index]
                    if isinstance(device, Light):
                        new_state = input("Digite o novo estado (on/off): ")
                        if new_state == "on":
                            device.turnOn()
                        elif new_state == "off":
                            device.turnOff()
                    elif isinstance(device, Thermostat):
                        new_state = input("Digite o novo estado (heating/cooling/off): ")
                        if new_state == "heating":
                            device.warm()
                        elif new_state == "cooling":
                            device.coolDown()
                        elif new_state == "off":
                            device.turnOff()
                    elif isinstance(device, SecuritySystem):
                        new_state = input("Digite o novo estado (armed_home/armed_away/disarmed): ")
                        if new_state == "armed_home":
                            device.armed_with_people_at_home()
                        elif new_state == "armed_away":
                            device.armed_without_people_at_home()
                        elif new_state == "disarmed":
                            device.unarmed()
                    print(f"Estado do dispositivo atualizado para {device.current_status()}")
                else:
                    print("Índice de dispositivo inválido.")
            elif choice == 4:
                device_type = input("Digite o tipo de dispositivo para alterar (light, thermostat, security_system): ")
                new_state = input("Digite o novo estado para todos os dispositivos do mesmo tipo: ")
                for device in home.devices:
                    if isinstance(device, Light) and device_type == "light":
                        if new_state == "on":
                            device.turnOn()
                        elif new_state == "off":
                            device.turnOff()
                    elif isinstance(device, Thermostat) and device_type == "thermostat":
                        if new_state == "heating":
                            device.warm()
                        elif new_state == "cooling":
                            device.coolDown()
                        elif new_state == "off":
                            device.turnOff()
                    elif isinstance(device, SecuritySystem) and device_type == "security_system":
                        if new_state == "armed_home":
                            device.armed_with_people_at_home()
                        elif new_state == "armed_away":
                            device.armed_without_people_at_home()
                        elif new_state == "disarmed":
                            device.unarmed()
                print(f"Estado de todos os dispositivos do tipo {device_type} atualizado para {new_state}")
            elif choice == 5:
                turn_off_all_lights(home)
            elif choice == 6:
                on_devices = get_on_devices(home)
                for device in on_devices:
                    print(f"{device.__class__.__name__} - {device.current_status()}")
            elif choice == 7:
                on_count = count_on_devices(home)
                print(f"Número total de dispositivos ligados: {on_count}")
            elif choice == 8:
                list_devices(home)
                device_index = int(input("Digite o índice do dispositivo que deseja remover: "))
                if 0 <= device_index < len(home.devices):
                    home.devices.pop(device_index)
                    print("Dispositivo removido com sucesso.")
                else:
                    print("Índice de dispositivo inválido.")
        else:
            print('Saindo do programa')
            system = False

if __name__ == "__main__":
    main()
