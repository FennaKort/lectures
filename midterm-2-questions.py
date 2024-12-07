def convert_km_to_m(km: float) -> float:
	"converts kilometers to meters by dividing kilometers by 1000" # should have been multiplying
	m = km * 1000
	return m

def calculate_slope(elevation_gain: float, distance: float) -> float:
	"calculate slope as a value <=100 that can be formatted as a percentage using f strings"
	# should have been a value <=1, w/o multiplying by 100
	slope = (elevation_gain / distance) 
	return slope

def rate_difficulty(slope: int) -> str:
	"evaluates a given slope against common difficulty ratings for hikes"
	# should have left slope as value <=1 and converted slope rating percents to decimal point
	if slope < 0:
		return 'Not Rated'
	elif slope <= 0.05:
		 return 'Easy'
	elif slope <= 0.10:
		return 'Moderate'
	elif slope <= 0.20:
		return 'Hard'
	else:
		return 'Grueling'

def main() -> None:
	"""
	Main function for trail rater 1.0 program. Prompts user for integers representing the 
	elevation gain in meters and distance in kilometers of a given hike and provides a
	difficulty rating for the hike.
	"""
	print('Training Rater 1.0')
	elevation_gain_m = float(input('Enter the elevation gain in meters: '))
	distance_km = float(input('Enter the distance in kilometers: '))
	distance_m = convert_km_to_m(distance_km)
	
	slope = calculate_slope(elevation_gain_m, distance_m)
	difficulty_rating = rate_difficulty(slope)
	
	print(f'The trail has a slope of {slope: .1%} and is rated {difficulty_rating}')

main()
