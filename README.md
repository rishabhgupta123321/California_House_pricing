# California House Pricing Prediction
<br>

## Software and Tools Requirements

1. [GitHub Account](https://github.com/)  
2. [Heroku Account](https://www.heroku.com/)  
3. [VSCode IDE](https://code.visualstudio.com/)  
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)  

---
<br>

## Create a New Environment  

Open **CMD (Command Prompt) in VsCode terminal** and create a new Python environment.  

👉 If another environment is already active, deactivate it first:  
```cmd
deactivate
```


Then create a new one:

``` 
    For Standard Python Environment:     
        python -m venv env
    For Conda Environment:
        conda create -p venv python=3.13.7 -y  
```
<br>

## 🚀 Activate the Environment

```
    For Standard Python Environment:
        env\Scripts\activate
    For Conda Environment:
        conda activate env       
```
---

<br>

## 📒 Jupyter Notebook Kernel Setup

Change the kernel of ``Linear_Regression_ML_Implementation.ipynb`` to the active environment.

For example, if you created a standard Python environment, select:
```cmd 
env (Python 3.13.7)
```
---
<br>

## 📦Installation of Libraries

1. Create a ``requirements.txt`` file and add all the necessary libraries.

⚠️ Important:
- When installing, use:

```
scikit-learn
```

- When importing in Python code, always use:

```python
import sklearn
```
(This is the convention defined by the maintainers.)


2. Install the libraries: 

```cmd 
pip install -r requirements.txt 
```

| Note: The `-r` flag tells pip to read and install dependencies from the `requirements.txt` file.

--- 
<br>

## 🔧 Git Configuration

Before pushing code, configure Git with your name and email.

```cmd 
git config --global user.name "YourName"
git config --global user.email "YourEmail"
```
### ⚠️ Note:

* The email must match your GitHub account email, otherwise commits won’t link to your profile.

* You can freely change your name, but changing the email to something not connected to GitHub breaks commit linking.

To verify:
```cmd 
git config --global user.name
git config --global user.email
```

| This setup is typically done only once. After that, no need to reconfigure unless you change accounts. 

--- 

<br>

## 📝 Workflow: Commit and Push Code to GitHub

### Step 1: Initialize Git
```cmd 
git init 
``` 

--- 

### Step 2: Add Remote or Clone Repository
#### Option A: Clone an existing repository
#### Copy the HTTPS URL from GitHub → run:

```cmd 
git clone <repo_url>
```

#### Option B: Add a remote to an existing local repo
```cmd 
git remote add origin <repo_url>
```

| The `.git` at the end of the URL is optional. It’s just a convention.  

--- 
### Step 3: Verify Remote
```cmd 
git remote -v
```

---
### Step 4: Add Files to Staging
- Add a specific file:
```cmd 
git add requirements.txt
```
* Add all files:
```cmd 
git add .
```

---
### Step 5: Check Status
```cmd 
git status
``` 

- Modified files → already tracked but changed

- Untracked files → new files not yet added

- Staged files → ready to commit

---

### Step 6: Commit Changes
```cmd 
git commit -m "Your commit message"
```
---
### Step 7 (Optional): Rename Branch
```cmd 
git branch -M <branch_name>
``` 
--- 
### Step 8: Push Code to GitHub
```cmd 
git push -u origin main
```
| The `-u` flag sets the upstream branch. After the first push, you can simply use:
```cmd 
git push
```
Without `-u`, you’d always need to specify `origin main`.
--- 

### ✅ That’s it! Your code is now committed and pushed to GitHub.

---
<br>


## Git Flow

1. Edit files
2. Stage changes: (Bring all on the stage)
```cmd
   git add .
```
3. Commit snapshot locally: (save in local system)
```
git commit -m "your message" 
```
4. Push to GitHub: (push to github via orgin repo_url)
```cmd
git push origin main
```

--- 
<br>

## 🚀 Creating a Flask Web Application


### Project Structure

- All backend logic is in `app.py`

- Two model-related files are used:

    - `california_housing_model.pkl`

    - `scaling.pkl`

- A folder named `templates/` contains the frontend:

    -  `home.html`

- An API endpoint `/predict_api` is implemented in `app.py`

--- 
<br>

### Steps to Run the App

#### 1. Check Virtual Environment
   Make sure you are inside your virtual environment (`env`).

#### 2. Run Flask App

```cmd
python app.py
```
This will give a local server link like:
`http://127.0.0.1:5000`

#### 3. Access via Browser

- Go to `http://127.0.0.1:5000` → loads `home.html`

- Go to `http://127.0.0.1:5000/predict_api` → calls the prediction API (not fully functional via browser, requires Postman).



--- 


## 🔧 Using Postman for Prediction

#### 1. Download & Open Postman

#### 2. Create a New Request

    - Select POST method
    - Enter the URL (example)
    
    http://127.0.0.1:5000/predict_api  (as a example)

    - Go to Body → raw → JSON

#### 3. Send JSON Data

    Example input:
    {
    "data": {
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveRooms": 6.98412698,
        "AveBedrms": 1.02380952,
        "Population": 322.0,
        "AveOccup": 2.55555556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
}

#### 4. Click Send
    - You’ll receive the model’s prediction as output.
    - This helps verify whether the model is performing correctly.

--- 


<br>

## Project Overview

```
So far, we have created an API endpoint called `predict_api` that handles POST requests.  
We used **Postman** to send data to this API, where the input data is processed through **StandardScaler** for normalization.  
The scaled data is then passed to our **regression model**, which generates and returns the prediction as output.
```


--- 
<br>


## Updates Made  

- Added a `/predict` route in **app.py** to:  
  - Process form inputs  
  - Scale the data  
  - Run the regression model  
  - Return predictions  

- Updated **home.html** with a form to collect user inputs:  
  - MedInc  
  - HouseAge  
  - AveRooms  
  - AveBedrms  
  - Population  
  - AveOccup  
  - Latitude  
  - Longitude  

- Displayed the prediction result dynamically on the webpage using a placeholder.  
---
<br>


## Next Steps

- Deploy the project to the cloud using **Heroku**    
- Dockerize the application  
- Integrate **GitHub Actions** for CI/CD pipeline automation

  
<br>

---


## Deployment on Heroku

- To deploy the app, we will use **Heroku**.  
- Create a file named **`Procfile`**, which defines the command Heroku will run to start the app.  

- The command to use is: (in Procfile)  
```
  gunicorn app:app
```


- Gunicorn (Green Unicorn) is a pure Python HTTP server for WSGI applications.

    - It allows the app to handle multiple requests concurrently by running multiple worker processes.

- Finally, update the `requirements.txt` file and add `gunicorn` so Heroku installs it during deployment.









