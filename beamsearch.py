import numpy as np

# Define the beam search function
def beam_search(start_sequence, max_length, beam_width, transition_probabilities):
    # Initialize the beam with the start sequence and its probability
    beam = [(start_sequence, 1.0)]
    
    # Iterate until we reach the maximum length
    for _ in range(max_length):
        # Create an empty list to store new candidates
        new_beam = []
        
        # Expand each candidate in the current beam
        for sequence, probability in beam:
            # Get the last token in the sequence
            last_token = sequence[-1]
            
            # Get the transition probabilities for the next token
            next_token_probs = transition_probabilities[last_token]
            
            # Sort the next tokens based on their probabilities
            sorted_tokens = sorted(next_token_probs.items(), key=lambda x: x[1], reverse=True)
            
            # Take only the top candidates based on the beam width
            top_candidates = sorted_tokens[:beam_width]
            
            # Generate new sequences by appending each token to the current sequence
            for token, token_prob in top_candidates:
                new_sequence = sequence + [token]
                new_probability = probability * token_prob
                new_beam.append((new_sequence, new_probability))
        
        # Sort the new candidates based on their probabilities
        new_beam = sorted(new_beam, key=lambda x: x[1], reverse=True)
        
        # Take only the top candidates based on the beam width
        beam = new_beam[:beam_width]
    
    # Return the top sequence from the final beam
    return beam[0][0]

# Example transition probabilities (just for demonstration)
transition_probs = {
    'start': {'A': 0.7, 'B': 0.2, 'C': 0.1},
    'A': {'D': 0.6, 'E': 0.3, 'F': 0.1},
    'B': {'G': 0.4, 'H': 0.3, 'I': 0.3},
    'C': {'J': 0.5, 'K': 0.4, 'L': 0.1},
    'D': {'M': 0.8, 'N': 0.1, 'O': 0.1},
    # Add more transition probabilities as needed...
}

# Define parameters
start_sequence = ['start']
max_length = 5
beam_width = 2

# Perform beam search
result = beam_search(start_sequence, max_length, beam_width, transition_probs)
print("Generated sequence:", result)