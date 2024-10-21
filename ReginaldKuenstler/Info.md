#  DEVLOG

## Backlog
- For missed connections, estimate the mixes of colour one would need to make that colour from the palette.
- Given an input of about 7 images, generate the least amount of colours needed to make a palette.

..

## Diary

# October 21, 2024
- User should be able to select their palette.

TODOs:
- Create the PaletteSelectionView
    - [ ] Disable selection on colours already owned. Or should we remove them?
        - Fuck. `isUserOwned` logic is wonky. We never set it properly.
    - [ ] Reset the user palette without having to restart the app. On navigation back to it from the select palette form, it should be populated after we click the "save" button.
- Successfully flow back to user palette page.


# October 20, 2024 (Sunday)
It's a cold Sunday to complain.

Next steps:
- ColourComparison: Involve `UserPalette`
    - Only show "Your Palette" if user has a palette. Otherwise completely remove it.
    - Find connections between generated colours and user palette.
    - For missed connections, estimate the mixes of colour one would need to make that colour from the palette.
    
    

- Given an input of about 7 images, generate the least amount of colours needed to make a palette.

----------------------

UPDATE: Was easy thanks to previous projects. Timer App, Itinerario and NRC clone helped me figure these out. we move on.

Action items for today:
- Create the palette display (data and view)
    - Allow searchability
- Start work on user palette functionality (UI forms can be skipped)
    - UserPalette:
        - title of palette
        - [colours] = (hex_code)

# October 18, 2024 (Friday)
10:23 P.M.
I think this is how we get user palette to work:
- Create `UserPaletteViewModel` and `PaletteViewModel`

- User chooses from colour map to create their palette. (`UserPalette`)
- Use the hex codes gathered from `ColourInfo.estimatedColour` to match hex codes with colours in user palette.
- `fromYourPalette = set_union(ColourInfo.estimatedColourHexCodes, userPalette.hexCodes)
- Enhancement: Add a way to suggest how to mix two (or more) colours to get to a certain colour.

# October 17, 2024 (Thursday)
The fucking thing I was stuck on (using a populated map to analyze my image with Vibrant which kept being empty) 
was just a matter of changing `@State` to `@Published` on a ViewModel property. Fuck.

On deck:
- Combine the view/functionality that gets the image input with the view/functionality for analyzing it and spitting back results out
- Make it flow better.

Then later user can create their own palette.

# October 16, 2024 (Wednesday)

Started the project today.
Next thing I'm curious about is how to take in image as user input.

later on, it'll be things like...
how to use userdefaults or swiftdata to store custom palette

Might need this:
https://www.hackingwithswift.com/quick-start/concurrency/how-to-use-mainactor-to-run-code-on-the-main-queue

