
# For shor creativity, i put the code in to functions to better presentation
# Create a new input to user type any country to verify data on our database

def min_max_expectancy(lifeExpectancy):
# Variables that find the position on the database
   lowerstExpectancy = min(lifeExpectancy)
   highestExpectancy = max(lifeExpectancy)

   positionLower = lifeExpectancy.index(min(lifeExpectancy))
   positionHighest = lifeExpectancy.index(max(lifeExpectancy))

   countryLowest = entity[positionLower]
   countryHighest = entity[positionHighest]

   yearLowest = years[positionLower]
   yearHighest = years[positionHighest]
   
   print("")
   print(f"The overall max life expectancy is: {highestExpectancy} from {countryHighest} in {yearHighest} ")
   print(f"The overall min life expectancy is: {lowerstExpectancy} from {countryLowest} in {yearLowest} ")
   print("")

def general_average(years):
  yearListPosition = []
  inputYear = input("Enter the year of interest: ")
  for i, item in enumerate(years):
      if item == inputYear:
         yearListPosition.append(i)

  expectancyListYear = []
  for positionYear in yearListPosition:
     expectancyListYear.append(float(lifeExpectancy[positionYear]))
  
  quantity = len(expectancyListYear)
  sumTotal = sum(expectancyListYear)

  media = sumTotal/quantity
  return inputYear, expectancyListYear, media, yearListPosition

def search_required_year(inputYear, expectancyListYear, media, yearListPosition):
   print(f"For the year {inputYear}:")
   print(f"The average life expectancy across all countries was: {round(media,2)}")

   yearExpectancyLowerest = min(expectancyListYear)
   yearExpectancyLowerestPosition = expectancyListYear.index(yearExpectancyLowerest)

   yearExpectancyHightest = max(expectancyListYear)
   yearExpectancyHightestPosition = expectancyListYear.index(yearExpectancyHightest)

   yearEntityLowerest = entity[yearListPosition[yearExpectancyLowerestPosition]]
   yearEntityHightest = entity[yearListPosition[yearExpectancyHightestPosition]]

   print(f"The max life expectancy was in {yearEntityHightest} with {yearExpectancyHightest}")
   print(f"The max life expectancy was in {yearEntityLowerest} with {yearExpectancyLowerest}")
   print("")

def required_country(entity):
   inputCountry = input("Enter the Country of interest: ")
   print("")
   entityListPosition = []
   for i, item in enumerate(entity):
         if item == inputCountry.capitalize():
            entityListPosition.append(i)

   while len(entityListPosition) <= 0:
      print("Country does not exist on our database. Try type again")
      print("")
      required_country(entity)
      return 

   expectancyListEntity = []
   for positionEntity in entityListPosition:
      expectancyListEntity.append(float(lifeExpectancy[positionEntity]))
   
   quantity = len(expectancyListEntity)
   sumTotal = sum(expectancyListEntity)

   media = sumTotal/quantity

   entityExpectancyLowerest = min(expectancyListEntity)
   entityExpectancyHightest = max(expectancyListEntity)

   print(f"The average life expectancy in {inputCountry} was: {round(media,2)}")
   print(f"The overall max life expectancy from {inputCountry} in {entityExpectancyHightest} ")
   print(f"The overall min life expectancy from {inputCountry} in {entityExpectancyLowerest} ")


with open("life-expectancy.csv") as database:
  entity = []
  code = []
  years = []
  lifeExpectancy = []
  for i, data in enumerate(database):
      parts = data.strip().split(',')
      if i == 0:
         continue
      entity.append(parts[0])
      code.append(parts[1])
      years.append(parts[2])
      lifeExpectancy.append(parts[3])


  # CALLING FUNCTIONS
  min_max_expectancy(lifeExpectancy)
  inputYear, expectancyListYear, media, yearListPosition = general_average(years)
  search_required_year(inputYear, expectancyListYear, media, yearListPosition)
  required_country(entity)





