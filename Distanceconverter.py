
#Defined a variable in which user will give input
km = float(input("The distance in kilometer: "))

#one parameter is kept default
#User can give an input of distance in km and get an output in different metric values


def converter(km , meter=1000) :
    return km*meter

print("Distance in meter",converter(km))



def convert_km_to_decimeter(km, decimeter= 10000):
    return km*decimeter
print("Distance in decimeter",convert_km_to_decimeter(km))



def convert_km_to_centimeter(km, centimeter= 100000):
    return km*centimeter
print("Distance in centimeter",convert_km_to_centimeter(km))



def convert_km_to_millimeter(km, millimeter= 1000000):
    return km* millimeter
print("Distance in millimeter",convert_km_to_millimeter(km))