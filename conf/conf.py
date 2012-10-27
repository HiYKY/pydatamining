#!/usr/bin python
#encoding:utf-8

#Basic

neighbor=3
rec_num=3
active_count=5
reverse_weight=0.2

save_type = "Pickle"          #Pickle/Json/Mongo

recommend_type="Hot"        #Hot/Fast/Editor/Scence/Normal
cal_distance_type="Manhattan"
rec_list_prefer = "Pearson"   #Neighbor_count or High_score
pearson_cal_type = "formula"  #formula/normal/cosine

#Extra