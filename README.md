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
    >>> df =pd.read_json("result_all_products.json")
    >>> df.head()
              category                                              title  stock  rating               upc product_type price_excl_tax price_incl_tax    tax  number_of_reviews
    0           Poetry                               A Light in the Attic     22       3  a897fe39b1053632        Books         £51.77         £51.77  £0.00                  0
    1   Sequential Art  Scott Pilgrim's Precious Little Life (Scott Pi...     19       5  3b1c02bac2a429e6        Books         £52.29         £52.29  £0.00                  0
    2            Music                          Rip it Up and Start Again     19       5  a34ba96d4081e6a4        Books         £35.02         £35.02  £0.00                  0
    3           Poetry                                               Olio     19       1  feb7cc7701ecf901        Books         £23.88         £23.88  £0.00                  0
    4  Science Fiction  Mesaerion: The Best Science Fiction Stories 18...     19       1  e30f54cea9b38190        Books         £37.59         £37.59  £0.00                  0
    >>> 

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
