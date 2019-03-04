# -*- coding: utf-8 -*-
import sys
from models.userCF import UserCF
from models.itemCF import ItemCF
from configs.config import Config
import numpy as np
import time

if __name__ == '__main__':
    config = Config()
    config.rating_cv_path = sys.argv[1]
    config.dataset_name = sys.argv[2]
    config.k_fold_num = int(sys.argv[3])
    model = ItemCF(config)
    rmse_list, mae_list = [], []
    for tmp in range(config.k_fold_num):
        model.init_model(tmp)
        ti = time.time()
        rmse, mae = model.predict_model()
        to = time.time()
        print('消耗时间:',(to-ti))
        rmse_list.append(rmse)
        mae_list.append(mae)
    print('rmse:', np.mean(rmse_list),'\n', 'mae:', \
          np.mean(mae_list))
    print('######################################################################')
    for i in range(1,11):
        print(('# User{:>3} -- Recommended Results -- {:>6}{:>6}{:>6}{:>6}{:>6}#').format(str(i),str(res[i][0]),str(res[i][1]),str(res[i][2]),str(res[i][3]),str(res[i][4])))
    print('######################################################################')
    