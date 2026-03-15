

def main():

    time = input("What time is it? ")

    #we call the convert method so that we can change the time string into a float and the format of the hours
    time_to_eat = convert(time)

    if 7 <= time_to_eat <= 8:
        print("Breakfast time")
    elif 12 <= time_to_eat <= 13:
        print("Lunch time")
    if 18 <= time_to_eat <= 19:
        print("Dinner time")


def convert(time):

    #splits the input when it see's the colon and I assign the first split as hours and the second one as minutes
    hr, mins = time.split(":")

    #turn them into floats
    hr = float(hr)
    mins = float(mins)

    #should return in hours so divide the minuntes by 60 so it can be (ex: .5 or .2 hours)
    return hr + (mins/60)



if __name__ == "__main__":
    main()
