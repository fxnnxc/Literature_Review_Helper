
- [Literature Review Helper](#literature-review-helper)
  - [1. How to Use](#1-how-to-use)
  - [2. Waring ⚠️](#2-waring-️)
  - [3. Fun Utils 🥳](#3-fun-utils-)
- [Supports](#supports)

# Literature Review Helper 

Use it when you want to collect papers with keywords in [ACL Anthology](https://www.aclweb.org/anthology/)

<a>
<img src=https://img.shields.io/badge/Python-v3.6.8-blue?style=flat&logo=python  height=30px>
</a>


```bash
pip install -r requirements.txt
python run.py
```

```bash
Output : Papername / PaperLink paired txt file.
```


## 1. How to Use

What you have to set in **run.py**

<img src="docs/img4.png">

* **WORDS** : the key words that you want to catch. The program will select a paper if it has at least one of the key words. (not interaction it's union)
* **ACL_LINK** : there are many acl events and non-acl events. you have to choose which one and sepicify the year. 
* **BLOCK_ID** : one conference composed of many blocks. for example the below picuture of CLJ has 2 blocks. You have to find it by yourself by insepcting the html (Ctrl+Shift + I for chrome)

* **GITHUB_MD_FORMAT** : It is just for writing format. Use it when you want a github markdown foarmat.(default is tep seperate )

  e.g. [Provable Fast Greedy Compressive Summarization with Any Monotone Submodular Function](https://www.aclweb.org/anthology/N18-1157/)


|BLOCK_ID example|Block Examples|
|---|---|
|<img src="docs/img1.png" width=300px>|<img src="docs/img3.png" width=400px>|



## 2. Waring ⚠️ 

If the chrome version doesn't match. You may have error. Download Chrome 
driver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) when you have an error. 



## 3. Fun Utils 🥳

1. Reform to Table

   Reform the list of texts to the markdown table format.
   
   ```
   python fun_utils/reform_to_table.py fun_utils/temp
   ```




---


# Supports 

ACL Events or Non-ACL Events in [ACL Anthology](https://www.aclweb.org/anthology/)


<img src="docs/img2.png">
