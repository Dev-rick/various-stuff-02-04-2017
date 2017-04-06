# -*- coding: utf-8 -*-


hair_colors = {
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC"
}

facial_shapes = {
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA"
}

eye_colors = {
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC"
}

genders = {
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC"
}

races = {
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG"
}

suspects = {
    "Eva":["Female", "White", "Blonde", "Blue", "Oval"],

    "Larisa":["Female", "White", "Brown", "Brown", "Oval"],

    "Matej":["Male","White","Black","Blue","Oval"],

    "Miha":["Male", "White", "Brown", "Green", "Square"]

}


def result_gender(searched_dna, genders, criminal):
    for gender in genders:
        if searched_dna.find(genders[gender]) > -1: #mit find hinter einem string object, wird in diesem str nach dem str in der Klammer gesucht und wenn dieser gefunden wurde gibt Python eine positive Zahl wieder.
            criminal.append(gender)
            return "The criminal has the folowing gender: %s" % gender


def result_race(searched_dna, races, criminal):
    for race in races:
        if searched_dna.find(races[race]) > -1:
            criminal.append(race)
            return "The criminal has the following race: %s" % race

def result_hair_color(searched_dna, hair_colors, criminal):
    for hair_color in hair_colors:
        if searched_dna.find(hair_colors[hair_color]) > -1:
            criminal.append(hair_color)
            return "The criminal has the following hair color: %s" % hair_color

def result_eye_color(searched_dna, eye_colors, criminal):
    for eye_color in eye_colors:
        if searched_dna.find(eye_colors[eye_color]) > -1:
            criminal.append(eye_color)
            return "The criminal has the following eye color: %s" % eye_color

def result_facial_shape(searched_dna, facial_shapes, criminal):
    for facial_shape in facial_shapes:
        if searched_dna.find(facial_shapes[facial_shape]) > -1:
            criminal.append(facial_shape)
            return "The criminal has the following facial shape: %s" % facial_shape

def result_suspect(suspects, criminal):
    for suspect in suspects: #i ist hier ein str, passt sich immer dem Inhalt (hier ein dict, also strings) an.
        if suspects[suspect] == criminal: #Mit suspects[i] greife ich auf die verschiedenen Listen im dict zu!
            return "Your criminal is: %s" % suspect



