import read_csv
import charts
import utils

if __name__ == "__main__":
    data = read_csv.read_csv('./data.csv')
    country = input('Ingrese el país que desea graficar => ')
    
    result = utils.get_population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)