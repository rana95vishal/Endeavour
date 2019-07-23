
# coding: utf-8

# In[75]:

'''Uploads list of testing (target) and training genes and downloads the resulting ranked list of genes returned by Endeavour as a .csv file.'''


# In[76]:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time 


# In[77]:

#create a webdriver element and open the required webpage
#specify path to chromedriver
driver = webdriver.Chrome("C:\Users\Vishal\Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://endeavour.esat.kuleuven.be/Endeavour.aspx')


# In[78]:

#finds next button on Species tab
next_button = driver.find_element_by_id('MainContent_uc_endeavour1_btn_Species_next')
next_button.click()


# In[79]:

#change selection of data type from gene to tab
#hidden elements can't be manipulated directly

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_TrainingGene"]/div/ul/li[1]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_TrainingGene"]/div/ul/li[2]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink');
                       ''',elem_hidden) 

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_TrainingGene"]/div/ul/li[4]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink rtsBefore');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_TrainingGene"]/div/ul/li[5]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink rtsSelected');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath('.//input[@id="ctl00_MainContent_uc_endeavour1_RTS_TrainingGene_ClientState"]')
driver.execute_script('''
                        arguments[0].setAttribute('value','{"selectedIndexes":["4"],"logEntries":[],"scrollState":{}}');
                        ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="MainContent_uc_endeavour1_RPW_P1"]')
driver.execute_script('''
                        arguments[0].setAttribute('class','rmpView corporatePageView rmpHidden');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="MainContent_uc_endeavour1_RPW_P5"]')
driver.execute_script('''
                        arguments[0].setAttribute('class','rmpView  corporatePageView');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RMP_TrainingGene_ClientState"]')
driver.execute_script('''
                        arguments[0].setAttribute('value','{"selectedIndex":4,"changeLog":[]}');
                        ''',elem_hidden)


# In[80]:

#upload text file containing tab separated list of training genes
file_input1 = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RADUPT1file0"]')
file_input1.send_keys('C:\Users\Vishal\Documents\endeavour_test.txt')

#wait introduced to allow time for the file name to get updated. Custom wait times can be introduced
time.sleep(3)

file_upload1 = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_Btn_Add_TrainingGen_File_input"]')
file_upload1.click()

#Check if the file has been uploaded 
elem_style = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RLB_TrainingGenes"]').get_attribute("style")
itr=0
while(elem_style == "height: 300px; width: 100%;" and itr <10):
    elem_style = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RLB_TrainingGenes"]').get_attribute("style")
    time.sleep(2)
    itr = itr+1

#advance to the Data Sources tab
next_button2 = driver.find_element_by_id('MainContent_uc_endeavour1_Btn_trg_Next')
next_button2.click()


# In[81]:

source_index = ["01","16","17","29","30","31","32","33","34","35","36","37"]
source_name = ["Annotation – Gene Ontology","Annotation - GAD","Annotation - OMIM","Expression – Su et al (2002)","Expression – Su et al (2004)","Expression – CMAP","Lukk et al","Annotation – PaGenBase","Annotation – CGAP","Annotation – GNF","Annotation - eGenetics","Blast"]
source_count = str(len(source_index))
print(source_count)


# In[82]:

#sources loop
#edit these two lists to choose your data sources  

source_index = ["01","16","17","29","30","31","32","33","34","35","36","37"]
source_name = ["Annotation – Gene Ontology","Annotation - GAD","Annotation - OMIM","Expression – Su et al (2002)","Expression – Su et al (2004)","Expression – CMAP","Lukk et al","Annotation – PaGenBase","Annotation – CGAP","Annotation – GNF","Annotation - eGenetics","Blast"]
source_count = str(len(source_index))
#select the data sources
for idx in range(len(source_index)):
    
    source_xpath = "ctl00_MainContent_uc_endeavour1_RB_hsapiens_Ds_" + source_index[idx]                                         
    source_all = driver.find_element_by_xpath('//*[@id = \"' + source_xpath + '\"]/span[1]')
    
    driver.execute_script('''
                            arguments[0].setAttribute('class','rbPrimaryIcon rbToggleCheckboxChecked');
                           ''',source_all)
    
    source_hidden_xpath = "ctl00_MainContent_uc_endeavour1_RB_hsapiens_Ds_" + source_index[idx] + "_ClientState"
    source_hidden = driver.find_element_by_xpath('//*[@id = \"' + source_hidden_xpath +'\"]')
    source_value = '{"text":"' + source_name[idx] + '","value":"","checked":true,"target":"","navigateUrl":"","commandName":"","commandArgument":"","autoPostBack":false,"selectedToggleStateIndex":0,"validationGroup":null,"readOnly":false,"primary":false,"enabled":true}'
    
    driver.execute_script('''
                            arguments[0].setAttribute('value',arguments[1]);
                            ''',source_hidden,source_value)
    
source_number = driver.find_element_by_xpath('//*[@id="MainContent_uc_endeavour1_lbl_Sel_datasets"]')
driver.execute_script("arguments[0].innerText = '10'", source_number)

file_upload2 = driver.find_element_by_xpath('//*[@id="MainContent_uc_endeavour1_Btn_Ds_Next"]')
file_upload2.click()


# In[83]:

#change selection of data type from gene to tab
#hidden elements can't be manipulated directly

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_CanditaeGene"]/div/ul/li[1]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_CanditaeGene"]/div/ul/li[2]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink');
                       ''',elem_hidden) 

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_CanditaeGene"]/div/ul/li[4]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink rtsBefore');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_CanditaeGene"]/div/ul/li[5]/a')
driver.execute_script('''
                        arguments[0].setAttribute('class','rtsLink rtsSelected');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RTS_CanditaeGene_ClientState"]')
