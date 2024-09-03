# Modeling-Car-Insurance-Claim-Outcomes

## Project Overview

The objective of this project is to predict car insurance claim outcomes using logistic regression models. By analyzing features such as credit scores, annual mileage, and other relevant data, we aim to determine the most significant factors influencing claim outcomes.

Key Aspects:

Data Preprocessing: Handling missing values and ensuring data is clean for model input.
Exploratory Data Analysis (EDA): Analyzing and visualizing key features that affect insurance claims.
Model Development: Implementing logistic regression models to predict insurance claim outcomes.
Model Evaluation: Evaluating model performance using accuracy, confusion matrices, and other metrics.
Containerization: Encapsulating the project in a Docker container for easy deployment.
Experiment Tracking: Integrating MLflow to track experiments, model versions, and performance metrics.

Features:

Claim Outcome Prediction: Logistic regression models are used to predict whether a car insurance claim will be successful.
Feature Analysis: Identifying the most significant features influencing insurance claim outcomes.
Interactive Visualizations: Graphical representations of data to help understand key trends.
Containerized Environment: Dockerized project for easy setup and deployment.
Experiment Tracking: MLflow is used to manage and track model experiments.


### Prerequisites

To run this project, you'll need to have the following software installed:

- Python 3.9 or higher
- pip (Python package installer)

You can install Python and pip by following the instructions [here](https://www.python.org/downloads/).

### Installing

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/phoenixak/Analyzing-Car-Reviews-with-LLMs](https://github.com/phoenixak/Modeling-Car-Insurance-Claim-Outcomes).git
   cd Modeling-Car-Insurance-Claim-Outcomes

2. **Create a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
Or 

1. **Build the Docker image:**

   ```bash
   docker build -t Modeling-Car-Insurance-Claim-Outcomes .
  
   Run the Docker container:
2. **Run the Docker container:**

   ```bash
   Copy code
   docker run -v "$(pwd)/dataset":/app/dataset -it Modeling-Car-Insurance-Claim-Outcomes

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any feature requests or bugs.




