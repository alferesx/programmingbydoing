#capacidade de carros
cars=100
#quantidade de espaço dentro do carro
space_in_a_car =4
#numero de motoristas disponiveis
drivers = 30
#Numero de passageiros disponiveis
passengers = 90
#Calculo para saber a quantidade de carros que não tem motoristas
cars_not_driven = cars - drivers
#quantidade de motoristas que estao dirigindo
cars_driven = drivers

#Calculo para saber quantas pessoas eles podem transportar
carpool_capacity = cars_driven * space_in_a_car

#Media de passageiros por carro
average_passengers_per_car = passengers / cars_driven

print("There are " + str(cars) + " cars available.")
print("There are only " + str(drivers) + " drives available.")
print("There will be " + str(cars_not_driven) + " empty cars today.")
print("We can transport " + str(carpool_capacity) + " people today")
print("We have " + str(passengers) + " to carpool today")
print("We need to put about " + str(average_passengers_per_car) + " in each car")
