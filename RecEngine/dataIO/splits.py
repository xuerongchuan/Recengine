# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
from sklearn.model_selection import KFold


def splitByUser(data_path):
    if not os.path.isfile(data_path):
        print('the format of data path is wrong!')
        sys.exit()
    data = pd.read_csv(data_path, header=None, names=['uid', 'iid', 'rating'])
    user_list = list(data.uid.unique())
    cv1, cv2, cv3, cv4, cv5 = [], [], [], [], []

    for user in user_list:
        res = []
        user_data = data[data.uid == user].reset_index(drop=True)
        kf = KFold(5)
        for train_index, test_index in kf.split(user_data):
            res.append(user_data.iloc[test_index])
        cv1.append(res[0])
        cv2.append(res[1])
        cv3.append(res[2])
        cv4.append(res[3])
        cv5.append(res[4])
    pd.concat(cv1).to_csv('data/cv/data-0.csv', header=False, index=False)
    pd.concat(cv2).to_csv('data/cv/data-1.csv', header=False, index=False)
    pd.concat(cv3).to_csv('data/cv/data-2.csv', header=False, index=False)
    pd.concat(cv4).to_csv('data/cv/data-3.csv', header=False, index=False)
    pd.concat(cv5).to_csv('data/cv/data-4.csv', header=False, index=False)