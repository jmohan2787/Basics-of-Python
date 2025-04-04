class ElegiblityForMarriage():
    def Elegible():
        gender=str(input('Your Gender:'))
        age=int(input('Your Age:'))
        if gender.lower() == 'male':
            if age >= 21:
                return 'EILGIBLE'
            else:
                return 'NOT ELIGILBLE'
    
        elif gender.lower()=='girl':
            if age >=18:
                return 'EILGIBLE'
            else:
                return 'NOT ELIGILBLE'