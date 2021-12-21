import requests

def get_weather_desc_and_temp():

    api_key = "fcd7f851f3026413ffe9adf7c8d0575b"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    #print(json)



    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return{'description': description,
           'temp_min': temp_min,
           'temp_max': temp_max}

def main():

    weather_dict = get_weather_desc_and_temp()
    print("Todays forecast is", weather_dict.get('description'))
    print("The minimum temparature is", weather_dict.get('temp_min'))
    print("The maximum temparature is", weather_dict.get('temp_max'))

main()