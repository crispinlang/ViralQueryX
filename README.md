# ViralQueryX

## Overview

This project implements a full-stack web application for querying and exploring a relational biological database.  
The backend is built using Flask and connects to a previously created MySQL database containing viral metadata, genome sequences, protein sequences, and enzyme annotations.

In addition to the web interface, the application exposes a RESTful API that allows database queries to be executed directly via URL parameters and returned in JSON format. This enables both interactive use through a browser and programmatic access for external tools or scripts.

---

## Functionality

The application provides the following core features:

- A unified search interface for querying multiple database tables simultaneously
- Grouped display of search results by table
- Automatic truncation of long biological sequences with expandable “show more / show less” functionality
- Clickable search results that link to a detailed table view
- A RESTful API endpoint for retrieving query results as JSON
- Consistent, reusable page layout and styling across the application
- Configuration via environment variables to support local development and cloud deployment

---

## Technology Stack

### Backend
- Python
- Flask
- Flask-MySQLdb
- Gunicorn

### Database
- MySQL
- Relational schema designed for biological data

### Frontend
- HTML with Jinja2 templating
- CSS for layout and styling
- JavaScript for client-side interactivity

### API
- REST-style GET endpoints
- JSON response format

---

## Project Structure

```text
viralqueryx/
├── app.py                 # Main Flask application and route definitions
├── requirements.txt       # Python dependencies
├── Procfile               # Production entry point for Gunicorn
├── README.md              # Project documentation
├── .env                   # Environment variables (not committed)
│
├── templates/
│   ├── base.html          # Shared page layout and navigation
│   ├── search.html        # Database search interface
│   ├── tables.html        # Detailed table view
│   └── about.html         # Project information page
│
├── static/
│   ├── style.css          # Global styling
│   ├── landing.css        # Landing page styling
│   ├── scripts.js         # JavaScript helpers
│   └── logo.jpg           # Site logo and favicon
│
└── data/
    ├── schema.sql         # Database schema
    └── sample_data.sql    # Optional sample data

The API is intended for integration with analysis pipelines, scripts, or external applications.

---

## Running the Application Locally

1. Clone the repository:
---

## Running the Application Locally

1. Clone the repository:

---

## Skills Demonstrated

This project demonstrates experience in:
- Full-stack web application development
- Backend development with Flask
- Relational database querying and schema design
- REST API design and JSON serialization
- Server-side templating with Jinja2
- Frontend layout and client-side interaction
- Environment-based configuration and deployment readiness
- Structuring maintainable and reusable web applications

---

## Intended Use

This application is suitable as:
- A full-stack development portfolio project
- A foundation for a bioinformatics or data science MSc thesis
- A prototype for database-driven scientific dashboards
- A learning project for RESTful web services and cloud deployment

--- 

## License

This project is intended for educational and research purposes.
