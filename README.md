# AI Road Trip Planner

This project is a **Streamlit-based AI planner** that helps users create road trips with multiple travel modes such as **car, walking, biking, bus, or train**. It leverages **Azure OpenAI LLM** to interpret natural language queries, generates route plans, and displays them on an interactive **Folium map**.

## Features
- Plan trips with **multiple stops**  
- Choose travel mode: **Car, Walking, Biking, Bus, Train**  
- Get **optimized routes** and travel distance/time estimates  
- **Interactive Folium map** showing route lines and waypoints  
- AI-assisted trip planning using **LLM** to parse natural language queries  
- Adjustable starting point and destination  

## How It Works
1. User enters a query like:  
   `'Plan a road trip from Los Angeles to San Francisco with stops in Santa Barbara and Monterey by car'`  
2. The **LLM interprets** the query to identify:  
   - **Start location**  
   - **Destination**  
   - **Intermediate stops**  
   - **Travel mode** (car, walking, biking, bus, train)  
3. The app fetches route data using:  
   - **OpenRouteService API** (or similar routing API)  
   - **Geopy** for geocoding locations  
4. Displays the route on a **Folium map** with:  
   - **Polyline routes**  
   - **Markers for stops**  
   - Popups with **names, addresses, and Google Maps links**  

## Getting Started

### Prerequisites
- Python 3.10+  
- Streamlit  
- Folium  
- Requests  
- Geopy  
- Azure OpenAI access key & endpoint  
- OpenRouteService API key  

### Installation
 `git clone <YOUR_REPO_URL>`
 
 `cd <REPO_FOLDER>`
 
 `pip install -r requirements.txt`

### Run the App
`streamlit run roadtrip_planner.py`

## Project Structure
- `roadtrip_planner.py # Main Streamlit app`
- `requirements.txt # Python dependencies`
- `README.md # Project documentation`

## Environment Variables
Set your API keys inside the script or as environment variables:  
- **AZURE_OPENAI_KEY** → Your Azure OpenAI API Key  
- **AZURE_OPENAI_ENDPOINT** → Your Azure OpenAI Endpoint  
- **OPENROUTESERVICE_KEY** → Your OpenRouteService API Key  

## Tech Stack
- **Python**  
- **Streamlit** → Web interface  
- **Folium** → Interactive maps  
- **Geopy** → Geocoding (location → coordinates)  
- **Requests** → API calls  
- **Azure OpenAI GPT-4** → Query interpretation  
- **OpenRouteService API** → Route planning for multiple travel modes  

## Example Queries
- `'Plan a bike trip from UCLA to Santa Monica Pier with a stop at Venice Beach'`  
- `'Create a walking tour from Times Square to Central Park with 3 scenic stops'`  
- `'Plan a train route from San Jose to Sacramento'`  
- `'Road trip from San Francisco to Las Vegas with stops in Yosemite and Death Valley by car'`  

## License
This project is licensed under the **MIT License**.  
