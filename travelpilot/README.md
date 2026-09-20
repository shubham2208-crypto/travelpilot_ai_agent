# TravelPilot
## Intelligent Trip Planning & Disruption Management Agent

TravelPilot is an agentic AI-powered travel management system that continuously reasons across complete itineraries, detects disruptions, resolves conflicts in real-time, optimizes routes, and manages budgets dynamically.

---

## Architecture Diagram

```text
                USER
                 │
                 ▼
       STREAMLIT DASHBOARD
                 │
                 ▼
        TRAVELPILOT AGENT
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
   Trip Planner Conflict Budget
        │        │        │
        └────────┼────────┘
                 ▼
            DATA / TOOLS
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
   Activities  Hotels  Transport
                 │
                 ▼
          ITINERARY STATE
                 │
                 ▼
       DISRUPTION DETECTOR
                 │
                 ▼
       ALTERNATIVE SEARCH
                 │
                 ▼
              REPLAN
                 │
                 ▼
             VALIDATION
                 │
                 ▼
       UPDATED ITINERARY