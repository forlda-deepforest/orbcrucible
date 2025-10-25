# Orbcrucible

A node-based project management tool for the Deepforest Universe, built with FastAPI, Three.js, and Polygonjs. This tool enables visual workflow management using nodes and edges, with a 3D interface for interactive project visualization.

## Features
- **Node-based Workflow**: Manage tasks and dependencies using a graph-based structure.
- **FastAPI Backend**: Provides a high-performance API for node and edge data management.
- **Three.js Frontend**: Renders 3D visualizations of project workflows.
- **Polygonjs Customization**: Allows custom 3D node designs for enhanced interactivity.

## Prerequisites
- Python 3.8+ (for FastAPI backend)
- Node.js 16+ (for Three.js/Polygonjs frontend)
- Git

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/forlda-deepforest/orbcrucible.git
   cd orbcrucible
   ```

2. **Set up Python Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```

3. **Set up Node.js Environment (if frontend is included)**:
   ```bash
   npm install
   ```

4. **Run the Backend**:
   ```bash
   uvicorn src.main:app --reload
   ```
   Access the API at http://localhost:8000.

5. **Run the Frontend (example, to be implemented)**:
   ```bash
   node frontend/index.js
   ```

## Project Structure
```
orbcrucible/
├── src/
│   └── main.py           # FastAPI backend
├── frontend/             # Three.js/Polygonjs frontend (to be added)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignored files (e.g., venv/, node_modules/)
└── LICENSE               # MIT License
```

## Usage

- ** API Endpoints:
   - GET /: Returns a welcome message ({"message": "Welcome to Orbcrucible!"}).
   - More endpoints for node/edge management to be added.

- ** Frontend:
   - 3D visualization of nodes and edges (in development).

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions.

## License
MIT License