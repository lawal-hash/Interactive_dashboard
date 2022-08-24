#!/usr/bin/env python
# coding: utf-8




import hvplot.pandas
import hvplot
import pandas as pd
pd.options.plotting.backend = 'hvplot'
import holoviews as hv
hv.extension('bokeh')



from panel.template import DarkTheme
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,10)


# # **Investigate a Dataset - TMDb Movie Data**
# 
# **Table of content** 
# 
# 1. Introduction
# 2. Questions
# 3. Data Wrangling
# 4. Exploratory Data Analysis 
# 5. Conclusion
# 6. Limitation
# 7. Reference
# 
# 

# # **Introduction** 
# This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.
# 
# 
# 
# 
# 
# *   Certain columns, like ‘cast’ and ‘genres’, contain multiple values separated by pipe (|) characters.
# *   There are some odd characters in the ‘cast’ column. Don’t worry about cleaning them. You can leave them as is
# *   The final two columns ending with “_adj” show the budget and revenue of the associated movie in terms of 2010 dollars, accounting for inflation over time.
# 

# # **Questions**
# 
# 
# 
# *   Which genres are most popular from year to year?
# *   Which movies are the most profitable?
# 
# *  What is the percentage of all genres?
# *   Which actors acted the most movies from 1960 to 2015?
# *  Which movies have the highest Average Votes?
# *  Which movies have the highest Popularity?
# * Which directors have the highest popularity from year to year?
# *   Which director have the highest popularity?
# *  Which directors are the most profitable?
# 
# 

# # **Data Wrangling**
# 
# 
# 
# *   check and remove missing value 
# *   check and remove duplicate values
# *   convert to appropriate  datatype
# 
# 




path = 'tmdb-movies.csv'




def seperator(x):
   return x.split('|')


def preprocessing(path, seperator):
    df_tmdb = pd.read_csv(path, index_col='id')
    df_tmdb['release_date'] = pd.to_datetime(df_tmdb['release_date'])
    df_tmdb.drop(columns = ['imdb_id','homepage','tagline','overview','keywords', 'production_companies'],inplace=True,axis = 1)
    df_tmdb.dropna(inplace=True)
    df_tmdb.drop_duplicates(inplace=True)
    df_tmdb['genres']=df_tmdb ['genres'].apply(seperator)
    df_tmdb['cast']=df_tmdb ['cast'].apply(seperator)
    df_tmdb['director']=df_tmdb ['director'].apply(seperator)
    return df_tmdb





df_tmdb = preprocessing(path, seperator)




import panel as pn
#pn.extension(sizing_mode = 'stretch_width')





year = pn.widgets.IntRangeSlider(name='Years Range Slider', width=250, start=1960, end=2015)
pn.Column(year)





# TO DO - bar chart
@pn.depends(year=year)
def plot_most_popular_genre(year):
    years_df_tmdb = df_tmdb[df_tmdb['release_date'].dt.year.between(year[0],year[1])]
    df_genre = years_df_tmdb.explode('genres')#[['popularity', 'genres','release_year']]
    df_genre_grouped = df_genre.groupby(['release_year', 'genres']).mean()
    popular_yearly = df_genre_grouped.groupby(level='release_year')['popularity'].nlargest(1).to_frame()
    popular_yearly.reset_index(level=2, inplace=True)
    genre_yearly = popular_yearly['genres'].value_counts().to_frame()
    genre_yearly = genre_yearly.reset_index().rename(columns={"index":'genres', "genres":"Popularity count"})
    return genre_yearly.hvplot.bar(x='genres', y='Popularity count', xlabel='Genres', ylabel='Popularity count', title=f'Most popular genre from {year[0]} to {year[1]}', invert=False, rot=20)



# barh chart
@pn.depends(year=year)
def  plot_profitable_movies(year):
    years_df_tmdb = df_tmdb[df_tmdb['release_date'].dt.year.between(year[0],year[1])]
    years_df_tmdb['profit']=years_df_tmdb['revenue']-years_df_tmdb['budget']
    profitable_movies = years_df_tmdb.sort_values(by='profit', ascending = True).tail(10).reset_index(drop=True)
    return profitable_movies.hvplot.barh(x='original_title', y='profit',xlabel='Movie Title', ylabel='Profit', title=f'Top 10 most Profitable Movies from {year[0]} to {year[1]}', rot=20)


