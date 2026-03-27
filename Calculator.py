def calculate_effects():
    print("--- 2^3 Factorial Design Calculator ---")
    
    try:
        n = float(input("Enter number of replicates (n): "))
        
        # Input treatment totals
        one = float(input("Enter (1): "))
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        ab = float(input("Enter ab: "))
        ac = float(input("Enter ac: "))
        bc = float(input("Enter bc: "))
        abc = float(input("Enter abc: "))

        # ---- Main Effects ----
        A = (a + ab + ac + abc - one - b - c - bc) / (4 * n)
        B = (b + ab + bc + abc - one - a - c - ac) / (4 * n)
        C = (c + ac + bc + abc - one - a - b - ab) / (4 * n)

        # ---- Interaction Effects ----
        AB = (one - a - b + ab + c - ac - bc + abc) / (4 * n)
        AC = (one - a + b - ab - c + ac - bc + abc) / (4 * n)
        BC = (one + a - b - ab - c - ac + bc + abc) / (4 * n)
        ABC = (abc - bc - ac + c - ab + b + a - one) / (4 * n)

        # ---- Output ----
        print("\n" + "="*20)
        print("RESULTS (Effects):")
        print(f"A   = {A: .4f}")
        print(f"B   = {B: .4f}")
        print(f"C   = {C: .4f}")
        print(f"AB  = {AB: .4f}")
        print(f"AC  = {AC: .4f}")
        print(f"BC  = {BC: .4f}")
        print(f"ABC = {ABC: .4f}")
        print("="*20)

    except ValueError:
        print("\nError: Please enter numbers only!")

if __name__ == "__main__":
    calculate_effects()
