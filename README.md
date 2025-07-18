# Flask Exam Score App

This is a simple Flask application that demonstrates basic routing, form handling, and API endpoint creation. The app allows users to submit exam scores, calculates the average, and redirects to a pass/fail page based on the result. It also includes a simple API endpoint for calculation.

## Features

- **Home Page**: Welcome message at `/`
- **Index Page**: Additional welcome at `/index`
- **Pass/Fail Routing**: 
  - `/success/<int:score>` — Displays a success message with the score
  - `/fail/<int:score>` — Displays a fail message with the score
- **Form Submission**: 
  - `/form` — Submit scores for Maths, Science, and History; calculates the average and redirects accordingly
- **API Endpoint**: 
  - `/api` — Accepts JSON data, adds two numbers, and returns the result

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install dependencies:
    ```bash
    pip install flask
    ```

### Running the Application

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage

### Exam Form

- Visit `/form` to enter your scores for Maths, Science, and History.
- The app will calculate the average and redirect you to either the success or fail page.

### API Endpoint

- Send a POST request to `/api` with a JSON body:
    ```json
    {
      "a": 10,
      "b": 20
    }
    ```
- The response will be the sum of `a` and `b`.

## Project Structure

```
app.py
templates/
    form.html
README.md
```
## Author

PrachiVedant
