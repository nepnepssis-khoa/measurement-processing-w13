import csv

pressures = []
temperatures = []
num_of_lines_to_process = 1000
biggestPressureNumber = float('-inf')
biggestPressureNumberIndex = 0
smallestPressureNumber = float('inf')
smallestPressureNumberIndex = 0
biggestTemperatureNumber = float('-inf')
biggestTemperatureNumberIndex = 0
smallestTemperatureNumber = float('inf')
smallestTemperatureNumberIndex = 0

with open('pressure_full.csv') as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',')
    line_count1 = 0
    for row in csv_reader1:
        if line_count1 == 0:
            print(f'Column names are {", ".join(row)}')
            line_count1 += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count1 == 1):
            smallestPressureNumber = float(row[1])
            smallestPressureNumberIndex = 0
            biggestPressureNumber = float(row[1])
            biggestPressureNumberIndex = 0

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestPressureNumber<float(row[1])):
            biggestPressureNumber = float(row[1])
            biggestPressureNumberIndex = len(pressures)-1

            
          if(smallestPressureNumber>float(row[1])):
            smallestPressureNumber = float(row[1])
            smallestPressureNumberIndex = len(pressures)-1


          line_count1 += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    #print(f'Processed {line_count} lines.')


with open('temperature_full.csv') as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter=',')
    line_count2 = 0
    for row in csv_reader2:
        if line_count2 == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count2 += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count2 == 1):
            smallestTemperatureNumber = float(row[1])
            smallestTemperatureNumberIndex = 0
            biggestTemperatureNumber = float(row[1])
            biggestTemperatureNumberIndex = 0

          #print(f'Pressure: \t{row[1]}')
          temperatures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestTemperatureNumber<float(row[1])):
            biggestTemperatureNumber = float(row[1])
            biggestTemperatureNumberIndex = len(temperatures)-1

            
          if(smallestTemperatureNumber>float(row[1])):
            smallestTemperatureNumber = float(row[1])
            smallestTemperatureNumberIndex = len(temperatures)-1


          line_count2 += 1


#print(len(pressures))
#print(len(temperatures))

print(biggestPressureNumber)
print(biggestPressureNumberIndex)

print(biggestTemperatureNumber)
print(biggestTemperatureNumberIndex)

print(smallestPressureNumber)
print(smallestPressureNumberIndex)

print(smallestTemperatureNumber)
print(smallestTemperatureNumberIndex)

#print(f'pressure is {pressures[len(pressures)-1][0]} at {pressures[len(pressures)-1][1]}' )
