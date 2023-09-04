import dependencies.cleaning.dic_converter as dc
import dependencies.scraping.text_Scraper as ts
import dependencies.standardization.csv_converter_1 as cc
import dependencies.scraping.json_dic as jd
import dependencies.scraping.api_Commons_Data as apiC
import dependencies.cleaning.filter as fl
import dependencies.standardization.csv_converter as cs
import dependencies.scraping.scrape_task2_json as sct
# import dependencies.standardization.csv_converter
def main():
    # task1
    url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"
    cls= "clearfix text-formatted field field--name-field-text-content field--type-text-long field--label-hidden field__item"
    tag ="div"
    #text_scraper return list of data 
    lst = ts.text_Scraper(url,tag,class_=cls)
    dic = dc.dic_converter(lst)# dic_converter filter the data and return the dictionary(key:value)
    csv_filename = 'data1.csv'
    # Write the data to a CSV file
    # print(dic)
    cc.csv_converter(csv_filename,dic,pointer='task1')
   
    # task2
    data = sct.scrape_task2_json()
    csv_header = ['URL', 'Tile_Directory_URL','Name', 'DateRecorded']
    cc.csv_converter("gld1.csv",data,pointer="task2",csv_header = csv_header)
    
    #task4
    #common Time Series Data
    country_id = 'IND' #country id
    variable = 'FertilityRate_Person_Female' # we are point the particular data point
    data = apiC.api_Commons_Data(country_entities=country_id,variable=variable)
    dic = fl.filter(country=country_id,var=variable,data=data) #cleaning the non useful data
    cs.ctt("Common_IND.csv",dic,var=variable)
    
if __name__ == '__main__':
    main()    
    


