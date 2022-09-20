
# **Interactive Dashboard - TMDb Movie Data**

This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.

*   Certain columns, like ‘cast’ and ‘genres’, contain multiple values separated by pipe (|) characters.
*   There are some odd characters in the ‘cast’ column. Don’t worry about cleaning them. You can leave them as is
*   The final two columns ending with “_adj” show the budget and revenue of the associated movie in terms of 2010 dollars, accounting for inflation over time.

[![](demo.gif)]()

# **Questions**

*   Which genres are most popular from year to year?
*   Which movies are the most profitable?

*  What is the percentage of all genres?
*   Which actors acted the most movies from 1960 to 2015?
*  Which movies have the highest Average Votes?
*  Which movies have the highest Popularity?
* Which directors have the highest popularity from year to year?
*   Which director have the highest popularity?
*  Which directors are the most profitable?



## **Run Locally**

Clone the project

```bash
  git clone https://github.com/lawal-hash/Interactive_dashboard.git
```

Go to the project directory

```bash
  cd Interactive_dashboard
```

Install dependencies

```bash
  pip download requirements.txt
```

Start the server

```bash
  panel serve run.ipynb
```


# **Conclusion**

From the analysis, I tried to answer 9 different questions from tmdb movie dataset. 
* Movies with high popularity tend to be profitable.
* There is a very strong correlation between profit and revenue. 
* The movie Avatar directed by  James Cameron is the most profitable in the dataset
* However, Pierre Coffin is the most profitable director in the Dataset
* Jurassic World is the most popular movie
*  The Story of Film: An Odyssey is the movie with the highest vote average
*  Robert De Niro and Samuel L. Jackson acted 72 and 71 movies respectively from 1960 to 2015
*   Movie genre ADVENTURE has the highest popularity (14 times) from 1960 to 2015
* Movie genre DRAMA is the most produce genre(17.74%) from year 1960 to 2015
* It is worth noting that the most popular director doesn't translate to the most profitable director as shown in the  analysis. 
*  Pierre Coffin is the only director in the list most profitable and popular directors.


## Authors

- [@lawal-hash](https://github.com/lawal-hash)


## Contributing

Find any typos? Contributions are welcome!

First, fork this repository.

[![portfolio](https://raw.githubusercontent.com/udacity/ud777-writing-readmes/master/images/fork-icon.png)]()



Next, clone this repository to your desktop to make changes.

```
$ git clone {YOUR_REPOSITORY_CLONE_URL}

```


Once you've pushed changes to your local repository, you can issue a pull request by clicking on the green pull request icon.

[![portfolio](https://raw.githubusercontent.com/udacity/ud777-writing-readmes/master/images/pull-request-icon.png)]()

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)]()
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sophia-lawal/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Ayan_Yemi)

