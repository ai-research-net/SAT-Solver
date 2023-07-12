# SAT Solver Web Application

This is the web interface for the SAT Solver project. It is built using the [Flask](https://flask.palletsprojects.com/) web framework.

## Getting Started

These instructions will get you a copy of the web application up and running on your local machine for development and testing purposes.

### Prerequisites

To run this application, you will need Python 3 and pip, the Python package installer. You will also need to install the project's dependencies, which are listed in the `requirements.txt` file in the root directory of this repository.

### Installing

1. Navigate to the root directory of this repository and install the necessary Python packages with pip:

    ```bash
    pip install -r requirements.txt
    ```

2. Navigate to the `app` directory:

    ```bash
    cd app
    ```

3. Start the Flask development server:

    ```bash
    export FLASK_APP=routes.py
    flask run
    ```
or 

    ```bash
    python3 app.py
    ```


4. Open your web browser and navigate to `http://localhost:5000` to see the application running.

## Usage

The web application provides an interface for using the SAT Solver. You can upload a `.cnf` file containing a set of clauses, and the application will display a solution.

To use the application:

1. Click the "Choose File" button and select your `.cnf` file.
2. Click the "Upload" button to upload the file and start the solver.
3. The solution will be displayed on the page when it is ready.

Please refer to the [main project README](../README.md) for more information about the SAT Solver project and the structure and syntax of `.cnf` files.
