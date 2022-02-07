# Programa simples para vericar a porcentagem da bateria do seu notebook.
# Desenvolvido por: Maria Silveira.
# O código é livre, mas peço que mantenham as informações da autora.

# Não esqueçam de instalar a package psutil
import psutil

# Vamos capturar o sensor da bateria
battery = psutil.sensors_battery()

# Vamos capturar o percentual da bateria
battery = str(battery.percent)

# Vamos mostrar o resultado
print(f'Você está com {battery}% de bateria para utilização!')

###--------------output--------------###