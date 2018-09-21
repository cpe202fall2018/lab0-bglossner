def weight_on_planets():
    response = input("What do you weigh on earth? ")
    number = float(response)
    print("\nOn Mars you would weigh {} pounds.".format(number * 0.38) + "\nOn Jupiter you would weigh {} pounds.".format(number * 2.34))
                                                                                                           
if __name__ == '__main__':
   weight_on_planets()
