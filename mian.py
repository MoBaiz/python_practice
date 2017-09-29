import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import csv
count=6
for i in range(41):
    csv_reader = csv.reader(open("data.csv", encoding='utf-8'))
    os=[]
    od=[]
    all=[]
    for row in csv_reader:
        all.append(row[count])
        if row[5]=='OS':
            os.append(row[count])
        elif row[5]=='OD':
            od.append(row[count])
        elif row[5]=='Eye':
            pass
        else:
            print(row[5])
    print(all[0])
    name=all[0]
    del all[0]
    os=list(map(eval,os))
    od = list(map(eval,od))
    all = list(map(eval,all))
    p1 = plt.subplot(311)
    p2 = plt.subplot(312)
    p3 = plt.subplot(313)
    p1.set_title(name+'_os_total:'+str(len(os)))
    p2.set_title(name + '_od_total:' + str(len(od)))
    p3.set_title(name + '_all_total:' + str(len(all)))
    n,bins,patches = p1.hist(os,300, histtype='bar', facecolor='green', alpha=0.75)
    n, bins, patches =p2.hist(od, 300, histtype='bar', facecolor='green', alpha=0.75)
    n, bins, patches = p3.hist(all, 300, histtype='bar', facecolor='green', alpha=0.75)
   # plt.title(name)
    plt.grid(True)
    plt.savefig(name + '.png')
    plt.clf()
    count=count+1
    #plt.show()
