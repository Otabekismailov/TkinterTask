import os
from datetime import datetime, timedelta
import json
import tkinter
from tkinter import Label, Entry, Button
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherManager:
    API_KEY = os.environ.get("API_KEY")

    def __init__(self, city):
        self.city = city

    @staticmethod
    def convert_to_datetime(date_str):
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

    def get_data(self):
        url = f"https://api.tomorrow.io/v4/weather/forecast?" \
              f"location={self.city}&apikey={self.API_KEY}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print(response.text)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return json.loads(response.text)

    def get_timelines(self):
        res = self.get_data()
        return res.get("timelines")

    def get_daily_data(self):
        timelines = self.get_timelines()
        if timelines:
            return timelines.get("daily")

    def get_hourly_data(self):
        timelines = self.get_timelines()
        if timelines:
            return timelines.get("hourly")

    def get_day_hours_temperature_with_time(self, day_date):
        hourly_data = self.get_hourly_data()
        data = []

        for hour_data in hourly_data:
            time = hour_data.get("time")
            if self.convert_to_datetime(time).date() == day_date.date():
                data.append({
                    "time": self.convert_to_datetime(time).strftime("%H:%M"),
                    "temperature": hour_data["values"].get("temperature")
                })
        return data

    def get_daily_temperature(self):
        data = []

        for day in self.get_daily_data():
            day_values = day.get("values")
            average_temperature = None
            if day_values:
                average_temperature = day_values.get("temperatureAvg")
            day_date = datetime.strptime(day.get("time"), "%Y-%m-%dT%H:%M:%SZ")
            data.append({
                "day": day_date.strftime("%Y.%m.%d"),
                "average_temperature": average_temperature,
                "hours": self.get_day_hours_temperature_with_time(day_date)}
            )

        return data


def time2():
    day2 = datetime.now() + timedelta(days=1)
    time2 = datetime.strptime(day2.time().strftime("%H:%M"), "%H:%M")
    day1 = datetime.now()

    time1 = datetime.strptime(day1.time().strftime("%H:%M"), "%H:%M")
    weather_res = WeatherManager(weather_entery.get()).get_daily_temperature()

    for row in weather_res:
        data_day = datetime.strptime(row.get('day'), "%Y.%m.%d")

        data_time1 = row["hours"]
        if data_day.date() == day1.date():
            weather_data.configure(text=row.get('day'))
            weather_temperatureAvg.configure(
                text=row.get('average_temperature'))
        if data_day.date() == day2.date():
            weather_data2.configure(text=row.get('day'))
            weather_temperatureAvg2.configure(text=row.get('average_temperature'))
        for time in data_time1:
            data_time = datetime.strptime(time['time'], "%H:%M")
            if data_time.time() >= time1.time():
                weather_time2.configure(text=time.get('time'))
                weather_temp2.configure(text=time.get('temperature'))

            if data_time.time() <= time1.time():
                weather_time3.configure(text=time.get('time'))
                weather_temp3.configure(text=time.get('temperature'))

            if data_time.time() >= time2.time():
                weather_time5.configure(text=time.get('time'))
                weather_temp5.configure(text=time.get('temperature'))

            if data_time.time() <= time2.time():
                weather_time6.configure(text=time.get('time'))
                weather_temp6.configure(text=time.get('temperature'))


weather = tkinter.Tk()
weather.title("P10_Weather")

# weather.resizable(width=False, height=False)
weather_color = tkinter.Frame(weather, height=400, width=800, )
weather_color.grid(row=0, column=1)

weter_heder = Label(weather, text="Weather Applecition", font=50)
weter_heder.place(x=300, y=0)

weather_label = Label(weather, text="Select City:", bg='red', font=50)
weather_label.place(x=200, y=50)

weather_data = Label(weather, text="", bg="red", font=20)
weather_data.place(x=100, y=90)

weather_tempertura_label = Label(weather, text="O'rtacha harorat:", font=40)
weather_tempertura_label.place(x=250, y=90)

weather_temperatureAvg = Label(weather, text="", bg="red", font=20)
weather_temperatureAvg.place(x=400, y=90)

weather_time = Label(weather, text="VAQT:", bg="red")
weather_time.place(x=100, y=120)

weather_time2 = Label(weather, text="", bg='red')
weather_time2.place(x=160, y=120)
weather_time3 = Label(weather, text="", bg='red')
weather_time3.place(x=220, y=120)

weather_temp = Label(weather, text="Harorat:", bg="red")
weather_temp.place(x=100, y=150)

weather_temp2 = Label(weather, text="", bg="red")
weather_temp2.place(x=160, y=150)

weather_temp3 = Label(weather, text="", bg='red')
weather_temp3.place(x=220, y=150)

weather_data2 = Label(weather, text="", bg="red", font=20)
weather_data2.place(x=100, y=190)

weather_tempertura_label2 = Label(weather, text="O'rtacha harorat:", font=40)
weather_tempertura_label2.place(x=250, y=190)

weather_temperatureAvg2 = Label(weather, text="", bg="red", font=20)
weather_temperatureAvg2.place(x=400, y=190)

weather_time4 = Label(weather, text="VAQT:", bg="red")
weather_time4.place(x=100, y=220)

weather_time5 = Label(weather, text="", bg='red')
weather_time5.place(x=160, y=220)
weather_time6 = Label(weather, text="", bg='red')
weather_time6.place(x=220, y=220)

weather_temp4 = Label(weather, text="Harorat:", bg="red")
weather_temp4.place(x=100, y=250)

weather_temp5 = Label(weather, text="", bg="red")
weather_temp5.place(x=160, y=250)

weather_temp6 = Label(weather, text="", bg='red')
weather_temp6.place(x=220, y=250)

weather_entery = Entry(weather, width=20, font=20)
weather_entery.place(x=300, y=50)

weather_button = Button(weather, text="Enter", bg="red", font=60, command=time2)
weather_button.place(x=510, y=50)

if __name__ == "__main__":
    weather.mainloop()
