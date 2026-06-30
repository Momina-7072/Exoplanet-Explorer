
# Exoplanet Explorer 

This project analyzes NASA's confirmed exoplanet dataset to understand discovery trends and planetary characteristics. I built it while learning Pandas, NumPy, and Matplotlib in my CS course.

## What I did
- Cleaned a dataset of 6,247+ confirmed exoplanets (lots of missing values had to be handled)
- Looked at how exoplanet discoveries have changed over the years
- Compared the different methods used to detect exoplanets
- Studied the relationship between a planet's orbital period and its size

## Graphs
1. **Discoveries Per Year** - shows how the Kepler telescope launch caused a huge jump in discoveries
2. **Discovery Methods** - pie chart comparing Transit, Radial Velocity, Microlensing, etc.
3. **Orbital Period vs Planet Radius** - scatter plot to see if there's any pattern

## Libraries Used
- Pandas - reading and cleaning the data
- NumPy - calculations
- Matplotlib - making the graphs

## Dataset
I used the Planetary Systems Composite table from NASA's Exoplanet Archive:
https://exoplanetarchive.ipac.caltech.edu/

Download it as CSV and save it in the project folder as `Nasa_Exoplanet_archive.csv`.

## Running it
```bash
pip install pandas numpy matplotlib
python main.py

##Author
Momina Ahmad
