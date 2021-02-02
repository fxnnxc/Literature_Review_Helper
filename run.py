from tqdm.auto import tqdm
from selenium import webdriver


def main():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver =webdriver.Chrome('chromedriver', options=chrome_options)
   
    #----------------------------------------------------------------
    WORDS =["transformer"]
    ACL_LINK = "https://www.aclweb.org/anthology/events/acl-2018/"
    BLOCK_ID = "p18-1"    
    GITHUB_MD_FORMAT = True
    SAVE_TAG ="ACL"+BLOCK_ID+"_"+"_".join(WORDS)
    #----------------------------------------------------------------

    a = driver.get(ACL_LINK)
    a = driver.find_element_by_id(BLOCK_ID)
    a = a.find_elements_by_tag_name("strong")
    names = []
    links = []

    for e in tqdm(a):
        e = e.find_element_by_tag_name("a")
        names.append(e.text)
        links.append(e.get_attribute('href'))

    count = 0
    with open(SAVE_TAG+".txt", "w", encoding="utf8") as f :
        for n, w in zip(names, links):
            L = n.lower()
            if not all([word not in L for word in WORDS]):
                #------------------------------------------------------
                # WRITE FORMAT
                if GITHUB_MD_FORMAT:
                    f.write(f"[{n}]({w})\n")
                else:
                    f.write(f"{n}   {w}\n")
                count +=1 
                #------------------------------------------------------

    print("*----- Done -----*")
    print("Total : ", len(names), "Selected : ", count)
    print("------------------")


if __name__=="__main__":
    main()