import numpy as np
import matplotlib.pyplot as plt
import os

# --- Configuración de Matplotlib ---
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 16,
    "axes.titlesize": 16,
    "axes.labelsize": 16,
    "legend.fontsize": 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
})

# --- Parámetros ---
N_SEEDS = 10
ZZZ = "082"
NNN = "100"

std_folder = f"{ZZZ}_{NNN}_PNAMP_Std_Regular_Split_2D"

if not os.path.exists(std_folder):
    raise FileNotFoundError(f"La carpeta '{std_folder}' no existe.")

all_data = []

for i in range(N_SEEDS):
    filename = os.path.join(std_folder, f"Pred_Std_Iter_{i}.txt")
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Archivo no encontrado: {filename}")
    data = np.loadtxt(filename, skiprows=1)
    all_data.append(data)

all_data = np.array(all_data)
x_values = all_data[0, :, 0]
y_values = all_data[:, :, 1]

y_mean = np.mean(y_values, axis=0)
y_std = np.std(y_values, axis=0)

plt.figure(figsize=(10, 6))
plt.fill_between(x_values, y_mean - y_std, y_mean + y_std,
                 color='red', alpha=0.5, label=r'$\pm 1\sigma$')
plt.plot(x_values, y_mean, color='black', linewidth=2.5, label=r'Media')

plt.xlabel(r"Fracci\'on de Test")
plt.ylabel(r"Desviaci\'on media [MeV]")
plt.title(rf"Desviaci\'on media PNAMP (con HFB)vs Fracci\'on Test (Regular) para Z={ZZZ} | N={NNN}")
plt.legend()
plt.tight_layout()

output_name = (f"Std_Regular_PNAMPwHFB_{ZZZ}_{NNN}.pdf")
plt.savefig(output_name, dpi=300)

plt.show()
