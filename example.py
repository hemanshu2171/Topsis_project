import pandas as pd
import math
import csv
from topsis import Topsis
import sys
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s {%(pathname)s:%(lineno)d}  %(name)s - %(message)s')
logger = logging.getLogger(__name__)
args = sys.argv[1:]
def mapper(val):
	if val == '+':
		return True
	else:	return False
if len(args)>3:
    string="More arguments are passed than expected.\nPass only filename as argument"
    sys.exit(string)
try:
	filename = args[0]
	weight = [int(x) for x in args[1].split(',')]
	print(args[2])
	impacts = list(map(mapper,args[2].split(',')))
	# data = pd.read_excel(r'data.xlsx').to_csv(r'data.csv',header=True,index=None)
	data = pd.read_csv(filename)
	rss = 0
	min_dict = {}
	max_dict = {}
	s_plus_dict = {}
	s_minus_dict = {}
	t= Topsis(data,weight,impacts)
	rank,perf_list=t.calc()
	headers = (list(data.columns))
	headers.append('Performance Score')
	headers.append("Rank")
	output = open('output.csv','w')
	writer = csv.writer(output)
	writer.writerow(headers)
	for i in range(len(data.index)):
	  val_arr = list(data.iloc[i,:])
	  val_arr.append(perf_list[i])
	  val_arr.append(rank[i])
	  writer.writerow(val_arr)
except Exception as e:
    logger.error(e)