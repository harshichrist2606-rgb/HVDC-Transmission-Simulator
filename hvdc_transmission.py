import math

print("=" * 55)
print("        HVDC TRANSMISSION SIMULATOR")
print("=" * 55)

# Input parameters
voltage_kv = float(input("Enter HVDC transmission voltage (kV): "))
power_mw = float(input("Enter transmitted power (MW): "))
line_length_km = float(input("Enter transmission line length (km): "))
resistance_ohm_per_km = float(
    input("Enter resistance of one conductor (ohm/km): ")
)

# Convert units
V = voltage_kv * 1000
P = power_mw * 1_000_000

# HVDC current
I = P / V

# Total conductor resistance
# HVDC uses two conductors: positive and negative
R_total = 2 * resistance_ohm_per_km * line_length_km

# Line losses
loss_watts = I ** 2 * R_total
loss_mw = loss_watts / 1_000_000

# Receiving-end power
receiving_power_mw = power_mw - loss_mw

# Voltage drop
voltage_drop = I * R_total
receiving_voltage = V - voltage_drop

# Efficiency
efficiency = (receiving_power_mw / power_mw) * 100

# Results
print("\n" + "=" * 55)
print("             HVDC SIMULATION RESULTS")
print("=" * 55)

print(f"Transmission Voltage       : {voltage_kv:.2f} kV")
print(f"Transmitted Power          : {power_mw:.2f} MW")
print(f"Line Length                : {line_length_km:.2f} km")
print(f"HVDC Line Current          : {I:.2f} A")
print(f"Total Line Resistance      : {R_total:.4f} ohm")
print(f"Voltage Drop               : {voltage_drop / 1000:.4f} kV")
print(f"Receiving-End Voltage      : {receiving_voltage / 1000:.4f} kV")
print(f"Transmission Loss          : {loss_mw:.4f} MW")
print(f"Receiving-End Power        : {receiving_power_mw:.4f} MW")
print(f"Transmission Efficiency    : {efficiency:.2f} %")

print("=" * 55)

# Performance assessment
if efficiency >= 95:
    print("System Status              : EXCELLENT")
elif efficiency >= 90:
    print("System Status              : GOOD")
elif efficiency >= 80:
    print("System Status              : MODERATE")
else:
    print("System Status              : HIGH LOSSES")

print("=" * 55)
