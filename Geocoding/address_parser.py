import pyap
import re
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAKLe-3vkSSHZ67pkBrxEjCnZDffKOUXNU')

regexp = "[0-9]{1,4} .+, .+, [A-Z]{2} [0-9]{5}"

strings = [

"On 11/8 at 3:00 pm, a 12-year-old female was standing outside 1149 Tiffany Street in the Bronx when an unknown male lured her into an alleyway &amp; forced her to perform a sex act.We need your finding this individual, call/DM @nypdtips at 800-577-TIPS w/ any info.🎥: @news12bx https://t.co/HNl0WqShTK",

"🚨WANTED for PUBLIC LEWDNESS: Do you know this guy? On 11/11/20 at approx 2:40 PM, inside of 1237 Ave U in Brooklyn, the suspect exposed his genitals to a 16-year-old female victim, then fled in a gray Volkswagen SUV. Any info call or DM @NYPDTips at 800-577-TIPS. https://t.co/RvdCjRWEp4",

"1019 Everglades Dr, Allen, Texas, 75013"

]



for string in strings:
    #print(string + "\n")
    address = pyap.parse(string, country='US')
    addressregex = re.findall(regexp, string)

    #print(address)
    #print("Regex: " + str(addressregex))
    #addresses.append(address)


#print(str(addresses))


addresses = [
    "610 West Loop into the Galleria",
    "Emerson Ave S and Lagoon Ave"
    "7th Ave at Pike",
    "1149 Tiffany Street in the Bronx"
]

for address in addresses:
    geocode_result = gmaps.geocode(address)
    coordinates = geocode_result[0]['geometry']['location']
    print(str(coordinates['lat']) + ", " + str(coordinates['lng']))

