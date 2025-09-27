from pasha.powermod import PowerManager

pm = PowerManager()

print(pm.set_power(100))      # Güç 100 olarak ayarlandı.
print(pm.get_power())         # Mevcut güç: 100
print(pm.unpower(30))         # Güç 30 azaltıldı. Yeni güç: 70

# Proje Yapısı:
# pasha-powermod/
# ├── pasha/
# │   └── powermod/
# │       ├── __init__.py
# │       └── core.py
# ├── setup.py
# ├── pyproject.toml (pasha TOML modified)
# └── README.md

# Kurulum:
# pip install pasha.powermod

# Veya manuel:
# git clone https://github.com/yourusername/pasha.powermod.git
# cd pasha.powermod
# pip install .

# core.py:
class PowerManager:
def __init__(self):
self.power = 0

    def set_power(self, amount):
        try:
            self.power = int(amount)
            return f"Güç {self.power} olarak ayarlandı."
        except ValueError:
            return "Geçersiz sayı!"

    def get_power(self):
        return f"Mevcut güç: {self.power}"

    def unpower(self, amount):
        try:
            amount = int(amount)
            self.power -= amount
            return f"Güç {amount} azaltıldı. Yeni güç: {self.power}"
        except ValueError:
            return "Geçersiz sayı!"

# __init__.py:
from .core import PowerManager

# setup.py:
from setuptools import setup, find_packages

setup(
name='pasha.powermod',
version='0.1.0',
description='Basit bir güç yönetimi modülü',
author='Pasha',
author_email='pasha@example.com',
packages=find_packages(),
install_requires=[],
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)

# pyproject.toml:
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
