# 05-temperature-convert.py
# Temperature Converter

c_deg_in = 100.0  # Boiling C (100) -> Boiling F (212)
f_deg_in = 32.0   # Freezing F (32) -> Freezing C (0)

c_deg_out = (f_deg_in - 32) * (5/9)
f_deg_out = c_deg_in * (9/5) + 32

print(f"{c_deg_in}°C -> {f_deg_out}°F")
print(f"{f_deg_in}°F -> {c_deg_out}°C")
