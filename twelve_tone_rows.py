__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3 License"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Beta"

import itertools
import random

# Define the 12 tones possible in a 12 tone row
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

c_chords = {
    'Dm7': ["D","F", "A", "C"],
    'G7': ["G", "B", "D", "F"],
    'Cmaj7': ["C", "E", "G", "B"]
}

d_chords = {
    'Dm7': [],
    'D7': [],
    'Dmaj7': []
}

e_chords = {

}

f_chords = {

}

g_chords = {

}

a_chords = {

}

b_chords = {

}

def generate_ii_V_I(key):
    """Generate the 'ii-V-I' chords in a given key."""
    chords = []
    # Define the scale degrees for the 'ii-V-I' progression
    scale_degrees = {'ii': 2, 'V': 5, 'I': 1}
    # Define the chord qualities for each scale degree
    chord_qualities = {'ii': 'm7', 'V': '7', 'I': 'maj7'}
    
    # Generate the chords
    for chord_name, degree in scale_degrees.items():
        # Calculate the note for the chord
        note_index = (degree - 1) % len(key)  # Ensure index wraps around
        note = key[note_index]
        # Append the chord to the list
        chords.append(note + chord_qualities[chord_name])
    
    return chords


def generate_12_tone_rows(length: int):
    """Generate all possible 12-tone rows."""

    # Generate all permutations of the pitch classes
    rows = list(itertools.islice(itertools.permutations(notes), length))
    return rows

def sample_rows(rows: list) -> list:
    sample = []

    for row in rows:
        if bool(random.getrandbits(1)):
            sample.append(row)
    
    return sample

def find_ii_V_I_occurrences(rows):
    """Find the occurrences of 'ii-V-I' chords in the set of 12-tone rows."""
    occurrences = 0
    for row in rows:
        # Convert the row to a list of strings
        row = list(row)
        # Iterate over each possible starting position for the 'ii' chord
        for start_pos in range(12):
            # Extract the subset of notes starting from the current position
            subset = row[start_pos:] + row[:start_pos]
            # Generate the 'ii-V-I' chords for the current key
            for key in notes:
                chords = generate_ii_V_I([note + key for note in subset])
                # Check if the 'ii-V-I' chords occur in the row
                if all(chord in row for chord in chords):
                    occurrences += 1
                    break  # Break out of the loop if found to avoid double counting
    return occurrences

def get_chord_notes(c):
    n = []
    for chords, notes in c_chords.items():
        n.append(notes)  
    
    return n


def has_duplicates(notes: str) -> bool:
    return len(set(notes)) == len(notes)

# TODO: calculate % sample size given rows population total -- 385 for 95 CL, 5 MoE
# TODO: add output details for potential data analysis
if __name__ == "__main__":
    #chords = generate_ii_V_I('D')
    #print(chords)
    row_count = 4500
    matches = 0
    c = get_chord_notes(c_chords)
    #print(c)

    rows = generate_12_tone_rows(row_count)
    sample = sample_rows(rows)

    for row in sample: #rows:
        #print("Searching row :", row)
        r = ''.join(row)

        # turn row to string
        for element in itertools.product(*c):
            # turn element to string
            sequence = ''.join(element)
            #print("Searching {} for {}".format(r, sequence))
            # search for substring (element) in row (string)
            if sequence in r and has_duplicates(sequence):
                print("{};{}".format(element, row))
                matches += 1

    print("Total row count is: ", row_count)
    print("Total sample size is: ", len(sample))
    print("Total number of matches: ", matches)
        
    """
        # this block will check all notes from a chord are a subset of the row
        for chord, notes in c_chords.items():
            if set(notes).issubset(row):
                print("{} from {} present in {}".format(notes, chord, row))
    """

    """
        # this will give us the non-unique note combinations of the chords
        chords = [["D","F", "A", "C"],["G", "B", "D", "F"], ["C", "E", "G", "B"]]
        for element in itertools.product(*chords):
            print(element)
        
    """