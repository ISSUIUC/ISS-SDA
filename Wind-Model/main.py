# ADD STUFF HERE!
import API_KEY
import util.stormglass
import matplotlib.pyplot as plt

# CONFIGURATION
latitude = 40.112283
longitude = -88.226541






#################

dataloader = util.stormglass.StormGlass(API_KEY.API_KEY)
dataloader.load_file("./dl_out.json")
# dataloader.load_data(latitude, longitude)
# dataloader.dump_file("./dl_out.json")


df: util.stormglass.StormGlassData = dataloader.get_dataframe()

ax = plt.figure().add_subplot(projection='3d')

for ind, row in enumerate(df[0:23]):
    a, s, _ = row.get_wind_gradient_raw()
    ax.plot(a, s, zs=ind)

ax.set_xlabel("Altitude (m)")
ax.set_ylabel("Wind speed (m/s)")
ax.set_zlabel("Hour")

plt.show()

      
    




