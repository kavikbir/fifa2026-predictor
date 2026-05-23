# FIFA 2026 Predictor Model

A modern machine learning model and backend service for predicting outcomes, player stats, and team dynamics for the FIFA World Cup 2026.

## Project Structure

```text
fifa2026-predictor/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD pipelines
├── backend/
│   ├── api/                # API routers, dependency injections
│   ├── models/             # Request/Response schemas, database models
│   ├── services/           # Business logic and ML model invocation
│   ├── tests/              # Test suite
│   ├── __init__.py         # Package initialization
│   └── main.py             # FastAPI entrypoint
├── data/
│   └── raw/                # Raw dataset files (ignored in git)
├── docs/                   # Documentation files
├── frontend/               # Frontend user interface
├── ml/
│   ├── data/               # ML processed data (ignored)
│   └── models/             # Trained ML model weights / serializations
├── .env.example            # Environment configuration template
├── .gitignore              # Git ignored files
├── README.md               # Project documentation
└── requirements.txt        # Python dependency list
```

## Getting Started

### Prerequisites
- Python 3.10 or higher
- `pip` or another package manager (e.g., `poetry`, `conda`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "fifa26 predictor model"
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure environment variables**:
   ```bash
   copy .env.example .env
   ```
   *(Or `cp .env.example .env` on macOS/Linux)*

### Running the Backend

Start the FastAPI development server with reload support:
```bash
python -m uvicorn backend.main:app --reload
```

The application will be accessible at `http://localhost:8000`.
- Interactive API Documentation (Swagger): `http://localhost:8000/docs`
- Alternative Documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

- `GET /` - Root status and API metadata
- `GET /health` - API health and version check

## Testing

Run tests using `pytest`:
```bash
pytest
```
