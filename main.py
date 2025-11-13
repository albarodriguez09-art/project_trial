# TODO document

from final_project.city import City

area_rates = {
    0: (100, 200),
    1: (50, 250),
    2: (250, 350),
    3: (150, 450),
}

city = City(size = 10, area_rates = area_rates)
city.initialize()

# TODO iterations
# TODO requested graph
# plt.savefig('reports/graph1.png')
# TODO proposed graph
# plt.savefig('reports/graph2.png')