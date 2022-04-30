import requests
import json

city="Seoul"
lang="kr"
apikey="834953ea3200c90ac68b808d1721bc42"

api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

result_raw=requests.get(api)

result=json.loads(result_raw.text)

print(result["name"]+"지역의 날씨입니다.")
print("날씨 : "+result["weather"][0]["description"])
print("기온 : "+str(result["main"]["temp"])+"℃")
print("체감온도 : "+str(result["main"]["feels_like"])+"℃")
print("최고기온 : "+str(result["main"]["temp_max"])+"℃")
print("최저기온 : "+str(result["main"]["temp_min"])+"℃")
print("풍향 : "+str(result["wind"]["deg"])+"º")
print("풍속 : "+str(result["wind"]["speed"])+"m/s")
print("기압 : "+str(result["main"]["pressure"])+"hPa")
print("습도 : "+str(result["main"]["humidity"])+"%")