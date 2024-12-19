# Intrusion Detection System (IDS) with Python

## Overview

This project implements a basic Intrusion Detection System (IDS) using Python. The system monitors network logs for suspicious activities by analyzing IP addresses and logs alerts when any suspicious activity is detected.

## Features

- **Suspicious IP Detection**: Detects suspicious IP addresses based on a predefined list.
- **Alert Generation**: Creates alerts when suspicious activity is detected and encodes them in base64.
- **Alert Logging**: Saves alerts with timestamps in a `alerts.json` file for further analysis.
- **Real-Time Feedback**: Provides feedback on how many suspicious activities were found.

## Installation

### Prerequisites

- Python 3.x (download from [python.org](https://www.python.org/downloads/))

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/Amine-M07/IntrudeSafe-IDS-with-Python.git
   cd IntrudeSafe-IDS-with-Python
