# Intrusion Detection System (IDS)

This is a Python-based Intrusion Detection System (IDS) that reads log files, analyzes network activity, and detects suspicious IP addresses.

## Overview

This project implements a basic Intrusion Detection System (IDS) using Python. The system monitors network logs for suspicious activities by analyzing IP addresses and logs alerts when any suspicious activity is detected.

## Features

- **Suspicious IP Detection**: Detects suspicious IP addresses based on a predefined list.
- **Alert Generation**: Creates alerts when suspicious activity is detected and encodes them in base64.
- **Alert Logging**: Saves alerts with timestamps in a `alerts.json` file for further analysis.
- **Real-Time Feedback**: Provides feedback on how many suspicious activities were found.

## Prerequisites

- Python 3.x (download from [python.org](https://www.python.org/downloads/))
- A `network.log` file to analyze (included in the project or generated by a server)

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Amine-M07/IntrudeSafe-IDS-with-Python.git
   cd IntrudeSafe-IDS-with-Python  # Navigate to the project directory

