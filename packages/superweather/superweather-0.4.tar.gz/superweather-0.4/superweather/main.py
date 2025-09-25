import requests
import pyttsx3
import time
import json
from colorama import Fore, init
import tkinter as tk
from tkinter import ttk, messagebox

# Initialize colorama
init(autoreset=True)

class AirQualityData:
    def __init__(self, city="tehran"):
        self.input_city = city.lower()
        self.data = None
        self.raw_data = None
        self._fetch_data()

    def _fetch_data(self):
        """Fetch data from API"""
        try:
            url = f"http://api.waqi.info/feed/{self.input_city}/?token=a77ec062d00fbba59f2107ba7e85848113d7447e"
            response = requests.get(url).json()
            self.raw_data = response
            if response.get("status") == "ok":
                self.data = {
                    "city": response['data']['city']['name'],
                    "aqi": response['data']['aqi'],
                    "temperature": response['data']['iaqi'].get('t', {}).get('v', 'N/A'),
                    "humidity": response['data']['iaqi'].get('h', {}).get('v', 'N/A'),
                    "air_pollution_level": self.air_pollution_level(response['data']['aqi'])
                }
            else:
                print(Fore.RED + "Invalid city name or data not available.")
                self.data = None
        except Exception:
            print(Fore.RED + "Error fetching data. Please try again.")
            self.data = None

    def air_pollution_level(self, aqi):
        """Determine air quality based on AQI"""
        try:
            aqi = int(aqi)
        except:
            return "Unknown"
        if 0 <= aqi <= 50:
            return 'Good'
        elif 51 <= aqi <= 100:
            return 'Moderate'
        elif 101 <= aqi <= 150:
            return 'Unhealthy for Sensitive Groups'
        elif 151 <= aqi <= 200:
            return 'Unhealthy'
        elif 201 <= aqi <= 300:
            return 'Very Unhealthy'
        else:
            return 'Hazardous'

    def get_full_info(self):
        return self.data

    def get_aqi_info(self):
        return f"AQI: {self.data['aqi']} ({self.data['air_pollution_level']})" if self.data else "No data available"

    def get_temperature_info(self):
        return f"Temperature: {self.data['temperature']}°C" if self.data else "No data available"

    def get_humidity_info(self):
        return f"Humidity: {self.data['humidity']}%" if self.data else "No data available"

    def speak_info(self):
        """Speak information"""
        if not self.data:
            print(Fore.RED + "No data available to speak.")
            return
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        message = (f"The AQI in {self.data['city']} is {self.data['aqi']} quality {self.data['air_pollution_level']}. "
                   f"The temperature is {self.data['temperature']} degrees Celsius and the humidity is {self.data['humidity']} percent.")
        engine.say(message)
        print(message)
        engine.runAndWait()

    def print_formatted_info(self, info_type):
        """Print formatted information with emojis"""
        if info_type == "full":
            info = self.get_full_info()
            if info is not None:
                print(Fore.CYAN + "=" * 35)
                print(Fore.GREEN + f"🌍 City: {info['city']}")
                print(Fore.YELLOW + f"💨 AQI: {info['aqi']} ({info['air_pollution_level']})")
                print(Fore.MAGENTA + f"🌡 Temperature: {info['temperature']}°C")
                print(Fore.BLUE + f"💧 Humidity: {info['humidity']}%")
                print(Fore.CYAN + "=" * 35)
            else:
                print(Fore.RED + "No data available.")
        elif info_type == "aqi":
            print(Fore.YELLOW + f"💨 {self.get_aqi_info()}")
        elif info_type == "temperature":
            print(Fore.MAGENTA + f"🌡 {self.get_temperature_info()}")
        elif info_type == "humidity":
            print(Fore.BLUE + f"💧 {self.get_humidity_info()}")
        else:
            print(Fore.RED + "Invalid information type.")

    def get_all_json_data(self):
        if self.raw_data:
            return self.raw_data
        else:
            return Fore.RED + "No raw data available."

    def print_show_all_json_data(self):
        if self.raw_data:
            print(Fore.GREEN + "===== Raw API Data =====")
            print(json.dumps(self.raw_data, indent=4, ensure_ascii=False))
            print(Fore.GREEN + "========================")
        else:
            print(Fore.RED + "No raw data available.")

