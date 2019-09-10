earth_distance = 92957100.0

jupiter_distance = 483632000.0

earth_diameter = 7926.0

jupiter_diameter = 88846.0

distance_ratio = jupiter_distance / earth_distance

print "Jupiter is", distance_ratio, "times farther from the Sun than the Earth is."



pi = 3.14159

earth_radius = earth_diameter / 2

earth_volume = (4/3)*pi*(earth_radius**3)

jupiter_radius = jupiter_diameter / 2

jupiter_volume = (4/3)*pi*(jupiter_radius**3)

volume_ratio = jupiter_volume / earth_volume

print "Jupiter's volume is", volume_ratio, "times larger than Earth's volume."



earth_totalseconds = 92957100/186000

earth_minutes = earth_totalseconds / 60

earth_secondsleft = earth_totalseconds % 60

print "The time it takes for light to travel from the Sun to Earth is about", earth_minutes, "minutes and", earth_secondsleft, "seconds." 



jupiter_totalseconds = 483632000/186000

jupiter_minutes = jupiter_totalseconds / 60

jupiter_secondsleft = jupiter_totalseconds % 60

print "The time it takes for light to travel from the Sun to Jupiter is about", jupiter_minutes, "minutes and", jupiter_secondsleft, "seconds." 