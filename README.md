# 🎯 SceneSolver

SceneSolver is an AI-powered forensic tool designed to analyze and solve crime scenes through advanced image processing and text generation. It uses a Python Flask backend for processing and a React + Vite frontend for a smooth user experience.

🚀 **Live Demo:** [https://scenesolver-omega.vercel.app](https://scenesolver-omega.vercel.app)

---

## 📦 Tech Stack

- **Frontend:** React + Vite + TypeScript
- **Backend:** Python (Flask)
- **AI Models:** Object Detection, Scene Description, Text Generation
- **Deployment:** Vercel (Frontend), Render/Other (Backend)

---

## 🏗️ Project Structure

SceneSolver/
│
├── backend/ # Flask Backend
│ ├── app.py # Flask App Entry
│ ├── models/ # AI Model Scripts
│ └── ...
│
├── frontend/ # React + Vite Frontend
│ ├── src/ # React Components, Pages, Styles
│ ├── public/
│ └── ...
│
├── README.md # Project Documentation (this file)
└── ...


---

## ⚙️ Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/Abhinav777-77/SceneSolver.git
cd SceneSolver
2. Backend Setup (Flask)
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt

python app.py
The backend will start at http://127.0.0.1:5000/.

3. Frontend Setup (React + Vite)
bash
Copy
Edit
cd ../frontend
npm install
npm run dev
The frontend will start at http://localhost:5173/.

🌐 Live Deployment
Service	Platform	URL
Frontend	Vercel	https://scenesolver-omega.vercel.app
Backend	Render / Other	(Your backend deployment URL here)

🧪 Features
Upload crime scene images for AI analysis

Object Detection & Scene Identification

Auto-generated Forensic Text Reports

Fast & Responsive React + Vite Frontend

Easy-to-extend Flask Backend with AI Models

📝 Usage Workflow
Open the web app.

Upload or select a crime scene image.

The backend processes the image and generates predictions & reports.

Results are displayed on the frontend dashboard.

💡 Technologies Used
Flask (REST API for AI models)

React + Vite (Fast Frontend)

AI Models (CLIP, Gemini API, Object Detection Models, etc.)

Python Libraries: torch, transformers, flask, etc.

✅ Contributing
We welcome contributions! Here’s how you can help:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes.

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

📜 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

👤 Author
Developed by Abhinav777-77

📬 Contact
For any queries, issues, or collaborations, please open an issue on this repository.