def terminal_mode():
    city_list = {
        "1": "tehran",
        "2": "varamin",
        "3": "mashhad",
        "4": "esfahan",
        "5": "shiraz",
        "6": "tabriz",
        "7": "karaj",
        "8": "rasht",
        "9": "ahvaz",
        "10": "bushehr"
    }
    print(Fore.CYAN + "City List:")
    for key, city in city_list.items():
        print(Fore.GREEN + f"{key}. {city.capitalize()}")
    city_choice = input(Fore.YELLOW + "Enter city number or city name: ").strip()

    if city_choice in city_list:
        city = city_list[city_choice]
    else:
        city = city_choice

    aq = AirQualityData(city)
    if aq.data is None:
        print(Fore.RED + "Failed to retrieve data for the city. Exiting terminal mode.")
        return

    while True:
        print(Fore.CYAN + "\nChoose an option:")
        print(Fore.GREEN + "1. Get full information")
        print(Fore.YELLOW + "2. Get AQI")
        print(Fore.MAGENTA + "3. Get temperature")
        print(Fore.BLUE + "4. Get humidity")
        print(Fore.CYAN + "5. Audio output")
        print(Fore.GREEN + "6. Show all json data")
        print(Fore.YELLOW + "7. Change city")
        print(Fore.RED + "0. Exit")

        choice = input(Fore.YELLOW + "Enter option: ").strip()
        print('\n  ')
        if choice == "1":
            aq.print_formatted_info("full")
        elif choice == "2":
            aq.print_formatted_info("aqi")
        elif choice == "3":
            aq.print_formatted_info("temperature")
        elif choice == "4":
            aq.print_formatted_info("humidity")
        elif choice == "5":
            aq.speak_info()
        elif choice == "6":
            aq.print_show_all_json_data()
        elif choice == "7":
            return terminal_mode()
        elif choice == "0":
            print(Fore.GREEN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Try again.")




def gui_mode():
    

    def get_bg_color(aqi_level):
        """ تعیین رنگ بر اساس سطح آلودگی """
        levels = {
            'Good': '#A8E6CF',
            'Moderate': '#FFD3B6',
            'Unhealthy for Sensitive Groups': '#FFAAA5',
            'Unhealthy': '#FF8B94',
            'Very Unhealthy': '#FF6F69',
            'Hazardous': '#FF3F34',
        }
        return levels.get(aqi_level, '#CCCCCC')

    def animate_color_change(target_color):
        current_color = info_frame.cget("background")
        steps = 20
        for i in range(steps):
            time.sleep(0.01)
            new_color = "#" + "".join([
                hex(int((int(current_color[j:j+2], 16) * (steps - i) + int(target_color[j:j+2], 16) * i) / steps))[2:].zfill(2)
                for j in (1, 3, 5)
            ])
            info_frame.configure(background=new_color)
            root.update()

    def get_air_quality():
        """ دریافت اطلاعات شهر و نمایش داخل کادر """
        city = city_entry.get().strip()
        nonlocal aq_instance
        aq_instance = AirQualityData(city)

        if aq_instance.data:
            target_color = get_bg_color(aq_instance.data['air_pollution_level'])
            animate_color_change(target_color)
            info_text.set(f"🌍 City: {aq_instance.data['city']}\n"
                          f"💨 AQI: {aq_instance.data['aqi']} ({aq_instance.data['air_pollution_level']})\n"
                          f"🌡 Temperature: {aq_instance.data['temperature']}°C\n"
                          f"💧 Humidity: {aq_instance.data['humidity']}%")
        else:
            messagebox.showerror("❌ Error", "Failed to retrieve data!")

    def speak_data():
        """ خواندن اطلاعات با صدای صوتی """
        if aq_instance and aq_instance.data:
            try:
                aq_instance.speak_info()
            except Exception as e:
                messagebox.showerror("❌ Error", f"Speech error: {e}")
        else:
            messagebox.showwarning("⚠️ Warning", "No data available!")

    # ====== طراحی رابط گرافیکی ======
    root = tk.Tk()
    root.title("🌍 Air Quality App")
    root.geometry("640x460")
    root.configure(bg="#1E1E2E")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14, "bold"), padding=10)
    style.configure("TLabel", font=("Arial", 13), background="#1E1E2E", foreground="white")
    style.configure("TFrame", background="#1E1E2E")

    main_frame = ttk.Frame(root, padding=20, style="TFrame")
    main_frame.pack(expand=True, fill="both")

    ttk.Label(main_frame, text="🌀 Welcome to Air Quality App", style="TLabel",
              font=("Arial", 16, "bold")).pack(pady=10)

    ttk.Label(main_frame, text="🌍 Enter City Name:", style="TLabel").pack(pady=5)
    city_entry = ttk.Entry(main_frame, font=("Arial", 14))
    city_entry.pack(pady=5)

    btn_frame = ttk.Frame(main_frame, style="TFrame")
    btn_frame.pack(pady=10)

    ttk.Button(btn_frame, text="✅ Get Data", style="TButton", command=get_air_quality).pack(side="left", padx=10)
    ttk.Button(btn_frame, text="🔊 Speak", style="TButton", command=speak_data).pack(side="right", padx=10)

    info_text = tk.StringVar()
    info_frame = tk.Frame(main_frame, bg="#2E2E3E", bd=3, relief="ridge")
    info_frame.pack(pady=20, fill="both", expand=True)

    info_label = tk.Label(info_frame, textvariable=info_text, bg="#2E2E3E", fg="white",
                          font=("Consolas", 14, "bold"), justify="left", padx=15, pady=15)
    info_label.pack(fill="both", expand=True)

    aq_instance = None
    root.mainloop()


