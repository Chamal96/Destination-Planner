
---

# Destination Planner

Plan your dream getaway effortlessly using AI! This project harnesses the power of Large Language Models (LLMs) and integrated APIs to create personalized travel itineraries—including weather updates, tourist spots, hotel options, and currency conversions.

## ✨ Key Features

* **Smart Trip Planning**: Understands natural language inputs for destinations, travel dates, number of travelers, budgets, and more.
* **Live Weather Forecasts**: Retrieves real-time and future weather conditions for any location.
* **Attraction Recommendations**: Suggests must-visit places using Google Places and Tavily Search.
* **Hotel Finder**: Recommends accommodations tailored to your preferences and location.
* **Currency Converter**: Converts budgets into local currencies using real-time exchange rates.
* **User-Friendly Interface**: Built with Streamlit for smooth and interactive user experience.
* **Powerful Backend**: FastAPI handles all backend operations and API serving efficiently.

## 🚀 Tech Stack

### **Backend (Python - FastAPI)**

* `FastAPI`: High-performance API framework.
* `LangChain`: LLM-powered application framework.
* `LangGraph`: Manages multi-agent workflows with LLMs.
* `LangChain Community`: Connects to external services like Google.
* `Groq`: Ultra-fast inference engine for LLMs.
* `Pydantic`: For data validation and schema enforcement.
* `Requests`: Handles HTTP calls to third-party APIs.
* `python-dotenv`: Manages environment variables securely.

### **Frontend (Python - Streamlit)**

* `Streamlit`: Lightweight tool for creating beautiful ML web apps.

### **External APIs**

* `WeatherAPI`: Fetches current and forecast weather.
* `Google Places API`: Locates attractions and hotels.
* `Tavily Search`: AI-optimized search for fallback retrieval.
* `ExchangeRate-API`: Provides live currency exchange rates.

---

## ⚙️ Setup Guide

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Chamal96/Destination-Planner.git
cd Destination-Planner
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` or `config.py` and add the following keys:

```env
# WeatherAPI
WEATHER_API_KEY="your_key_here"
WEATHER_BASE_URL="http://api.weatherapi.com/v1"

# Google Places API
GOOGLE_PLACES_API_KEY="your_key_here"
GOOGLE_PLACES_BASE_URL="https://maps.googleapis.com/maps/api/place"

# Tavily Search API
TAVILY_API_KEY="your_key_here"

# ExchangeRate-API
EXCHANGE_RATE_API_KEY="your_key_here"
EXCHANGE_RATE_BASE_URL="https://v6.exchangerate-api.com/v6"

# Groq
GROQ_API_KEY="your_key_here"
LLM_MODEL_NAME="llama3-8b-8192"
TEMPERATURE=0.7
```

---

## ▶️ Run the Application

### Start the FastAPI Backend

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

This launches the backend server at [http://localhost:8000](http://localhost:8000).

### Launch the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

This opens the app in your browser at [http://localhost:8501](http://localhost:8501).

---

