inglist = input('Please enter ingredients separated by a comma: ')
sulfates = ['test', 'alkybenzene sulfonate', 'ammonium laureth sulfate', 'ammonium lauryl sulfate']
inglist = inglist.lower()
ingredients = inglist.split(',')
for ingredient in ingredients:
    ingredient = ingredient.strip()
    if ingredient in sulfates:
        print('Sulfate: ', ingredient)      
        