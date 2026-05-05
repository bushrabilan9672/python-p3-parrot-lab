#!/usr/bin/env python3

def parrot(phrase=None):
    """Prints the phrase (or "Squawk!" if no phrase given) and returns the phrase"""
    # Determine what to print/return
    output = phrase if phrase is not None else "Squawk!"
    
    # Print the output
    print(output)
    
    # Return the output
    return output