#!/usr/bin python
#encoding: utf-8

from Recommendation import Recommendation
from common.distance import convert_values_normalization

class ItemBasedRecommendation(Recommendation):
	def __init__(self):
		self.user_rating_std = False

	def use_standard_user_rating(self, item_list=[]):
		"""没有评分暂时用None表示，与0区别"""
		all_user = self.get_all_users()
		if item_list==[]:
			item_list = self.get_all_items()
			self.user_rating_std = True

		for x in item_list:
			input_list = []
			for u in all_user:
				if self.user_rating[u].has_key(x):
					input_list.append(self.user_rating[u][x])
				else:
					input_list.append(None)

			normal_value = convert_values_normalization(input_list)
			#            update value
			for i in len(normal_value):
				self.user_rating[all_user[i]][x] = normal_value[i] or None

	def get_slope_one_rec(self, user):
		rec_list = []

		return rec_list


if __name__ == '__main__':

	from data_format.input_format import user_install_record_to_dict

	user_dict = user_install_record_to_dict(file('./input/ml-100k/u.data'), training=False)

	ibr = ItemBasedRecommendation(neighbor=5, user_rating_dict=user_dict, training=False)
	print ibr.user_rating
	ibr.use_standard_user_rating()
	print ibr.user_rating
#	print ibr.get_all_users()
#	print len(ibr.get_all_items(user='123'))
	pass