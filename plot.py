from firebase import firebase
import folium

# function to sort color of popups by altitude
def color_producer(x,y,z):
    vk=-8.5
    if (x >8.5 or x<vk):
        #if (y>0 or z>0)and(y<0.8 or z<0.8):
        #if (y>1.5 or z>1.5) and(y<2.5 or z<2.5)and():
         #   return 'blue'
        if(y>=2 or z>=2)and(y<=2.25  or z<=2.25):
        #elif(y>2.5 or z>2.5) and(y<3.5 or z<3.5):
            return 'yellow'
        elif(y>2.25 or z>2.25)and(y<2.5 or z<2.5):
            return'green'
        elif (y>2.5 or z>2.5)and(y<4.5 or z<4.5):
            return 'red'
        #else:
            #print('entered black')
         #elif   return 'blue'
        #elif (x<0 or  y<0 or z<0):
         #   print('.x:',x,'y:',y,'z:',z,"\n")
          #  return 'blue'

    if (y >8.5 or y< vk):
        #if (x>0 or z>0)and(x<0.8 or z<0.8):
        #if (y>1.5 or z>1.5) and(y<2.5 or z<2.5)and():
         #   return 'blue'
        if(x>=2 or z>=2)and(x<=2.25  or z<=2.25):
        #elif(y>2.5 or z>2.5) and(y<3.5 or z<3.5):
            return 'yellow'
        elif(x>2.25 or z>2.25)and(x<2.5 or z<2.5):
            return'green'
        elif (z>2.5 or x>2.5)and(z<4.5 or x<4.5):
            return 'red'
        #else:
          #  return 'red'


    if (z >8.5 ):
        #if (y>0 or x>0)and(y<0.8 or x<0.8):
        #if (y>1.5 or z>1.5) and(y<2.5 or z<2.5)and():
         #   return 'blue'
        if(y>=2 and y<2.25)or( x>=2 and x<2.25):
            #print('entered yellow x:',x,'y:',y)
        #elif(y>2.5 or z>2.5) and(y<3.5 or z<3.5):
            return 'green'
        elif(y>2.25 and y<3.5 )or(x>2.25 and x<3.5):
            #print()
            return'yellow'
        elif (y>5.5 and y<6.5 )or( x>5.5 and x<6.5):
            return 'red'
        #elif (x<0 or  y<0 or z<0):
           # print('.x:',x,'y:',y,'z:',z,"\n")
         #   return 'blue'

#map = folium.Map(location=[19.065958,72.894041317], zoom_start=13, tiles='Mapbox Bright')
fgv = folium.FeatureGroup(name='Potholes')
map = folium.Map(location=[19.0344648,73.0022548], zoom_start=15, tiles='Stamen Terrain')
#folium.TileLayer('mapquestopen').add_to(map)
print("fetching db")
firebase=firebase.FirebaseApplication('https://geoacc-48211.firebaseio.com')
print("fetched db")
#for i in range (0,50):
result=firebase.get('/DEMO',None)
print("plotting cordi")
for i in result[1:]:
    lat=i.get("lat")
    lon=i.get("lon")
    x=i.get("x")
    y=i.get("y")
    z=i.get("z")
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius=1.5,fill_color=color_producer(x,y,z),color=color_producer(x,y,z),fill=True, fill_opacity=0.))
print("plotted cordi")
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save('plotted.html')

