# Data-Driven Gym Environmental Monitoring Framework

This repository contains the implementation files for my bachelor thesis project on gym environmental monitoring.

## Project Overview
This project uses an SHT31 sensor, Arduino UNO, and Python-based logging to collect indoor temperature and relative humidity data in a gym environment. The collected data are used for preliminary thermal comfort-related analysis based on Effective Temperature (Teff).

## Files
- `sketch_apr16a.ino` — Arduino code for reading SHT31 sensor data
- `read_sht31.py` — Python script for serial data logging
- `temperature_humidity_log.csv` — sample logged dataset
- `temp_0421.png` — temperature plot
- `rh_0421.png` — relative humidity plot

## Notes
The current implementation focuses on real-time sensing, data logging, and preliminary analysis. Short-term forecasting and HVAC control are treated as future extensions.
