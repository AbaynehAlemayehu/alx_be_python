# weather_advice.py

weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
git add control-flow/weather_advice.py
git commit -m "Add weather_advice.py script with clothing recommendations"
