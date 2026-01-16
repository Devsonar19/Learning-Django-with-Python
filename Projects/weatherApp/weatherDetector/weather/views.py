from django.shortcuts import render
import json
import urllib.request
import urllib.parse

def index(request):
    data = {}
    city = ""

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            import urllib.parse
            try:
                city_encoded = urllib.parse.quote(city)
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid=c1ad719f9b59c9f2dbf623884fc00221"
                res = urllib.request.urlopen(url).read()
                json_data = json.loads(res)

                data = {
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
                    "temp": str(json_data['main']['temp']) + 'k',
                    "pressure": str(json_data['main']['pressure']),
                    "humidity": str(json_data['main']['humidity']),
                }
            except:
                data = {"error": "Invalid city"}

    return render(request, 'index.html', {"data": data, "city": city})
