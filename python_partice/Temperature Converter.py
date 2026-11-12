def main():
    C = float(input("Enter temperature (C): "))

    K = convert(C)
    print(f"Temperature = {K:.2f} K")

def convert(C):
    K = C + 273.15
    return K

main()
