def calor_extremo(temp,rain,code):
    return temp > 32

def chuva_forte(temp,rain,code):
    return rain > 10

def tempestade(temp,rain,code):
    return code == 95

def chuva(temp,rain,code):
    return code in [61,63,65]