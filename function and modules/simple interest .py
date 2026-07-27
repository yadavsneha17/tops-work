def Sim_Interest(P, R, N):
    SI = P * R * N / 100
    print("The simple interest is:", SI)

for i in range(5):
    P = int(input("Enter Principal amount: "))
    R = float(input("Enter Rate of interest: "))
    N = int(input("Enter Time (in years): "))
    Sim_Interest(P, R, N)