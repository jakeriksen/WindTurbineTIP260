# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'


import os
import pandas as pd
from windpowerlib.modelchain import ModelChain
from windpowerlib.wind_turbine import WindTurbine
from windpowerlib import wind_turbine as wt



from requests import get

result = get('https://openenergy-platform.org/api/v0/schema/supply/tables/wind_turbine_library/rows')
for row in result.json():
  print(row)


token = input("Input token: ")
