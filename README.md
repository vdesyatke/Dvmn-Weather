# Dvmn-Weather
Devman task project - weather in London, Cherepovets, Sheremetyevo.
Source of weather data is wttr.in

## Installation
0. You need python interpreter installed on your PС. The project is tested on Python 3.10.
1. Clone the project to your PC, details [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Install, run and activate your virtual environment, details [here](https://docs.python-guide.org/dev/virtualenvs/).
3. To install the dependencies, simply run ```pip install -r requirements.txt```.

## Examples of use
```python
>>> python main.py
Лондон

     \  /       Переменная облачность
   _ /"".-.     +6(3) °C
     \_(   ).   ↗ 4 м/c
     /(___(__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Пт. 23 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Partly Cloudy  │               Overcast       │
│  _ /"".-.     +9(6) °C       │      .--.     +5(3) °C       │
│    \_(   ).   ↗ 4-5 м/c      │   .-(    ).   ↗ 2-3 м/c      │
│    /(___(__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
>>> python main.py -h
usage: main.py [-h]

Description: this program prints out Weather in London, Cherepovets, Sheremetyevo

options:
  -h, --help  show this help message and exit
```

## License
This software is licensed under the MIT License - see the [LICENSE](https://github.com/vdesyatke/Dvmn-Weather/blob/master/LICENSE) file for details
