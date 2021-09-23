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
		self.id = dr_id;

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
		self.jobs = ['']*5#np.zeros(5) # The array is for jobs scheduling => needs to filled with dr's id
		self.date = date
				
		
#==============================================================

dr_list = list();
workingDay_list = list();

def parseCSV(filename):
	# here to read the file and do the parsing
	with open(filename, newline='') as csvfile:
		rows = list(csv.reader(csvfile))
		drDict = dict(zip(rows[1], rows[0]))
		print(drDict)
		for dr_id, dr_level in drDict.items():
			print(dr_id, dr_level)
			dr_list.append(Doctor(int(dr_level),dr_id))
		#print(dr_list)
#	dr_list.append(Doctor()) # Todo: fill the dr info
#	d1 = datetime.date(2021, 9, 1);
#	d2 = datetime.date(2021, 9, 30);
#	delta = d2 - d1
#	for i in range(delta.days + 1):
#		d_tmp = d1 + datetime.timedelta(days=i)
#		workingDay_tmp = WorkingDay(d_tmp)
#		print("date: %s, weekday: %d, count %d, jobs %s" % (d_tmp, d_tmp.weekday(), workingDay_tmp.count, workingDay_tmp.arr))

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

def findDrWithHighestPoint(dr_list):
	highestPoint = 0
	id_of_the_dr = 0
#	candidateDr
	for dr in dr_list:
		if(dr.get_point() > highestPoint):
#			candidateDr = dr
			highestPoint = dr.get_point()
			id_of_the_dr = dr.get_id()
	return id_of_the_dr
	
def getDrFromList(dr_id):
	for dr in dr_list:
		if(dr.get_id() == dr_id):
			return dr
		

def fillWorkingDay(workingDay):
	for i in range(len(workingDay.jobs)):
#	for job in workingDay.jobs:
		_id = findDrWithHighestPoint(dr_list)
		getDrFromList(_id).point -= workingDay.count
		workingDay.jobs[i] = _id
		print(_id)

def schedule(dr_list, wd_list):
	for wd in wd_list:
		print(wd.date, wd.count)
		fillWorkingDay(wd)
		print(wd.jobs)
	
			
def showDrList():
	for dr in dr_list:
		print(dr.get_id(), dr.get_point())

def createCSVoutput(filePos):
	with open(filePos, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)

		#first row
		id_row = ['ID']
		for dr in dr_list:
			id_row.append(dr.get_id())
		writer.writerow(id_row)

		#date
		for wd in workingDay_list:
			date_row = [wd.date]
			for dr in dr_list:
				_id = dr.get_id()
				if _id == wd.jobs[0]:
					date_row.append('A')
				elif _id == wd.jobs[1]:
					date_row.append('B')
				elif _id == wd.jobs[2]:
					date_row.append('C')
				elif _id == wd.jobs[3]:
					date_row.append('D')
				elif _id == wd.jobs[4]:
					date_row.append('E')
				else:
					date_row.append('')
			writer.writerow(date_row)
		
		remainingPoint_row = ['point left']
		for dr in dr_list:
			remainingPoint_row.append(dr.get_point())
		writer.writerow(remainingPoint_row)
	
	
		

def main():
#	dr = Doctor(3);
	td = WorkingDay(datetime.date.today());
	wend = WorkingDay(datetime.datetime(2021,9,19));
#	print (dr.get_point());
	print (datetime.date.today().weekday());
	print (datetime.datetime(2021,9,20).weekday());
	print ("today has %d count" % td.count)
	print ("2021.9.19 has %d count" % wend.count)
	parseCSV("data/dr-level.csv")
	createWDList(2021,9)
	for doctor in dr_list:
		print(doctor.get_id(), doctor.get_point())
	schedule(dr_list, workingDay_list)
	showDrList()
	createCSVoutput("output/test.csv")

# main function starts here
main();


