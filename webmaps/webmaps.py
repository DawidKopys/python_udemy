import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
data = pandas.read_csv("http://www.pythonhow.com/data/Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
names = list(data["NAME"])
elev = list(data["ELEV"])


def choose_color(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

fg_volcanoes = folium.FeatureGroup(name="Volcanoes_USA")

# tutaj wyswietlamy elv w popupie, proste
for lt, ln, el in zip(lat, lon, elev):
    fg_volcanoes.add_child(child=folium.CircleMarker(location=[lt, ln], popup=str(el)+" m",
        fill_color=choose_color(el), color='black', fill=True, radious=7, fill_opacity=0.8))

fg_countries = folium.FeatureGroup(name="Countries")
polygon_file = open('world.json', 'r', encoding='utf-8-sig')
polygon_str = polygon_file.read()
fg_countries.add_child(child=folium.GeoJson(data=polygon_str,
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

# teraz w popupie wyswietlamy NAME, trudniejsze, bo .Marker nie dziala gdy sa ' w stringu
# for lt, ln, nm in zip(lat, lon, names):
#     print(str(lt) + " and " + str(ln) + " and " + str(nm))
#     fg.add_child(child=folium.Marker(location=[lt, ln],
#                                 popup=folium.Popup(str(nm), parse_html=True),
#                                 icon=folium.Icon(color='green')))

map.add_child(fg_volcanoes)
map.add_child(fg_countries)
map.add_child(folium.LayerControl())
map.save("Map1.html")
