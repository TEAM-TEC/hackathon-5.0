import folium
import pandas
from firebase import firebase

map=folium.Map(location=[19.1616,72.9964],zoom_start=12,tiles="OpenStreetMap")
fg=folium.FeatureGroup(name="POTHOLE")
def color_producer(x,y,z,type_r):
    if (type_r=='ph'):
        vk=-8.5
        if (x >8.5 or x<vk):
        
             if(y>=2 or z>=2)and(y<=2.25  or z<=2.25):
                 return 'yellow'
             elif(y>2.25 or z>2.25)and(y<2.5 or z<2.5):
                 return'green'
             elif (y>2.5 or z>2.5)and(y<4.5 or z<4.5):
                 return 'red'

        if (y >8.5 or y< vk):
            #and(y<2.5 or z<2.5)and():
            if(x>=2 or z>=2)and(x<=2.25  or z<=2.25):
                return 'yellow'
            elif(x>2.25 or z>2.25)and(x<2.5 or z<2.5):
                return'green'
            elif (z>2.5 or x>2.5)and(z<4.5 or x<4.5):
                return 'red'

        if (z >8.5 ):
             if(y>=2 and y<2.25)or( x>=2 and x<2.25):
                return 'green'
             elif(y>2.25 and y<3.5 )or(x>2.25 and x<3.5):
                return'yellow'
             elif (y>5.5 and y<6.5 )or( x>5.5 and x<6.5):
                return 'red'
    else:
        return 'grey'

fgv = folium.FeatureGroup(name='Potholes')
map = folium.Map(location=[19.0344648,73.0022548], zoom_start=15, tiles='Stamen Terrain')
firebase=firebase.FirebaseApplication('https://geoacc-48211.firebaseio.com')

result=firebase.get('/DEMO',None)

print("plotting data")

for i in result[1:]:
	lat=i.get("lat")
	lon=i.get("lon")
	x=i.get("x")
	y=i.get("y")
	z=i.get("z")
	plot_color=color_producer(x,y,z,type_r)
	fgv.add_child(folium.CircleMarker(location=[lat, lon], radius=1.5,fill_color=plot_color,color=plot_color,fill=True, fill_opacity=0.))

map.add_child(fg)
map.add_child(folium.LayerControl())
print("saving map")
map.save("m1.html")