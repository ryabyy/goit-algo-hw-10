import pulp

model = pulp.LpProblem("Production", pulp.LpMaximize)

L = pulp.LpVariable('Lemonade', 0, cat='Continuous')
F = pulp.LpVariable('Fruit juice', 0, cat='Continuous')

model += L + F, "Production amount"

model += 2*L + 1*F <= 100, "Water constraint"
model += 1*L <= 50, "Sugar constraint"
model += 1*L <= 30, "Lemon constraint"
model += 1*F <= 40, "Fruit constraint"

model.solve()

print("Solution status:", pulp.LpStatus[model.status])
print(f"Optimal production of {L.name}:", L.varValue)
print(f"Optimal production of {F.name}:", F.varValue)