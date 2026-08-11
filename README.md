# Campus Connect ML

A Machine Learning project designed to connect students by matching their skills, interests, and academic profiles. It provides personalized student recommendations, generates icebreakers for networking, identifies isolated students, recommends mentors, and clusters students into groups.

## Features

- **Student Recommendation:** Recommends connections based on vector similarity.
- **Match Explanation & Icebreakers:** Explains why two students match and generates icebreaker messages to start conversations.
- **Clustering & Grouping:** Groups students into clusters using ML techniques and labels clusters by top skills.
- **Isolation Detection:** Identifies isolated students who may need engagement.
- **Mentor Matching:** Recommends mentors based on a student's profile.
- **Graph Network:** Builds a network graph to visualize student connections.

## Project Structure

- `data/`: Contains student data in JSON format (`students.json`).
- `src/`: Source code modules for ML logic:
  - `preprocess.py`: Data loading and corpus preparation.
  - `vectorize.py`: Text vectorization.
  - `recommend.py`: Recommendation engine.
  - `cluster.py`: Clustering algorithms.
  - `analyze.py`: Isolation detection.
  - `explain.py`: Match explanation logic.
  - `icebreaker.py`: Icebreaker generation.
  - `mentor.py`: Mentor matching logic.
  - `graph.py`: Graph network building.
- `main.py`: Main entry point to run all features.
- `requirements.txt`: Python dependencies.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment (optional but recommended).
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script to see all the features in action for a test user:

```bash
python main.py
```
