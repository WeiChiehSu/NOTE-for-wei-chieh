def main():
    materials = {
        "Fe": 2.2,
        "Co": 1.7,
        "Ni": 0.6,
        "Mn": 4.0,
        "Cu": 0.0
    }
    Strong_materials = 0
    Total_moment = 0
    Total_moment, Strong_materials= analyze(materials,Strong_materials,Total_moment)
    Average_moment = Total_moment/len(materials)
    print(f"Strong materials = {Strong_materials}")
    print(f"Average moment = {Average_moment:.2f}")
    
def analyze(materials,Strong_materials,Total_moment):
    for i in materials:
        Total_moment = Total_moment + materials[i]
        if materials[i] >= 2.0:
            Strong_materials = Strong_materials + 1
            print(i,materials[i],"STRONG")
        elif 0 < materials[i] < 2.0:
            print(i,materials[i],"WEAK")
        else:
            print(i,materials[i],"NON-MAGNETIC")
    return Total_moment, Strong_materials

main()


%runfile C:/Users/user/Downloads/untitled2.py --wdir
Fe 2.2 STRONG
Co 1.7 WEAK
Ni 0.6 WEAK
Mn 4.0 STRONG
Cu 0.0 NON-MAGNETIC
Strong materials = 2
Average moment = 1.70
