import sys
import subprocess
import os

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке {package}: {e}")
        sys.exit(1)

try:
    from sklearn.linear_model import LinearRegression
except ModuleNotFoundError:
    print("Module 'scikit-learn' not found. Installing it now...")
    install("scikit-learn")
    from sklearn.linear_model import LinearRegression

import numpy as np

try:
    from sklearn import __version__
    major_version = int(__version__.split('.')[0])
    if major_version < 1:
        print("Версия scikit-learn устарела. Обновите до версии 1.0 или выше.")
        install("--upgrade scikit-learn")
except Exception as e:
    print(f"Ошибка проверки версии scikit-learn: {e}")
    sys.exit(1)

ad_spend = [10, 20, 30, 40, 50]
sales = [25, 50, 70, 90, 120]

X = np.array(ad_spend).reshape(-1, 1)
y = np.array(sales)

try:
    model = LinearRegression()
    model.fit(X, y)
except Exception as e:
    print(f"Ошибка обучения модели: {e}")
    sys.exit(1)

try:
    new_ad_spend = np.array([[60]])
    predicted_sales = model.predict(new_ad_spend)
    print(f"Прогнозируемые продажи для затрат 60: {predicted_sales[0]:.2f}")
except Exception as e:
    print(f"Ошибка прогнозирования: {e}")
    sys.exit(1)

try:
    print(f"Уравнение модели: y = {model.coef_[0]:.2f} * x + {model.intercept_:.2f}")
except Exception as e:
    print(f"Ошибка получения уравнения модели: {e}")
    sys.exit(1)
