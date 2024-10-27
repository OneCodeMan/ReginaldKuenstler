#  DEVLOG

## Backlog
- For missed connections, estimate the mixes of colour one would need to make that colour from the palette.
- Given an input of about 7 images, generate the least amount of colours needed to make a palette.

..

# Diary

## POST MVP
- [ ] Multi select imagess, average palette.
    - [ ] User can easily delete/re-add images and it's dynamic
- [ ] Vertical center to the right there is a vertical menu of Circle() colour groups.
- [ ] Colour mapper can be better

## BIG BATCH TO MVP

### MARKETING
- [ ] Create app logo
- [ ] Create website
- [ ] Create screenshots
- [ ] Create demo video

### BULK

### Wave 1 to MVP
- [x] Add select state on user palette creation.
    - [ ] Select state rectangle corners rounded
    - [ ] Select state rectangle matches colour of selected colour group
- [x] Dark mode vs. light mode, generate appropriate text.
- [ ] Search functionality, get that shit done.
    - [x] on creation view
    - [ ] on user palette view
- [ ] Buttons styling on Analyze View needs work.
- [ ] On "Done" edit user palette state, animate the state change.
- [ ] Consider removing "Detected Colours" if nothing from user palette.
- [ ] Analyze View - Asking for photo change text
- [ ] Tab View -- change icon

### Wave 2 to MVP
- [ ] IMPLEMENT AD MOB
- [ ] Revisit the colour grouper.

### Wave 3 to MVP -- Beat the spaghetti code allegations.
- [ ] On another branch, one big code cleanup
- [ ] And then two small code cleanups
- [ ] Then one more big code cleanup



## DONE -- ON DECK
- [x] Fix select state on `PaletteCreationView`, currently lacks one.
- [ ] Make search functionality work with everything else.
- [ ] Fix mixed colours how they're presented.

## October 25, 2024
- [x] Alert on deletion (are you sure)
- [ ] ???

## October 24, 2024
This morning, I worked on the ProgressView() between Analysis. And the colour mixing logic, preliminary.
On deck for later:
- [x] Fix app crash on user palette item deletion

## October 22, 2024
Next steps is perfecting these items:
- [ ] Colour estimation for analysis
    - [ ] Have a mock user palette ready
    - [ ] Have mock image inputs that partially generate colours the user has.
- [x] Colour Analysis carousel view
- [x] Top tab bar button item for `UserPalette` edit state, or long press on any PaletteColourItem, and the user can delete or rearrange grid items.
- [x] Group PaletteColourItems by colour

## October 21, 2024
- User should be able to select their palette.

TODOs low hanging fruit:
- [ ] The coloursSelectedView should be able to wrap overflow.

TODOs next next wave:
- [ ] User can save analyzed pieces

TODOs next wave:
- [ ] Colour Analysis carousel view
- [ ] Top tab bar button item for `UserPalette` edit state, or long press on any PaletteColourItem, and the user can delete or rearrange grid items.
- [ ] Group PaletteColourItems by colour
- [ ] Colour estimation for Analysis

TODOs:
- Create the PaletteSelectionView
    - [x] Disable selection on colours already owned. Or should we remove them?
        - Fuck. `isUserOwned` logic is wonky. We never set it properly.
    - [x] Reset the user palette without having to restart the app. On navigation back to it from the select palette form, it should be populated after we click the "save" button.
    - [x] Go back to UserPalette page on button tap
    ...
    - [x] Float button on top of tab bar.
    - [x] While user is on select page, give information on what they've selected so far.
    ...
    - [x] Disable button when user hasn't selected any colour

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

