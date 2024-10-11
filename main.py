import serial

# Configuração da porta serial para o LoRa
lora_serial = serial.Serial(
    port='/dev/ttyS0',  # Verifique qual é a porta serial usada no seu Raspberry Pi
    baudrate=9600,
    timeout=1
)

def process_lora_data(data):
    try:
        # Divide os dados recebidos em partes
        temperature, humidity, wind_speed, rain_amount, uv_index, is_raining = data.split(',')

        # Converte os valores para os tipos corretos
        temperature = float(temperature)
        humidity = float(humidity)
        wind_speed = float(wind_speed)
        rain_amount = float(rain_amount)
        uv_index = int(uv_index)
        is_raining = bool(int(is_raining))

        # Exibe os dados recebidos
        print(f"Temperatura: {temperature} °C")
        print(f"Umidade: {humidity} %")
        print(f"Velocidade do Vento: {wind_speed} km/h")
        print(f"Quantidade de Chuva: {rain_amount} mm")
        print(f"Índice UV: {uv_index}")
        print(f"Está chovendo: {'Sim' if is_raining else 'Não'}")
    except ValueError:
        print("Erro ao processar dados LoRa:", data)

def main():
    print("Aguardando dados do LoRa...")

    while True:
        if lora_serial.in_waiting > 0:
            data = lora_serial.readline().decode('utf-8').strip()
            if data:
                print(f"Dados recebidos: {data}")
                process_lora_data(data)

if __name__ == "__main__":
    main()

