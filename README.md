# Social Media Dashboard

This project is a **Social Media Dashboard** built using **Django**. It enables users to view and manage their social media activity from various platforms such as **Twitter** and **Facebook** in one unified interface. The dashboard allows users to interact with their posts, comments, and likes, as well as create new posts, all from a single platform.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles securely.
- **Social Media Integration**: The dashboard fetches data from social media platforms like Twitter and Facebook, displaying posts, likes, comments, and other relevant data.
- **User Interactions**: Users can like, comment, and perform basic interactions on their posts directly from the dashboard.
- **Post Management**: Users can create, view, and manage posts across multiple social media platforms.
- **Responsive Design**: The user interface is designed to be responsive and mobile-friendly.
- **Error Handling**: Graceful error handling with informative messages in case of API issues or data retrieval errors.

## Technologies Used

- **Django**: A high-level Python web framework used for the backend.
- **Bootstrap**: For creating a responsive and user-friendly front-end.
- **Python**: The primary programming language for the backend logic.
- **Social Media APIs**: Integrates with Twitter and Facebook to retrieve and manage social media data.
- **SQLite/MySQL/PostgreSQL**: Database for storing user data and social media interactions.

## Prerequisites

Before you can run this project, ensure that you have the following installed:

- **Python 3.x** (preferably 3.8+)
- **pip** (Python's package installer)
- Social Media API credentials (Twitter API keys, Facebook Developer credentials)

## Installation

### 1. Clone the repository

Clone this repository to your local machine:
git clone https://github.com/<username>/social-media-dashboard.git
cd social-media-dashboard
Set up a virtual environment
Create a virtual environment to manage project dependencies:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install dependencies
Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt
4. Set up API credentials
Twitter: Sign up for a developer account, create an application, and get your API key, secret, access token, and access token secret.

Facebook: Similarly, create a Facebook Developer account, set up an app, and get your credentials.

Add the obtained credentials to your Django settings.py file (or use environment variables for enhanced security).

5. Apply database migrations
Run the migrations to set up the database:
python manage.py migrate
