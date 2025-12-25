from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
rg = KNeighborsRegressor()
parameter ={
    "n_neighbor":np.arange(1,20),
    "weights":["uniform", "distance"],
    "metric":["euclidean","mahattan","minkowski"]
}
girdCV = GridSearchCV(estimator=rg,param_grid=parameter,cv=5)