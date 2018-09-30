#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
	with open(filename) as sample:
		csvreader = csv.reader(sample,delimiter = ',')
		line_count = 0
		resultarray = []
		resultarray[0:24] = [0] * 24
		for row in csvreader:
			if line_count == 0:
				line_count += 1
			else:
				if row[1] != "":
					row[1] = row[1].replace(":", " ")
					time = [int(s) for s in row[1].split() if s.isdigit()]
					if len(time) == 2:
						if time[0] == 24:
							time[0] = 0
						if time[0] < 24:
							resultarray[time[0]] += 1
		return resultarray


def weigh_pokemons(filename, weight):
	with open(filename) as sample:
		fullList = json.load(sample)
		pokemonList = fullList["pokemon"];
		result = list()
		for individual in pokemonList:
			textweight = individual["weight"]
			textweight = textweight.replace(":", " ")
			weighta = float(textweight.split()[0])
			if weighta == weight:
				result.append(individual["name"])
		return result
		

def single_type_candy_count(filename):
	with open(filename) as sample:
		fullList = json.load(sample)
		pokemonList = fullList["pokemon"];
		totalcandy = 0
		for individual in pokemonList:
			if 'candy_count' in individual and len(individual["type"]) == 1:
				candy = individual["candy_count"]
				totalcandy += candy
			else:
				totalcandy += 0
		return totalcandy
		

def reflections_and_projections(points):
	result = [[],[]]
	for i in range(0, len(points[0])):
		distTo1 = points[1][i] - 1
		points[1][i] = -2 * distTo1 + points[1][i]
		tempY = points[1][i]
		points[1][i] = points[0][i]
		points[0][i] = -1*tempY
		newX = (points[0][i] + 3*points[1][i])/10
		newY = (3*points[0][i] + 9*points[1][i])/10
		result[0].append(newX)
		result[1].append(newY)
	return np.array(result)

def normalizeFunction(point, max, min):
	return 255*(point-min)/(max-min)

def normalize(image):
	max = np.amax(image)
	min = np.amin(image)
	return normalizeFunction(image, max, min)

def sigmoid_normalize(image, variance):
	image = np.floor(255*(1+math.e**(-1*(variance**(-1))*(image - 128)))**-1)
	return image