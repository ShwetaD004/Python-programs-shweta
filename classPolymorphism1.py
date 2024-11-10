
class India:
    def capital(self):
        print("New Delhi is capital of India.")

class USA:
    def capital(self):
        print("Washington is capital of USA")

ind=India()
usa=USA()
for country in(ind,usa):
    country.capital()