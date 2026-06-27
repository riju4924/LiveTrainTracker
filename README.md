# 🚆 Live Train Tracker

A Python-based web application that tracks the live running status of Indian Railways trains using the RailRadar API.

## Features

- 🚆 Search train by train number
- 📍 Live train status
- 🚉 Current station
- ➡️ Next station
- ⏱️ Delay information
- 🚄 Train speed
- 🛤️ Complete route
- 📅 Journey information
- 📱 Streamlit web interface

## Tech Stack

- Python
- Streamlit
- Requests
- Python-dotenv
- RailRadar API

## 🔑 Getting a RailRadar API Key

This project uses the **RailRadar API** to fetch live train running status.

Follow these steps to get your own API key:

1. Visit the RailRadar Developer Portal:
   https://railradar.in

2. Create a free account or log in.

3. Navigate to the API documentation:
   https://railradar.in/docs

4. Generate or copy your API key from your developer dashboard.

5. Create a `.env` file in the project root directory.

6. Add your API key to the `.env` file:

```env
API_KEY=YOUR_RAILRADAR_API_KEY
```

> **Important**
>
> - Never commit your `.env` file to GitHub.
> - Never share your API key publicly.
> - The `.gitignore` file already excludes the `.env` file from version control.

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LiveTrainTracker.git
```

### Navigate to the project

```bash
cd LiveTrainTracker
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```text
API_KEY=YOUR_RAILRADAR_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

## Author

Mrinmoy Mukherjee