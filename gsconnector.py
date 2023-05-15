# THIS IS THE MICROSERVICE PORTION

import gspread
from formulas import *

# Connecting to Google Sheet using gspread
gc = gspread.service_account(filename='.config/credentials.json')

# Accessing the required sheets
# used for receiving data
sh_microservice = gc.open("CorrelateIt_Microservice")
sh_result = gc.open("CorrelateIt_Result")               # used for sending data

# Accessing the first sheet in the Microservice and Result Google Sheets
microservice_sheet = sh_microservice.sheet1
result_sheet = sh_result.sheet1

# Reading data from Microservice sheet
data_label_1 = microservice_sheet.col_values(1)[1]
data_values_1 = microservice_sheet.col_values(2)[1:]
data_label_2 = microservice_sheet.col_values(3)[1]
data_values_2 = microservice_sheet.col_values(4)[1:]

# Converting the data values from string to float
data_array_1 = [float(x) for x in data_values_1]
data_array_2 = [float(x) for x in data_values_2]

# Updating the result sheet with the data analysis results
result_sheet.update('A2', data_label_1)
result_sheet.update('B2', min(data_array_1))
result_sheet.update('C2', max(data_array_1))
result_sheet.update('D2', max(data_array_1) - min(data_array_1))
result_sheet.update('E2', len(data_array_1))
result_sheet.update('F2', sum(data_array_1))
result_sheet.update('G2', mean(data_array_1))
result_sheet.update('H2', median(data_array_1))
result_sheet.update('I2', mode(data_array_1))
result_sheet.update('J2', standard_deviation(data_array_1))
result_sheet.update('K2', variance(data_array_1))

result_sheet.update('L2', data_label_2)
result_sheet.update('M2', min(data_array_2))
result_sheet.update('N2', max(data_array_2))
result_sheet.update('O2', max(data_array_2) - min(data_array_2))
result_sheet.update('P2', len(data_array_2))
result_sheet.update('Q2', sum(data_array_2))
result_sheet.update('R2', mean(data_array_2))
result_sheet.update('S2', median(data_array_2))
result_sheet.update('T2', mode(data_array_2))
result_sheet.update('U2', standard_deviation(data_array_2))
result_sheet.update('V2', variance(data_array_2))

# Converting data into numpy arrays
x = np.array(data_array_1)
y = np.array(data_array_2)

n = len(data_array_1)

# Calculating pearson correlation coefficient and p-value
pearson_coeff = pearson_correlation(data_array_1, data_array_2)
pearson_pval = pearson_pval(pearson_coeff, n)

# Updating the result sheet with correlation analysis results
result_sheet.update('W2', pearson_coeff)
result_sheet.update('X2', pearson_pval)
result_sheet.update('Y2', np.cov(x, y)[0, 1])

# Determining the significance and relationship between the two variables
significance, relationship = stat_conclusion(
    pearson_pval, pearson_coeff)

# Updating the result sheet with the conclusion
conclusion = conclude_stat(significance, relationship,
                           data_label_1, data_label_2)
result_sheet.update('Z2', conclusion)
