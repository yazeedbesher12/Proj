#### First Read The Requirments file to understand what you want . 

# Featrues 
- Create notes
- List notes
- Read one note
- Update notes
- Delete notes
- Create tasks
- List tasks
- Mark tasks as done or not done
- Delete tasks

# Setup 
 - Create a virtual environment : 

 ```powershell 
 python -m venv .venv 
 .venv\Scripts\Activate.ps1

 - pip install -r requirments.txt
 ``` 

# Create a .env File 
 - DATABASE_URL = "Your DataBase Link"

# Run the App : 
uvicorn app.main:app --reload

# Open Api Docs : 
 - http://127.0.0.1:8000/docs

 
