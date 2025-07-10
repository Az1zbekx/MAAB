def convert_cel_to_far(C):
    return (C * 9 / 5) + 32

def convert_far_to_cel(F):
    return (F - 32) * 5 / 9
try:
    F = float(input("Enter a temperature in degrees F: "))
    res = convert_far_to_cel(F)
    print(f"{F:.0f} degrees F = {res:.2f} degrees C\n")

    C = float(input("Enter a temperature in degrees C: "))
    res = convert_cel_to_far(C)
    print(f"{C:.0f} degrees C = {res:.2f} degrees F\n")
except ValueError:
    print("Error")
