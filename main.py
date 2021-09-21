import numpy as np
import datetime
import csv


#=================== Object docotr ============================
# dr_level: 0 - pgy1
#			1 - pgy2
#			2 - r1
#			3 - r2
#			4 - r3
#			5 - r4
# 			6 - r5
#			7 - r6
class Doctor :
	def __init__(self, dr_level, dr_id):
		self.point = 8 - dr_level;
		self.id = dr_rd;

#	point = 5;
	def get_point(self):
		return self.point;

	def get_id(self):
		return self.id;



#==============================================================


#=================== Object WorkingDay ========================
class WorkingDay :
	def __init__(self, date):
		if( date.weekday() > 4): #Monday is 0
			self.count = 2;
		else:
			self.count = 1;
		self.arr = np.zeros(5) # The array is for jobs scheduling => needs to filled with dr's id
		self.date = date
				
		
#==============================================================

dr_list = list();
workingDay_list = list();

def parseCSV(filename):
	# here to read the file and do the parsing
#	dr_list.append(Doctor()) # Todo: fill the dr info
	d1 = datetime.date(2021, 9, 1);
	d2 = datetime.date(2021, 9, 30);
	delta = d2 - d1
	for i in range(delta.days + 1):
		d_tmp = d1 + datetime.timedelta(days=i)
		workingDay_tmp = WorkingDay(d_tmp)
		print("date: %s, weekday: %d, count %d, jobs %s" % (d_tmp, d_tmp.weekday(), workingDay_tmp.count, workingDay_tmp.arr))

# create the working day list
def createWDList(year, month):
	ndays = (datetime.date(year, month+1, 1) - datetime.date(year, month, 1)).days
	d1 = datetime.date(year, month, 1)
	d2 = datetime.date(year, month, ndays)
	delta = d2 - d1

	print("year=%d, month=%d, ndays=%d" %(year, month, ndays))
	for i in range(ndays):
		workingDay_list.append(WorkingDay(d1+datetime.timedelta(days=i)))
	for item in workingDay_list:
		print ("item.date :%s, item.count:%d" %(item.date, item.count))
	
#print(workingDay_list)


def main():
#	dr = Doctor(3);
	td = WorkingDay(datetime.date.today());
	wend = WorkingDay(datetime.datetime(2021,9,19));
#	print (dr.get_point());
	print (datetime.date.today().weekday());
	print (datetime.datetime(2021,9,20).weekday());
	print ("today has %d count" % td.count)
	print ("2021.9.19 has %d count" % wend.count)
	print (td.arr)
	parseCSV(None)
	createWDList(2021,9)

# main function starts here
main();


