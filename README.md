# PineVox Analytics Dashboard

```{=html}
<p align="center">
```
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb)
![Render](https://img.shields.io/badge/API-Render-46E3B7)

Interactive analytics dashboard for visualising and exploring Call
Detail Record (CDR) data through a secure FastAPI backend.

```{=html}
</p>
```

------------------------------------------------------------------------

# Overview

The PineVox Analytics Dashboard is a Streamlit application that provides
an interactive interface for analysing call activity, operational
performance and regional trends.

Unlike traditional dashboards that process data locally, all business
logic and analytics are retrieved from a secured FastAPI backend through
authenticated REST API requests. Users authenticate using JWT
credentials before accessing protected dashboard resources.

------------------------------------------------------------------------

# Features

-   Secure JWT authentication
-   Interactive filtering
-   KPI overview cards
-   Call activity trends
-   Call performance analytics
-   Cost analytics
-   Regional insights
-   Paginated call records
-   Responsive layout
-   Backend-driven analytics
-   Automatic logout when authentication expires

------------------------------------------------------------------------

# Dashboard Architecture

``` text
                 User
                  │
                  ▼
          Streamlit Dashboard
                  │
        HTTPS + Bearer JWT
                  │
                  ▼
          FastAPI REST API
                  │
                  ▼
            MongoDB Atlas
```

------------------------------------------------------------------------

# Technology Stack

  Technology      Purpose
  --------------- ----------------------------
  Python          Application language
  Streamlit       Dashboard framework
  Plotly          Interactive visualisations
  Pandas          Data processing
  Requests        REST API client
  FastAPI         Backend API
  MongoDB Atlas   Database
  Render          Backend hosting

------------------------------------------------------------------------

# Dashboard Sections

## Overview

Displays high-level KPIs including:

-   Total Calls
-   Total Cost
-   Average Duration
-   Success Rate
-   Active Cities

## Activity Trends

Interactive charts showing:

-   Calls per Hour
-   Calls per Day

## Call Performance

Visualisations include:

-   Duration Distribution
-   Duration vs Cost
-   Longest Call
-   Shortest Call
-   Average Duration

## Cost Performance

Displays:

-   Total Cost
-   Average Cost per Call
-   Highest Call Cost
-   Cost by City
-   Cost by Duration

## Regional Insights

Compare call activity across cities.

## Recent Calls

Paginated Call Detail Record table supporting backend filtering.

------------------------------------------------------------------------

# Authentication Flow

``` text
User Login
     │
     ▼
Streamlit Login Page
     │
     ▼
POST /auth/login
     │
     ▼
Receive JWT
     │
     ▼
Store Token in Session State
     │
     ▼
Authenticated API Requests
     │
     ▼
Dashboard Data
```

------------------------------------------------------------------------

# Project Structure

``` text
analytics_dashboard/
│
├── api/
├── charts/
├── data/
├── sections/
├── utils/
├── config.py
├── app.py
└── requirements.txt
```

------------------------------------------------------------------------

# Installation

``` bash
git clone <repository-url>
cd analytics_dashboard
python -m venv .venv
```

Activate the environment.

Windows:

``` bash
.venv\Scripts\activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Environment Variables

Create a `.env` file.

``` env
API_URL=http://127.0.0.1:8000
```

For deployment, configure:

``` text
API_URL=https://your-render-api.onrender.com
```

------------------------------------------------------------------------

# Running the Dashboard

``` bash
streamlit run app.py
```

The application is available at:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

# Deployment

The dashboard is deployed to Streamlit Community Cloud.

Configuration includes:

-   API URL stored as a secret
-   Automatic GitHub deployments
-   Secure communication with the FastAPI backend

------------------------------------------------------------------------

# Screenshots

Add screenshots of:

-   Login Page
-   Dashboard Overview
-   Activity Trends
-   Cost Performance
-   Regional Insights

------------------------------------------------------------------------

# Backend API

This dashboard consumes the companion FastAPI backend using
authenticated REST requests.

The backend provides:

-   JWT authentication
-   RBAC
-   Analytics endpoints
-   Metadata endpoints
-   Paginated CDR endpoints

------------------------------------------------------------------------

# Future Improvements

-   Dark/light theme enhancements
-   Export dashboard reports
-   Additional analytics
-   User profile management
-   Refresh token support
-   Caching for improved performance
-   Docker deployment

------------------------------------------------------------------------

# Author

**Mathew Meisinger**

Software Engineer \| Data Analyst \| AI Enthusiast
