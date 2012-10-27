#!/usr/bin python
# encoding: utf-8

from common import Martrix
from common.distance import get_manhattan_distance

from conf.conf import *

class Recommendation():
	def __init__(self, nb=neighbor, recommendation=rec_num, user_rating={}, training=False):
		self.n = nb #num
		self.r = recommendation #num
		self.save_type = save_type
		self.cal_type = cal_distance_type
		self.pearson_type = pearson_cal_type
		if not training:
			if self.save_type == "Pickle":
				import pickle
				with file('./inter_data/user_items_rating.dict') as f:
					self.user_rating = pickle.load(f)
		else:
			self.user_rating = user_rating

	def reload_configuration(self):
		"""load configuration XML file"""
		pass

	def get_active_users(self):
		result = []
		# if number of items from one user > 3, consider as active user
		for u in self.get_all_users():
			if len(self.user_rating[u]) >= active_count:
				result.append(u)
		return  result

	def get_all_users(self):
		users = set(self.user_rating.iterkeys())
		return list(users)

	def get_all_items(self):
		items_set = set()
		dict.itervalues()
		for d in self.user_rating.itervalues():
			for item in d.iterkeys():
				items_set.add(item)
		return list(items_set)

	def revert_user_item(self, user_item_pairs={}):
		"""revert user:value pairs, return value:user dict"""
		result = {}
		if len(user_item_pairs):
			for k,v in user_item_pairs.iteritems():
				for item in v:
					if item not in result:
						result[item]=[]
					result[item].append(k)
			return result
		else:
			return self.revert_user_item(user_item_pairs=self.user_rating)

if __name__ == '__main__':
	import os
#	print os.environ['COMPUTERNAME']
	r = Recommendation()
	print r.revert_user_item(r.user_rating)
#	for u in r.get_all_users():
#		print u, r.user_rating[u]
#		break
	pass