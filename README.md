# scrapy-BooksToScrape
This repository contain project to scrape http://books.toscrape.com/ website

This is some function of this project
<ul>
  <li>
    To get all of products, use this command<br>
    <b><i>scrapy crawl all_products -o result_all_products.json</i></b>
    <br><br>
    After get the json output, you can analyze the result using data science tool like pandas
    
    ```
    >>> import pandas as pd
    >>> df = pd.read_json("result_all_products.json")
    >>> 
    >>> df.head()
                                                   title  stock  rating   price
    0                               A Light in the Attic     22       3  £51.77
    1  Scott Pilgrim's Precious Little Life (Scott Pi...     19       5  £52.29
    2  Our Band Could Be Your Life: Scenes from the A...     19       3  £57.25
    3                            It's Only the Himalayas     19       2  £45.17
    4                          Rip it Up and Start Again     19       5  £35.02
    ```
  </li>
  
</ul>
