import csv
import functools

filename="test.csv"

curr_s = 0
i=1
counter=0

fields = []
row = []
vals_x = []
vals_x_neg = []
vals_y = []
vals_y_neg = []
vals_z = []
vals_z_neg = []
vals_lat = []
vals_long = []
fin_x = 0
fin_y = 0
fin_z = 0

    
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)

    for rows in csvreader:
        row.append(rows)

print(len(row))

for r in row:
    counter +=1
    
    lat,longi=list(map(float, r[:2]))
    
    cordi=r[2:]

    time,x,y,z=cordi
    
    x=float(x)
    y=float(y)
    z=float(z)
    

    time_h=int(time[11:13])
    time_m=int(time[14:16])
    time_s=int(time[17:19])

    
    if curr_s!=time_s or counter==len(row):
        print("time_s: ",time_s)
        curr_s=time_s
        if vals_x!=[]:
            
            if vals_x_neg!=[]:
                if( max(vals_x) > max(vals_x_neg)):
                    fin_x = max(vals_x)
                else:
                    fin_x = -(max(vals_x_neg))
            else:
                fin_x=max(vals_x)
            
            if vals_y_neg!=[]:
                if vals_y!=[]:
                    if( max(vals_y) > max(vals_y_neg)):
                        fin_y = max(vals_y)
                    else:
                        fin_y = -(max(vals_y_neg))
                else:
                    fin_y = -(max(vals_y_neg))
            else:
                fin_y=max(vals_y)
            
            if vals_z_neg!=[]:
                if vals_z!=[]:
                    if( max(vals_z) > max(vals_z_neg)):
                        fin_z = max(vals_z)
                    else:
                        fin_z = -(max(vals_z_neg))
                else:
                    fin_z = -(max(vals_z_neg))
            else:
                fin_z = max(vals_z)
                
            str_vals=",".join([str(fin_x),str(fin_y),str(fin_z),str(max(vals_lat)),str(max(vals_long)),'\n'])
            with open('test.txt','a') as the_file:
                i +=1
                print(i)
                the_file.write(str_vals)
                fin_x=0
                fin_z=0
                fin_y=0
       
        vals_x = []
        vals_y = []
        vals_z = []
        vals_x_neg = []
        vals_y_neg = []
        vals_z_neg = []
        vals_lat = []
        vals_long = []
    
        
        
    if(x<0):
        vals_x_neg.append(abs(x))
    else:
        vals_x.append(x)
    
    if(y<0):
        vals_y_neg.append(abs(y))
    else:
        vals_y.append(y)
        
    if(z<0):
        vals_z_neg.append(abs(z))
    else:
        vals_z.append(z)
        
    vals_lat.append(lat)
    vals_long.append(longi)
    


