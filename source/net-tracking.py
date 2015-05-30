from tkinter import *
import pygeoip
import random
import urllib.request

root = Tk()
root.title("NetID Tracking")

label_ipaddr = Label(root, text = "IP address")
entry_ipaddr = Entry(root)
label_desc_countryname = Label(root, text = "Country Name: ")
label_desc_city = Label(root, text = "City: ")
label_desc_postalcode = Label(root, text = "Postal Code:")
label_desc_longitude = Label(root, text = "Longitude: ")
label_desc_latitude = Label(root, text = "Latitude: ")

label_ipaddr.grid(row = 0, column = 0)
entry_ipaddr.grid(row = 0, column = 1)
label_desc_countryname.grid(row = 2, column = 0)
label_desc_city.grid(row = 3, column = 0)
label_desc_postalcode.grid(row = 4, column = 0)
label_desc_longitude.grid(row = 5, column = 0)
label_desc_latitude.grid(row = 6, column = 0)

ipaddress = StringVar()
entry_ipaddr["textvariable"] = ipaddress

countryname = StringVar()
label_countryname = Label(root, textvariable = countryname)
label_countryname.grid(row = 2, column = 1)
city = StringVar()
label_city = Label(root, textvariable = city)
label_city.grid(row = 3, column = 1)
postalcode = StringVar()
label_postalcode = Label(root, textvariable = postalcode)
label_postalcode.grid(row = 4, column = 1)
longitude = StringVar()
label_longitude = Label(root, textvariable = longitude)
label_longitude.grid(row = 5, column = 1)
latitude = StringVar()
label_latitude = Label(root, textvariable = latitude)
label_latitude.grid(row = 6, column = 1)

gi = pygeoip.GeoIP("GeoLiteCity.dat")

rb_selection_val = IntVar()

rb_ipv4_address = Radiobutton(root, text = "IPv4 Address", variable = rb_selection_val, value = 1)
rb_ipv4_address.grid(row = 1, column = 0)
rb_hostname = Radiobutton(root, text = "Hostname", variable = rb_selection_val, value = 2)
rb_hostname.grid(row = 1, column = 1)

geoiprecord = 0

def netid_to_geoloc():
    ipaddr = ipaddress.get()
    if rb_selection_val.get() == 1:
        geoiprecord = gi.record_by_addr(ipaddr)
    elif rb_selection_val.get() == 2:
        geoiprecord = gi.record_by_name(ipaddr)
    countryname.set(geoiprecord["country_name"])
    city.set(geoiprecord["city"])
    postalcode.set(geoiprecord["postal_code"])
    longitude.set(geoiprecord["longitude"])
    latitude.set(geoiprecord["latitude"])
    filename = random.randrange(1, 1000)
    full_filename = str(filename) + ".png"
    url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(geoiprecord["latitude"]) + "," + str(geoiprecord["longitude"]) + "&zoom=10&maptype=roadmap&size=400x400"
    urllib.request.urlretrieve(url, full_filename)
    mappic = PhotoImage(file = full_filename)
    maplabel = Label(root, image = mappic)
    maplabel.image = mappic
    maplabel.grid(row = 7, column = 1)
    

button_find = Button(root, text = "Find")
button_find.grid(row = 0, column = 2)
button_find["command"] = netid_to_geoloc

root.mainloop()
