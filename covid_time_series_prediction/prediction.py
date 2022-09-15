import pickle
import pandas as pd
import numpy as np


def predict(X_test,country,data,y):
    
    y_train=y[:(len(y)-15)]
    path = f'/Users/albertogutierrez/code/albgutgam/Teky-Teka/covid_time_series_prediction/covid_time_series_prediction/data/models/model_{country}.pkl'
    #path=f'data/models/model_{country}.pkl'
    #covid_time_series_prediction/covid_time_series_prediction/data/models/model_France.pkl
    
    model=pickle.load(open(path,'rb'))
    X_test_columns=data.drop(columns=['total_deaths','new_cases','new_deaths'])
    X_test_columns.columns
    X_test_df=pd.DataFrame(X_test,columns=X_test_columns.columns)
    X_predict=X_test_df.tail(10)
    X_predict=X_predict.reset_index(drop=True)
    for i in range(1,10):
        X_predict.loc[i,'containment_and_health':'total_boosters']=X_predict.loc[0,'containment_and_health':'total_boosters']
    min_num=min(y)
    max_num=max(y)
    list_pred=[]

    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[0]).T))

    if (y_pred_ < y_train.tail(1).tolist())[0]:
        y_pred_=y_train.tail(1)
        y_pred_2=y_train.tail(1)
    else:
        y_pred_2=y_pred_

    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
   
    for j in range(1,11):
        X_predict.loc[j,f'day-{j}']=y_pred_scale[0]

    y_pred_ = np.round(model.predict(pd.DataFrame(X_predict.loc[1]).T))

    if y_pred_[0] < y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]

    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
    for j in range(2,11):
        X_predict.loc[j,f'day-{j-1}']=y_pred_scale

    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[2]).T))
    
    if y_pred_[0] < y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
    for j in range(3,11):
        X_predict.loc[j,f'day-{j-2}']=y_pred_scale

    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[3]).T))
    
    if y_pred_[0]< y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
    for j in range(4,11):
        X_predict.loc[j,f'day-{j-3}']=y_pred_scale


    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[4]).T))
    if y_pred_[0]< y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
    for j in range(5,11):
        X_predict.loc[j,f'day-{j-4}']=y_pred_scale
    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[5]).T))
    if y_pred_[0]< y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
    for j in range(6,11):
        X_predict.loc[j,f'day-{j-5}']=y_pred_scale


    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[6]).T))
    if y_pred_[0]< y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)

    for j in range(7,11):
        X_predict.loc[j,f'day-{j-6}']=y_pred_scale
    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[7]).T))
    if y_pred_[0]< y_pred_2[0]:
        y_pred_=y_pred_2[0]
    else:
        y_pred_2=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)

    for j in range(8,11):
        X_predict.loc[j,f'day-{j-7}']=y_pred_scale


    y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[8]).T))
    if y_pred_[0]< y_pred_2[0]:
        y_pred_=y_pred_2
    else:
        y_pred_2[0]=y_pred_[0]
    y_pred_scale=((y_pred_)-min_num) / ((max_num)-(min_num))
    list_pred.append(y_pred_)
    
    #for j in range(9,11):
    #    X_predict.loc[j,f'day-{j-8}']=y_pred_scale


    #y_pred_=np.round(model.predict(pd.DataFrame(X_predict.loc[9]).T))
    #if y_pred_[0]< y_pred_2[0]:
     #   y_pred_=y_pred_2[0]
    #else:
    #    y_pred_2=y_pred_[0]
    #list_pred.append(y_pred_)
    return list_pred,X_predict
