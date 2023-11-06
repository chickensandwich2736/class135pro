import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("filtered_stars.csv")

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()\

plt.figure(figsize=(10,5))
plt.title("Stars Solar Mass")
plt.bar(name[0:9],mass[0:9])

plt.figure(figsize = (10,5))
plt.title("Stars Solar Radius")
plt.bar(name[0:9],radius[0:9])

plt.figure(figsize = (10,5))
plt.title("Stars Gravity")
plt.bar(name[0:9], gravity[0:9])

plt.figure(figsize = (10,5))
plt.title("Stars Gravity")
plt.bar(name[0:9], distance[0:9])