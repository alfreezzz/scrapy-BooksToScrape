# scrapy-BooksToScrape
This repository contain project to scrape http://books.toscrape.com/ website

This is some function of this project
<ul>
  <li>
    To get all of products, use this command<br>
    <b><i>scrapy crawl all_products -o result_all_products.json</i></b>
    <br><br>
    After get the json output, you can analyze the result using data science tool like pandas   
 
    >>> import pandas as pd
    >>> df = pd.read_json("result_all_products.json")
    >>> df.head()
                                                   title  stock  rating   price        category
    0                               A Light in the Attic     22       3  £51.77          Poetry
    1  Scott Pilgrim's Precious Little Life (Scott Pi...     19       5  £52.29  Sequential Art
    2                                        Set Me Free     19       5  £17.46     Young Adult
    3                              Shakespeare's Sonnets     19       4  £20.66          Poetry
    4     Starving Hearts (Triangular Trade Trilogy, #1)     19       2  £13.99         Default
    >>> 

    
  </li>
  <br>
  <li>
    To get all of products based on categories, use this command<br>
    <b><i>scrapy crawl book_categories -o result_book_categories.json</i></b>
    <br><br>
    After get the json output, you can analyze the result using data science tool like pandas   
 
    >>> import pandas as pd
    >>> pd = pd.read_json("result_book_categories.json")
    >>> pd.head()
         category_name                                               data
    0           Travel  [{'book_title': 'It's Only the Himalayas', 'bo...
    1       Nonfiction  [{'book_title': 'Worlds Elsewhere: Journeys Ar...
    2         Religion  [{'book_title': 'Don't Be a Jerk: And Other Pr...
    3        New Adult  [{'book_title': 'Without Borders (Wanderlove #...
    4  Science Fiction  [{'book_title': 'Mesaerion: The Best Science F...
    >>> 

    
  </li>
</ul>
