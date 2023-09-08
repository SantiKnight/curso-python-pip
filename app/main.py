import read_csv
import charts
import utils
import pandas as pd

def run():
    '''
    data = list(filter(lambda x: x['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentages = list(map(lambda x: x['World Population Percentage'], data))
    '''
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']
    
    countries = df['Country/Territory'].values
    porcentages = df['World Population Percentage'].values
    
    charts.generate_pie_chart(countries, porcentages)
    
    data = read_csv.read_csv('./data.csv')
    country = input("Ingrese el pais => ")
    result = utils.get_population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == "__main__":
    run()