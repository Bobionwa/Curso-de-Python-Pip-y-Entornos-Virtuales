import charts

def run(values):
    charts.pie_chart(values)

if __name__ == '__main__':
    values = input("Values(4): ")
    values = values.split(' ')
    values = [int(n) for n in values]
    run(values)
