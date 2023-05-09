SHIFT = 3
COMMENT = '#'
climate_data = open('data/sc_climate_data_10.csv', 'r')


def FahrToCelsius(fahr):
    """COnverts fahrenehit to celsius

    Args:
        fahr (float): temperature in fahrenheit

    Returns:
        float: temperature in Celsius
    """
    celsius = ((fahr - 32) * (5/9)) 
    return celsius
def FahrToKelvin(fahr):
    kelvin = FahrToCelsius(fahr) + 273.15
    return kelvin



for line in climate_data:
    data = line.split(',')
    if data[0][0] != COMMENT:
        fahr = float(data[3])
        celsius = FahrToCels(fahr)
        kelvin = FahrToKelvin(fahr)
        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
