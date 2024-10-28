import arrow
import util.stormglass
import API_KEY

start_day = '2024-03-21'
latlong = (37.198167, -97.734413)

start = arrow.get(start_day).to('UTC').timestamp()
end = arrow.get(start_day).shift(days=7).to('UTC').timestamp()

SG = util.stormglass.StormGlass(API_KEY.API_KEY)


SG.generate(latlong[0], latlong[1], start, end)
SG.dump_file("./out_historical_argonia.json")
print("File dumped")