import folium
import pandas
map=folium.Map(location=[22.82,69.63],zoom_start=2,title="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
def pointer_color(eleva):
    if 0<=eleva<=1000:
        return "green"
    elif 1000<eleva<=2000:
        return "blue"
    else:
        return "red"
vol=pandas.read_csv("Volcanoes.txt")

lat=list(vol["LAT"])
lon=list(vol["LON"])
ele=list(vol["ELEV"])

for latitues,longitudes,elevation in zip(lat,lon,ele):
    fgv.add_child(folium.CircleMarker(location=[latitues,longitudes],tooltip=folium.Tooltip,popup=str(elevation),color=pointer_color(elevation),fill_color=pointer_color(elevation)))
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']<=150000000 else 'orange' if 150000000<=x['properties']['POP2005']<=300000000 else 'red'} ))
fg7=folium.FeatureGroup(name="Seven Wonders")
fg7.add_child(folium.GeoJson(data=open('sevenwonders.json','r',encoding='utf-8-sig').read(),
popup=folium.GeoJsonPopup(fields=['name'],style="color:red"),
style_function=lambda x:{'fillColor':'red'}))
map.add_child(fg7)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
