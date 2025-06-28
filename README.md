# 🧠 Real Estate Work

This program is a real estate listing browser that allows users to filter and rank properties based on preferences such as city, price, size, etc. It reads listings from a CSV file with all available properties and allows user to view, sort, and export properties that match their preferences.

## 🚀 Features

- Analyze and display property listings from a CSV file
- Ask users for specific filter crtieria (location, budget, etc.)
- Filter listings based on respective user input
- Option to rank matching properties by value points (price, size, etc.)
- Additional functions such as price per sqft.
- Save filtered and ranked listings to a new CSV file

## 🛠️ Technologies Used

- Python 3
- CSV
- Pandas

## 📁 File Structure

```bash
project-folder/
|
|---Better_1Listings.py              # Main logic of the app
|---Better_Filtering.py             # Helper function to filter listings
|---Better_Ranking.py               # Helper function to rank listings
|---listings.csv             # File to retrieve listings from
|___README.md                # You're reading this!
