import dependencies.scraping.json_dic as jd
def scrape_task2_json():
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://www.nnvl.noaa.gov/view/globaldata.html',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
            'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
            }  

        params = {
            'Action': 'LoadFrames',
            'ProductID': '1',
            'Timespan': 'weekly',
            }
        
        url = 'https://www.nnvl.noaa.gov/view/ExecuteSQL_e4.php'
        data =jd.json_dic(url,params ,headers)
        return data