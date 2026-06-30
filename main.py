import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nasa_Exoplanet_archive.csv", low_memory=False)  # fixes the warning

# Keep only useful columns
cols = [
    'pl_name',        # Planet name
    'disc_year',      # Discovery year
    'discoverymethod',# How it was found
    'pl_rade',        # Planet radius (Earth radii)
    'pl_orbper',      # Orbital period (days)
    'pl_eqt',         # Equilibrium temperature (K)
    'st_teff',        # Star temperature (K)
    'pl_orbsmax',     # Orbit distance from star (AU)
    'sy_dist'         # Distance from Earth (light years)
]

df = df[cols]

print("Shape after selecting columns:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# Drop rows where critical columns are missing
df = df.dropna(subset=['pl_name', 'disc_year', 'discoverymethod', 'pl_rade'])

print("\nShape after cleaning:", df.shape)
print("\nDiscovery methods available:\n", df['discoverymethod'].value_counts())
# ── GRAPH 1: Exoplanet Discoveries Per Year ──────────────────────────
yearly = df['disc_year'].value_counts().sort_index()

plt.figure(figsize=(12, 5))
plt.bar(yearly.index, yearly.values, color='steelblue', edgecolor='black')
plt.title('Exoplanet Discoveries Per Year', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Number of Planets Discovered')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graph1_discoveries_per_year.png')
plt.show()

# ── GRAPH 2: Discovery Methods (Fixed) ───────────────────────────────
methods = df['discoverymethod'].value_counts()

# Group small slices (less than 1%) into "Other"
threshold = len(df) * 0.01
main = methods[methods >= threshold]
other = methods[methods < threshold].sum()
main['Other'] = other

plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    main.values,
    labels=main.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.tab10.colors,
    pctdistance=0.75,        # percentages closer to center
    labeldistance=1.15       # labels pushed outward
)

# Make labels bigger and bold so nothing overlaps
for text in texts:
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.title('Exoplanet Discovery Methods', fontsize=16, pad=20)
plt.tight_layout()
plt.savefig('graph2_discovery_methods.png')
plt.show()

# ── GRAPH 4: Orbital Period vs Planet Radius ──────────────────────────
df_orb = df.dropna(subset=['pl_orbper', 'pl_rade'])
df_orb = df_orb[(df_orb['pl_orbper'] < 1000) & (df_orb['pl_rade'] < 30)]

plt.figure(figsize=(10, 6))
plt.scatter(df_orb['pl_orbper'], df_orb['pl_rade'],
            alpha=0.4, s=10, color='purple')
plt.title('Orbital Period vs Planet Radius', fontsize=16)
plt.xlabel('Orbital Period (days)')
plt.ylabel('Planet Radius (Earth Radii)')
plt.tight_layout()
plt.savefig('graph4_period_vs_radius.png')
plt.show()

