def Fruit_region_list(data_gen) -> tuple[set, list]:
    """
    Returns lists of places and fruits from the data generator.
 
    @param data_gen: Generator yielding dictionaries containing the CSV data.
    @returns: A tuple containing a set of regions and a list of fruits.
    """
    places = []
    fruits = []
    for line in data_gen:
        fruits.append(line["Fruit"])
        places.append(line["Major Growing Region"])
    regions_list = set()
    for regions in places:
        for region in regions.split(','):
            regions_list.add(region.strip())
    return regions_list, fruits