driver.execute_script('''
                        arguments[0].setAttribute('value','{"selectedIndexes":["4"],"logEntries":[],"scrollState":{}}');
                        ''',elem_hidden)
                     
elem_hidden = driver.find_element_by_xpath( '//*[@id="MainContent_uc_endeavour1_RadPageView5"]')
driver.execute_script('''
                        arguments[0].setAttribute('class','rmpView corporatePageView rmpHidden');
                       ''',elem_hidden)


elem_hidden = driver.find_element_by_xpath( '//*[@id="MainContent_uc_endeavour1_RadPageView9"]')
driver.execute_script('''
                        arguments[0].setAttribute('class','rmpView  corporatePageView');
                       ''',elem_hidden)

elem_hidden = driver.find_element_by_xpath( '//*[@id="ctl00_MainContent_uc_endeavour1_RMP_CanditaeGene_ClientState"]')
driver.execute_script('''
                        arguments[0].setAttribute('value','{"selectedIndex":4,"changeLog":[]}');
                        ''',elem_hidden)
                     


# In[84]:

#uploading the list of candidate/testing genes

file_candidate = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RADUPT2file0"]')
file_candidate.send_keys('C:\Users\Vishal\Documents\endeavour_candidates.txt')
time.sleep(3)

file_upload2 = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_Btn_Add_Candidates_File_input"]')
file_upload2.click()


# In[85]:

elem_style2 = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RLB_Candidates"]').get_attribute("style")
itr=0

while(elem_style2 == "height: 300px; width: 100%;" and itr <20):
    elem_style2 = driver.find_element_by_xpath('//*[@id="ctl00_MainContent_uc_endeavour1_RLB_Candidates"]').get_attribute("style")
    time.sleep(2)
    itr = itr+1
    
next_button2 = driver.find_element_by_id('MainContent_uc_endeavour1_Btn_Can_Finish')
next_button2.click()

try:
    elem_load = WebDriverWait(driver, 300).until(
        ec.presence_of_element_located((By.ID, "export_selected"))
    )
finally:
    driver.find_element_by_xpath('//*[@id="export_selected"]').click()
    
#export the results
driver.find_element_by_xpath('//*[@id="export_selected"]').click()


# In[ ]:




# In[23]:




# In[ ]:



