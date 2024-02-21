# Flight Tracker

Flight Tracker is a Python project that helps users find the best flight deals from a specified departure city to various destinations. It fetches flight data, compares prices against user-defined thresholds, and sends email notifications for flights that meet the criteria.

## Features

- **Data Management**: Integrates with Google Sheets (or any data source) to manage flight destinations and price thresholds.
- **Flight Search**: Utilizes the Kiwi.com Tequila API to search for flights and fetch flight data.
- **Notifications**: Sends email notifications for flight deals that meet or beat price thresholds.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- A Kiwi.com Tequila API key
- Access to a Google Sheets document for managing flight data (optional)
- An SMTP server or service for sending emails (configured for Gmail by default)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/FlightTracker.git
   ```
2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables for sensitive information, including your Kiwi.com API key and email credentials:
   - `FLIGHT_API_KEY`: Your Kiwi.com Tequila API key.
   - `MY_EMAIL`: Your email address for sending notifications.
   - `MY_EMAIL_PASS`: Your email password or app-specific password.

## Configuration

- Update the `DataManager` class to point to your data source for managing destinations and price thresholds.
- Ensure the `FlightSearch`, `FlightData`, and `NotificationManager` classes are configured with your API key and email settings.

## Usage

Run the main script to start tracking flight prices and sending notifications:

```
python main.py
```
