NBA Statistics App 🏀
Welcome to the NBA Statistics App! This project is dedicated to all basketball enthusiasts who live and breathe the game of basketball, just like me. 🌟

Project Overview
The NBA Statistics App is a web application that provides real-time statistics for NBA players. Whether you're curious about LeBron James' latest triple-double, Kevin Durant's shooting percentage, or Giannis Antetokounmpo's rebounding numbers, this app has got you covered! 📊

Tech Stack
Python: Flask framework for building the backend API.
Web Scraping: Beautiful Soup for scraping player statistics from the NBA website.
Docker: Containerization of the application for easy deployment.
Kubernetes (K8s): Helm charts used to deploy and manage the application on Kubernetes clusters.
Why This Project?
As a passionate fan of NBA basketball, I often find myself checking player stats and game analytics. This project was born out of my love for the game and the desire to create a user-friendly app that fellow basketball fans can enjoy. Whether you're a casual fan or a die-hard supporter, this app aims to provide quick access to the latest player performance metrics, making it a slam dunk for all NBA enthusiasts! 🏀📈

How to Use
Installation:

Ensure Docker is installed on your system.
Clone this repository.
Building the Docker Image:

bash
Copy code
docker build -t orgam/NBA-statistics .
Running the Application:

bash
Copy code
docker run -p 5000:5000 orgam/NBA-statistics
Accessing the Application:

Open your web browser and go to http://localhost:5000.
Use endpoints like http://localhost:5000/stats/<player_name> to retrieve specific player statistics.
Deployment with Helm:

Ensure Kubernetes is set up and Helm is installed.
Customize values.yaml for your deployment.
Deploy using Helm:
bash
Copy code
helm install nba-stats-app ./nba-stats-app
Contributing
Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to fork the repository and submit a pull request. Let's make this app even more awesome together! 🚀

Contact
Have questions or suggestions? Feel free to reach out:

Email: your.email@example.com
Twitter: @yourhandle
LinkedIn: Your Name
License
This project is licensed under the MIT License - see the LICENSE file for details.

