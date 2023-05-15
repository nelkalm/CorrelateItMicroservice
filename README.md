# README

## Microservice README
This microservice connects to a Google Sheet using the gspread library and reads data from two columns in the sheet. It then converts the data from string to float, performs statistical analysis on the data, and updates another sheet with the results.

## Setup
To use this microservice, you need to install the gspread library and have a Google Sheet with the required format.

1. Install the gspread library by running `pip install gspread`.
2. Create a Google Cloud Platform (GCP) project, enable the Google Drive API, and create a service account with access to the Google Sheet.
3. Share the Google Sheet with the email associated with the service account.
4. Update the filename in `gc = gspread.service_account(filename='.config/credentials.json')` with the path to your service account credentials file.

## Usage
To use this microservice, run the script and ensure that the correct Google Sheet names are provided in the script. The script will read the data from the first sheet of the Microservice Google Sheet and perform statistical analysis on the two columns of data. It will then update the Result Google Sheet with the analysis results.

## UML Diagram
<img src="https://github.com/nelkalm/correlateit_st/blob/master/MicroserviceUML.png"
     alt="UML Diagram"
     style="float: left; margin-right: 10px;" />

## Dependencies
This microservice requires the following libraries:

- gspread
- numpy
- scipy

## License
This microservice is licensed under the MIT License.
