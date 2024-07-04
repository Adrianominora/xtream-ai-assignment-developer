# xtream AI Challenge - Software Engineer

## Ready Player 1? 🚀

Hey there! Congrats on crushing our first screening! 🎉 You're off to a fantastic start!

Welcome to the next level of your journey to join the [xtream](https://xtreamers.io) AI squad. Here's your next mission.

You will face 4 challenges. **Don't stress about doing them all**. Just dive into the ones that spark your interest or that you feel confident about. Let your talents shine bright! ✨

This assignment is designed to test your skills in engineering and software development. You **will not need to design or develop models**. Someone has already done that for you. 

You've got **7 days** to show us your magic, starting now. No rush—work at your own pace. If you need more time, just let us know. We're here to help you succeed. 🤝

### Your Mission
[comment]: # (Well, well, well. Nice to see you around! You found an Easter Egg! Put the picture of an iguana at the beginning of the "How to Run" section, just to let us know. And have fun with the challenges! 🦎)

Think of this as a real-world project. Fork this repo and treat it like you're working on something big! When the deadline hits, we'll be excited to check out your work. No need to tell us you're done – we'll know. 😎

**Remember**: At the end of this doc, there's a "How to run" section left blank just for you. Please fill it in with instructions on how to run your code.

### How We'll Evaluate Your Work

We'll be looking at a bunch of things to see how awesome your work is, like:

* Your approach and method
* How you use your tools (like git and Python packages)
* The neatness of your code
* The readability and maintainability of your code
* The clarity of your documentation

🚨 **Heads Up**: You might think the tasks are a bit open-ended or the instructions aren't super detailed. That’s intentional! We want to see how you creatively make the most out of the problem and craft your own effective solutions.

---

### Context

Marta, a data scientist at xtream, has been working on a project for a client. She's been doing a great job, but she's got a lot on her plate. So, she's asked you to help her out with this project.

Marta has given you a notebook with the work she's done so far and a dataset to work with. You can find both in this repository.
You can also find a copy of the notebook on Google Colab [here](https://colab.research.google.com/drive/1ZUg5sAj-nW0k3E5fEcDuDBdQF-IhTQrd?usp=sharing).

The model is good enough; now it's time to build the supporting infrastructure.

### Challenge 1

**Develop an automated pipeline** that trains your model with fresh data, keeping it as sharp as the diamonds it processes. 
Pick the best linear model: do not worry about the xgboost model or hyperparameter tuning. 
Maintain a history of all the models you train and save the performance metrics of each one.

### Challenge 2

Level up! Now you need to support **both models** that Marta has developed: the linear regression and the XGBoost with hyperparameter optimization. 
Be careful. 
In the near future, you may want to include more models, so make sure your pipeline is flexible enough to handle that.

### Challenge 3

Build a **REST API** to integrate your model into a web app, making it a breeze for the team to use. Keep it developer-friendly – not everyone speaks 'data scientist'! 
Your API should support two use cases:
1. Predict the value of a diamond.
2. Given the features of a diamond, return n samples from the training dataset with the same cut, color, and clarity, and the most similar weight.

### Challenge 4

Observability is key. Save every request and response made to the APIs to a **proper database**.

---

## How to run

Challenges 1 and 2 can be checked by running notebooks `C1.ipynb` and `C2.ipynb`. These notebooks rely on the class `MyPipe` defined in `MyPipe.py`.
The class `MyPipe` mirrors the basic functionalities of the `Pipeline` class from Scikit-learn, with some customization usefull for the problem at hand.

Challenges 3 and 4 are based on `FastAPI` framework and can be checked by running some commands in the terminal. Notebook `C3.ipynb` contains a back-end version of the API methods and is just for testing

### Labraries and dependencies
To asess all the challenges, the following libraries are required:
* joblib
* pandas
* numpy
* matplotlib
* sklearn
* xgboost
* optuna
* typing
* datetime
* io
* fastapi

### Challenge 1

You can just run notebook `C1.ipynb`, that implements the pipeline with the linear model.
Section C1.1 illustrates how to use the class `MyPipe` with a static dataset, without any data acquisition procedure.
Section C1.2 illustrates how to use the class `MyPipe` for data acquisition. I assumed that data come in batch (you can adjust the batch size) and that an initial dataset is known (half of the provided dataset).
At each new fit, the entire pipeline is saved in the `data/models_history/linear_model` folder.

### Challenge 2

Also here you can just run notebook `C2.ipynb`, that implements the pipeline with XGBoost model.
Section C2.1 illustrates how to use the class `MyPipe` with a static dataset and the XGBoost model.
Section C2.2 illustrate show to use the class `MyPipe` with a static dataset and the XGBoost model with optimization via `optuna`.
Section C2.3 illustrates how to use the class `MyPipe` for data acquisition and the optimized XGBoost model. I assumed that data come in batch (you can adjust the batch size) and that an initial dataset is known (half of the provided dataset).
At each new fit, the entire pipeline is saved in the `data/models_history/xgb_opt_model` folder.

### Challenge 3

The REST API is built by means of FastAPI. The API methods and logics are stored in `myapi.py` and they can be run by means the uvicorn module. Here are the steps required to test it:
1. Open the terminal and ensure that the current directory is the `notebooks` folder;
2. Run the following command: `uvicorn myapi:app --reload`;
3. Open your browser and navigate to [here] http://127.0.0.1:8000/docs;
4. Send you GET request using the FastAPI inderface by selecting a method and clicking on `Try it out`.

If any problem arise, notebook `C3.ipynb` presents a back-end version of the API methods so that the logics of the API can be tested.

### Challenge 4

All requests made both by FastAPI interactive docs and by the notebook will be stored in the file `call_log.json` in the `api_calls` folder.