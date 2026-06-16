# Call Data Analytics Dashboard

A Streamlit-based analytics dashboard for monitoring and exploring call detail records (CDRs). The application provides interactive filtering, KPI reporting, operational insights, and visualizations for call activity, performance, costs, and regional trends.

---

## Features

### Interactive Filters

Filter call records by:

- City
- Call Status (Successful / Failed)
- Date Range

### KPI Overview

View high-level metrics including:

- Total Calls
- Total Cost
- Average Call Duration
- Call Success Rate
- Active Cities

### Activity Analytics

Track call activity over time through:

- Calls per Hour
- Calls per Day

### Performance Analytics

Analyze call quality and behavior with:

- Duration Distribution
- Call Duration vs Cost Analysis
- Longest Call
- Shortest Call
- Average Duration
- Total Duration

### Cost Analytics

Monitor spending patterns using:

- Total Call Cost
- Average Cost per Call
- Highest Call Cost
- Average Cost by City
- Total Cost by City
- Cost vs Duration Correlation

### Regional Insights

Compare activity across locations with:

- Call Volume by City

### Recent Call Log

Inspect the latest call records in a searchable tabular view.

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Visualization | Plotly |
| Data Processing | Pandas |
| API Requests | Requests |
| UI Components | streamlit-shadcn-ui |
| Language | Python 3 |

---

## Project Structure

```text
analytics_dashboard/
│
├── app.py
├── helpers.py
├── requirements.txt
│
├── charts/
│   ├── activity.py
│   ├── cost.py
│   ├── performance.py
│   └── regional.py
│
├── data/
│   ├── loader.py
│   └── filters.py
│
└── utils/
    └── metrics.py
```

### Module Responsibilities

#### app.py

Main dashboard application.

Responsible for:

- Loading data
- Rendering filters
- Calculating metrics
- Building visualizations
- Displaying dashboard sections

#### data/loader.py

Handles:

- API retrieval
- Data cleaning
- Type conversions
- Phone number normalization

#### data/filters.py

Contains:

- Filter UI components
- Filtering logic

#### utils/metrics.py

Calculates dashboard KPIs.

#### charts/

Contains chart-generation functions grouped by business domain:

- Activity
- Cost
- Performance
- Regional

#### helpers.py

Reusable UI helpers for:

- KPI cards
- Chart containers
- Section headers
- Plotly theme configuration

---

## Data Source

The dashboard consumes call data from:

```text
https://69b30b45e224ec066bdb55a0.mockapi.io/api/v1/cdr
```

The API returns call detail records containing information such as:

- Caller details
- Receiver details
- Call duration
- Call cost
- Call timestamps
- Call status
- City information

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd analytics_dashboard
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The dashboard will become available at:

```text
http://localhost:8501
```

---

## Data Processing

Before visualization, the application:

### Numeric Conversion

Converts:

- id
- callCost
- callDuration

to numeric formats.

### Datetime Conversion

Converts:

- callStartTime
- callEndTime

to timezone-aware datetime objects.

### Phone Number Cleaning

Normalizes phone numbers by:

- Removing extensions
- Removing non-numeric characters
- Preserving digits only

---

## Dashboard Sections

### Overview

High-level operational KPIs.

### Activity Trends

Visualizes temporal call patterns.

### Call Performance

Analyzes duration characteristics and performance indicators.

### Cost Performance

Tracks spending and cost efficiency.

### Regional Insights

Compares call volume across cities.

### Recent Calls

Displays filtered call records.

---

## Caching

API responses are cached using Streamlit's caching mechanism:

```python
@st.cache_data(ttl=600)
```

Cache duration:

- 10 minutes (600 seconds)

This reduces unnecessary API requests and improves dashboard responsiveness.

---

## Future Improvements

Potential enhancements include:

- Export to CSV/Excel
- Authentication and role-based access
- Real-time streaming updates
- Database-backed storage
- Advanced KPI calculations
- Drill-down analytics
- Geospatial visualizations
- Forecasting and trend analysis
- Automated anomaly detection
