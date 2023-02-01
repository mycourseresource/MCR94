# https://www.cso.ie/en/census/census2011smallareapopulationstatisticssaps/

import pandas as pd
data_list = [
    ['P1', 'Province', 'Leinster', 1233352, 1271462, 705163, 677153, 12315, 47265, 261054, 677555, 607358, 895149],
    ['P2', 'Province', 'Munster', 620260, 625828, 345883, 314314, 10219, 8530, 101527, 317172, 272067, 453112],
    ['P3', 'Province', 'Connacht', 271110, 271437, 152116, 135462, 3117, 4726, 36870, 135194, 114619, 196530],
    ['P4', 'Province', 'Ulster', 147977, 146826, 82450, 72084, 1301, 656, 15487, 69377, 57898, 104617]
    ]
population_provinces = pd.DataFrame(data_list, columns = [
    'GEOGID', 'GEOGTYPE', 'GEOGDESC',
    'Total Males', 'Total Females',
    'Single Males', 'Single Females',
    'No Central Heating',
    'Commute Bicycle', 'Commute Foot',
    'Computer Household', 'Broadband Household',
    'Total Households'])
print(population_provinces)


































