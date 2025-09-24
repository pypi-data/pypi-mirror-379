TElectric
Simple and practical libraries for performing basic electrical calculations using Ohm's law and common electrical formulas.
* Installation
pip install TElectric
If you had the setup.py file : 
pip install -e .
* Example 
import TElectric

power = TElectric.power(current=5, voltage=220)
print(power)

Output: 1100
* Project structure 
TElectric/
├── TElectric/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_core.py
├── README.md
├── setup.py
└── LICENSE
* License 
This project is released under the MIT license. See the LICENSE file for more information.