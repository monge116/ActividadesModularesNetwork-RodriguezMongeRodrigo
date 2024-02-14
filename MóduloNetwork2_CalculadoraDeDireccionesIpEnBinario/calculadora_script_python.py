def generate_all_binary_combinations(ip_pattern):
    # Almacenar las direcciones IP en una lista
    ip_addresses = set()  # Utilizar un conjunto para evitar repeticiones

    for bit1 in [0, 1]:
        for bit2 in [0, 1]:
            for bit3 in [0, 1]:
                for bit4 in [0, 1]:
                    for bit5 in [0, 1]:
                        for bit6 in [0, 1]:
                            for bit7 in [0, 1]:
                                for bit8 in [0, 1]:
                                    for bit9 in [0, 1]:
                                        for bit10 in [0, 1]:
                                            for bit11 in [0, 1]:
                                                for bit12 in [0, 1]:
                                                    for bit13 in [0, 1]:
                                                        for bit14 in [0, 1]:
                                                            for bit15 in [0, 1]:
                                                                for bit16 in [0, 1]:
                                                                    ip_address = ip_pattern.format(
                                                                        bit1,
                                                                        bit2,
                                                                        bit3,
                                                                        bit4,
                                                                        bit5,
                                                                        bit6,
                                                                        bit7,
                                                                        bit8,
                                                                        bit9,
                                                                        bit10,
                                                                        bit11,
                                                                        bit12,
                                                                        bit13,
                                                                        bit14,
                                                                        bit15,
                                                                        bit16
                                                                    )
                                                                    ip_addresses.add(ip_address)

    return ip_addresses

# Patrón base para la dirección IP en binario con bits variables
ip_pattern = "11000000.{}{}{}{}{}{}{}{}.00001{}0{}.00010111"

# Generar todas las posibles combinaciones de direcciones IP en binario
all_ip_addresses = generate_all_binary_combinations(ip_pattern)

# Imprimir las direcciones IP en binario
for ip_address in all_ip_addresses:
    print(ip_address)

# Nombre del archivo de salida
output_file_name = "IP_address.txt"

# Escribir las direcciones IP en el archivo de salida
with open(output_file_name, "w") as output_file:
    for ip_address in all_ip_addresses:
        output_file.write(ip_address + "\n")