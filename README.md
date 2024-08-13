# OSM API Test Project
This project is designed to automate the testing of the website [OSM API](https://api.openstreetmap.org/api/0.6) using pytest. 

API documentation: https://wiki.openstreetmap.org/wiki/API_v0.6

## Project Structure

tests:
- test_osm_api_get.py: Test for get method
- test_osm_api_put.py: Test for put method
- test_osm_api_delete.py: Test for delete method

helpers:
- utils.py: Different helper functions
- logger.py: Logging functionality
- http_methods.py: HTTP methods functionality (GET, PUT, DELETE)

logs/: Logs dirrectory

parameters.json: File with main input parameters

conftest.py: Pytest configuration and fixtures

pytest.ini: Pytest configuration file

README.md: Project documentation

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- pytest
- requests

### Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

## Running the Tests
### Using PyCharm
1. Open the project in PyCharm.
2. Configure pytest as your test runner.
3. Run the tests using the Run button or through the pytest configuration.

### Using Command Line
1. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
2. Run all tests:

   ```bash
   pytest -s -v 
   
3. Run a specific test file:

   ```bash
   pytest tests/test_osm_api_get.py
   
## Project Features

### Structured and Modular Test Suite:
The tests are organized modularly, making it easy to maintain and extend the test suite. Each module is responsible for testing specific functionalities of the OSM API, ensuring clear task separation.
### Parameterized Tests:
Parameterized tests are used to test various API parameters, allowing multiple scenarios to be tested with minimal code duplication.
### Fixture-based Setup:
Pytest fixtures are utilized for setting up the testing environment and cleaning up after tests, ensuring that the tests are isolated and predictable.

## Adding New Tests

To add new tests:

- Create a new test file in the tests/ directory.
- Define your test functions, starting with test_.
- Use existing page objects or create new ones in the pages/ directory.
- Use pytest fixtures to manage setup and teardown as needed.
