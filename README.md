✈️ TravelPilot
Intelligent Agentic Trip Planning & Real-Time Disruption Management System
TravelPilot is a production-grade, agentic AI application built to move beyond static travel planning. Powered by LangGraph and Streamlit, TravelPilot dynamically constructs personalized itineraries for any city worldwide, monitors for real-time travel disruptions (e.g., attraction closures, scheduling conflicts), and instantly replans itineraries while keeping track of budgets and audit logs.
✨ Key Features
🌍 Universal City Planning: Enter any city in the world—TravelPilot automatically fetches or dynamically generates top landmarks, cultural spots, and dining experiences.
🧠 Multi-Step Agentic Reasoning: Built on LangGraph, utilizing state-driven workflow nodes for requirements parsing, route optimization, cost calculation, and conflict resolution.
⚡ Disruption Management Simulator: Simulates real-world trip interruptions (e.g., sudden venue closures) and seamlessly executes replacement lookups and replanning in real-time.
📊 Comprehensive Cost Breakdown: Tracks budget allocation dynamically across Transport/Flights, Hotels/Accommodation, Activities, and Food & Dining.
🔍 Transparent Agent Audit Logs: View step-by-step reasoning logs explaining every decision made by the agent during initial planning and disruption handling.
🔌 Multi-LLM Support: Easily switch between OpenAI, Google Gemini, or an offline Mock Model using simple .env flags.
🏗️ Architecture & Workflow
                     ┌──────────────────────────┐
                     │    User Inputs (UI)      │
                     │  (City, Budget, Dates)   │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │    Streamlit Frontend    │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │   LangGraph Orchestration│
                     └────────────┬─────────────┘
                                  │
           ┌──────────────────────┼──────────────────────┐
           ▼                      ▼                      ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Requirements    │    │  Smart Planner   │    │ Budget Optimizer │
│  & City Parser   │    │  & Landmark Gen  │    │  & Cost Calculator│
└──────────┬───────┘    └──────────┬───────┘    └──────────┬───────┘
           │                      │                      │
           └──────────────────────┼──────────────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │  Generated Itinerary     │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │   Disruption Engine      │
                     │   (Simulate & Replan)    │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │ Final Dynamic Itinerary  │
                     │  + Live Reasoning Log    │
                     └──────────────────────────┘


📁 Project Structure
travelpilot/
├── app.py                   # Streamlit interactive web application
├── run.py                   # One-click environment check & execution launcher
├── requirements.txt         # Project dependencies
├── .env                     # Environment configuration (API Keys & Providers)
├── agent/
│   └── graph.py             # LangGraph state graph & workflow node definitions
├── services/
│   ├── planner.py           # Dynamic city planner & landmark generator
│   ├── llm_service.py       # Multi-provider LLM gateway (OpenAI, Gemini, Mock)
│   └── optimizer.py         # Itinerary route & activity optimizer
├── tools/
│   └── disruption_tool.py   # Disruption simulation & alternative lookup tool
├── utils/
│   ├── dates.py             # Date range utilities
│   └── helpers.py           # JSON dataset loaders and helpers
└── data/
    ├── destinations.json    # Curated destination database
    └── activities.json      # Structured activity dataset


🚀 Quick Start & Installation
Prerequisites
Python 3.10 or higher installed on your system.
1. Installation
Clone or navigate into your project repository, then run the installation command:
py -m pip install -r requirements.txt


2. Environment Configuration
Create a .env file in the root directory of the project (you can base it on .env.example):
# Choose your provider: 'mock', 'openai', or 'gemini'
LLM_PROVIDER=mock

# Optional API Keys (Required only if LLM_PROVIDER is set to openai or gemini)
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here


💻 Running the Application
You can launch the application in two ways:
Option A: Using the Automatic Launcher Script (Recommended)
This script checks all required packages and starts the server automatically:
python run.py


Option B: Running Streamlit Directly
py -m streamlit run app.py


After starting, Streamlit will open the interactive dashboard in your default browser at http://localhost:8501.
🛠️ Tech Stack
Frontend Dashboard: Streamlit
Agent Orchestration: LangGraph & LangChain Core
Data Handling: Pandas, Pydantic
Environment Management: python-dotenv
📝 License
This project is open-source and built for demonstration and hackathon evaluation purposes.
