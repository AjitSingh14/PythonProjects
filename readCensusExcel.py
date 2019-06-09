import openpyxl, pprint

print('Opening Workbook')

wb=openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by Census Tract']

county_data={}

# TODO: Fill in countyData with each county's population and tracts.
print('Reading Rows')

for row  in range(2, sheet.max_row+1):
    state=sheet['B'+ str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
    county_data.setdefault(state, {})
    county_data[state].setdefault(county,{'tracts':0, 'pop':0})
    county_data[state][county]['tracts']+=1
    county_data[state][county]['pop']+=int(pop)
    


# Open the file and write the the result into file
print('write the result to file...')
resultfile= open('consus2010.py','w')
resultfile.write('AllData = ' + pprint.pformat(county_data))

resultfile.close()
print('Done...')




