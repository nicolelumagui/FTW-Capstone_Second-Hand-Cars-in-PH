#############################################################################################
######################################### LIBRARIES #########################################
#############################################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains

import os
import pandas as pd





#############################################################################################
######################################### MAIN CODE #########################################
#############################################################################################


##################################
##### Creating the Dataframe #####

### List of categories / features
column_list = ['title', 'brand', 'condition', 'body_type', 'webPage']

### Create empty dataframe
df = pd.DataFrame(columns=column_list)


########################
##### Chromedriver #####

dirpath = os.getcwd()
filepath = dirpath + '/chromedriver'
print 'Path to Driver: ', filepath


###########################
##### Listing Filters #####

# brands = ['aston-martin', 'audi', 'bentley', 'bmw', 'byd', 'cadillac', 'chevrolet', 'chrysler', 'dodge-1', 'ferrari', 'ford', 'foton', 'gmc', 'great-wall', 'honda', 'hummer', 'smart-1',
# 'hyundai', 'infiniti', 'isuzu', 'jaguar', 'jeep-2', 'joylong', 'kia', 'king-long', 'lamborghini', 'land-rover', 'lexus', 'lifan-1', 'lotus-1', 'mahindra', 'maserati', 'mazda', 
# 'mercedes-benz', 'mini-1', 'mitsubishi', 'nissan', 'peugeot', 'polaris', 'porsche', 'scion', 'ssangyong', 'subaru', 'suzuki', 'tata', 'toyota', 'volkswagen', 'volvo', 'lincoln']

conditions = ['used']

body_types = ['saloon', 'hatchback', 'luxury-car', 'hybridsgreen-cars', 'van-minibus', 'mpv-auv', 'off-road-vehicle-suv', 'pickup-trucks', 'sports-car-coupe']


#####################################
##### Run function for scraping #####

for c in conditions:

	for b in body_types:

		browser = webdriver.Chrome(executable_path = filepath) 
		wpg = "https://www.carmudi.com.ph/cars/"+ b + "/" + c + "/" #"https://www.carmudi.com.ph/cars/" + b + "/" + c + "/"
		print "##########################################"
		print wpg
		browser.get(wpg)

		print "##########################################"

		# brand = "bmw"
		# condition = c
		# body_type = b

		pageCont = True

		while pageCont:

			try:
				sleep(2)

				itemCont = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'catalog-listing-items-container')))
				items = itemCont.find_elements_by_class_name("catalog-listing-item")

				for item in items:
					title = item.find_element_by_class_name("catalog-listing-description-data").find_element_by_xpath(".//h3/a").text
					webPage = item.find_element_by_class_name("catalog-listing-description-data").find_element_by_xpath(".//h3/a").get_attribute("href")
					print "Title:", title
					#print "Brand:", brand
					print "Condition:", c
					print "Body Type:", b
					print "Web Page:", webPage
					print "##########################################"

					new_entry = {'title': title, 'condition': c, 'body_type': b, 'webPage': webPage}
					df = df.append(new_entry, ignore_index=True)

			except Exception as e:
				print "Scraping exception:", e

			print df.shape
			print "##########################################"

			try:
				nextPage = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'next-page')))
				nextPage.click()

			except Exception as e:
				print "Next page exception:", e
				print "Finished."
				pageCont = False

		browser.quit()


		#######################################
		##### Export the dataframe to CSV #####

		try:
			savepath = "C:/Users/acelo/Desktop/carmudi_car_condition-" + c + "_body-type-" + b  + ".csv"
			print savepath
			carmudi = df.to_csv(savepath, index=None, header=True)

		except:
			print "Export exception:", e