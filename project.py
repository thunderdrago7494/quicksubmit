import pandas as pd
df = pd.read_csv("star_with_gravity.csv","r")
df.drop(["unnamed:0"],axis=1,inplace=True)

name = df["star_name"].tolist()
mass = df["star_mass"].tolist()
gravity= df["star_gravity"].tolist()
radius = df["star_radius"].tolist()
distance = df["star_distance"].tolist()

