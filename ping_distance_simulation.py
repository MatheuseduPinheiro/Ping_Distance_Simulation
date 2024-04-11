import numpy as np
import matplotlib.pyplot as plt
import ping3

# Endereço IP do dispositivo a ser pingado
ip_address = ""

# # Define uma sequência de alcances em metros , necessário por o disposito alinhado com a representação conceitual (exemplo : 1 há 10 metros)
alcances = np.arange(1, 11, 1)  

# Lista para armazenar os tempos de resposta do ping
ping_times = []

# Pingar o dispositivo em cada alcance e armazenar os tempos de resposta
for alcance in alcances:
    ping_time = ping3.ping(ip_address, timeout=1, unit="ms")
    if ping_time is not None:
        ping_times.append(ping_time) # A resposta é entregue em número inteiro(ms)
    else:
        ping_times.append(0)  # se o ping falhar, assumimos que o tempo de resposta é 0

# Plotar o gráfico de sinal da rede em função do alcance

#Plotar gráfico de linha com Marcadores
plt.plot(alcances, ping_times, marker='o')
plt.title('Sinal da Rede em Função do Alcance')
plt.xlabel('Alcance (metros)')
plt.ylabel('Tempo de Resposta do Ping (segundos)')
plt.grid(True)
plt.show()

# Plotar um gráfico de barras
plt.bar(alcances, ping_times)
plt.title('Sinal da Rede em Função do Alcance')
plt.xlabel('Alcance (metros)')
plt.ylabel('Tempo de Resposta do Ping (segundos)')
plt.grid(True)
plt.show()

