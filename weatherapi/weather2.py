from flask import Flask, render_template , request
import requests
import time



app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
  if request.method == 'POST':
    city = request.form['location']
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=96358495d08d28ab53fc14c2e1308f8a"
    json_data = requests.get(api).json() 
    condition = json_data['weather'][0]['main']
    condition_desc = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    datalist = [city,condition,condition_desc,temp,min_temp,max_temp,pressure,humidity,wind,sunrise,sunset]
    return render_template('result.html', datalist = datalist)

  return render_template('weatherres.html')


if __name__ == "__main__":
  app.run(debug=True,port = 8000)