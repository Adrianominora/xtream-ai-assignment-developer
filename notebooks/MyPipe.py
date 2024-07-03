import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error

class MyPipe():
    def __init__(self, steps=[('scaler', StandardScaler()),('regression', LinearRegression())]):
        self.steps = steps
        self.history = []
        self.data = None
        self.pipe = Pipeline(steps=self.steps)
    
    def define_data(self, data: pd.DataFrame):
        self.data = data

    def augment_data(self, new_data: pd.DataFrame):
        if not(False in (self.data.columns==new_data.columns)):
            self.data = pd.concat([self.data, new_data], ignore_index=True)
    
    # def make_pipe(self, steps=[('scaler', StandardScaler()),('regression', LinearRegression())]):
    #     self.pipe = Pipeline(steps=steps)

    def fit(self, x, y):
        self.pipe.fit(x,y)
    
    def predict(self, x):
        return self.pipe.predict(x)
    
    def evaluate_performance(self, y_test, y_pred):
        results = {
            "r2": np.round(r2_score(y_test, y_pred), 4),
            "MAE": np.round(mean_absolute_error(y_test, y_pred), 2)
        }
        self.history.append(results)
        return results
        
    def get_history(self):
        return self.history
    
    def get_score(self, x, y):
        return self.pipe.score(x, y)
    
    def plot_history(self, trendline=False):
        df = pd.DataFrame(self.history)
        fig, axs = plt.subplots(2, 1)
        fig.tight_layout()
        axs[0].plot(df['r2'], color='C0')
        axs[0].set_ylabel('r2')
        axs[1].plot(df['MAE'], color='C1')
        axs[1].set_ylabel('MAE')
        for ax in axs:
            ax.grid(True)
            ax.set_xlabel('n')
        if trendline:
            xx = np.arange(len(df.index))
            z1 = np.polyfit(xx, np.array(df['r2']), 1)
            p1 = np.poly1d(z1)
            z2 = np.polyfit(xx, np.array(df['MAE']), 1)
            p2 = np.poly1d(z2)
            axs[0].plot(xx, p1(xx), color='C0', linestyle='--')
            axs[1].plot(xx, p2(xx), color='C1', linestyle='--')