import csv
import pygal

gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    table = {}

    with open(filename, 'rt', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator,
                                    quotechar=quote)
        for row in csv_reader:
            # print(row)
            rowid = row[keyfield]
            table[rowid] = row
    return table


print(read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"'))

def build_plot_values(gdpinfo, gdpdata):
    
    table = []
    gdpdat_v2 = {}
    for k, v in gdpdata.items():
        try:
            gdpdat_v2[int(k)] = float(v)
        except ValueError:
            pass

    min_max = [year for year in range(gdpinfo['min_year'], gdpinfo['max_year'] + 1)]

    for key in min_max:
        if key in gdpdat_v2:
            table.append((key, gdpdat_v2[key]))
    return table



def build_plot_dict(gdpinfo, country_list):
    gdp_dat = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"], gdpinfo["separator"],gdpinfo["quote"])

    country_fetch = [k for k in gdp_dat]
    table = {}


    for country in country_list:
        if country in country_list:
        try:
            table[country] = build_plot_values(gdpinfo, gdp_dat[country])
        except KeyError:
            table[country] = []

    return table


print(build_plot_dict({'min_year': 2000, 'country_name': 'Country Name', 'separator': ',', 'country_code': 'Code', 'gdpfile': 'gdptable1.csv', 'quote': '"', 'max_year': 2005}, ['Country1']))


print(build_plot_dict(gdpinfo, ['Bangladesh']))
