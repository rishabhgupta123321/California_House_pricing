### California_House_pricing Prediction

### Software and Tools Requirements

1. [Github Account](https://github.com/)
2. [Heroku Account](https://www.heroku.com/) 
3. [VSCode IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)



Create a new environment on CMD (Command Prompt) terminal

``` If any other environment is already activate, so first deactivate that with command```          **deactivate**   ``` then --     ```


``` 
    For Standard Python Environment:     
        python -m venv env
    For Conda Environment:
        conda create -p venv python=3.13.7 -y  
```


Activate the environment 

```
    For Standard Python Environment:
        env\Scripts\activate
    For Conda Environment:
        conda activate env       
```

<br>

#### Change the Kernal of Linear_Regression_ML_Implementation.ipynb to the Active Environment 
``` According to Standard Python we have to select env(Python 3.13.7) ```


<br> 


#### Installation of Libraries:

1. Create a `requirements.txt` file and add all the necessary libraries.  
   ⚠️ **Important:** Use `scikit-learn` instead of `sklearn` when installing, but while importing in your Python code, use `sklearn`. This is the convention set by the library maintainers.

2. Run the following command in the terminal:

```cmd
pip install -r requirements.txt
```

```Note: The -r flag tells pip to read from the requirements.txt file.```



<br> 
 

### Setting up Git

To set up Git, you need to configure two things: **username** and **user email**.  

If you haven’t set these up yet, or want to change them, run:

```cmd
git config --global user.name "YourName"
git config --global user.email "YourEmail"
```

```
Note: The email must match the one you used for your GitHub account. You can change the name freely, but changing the email to something not associated with your GitHub account will prevent commits from linking to your profile.
```
If you’ve already set them up and just want to check:

```cmd
git config --global user.name
git config --global user.email
```

``This configuration we have to do just first time and after that we don't need to do, okay`` 
<br> 


### Series of Steps need to follow for commit the code to github: 
1. First, if you don't know then direct you can also go to the documentation of the git CLI and take a look on that
2. For add the specific file just write the command -    ``git add requirements.txt``
    or , if you want to add all files in one go, just write the command - `` git add . `` 
3. Then if you want to see, the status of files , just write - `` git status `` and will able to see that how many are modified and how many are untracked files and how many are on stage .

`The modified files will be, those are added already to git but after that modified they will come in the modified status of git`

`` So far we have added all the files that need to be commited to the repository `` 

4. Now, we need to do the `commit`, where commit basically pushes the code or files from the out local to the staging environment.
