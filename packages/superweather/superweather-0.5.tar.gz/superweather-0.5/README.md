
# 🌍 superweather

A simple and practical tool to retrieve Air Quality Index (AQI), temperature, humidity, and pollution level for various cities — with both terminal and graphical (GUI) interfaces.

## ✨ Features

- Fetch air quality data using a global API
- Display AQI, temperature, humidity, and pollution level in a user-friendly way
- Voice output via TTS
- Interactive terminal and graphical user interface (GUI)
- View raw JSON output for developers

---

## 🚀 Installation

```bash
pip install superweather
```

---

## 🧠 Usage

### 📦 Using the `AirQualityData` class

Main class to fetch and process air quality information.

#### 🏗️ Create instance:

```python
from superweather import AirQualityData

aq = AirQualityData("tehran")
```

#### 📋 Main Methods:

| Method | Description |
|--------|-------------|
| `get_full_info()` | Get all data as a dictionary |
| `get_aqi_info()` | Get AQI and its status |
| `get_temperature_info()` | Get current temperature |
| `get_humidity_info()` | Get humidity percentage |
| `get_all_json_data()` | Get full raw API data |
| `print_show_all_json_data()` | Print raw JSON data |
| `print_formatted_info(info_type)` | Print colored info (`full`, `aqi`, `temperature`, `humidity`) |
| `speak_info()` | Speak air quality info aloud |

#### ✅ Example:

```python
aq = AirQualityData("mashhad")
aq.print_formatted_info("full")
aq.speak_info()
json_data = aq.get_all_json_data()

# Use raw json data
if isinstance(json_data, dict):
    pm25 = json_data['data']['iaqi'].get('pm25', {}).get('v', 'N/A')
    print(f"PM2.5: {pm25}")
```

---

## 🖥️ Terminal Interface: `terminal_mode()`

Run the `terminal_mode()` function to interact via a clean command-line interface with a list of cities and features.

### 🔸 Run:

```python
from superweather import terminal_mode

terminal_mode()
```

### Available Options:

1. Full info  
2. AQI only  
3. Temperature only  
4. Humidity only  
5. Voice output  
6. Show raw JSON data  
7. Change city  
0. Exit  

---

## 🪟 Graphical Interface: `gui_mode()`

Use `gui_mode()` for a user-friendly windowed interface.

### 🔸 Run:

```python
from superweather import gui_mode

gui_mode()
```

### GUI Features:

- Enter city name  
- Fetch info with a button  
- Display city, AQI, temperature, humidity  
- Text-to-speech feature  
- Simple and clean design 

---

## 🧰 Use in Other Projects

You can use this module inside your own applications or scripts. The output of `get_all_json_data()` is a full raw dictionary, perfect for extracting specific parameters like PM2.5, CO, etc.

```python
aq = AirQualityData("esfahan")
data = aq.get_all_json_data()

co = data['data']['iaqi'].get('co', {}).get('v', 'N/A')
print(f"CO Level: {co}")
```

---

## 🛠️ Dependencies

- `requests`
- `pyttsx3`
- `colorama`
- `tkinter` (built-in with Python)

---

## 📃 License

MIT

---

## 🙋‍♂️ Author

Made with ❤️ by a developer from Iran.

---

# 🌍 superweather (نسخه فارسی)

ابزاری ساده و کاربردی برای دریافت شاخص کیفیت هوا (AQI)، دما، رطوبت و سطح آلودگی برای شهرهای مختلف — با پشتیبانی از رابط کاربری ترمینال و گرافیکی (GUI).

## ✨ ویژگی‌ها

- دریافت اطلاعات کیفیت هوا از API جهانی
- نمایش AQI، دما، رطوبت و سطح آلودگی به زبان ساده
- خروجی صوتی با استفاده از تبدیل متن به گفتار (TTS)
- رابط تعاملی ترمینال و گرافیکی
- نمایش داده‌های خام JSON برای توسعه‌دهندگان

---

## 🚀 نصب

```bash
pip install superweather
```

---

## 🧠 نحوه استفاده

### 📦 استفاده از کلاس `AirQualityData`

کلاس اصلی برای دریافت و پردازش اطلاعات کیفیت هوا.

#### 🏗️ ساخت نمونه:

```python
from superweather import AirQualityData

aq = AirQualityData("tehran")
```

#### 📋 متدهای اصلی:

| متد | توضیح |
|------|--------|
| `get_full_info()` | دریافت همه اطلاعات به‌صورت دیکشنری |
| `get_aqi_info()` | دریافت الودگی هوا|
| `get_temperature_info()` | دمای فعلی |
| `get_humidity_info()` | درصد رطوبت |
| `get_all_json_data()` | دریافت تمام اطلاعات جیسون |
| `print_show_all_json_data()` | چاپ جیسون کامل در ترمینال |
| `print_formatted_info(info_type)` | نمایش زیبا و رنگی اطلاعات در ترمینال (`full`، `aqi`، `temperature`، `humidity`) |
| `speak_info()` | خواندن اطلاعات به‌صورت صوتی |

#### ✅ مثال:

```python
aq = AirQualityData("mashhad")
aq.print_formatted_info("full")
aq.speak_info()
json_data = aq.get_all_json_data()

# مثال استفاده از json data
if isinstance(json_data, dict):
    pm25 = json_data['data']['iaqi'].get('pm25', {}).get('v', 'N/A')
    print(f"PM2.5: {pm25}")
```

---

## 🖥️ حالت ترمینال: `terminal_mode()`

با اجرای تابع `terminal_mode()` وارد یک رابط تعاملی در ترمینال می‌شوید که لیستی از شهرها و امکانات مختلف را در اختیار کاربر می‌گذارد.

### 🔸 اجرا:

```python
from superweather import terminal_mode

terminal_mode()
```

### امکانات ترمینال:

1. نمایش تمام اطلاعات به صورت رنگی و زیبا  
2. نمایش فقط AQI  
3. نمایش فقط دما  
4. نمایش فقط رطوبت  
5. پخش صوتی اطلاعات  
6. نمایش داده‌ی خام JSON  
7. تغییر شهر  
0. خروج از برنامه

---

## 🪟 حالت گرافیکی: `gui_mode()`

اگر رابط کاربری گرافیکی را ترجیح می‌دهید، می‌توانید از تابع `gui_mode()` استفاده کنید.

### 🔸 اجرا:

```python
from superweather import gui_mode

gui_mode()
```

### امکانات رابط گرافیکی:

- ورود نام شهر دلخواه  
- دکمه دریافت اطلاعات  
- نمایش نام شهر، AQI، دما و رطوبت  
- قابلیت تبدیل متن به گفتار  
- طراحی ساده و کاربرپسند  

---

## 🧰 استفاده در پروژه‌های دیگر

شما می‌توانید از این ماژول در پروژه‌های شخصی خود استفاده کنید. خروجی `get_all_json_data()` یک دیکشنری JSON کامل است که می‌توانید داده‌های خاص مانند PM2.5، CO و... را از آن استخراج کنید.

### مثال:

```python
aq = AirQualityData("esfahan")
data = aq.get_all_json_data()

co = data['data']['iaqi'].get('co', {}).get('v', 'N/A')
print(f"مقدار CO: {co}")
```

---





---

## 🙋‍♂️ نویسنده

ساخته شده با ❤️ توسط یک نو جوان توسعه‌دهنده از ایران.
