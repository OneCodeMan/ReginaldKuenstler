#  Test Runs

To make sure the app still works as expected after changes.

# Analyzer

## When user analyzes an image and gets to `Detected Colours`, and then updates their palette, the `From Your Palette` on `Detected Colours` should update accordingly.

### Scenario 1
I analyze an image that detecs Teal, Charcoal, and Puce, 3 colours in my palette.
I navigate to my palette to delete those colours.
I go back to `Detected Colours`.
Expectation: `From Your Palette` is gone because those colours are no longer in my palette.

### Scenario 2
I analyze an image that detecs Ochre, Burnt Umber, and Tan, 3 colours NOT in my palette.
I go to `Your Palette` and add these colours to my palette.
I go back to `Detected Colours`.
Expectation: `From Your Palette` appears with Ochre, Burnt Umber, and Tan.
