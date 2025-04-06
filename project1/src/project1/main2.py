from crewai.flow.flow import Flow, start, listen, router
from litellm import completion
from pydantic import BaseModel

# Define API_KEY as a constant (either global or as a class attribute)
API_KEY = "AIzaSyC75m6TCr1cNKUy_wlI74ngwk9rjxlg7JA"

class MyFlow(Flow):

    @start()
    def generate_random_car(self):
        # Request a random car name using the Gemini Flash model
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{
                "content": "Return any random car name from world.",
                "role": "user"
            }]
        )
        car = result['choices'][0]['message']['content']
        print(car)
        return car

    @router(generate_random_car)
    def process_city_name(self, car_name: str):
        print(f"THIS IS YOUR CAR NAME: {car_name}")
        # Compare directly to the string "BMW"
        if car_name == "BMW":
            print("This is BMW")
        else:
            # If needed, store the car name as an instance variable
            self.car_name = car_name
            print("This is other car")

    @listen("This_is_BMW")
    def save_car_name(self, car_name: str):
        bmw = f"Tell me in detail {car_name}"
        return bmw

    @listen("This is other car")
    def save_car(self, car_name: str):
        other = f"Tell me in detail {car_name}"
        return other

def test_router():
    flow = MyFlow()
    flow.kickoff()

if __name__ == "__main__":
    test_router()

