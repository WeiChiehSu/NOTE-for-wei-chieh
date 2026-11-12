E = float(input("Enter energy (eV):"))
print(f"Energy = {E:.3f}")

if E > 0:
    print("POSITIVE")
elif E == 0:
    print("ZERO")    
else:
    print("NEGATIVE")
