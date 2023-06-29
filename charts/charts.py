import matplotlib.pyplot as plt

def pie_chart(values):
    labels = ['A', 'B', 'C']
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pieChart.png')
    plt.close()