# Pie chart



# To DO - table
@pn.depends(year=year)
def  plot_actors(year):
    years_df_tmdb = df_tmdb[df_tmdb['release_date'].dt.year.between(year[0],year[1])]
    df_cast = years_df_tmdb.explode('cast')#[['popularity', 'cast','release_year']]
    df_cast = df_cast['cast'].value_counts()[:10]
    df_cast = df_cast.to_frame().reset_index().rename(columns={"index":'Cast', "cast":'Frequency count'})
    return df_cast.hvplot.table(columns=['Cast', 'Frequency count'], title=f'Top 10 Actors with most Movies  from {year[0]} to {year[1]}') # + df_cast.hvplot.barh(x='Cast',y='Frequency count'))



# barh chart
@pn.depends(year=year)
def  plot_most_popular_movies(year):
    years_df_tmdb = df_tmdb[df_tmdb['release_date'].dt.year.between(year[0],year[1])]
    df_popular = years_df_tmdb[['original_title','popularity']]
    popular_movies = df_popular.sort_values(by='popularity', ascending = True).tail(10).reset_index(drop=True)
    return popular_movies.hvplot.barh(x='original_title', y='popularity',title=f'Top 10 Movies with the highest popularity from {year[0]} to {year[1]}')


# bar chart or table
@pn.depends(year=year)
def  plot_directors(year):
    years_df_tmdb = df_tmdb[df_tmdb['release_date'].dt.year.between(year[0],year[1])]
    years_df_tmdb['profit']=years_df_tmdb['revenue']-years_df_tmdb['budget']
    df_director = years_df_tmdb.explode('director')#[['director', 'profit', 'popularity']]
    df_directors = df_director.groupby('director').mean().reset_index()
    df_directors = df_directors.rename(columns={"popularity":'Average Popularity', "profit":'Average Profit'})
    df_directors[df_directors['Average Profit']>0] = df_directors
    df_directors = df_directors.sort_values(by='Average Profit',ascending = False)[:10]
    return df_directors.hvplot.table(columns=['director','Average Profit','Average Popularity'],title=f'Top 10 most Profitable and Popular Directors from {year[0]} to {year[1]}')





# scatter plot, box plot
@pn.depends(year=year)
def  plot_distribution(year):
    years_df_tmdb = df_tmdb[df_tmdb['release_date'].dt.year.between(year[0],year[1])]
    return years_df_tmdb.hvplot.hist(y='vote_average', bins=50, alpha=0.5, legend='top', title=f'Distribution of Vote Average from {year[0]} to {year[1]}')

pn.extension()


def get_app():
    pd.options.mode.chained_assignment = None
    pn.Column(year)
    pn.Row(year, plot_most_popular_movies)
    pn.Column(year, plot_most_popular_genre)


    link = 'movies.gif'
    gif_pane = pn.pane.GIF(link)




    bootstrap = pn.template.BootstrapTemplate(title='Investigate TMDB Movies', theme=DarkTheme)
    bootstrap.sidebar.append(gif_pane)
    bootstrap.sidebar.append(year)

    bootstrap.main.append(
        pn.Row(
            pn.Card(hv.DynamicMap(plot_most_popular_genre)),
            pn.Card(hv.DynamicMap(plot_actors)),
        )
    )

    bootstrap.main.append(
        pn.Row(
            pn.Card(hv.DynamicMap(plot_directors)),
            pn.Card(hv.DynamicMap(plot_profitable_movies)),
        )
    )



    bootstrap.main.append(
        pn.Row(
            pn.Card(hv.DynamicMap(plot_distribution))
        #pn.Card(hv.DynamicMap(plot_most_popular_movies))

        )
    )
    return bootstrap


if __name__ == 'main':#startswith("bokeh"):
    get_app().servable()







