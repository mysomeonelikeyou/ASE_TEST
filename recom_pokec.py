import networkx as nx
import pandas as pd
import sys
from operator import itemgetter
import math




def prediction(G,u,v):

	
	try:
		common_nei = []
		sum = 0
		for node in list(nx.common_neighbors(G, u, v)):
			#print(nx.degree(G,node))
			if nx.degree(G,node) > 0:
				de = abs(nx.degree(G,node))
				log = 1/math.log(de)
				sum = sum + log
		return sum

	except:
		return 0


	'''
	Which could also be implemented using the funciotn: adamic_adar_index
	try:
		preds = nx.adamic_adar_index(G,[(u,v)])
		for u,v,p in preds:
			return p
	except:
		return 0
	'''



	

def cal_degree_f(G):

	degree_dict = {}
	degree_sorted = []

	degree_sorted_1 = []
	degree_sorted_2 = []
	degree_sorted_3 = []

	count1 = 0
	count2 = 0
	count3 = 0

	num = nx.number_of_nodes(G)
	sub_num_1 = int(0.01 * num)
	sub_num_2 = int(0.1 * num)
	sub_num_3 = int(0.25 * num)

	for node in nx.nodes(G):
		x = len(list(nx.all_neighbors(G,node)))
		if x > 0:
			degree_dict[node] = x

	for key, value in sorted(degree_dict.items(), key = itemgetter(1), reverse = True):
		degree_sorted.append(key)

	# top 1%
	for i in range(0,sub_num_1):
		degree_sorted_1.append(degree_sorted[i])


	# top 10%
	for i in range(0,sub_num_2):
		degree_sorted_2.append(degree_sorted[i])


	# top 25%
	for i in range(0,sub_num_3):
		degree_sorted_3.append(degree_sorted[i])


	df = pd.read_csv('id_gender.csv', header = None, names = ['node','gender'],dtype={'node':int,'gender':int})

	for i in range(0,len(df)):

		if df.node[i] in degree_sorted_1:
			if df.gender[i] == 0:
				count1 = count1+1
				#print(count1)
		if df.node[i] in degree_sorted_2:
			if df.gender[i] == 0:
				count2 = count2+1

		if df.node[i] in degree_sorted_3:
			if df.gender[i] == 0:
				count3 = count3+1

	f1 = count1/len(degree_sorted_1)
	f2 = count2/len(degree_sorted_2)
	f3 = count3/len(degree_sorted_3)

	return f1, f2, f3




def cal_f_r(recommended):

	rwealth_dict = {}
	rwealth_sorted = []


	rwealth_sorted_1 = []
	rwealth_sorted_2 = []
	rwealth_sorted_3 = []


	count11 = 0
	count12 = 0
	count13 = 0

	for node in recommended:
		x = recommended.count(int(node))
		if x > 0:
			rwealth_dict[node] = x


	num = len(recommended)
	sub_num_1 = int(0.01 * num)
	sub_num_2 = int(0.1 * num)
	sub_num_3 = int(0.25 * num)

	for key, value in sorted(rwealth_dict.items(), key = itemgetter(1), reverse = True):
		rwealth_sorted.append(key)

	# top 1%
	for i in range(0,sub_num_1):
		rwealth_sorted_1.append(rwealth_sorted[i])


	# top 10%
	for i in range(0,sub_num_2):
		rwealth_sorted_2.append(rwealth_sorted[i])


	# top 25%
	for i in range(0,sub_num_3):
		rwealth_sorted_3.append(rwealth_sorted[i])




	df = pd.read_csv('id_gender.csv', header = None, names = ['node','gender'],dtype={'node':int,'gender':int})

	for i in range(0,len(df)):

		if df.node[i] in rwealth_sorted_1:
			if df.gender[i] == 0:
				count11 = count11+1
				#print(count1)
		if df.node[i] in rwealth_sorted_2:
			if df.gender[i] == 0:
				count12 = count12+1

		if df.node[i] in rwealth_sorted_3:
			if df.gender[i] == 0:
				count13 = count13+1

	f_r1 = count11/len(rwealth_sorted_1)
	f_r2 = count12/len(rwealth_sorted_2)
	f_r3 = count13/len(rwealth_sorted_3)

	return f_r1, f_r2, f_r3






def prepower(G):

	G_pre = nx.Graph()
	G_pre = nx.read_edgelist('predict_edges.csv', delimiter=',', nodetype=int)

	pre = 0

	sum = 0


	for node in nx.nodes(G_pre):

		if node in nx.nodes(G):

			for neighbor in list(nx.all_neighbors(G_pre,int(node))):

				if neighbor in list(nx.all_neighbors(G,int(node))):

					pre = pre + 1

			sum = sum + len(list(nx.all_neighbors(G,node)))


	power = pre/sum

	return power














def main():



	predict_nodes = []
	nonneigh = []
	predict = []
	#i = 0
	recommended = []
	u = []
	v = []

	explored = []




	G = nx.Graph()

	#G = nx.read_edgelist('graph_edges.csv', delimiter=',', nodetype=int)
	#print(G)
	G = nx.read_edgelist('soc-pokec-relationships.txt', nodetype=int)

	


	df = open('pre_nodes.csv', 'r')
	for line in df.readlines():
		print(line)
		predict_nodes.append(line)

	df.close()





	
	for node in predict_nodes:

		if node in explored:
			continue
		
		print(node)

		#print(node)
		n = predict_nodes.count(node)
		print(n)
		
		explored.append(node)
		
		#p_max = 0
		#pred_link = None
		dict_p = {}
		sorted_link = []

		

		for node_G in nx.nodes(G):

			
			if node_G not in list(nx.all_neighbors(G,int(node))):
				
				p = prediction(G, int(node), node_G)

				dict_p[node_G]=p

				
		for key, value in sorted(dict_p.items(), key = itemgetter(1), reverse = True):
				sorted_link.append(key)

		for i in range(0,n):
			if sorted_link is not None:
				print(int(node),sorted_link[i])
				u.append(int(node))
				v.append(sorted_link[i])
				recommended.append(sorted_link[i])
				#print(u,v)
		#print(recommended)

			




		#print(pre_link)


		#write the edges, write csv
	raw_data = {"u":u,"v":v}
	df2 = pd.DataFrame(raw_data)

	df2.to_csv('predict_edges_pokec.csv', columns=['u','v'],header = None, index = None)
		#write the predicted edges

	f1,f2,f3 = cal_degree_f(G)
	f_r1,f_r2,f_r3 = cal_f_r(recommended)
	fairness_score = abs(f_r1 - f1) + abs(f_r2 - f2) + abs(f_r3 - f3)

	predict_power = prepower(G)

	print("fairness_score",fairness_score)
	print("predict_power",predict_power)







if __name__ == "__main__":

	main()


