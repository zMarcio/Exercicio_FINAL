import sys
import logging

log = logging.Logger("alerta")

info = {
    "temperatura" : None,
    "umidade": None
}



while True:

    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])


    if info_size == filled_size:
        break


    keys = info.keys( )

    for key in keys:
        if info [key] is not None:
            continue
        try:    
            info[key] = float(input(f"Digite sua {key}: ").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            sys.exit(1)


temp_3 = info["temperatura"] * 3

if info["temperatura"] >= 45:
    print(f"ALERTA!!! Perigo de calor extremo, {info['temperatura']}ºC")
elif temp_3 >= info["umidade"]:
    print(f"ALERTA!!! Perigo de calor úmido, {info['temperatura']}ºC {info['umidade']} umidade")
elif 10 < info['temperatura'] <= 30:
    print(f"Normal, {info['temperatura']}ºC")
elif 0 <= info['temperatura'] <= 10:
    print(f"Frio, {info['temperatura']}ºC")
elif info['temperatura'] < 0:
    print(f"ALERTA: Frio extremo, {info['temperatura']}ºC")