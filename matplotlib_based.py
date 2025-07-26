import numpy as np
import matplotlib.pyplot as plt

# Speeds in km/h
speed_robber_kmh = 150
speed_police_kmh = 180

# Convert to km/min
speed_robber = speed_robber_kmh / 60   # 2.5 km/min
speed_police = speed_police_kmh / 60   # 3.0 km/min

# Time police starts (in minutes)
police_delay = 5

# Create time array (0 to 40 minutes)
t = np.linspace(0, 40, 1000)

# Robber's distance (starts at t=0)
d_r = speed_robber * t

# Police's distance (starts at t=5, so before that is 0)
d_s = speed_police * (t - police_delay)
d_s[t < police_delay] = 0  # Police hasn't started yet

# Calculate catch-up time and distance algebraically
# 2.5t = 3(t - 5)
# Solve for t:
catch_time = (speed_police * police_delay) / (speed_police - speed_robber)
catch_distance = speed_robber * catch_time

# Plotting
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')
plt.xlabel('Time (in minutes)')
plt.ylabel('Distance (in km)')
ax.set_xlim([0, 40])
ax.set_ylim([0, max(d_r.max(), d_s.max()) + 10])

# Plot distance curves
ax.plot(t, d_r, c='green', label='Robber')
ax.plot(t, d_s, c='brown', label='Police')

# Automatically plot the point of interception
plt.axvline(x=catch_time, color='purple', linestyle='--')
plt.axhline(y=catch_distance, color='purple', linestyle='--')
plt.plot(catch_time, catch_distance, 'ro', markersize=8)

# Annotate the result
plt.text(catch_time + 1, catch_distance - 5, 
         f'Caught at t={catch_time:.2f} min,\nd={catch_distance:.2f} km',
         fontsize=10, color='red', bbox=dict(facecolor='white', edgecolor='red'))

plt.legend()
plt.show()
