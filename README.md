# Talent API 🚀

##  📖 Description
Talent API is a scalable and robust RESTful API designed to streamline talent management processes for organizations. 

## 🛠️ Installation
Clone the repository:
```
git clone https://github.com/your-username/project-name.git
cd project-name
```
Set up a virtual environment: (if needed, you can run without virtual env as well)
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Configure environment variables:
```
cp .env.example .env
```
update your configuration details (e.g., API keys, database URIs).


## 🚀 Usage
Start the Flask server:
```
python run.py
```
Access the application: Open your browser and navigate to http://127.0.0.1:8080

Get profile API: (get request)

http://127.0.0.1:8080/profile/{wallet Address}

## 🧪 Testing
Run the test suite to ensure everything works as expected:

```
python -m unittest discover -s tests
```

## 💬 Contact
For questions or support, reach out to:

Your Name: anubnair90@gmail.com

GitHub: https://github.com/anubnair

## Recommendations for Storing Data and Improving Performance:

#### 1. Storing Results in a Database

For persistent storage and better management of the fetched profiles, it is recommended to store the results in a database. This will allow you to:

- Easily manage large volumes of profile data.
- Implement better data retrieval and querying capabilities.
- Ensure data integrity by persisting profiles between requests.
- Note: Talent profile also doenot update profile always,
so can have a timestamp, and update the profile data once in a month or so 

You can think of integrating any relational (e.g., PostgreSQL, MySQL) or NoSQL (e.g., MongoDB, Cassandra, dynamoDB) database depending on your needs.

### 2. Using Caching (Redis) for Faster Profile Fetching

To improve performance and speed up profile fetching, especially if you are frequently accessing the same profiles, it is recommend introducing a caching layer such as **Redis**. Caching will allow you to:

- Retrieve profiles much faster by reducing the need to repeatedly fetch data from external APIs or databases.
- Lower the load on external services and databases.
- Improve scalability and response times.