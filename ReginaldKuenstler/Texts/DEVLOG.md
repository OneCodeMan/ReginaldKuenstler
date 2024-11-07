#  DEVLOG

**MIGHT GO DOWN AS G.O.D**
[APP LOGO](https://imgur.com/m9Fb9lp)
# Design Questions // Next Steps
- Big Picture UX
    - When user opens app not first time, should open to previous tab they were in.
- Palette Colour Lists
    - Should be grouped RGB first, not alphabetically. Makes sense in this context.
- UserPaletteView
    - How do we make it more obvious that the user can edit their palette?
        - Long press on an item is synonymous to deleting apps on the iPhone, I assume user would make the connection.
            - Bad assumption.
    - Floating menu on the right of the screen. Each menu item is a circle of different colour.
        - User can tap on any of these circles to quickscroll to a certain colour group of their palette. Instead of scrolling so much.
- PaletteCreationView
    - After `Save Selected Colours` tap, there should be a confirmation popup with info on colours selected.
        - Same style as the palette colour lists.
    - It would be cool to make the select state highlight overlay not blue, but the colour group highlight of that selected colour.
        - e.g. user selects `Cadmium Red`, the select state background overlay is not blue, but rather a red.
        - e.g. the select state for `Pastel green` would be a green background overlay
        - e.g. for `Other` or other complicated scenarios, just use `.gray`
- ColourAnalysisView
    - When user taps on a single colour in the Swatch, should there be a popup view with more details on that colour?
        - e.g. similar colours to that selected single colour, maybe the user can choose out of those alternatives and replace that swatch colour.
    - If the user lacks a direct colour match, try to see if the user has a colour in the same group as that colour.
        - e.g. user has cadmium red, analysis detects alizarin crimson. `From Your Palette` shows `Cadmium Red`
            - but there should be an indicator that it is NOT a _DIRECT_ match, but rather, it is a _CLOSE_ match.
- Revisit Onboarding View.

- ~*Enhancements*~
    - User can add a bunch of images and get an AveragePalette for those images.
        - User can easily delete/add more images
    - User can take pictures of their paints to create their palette, fuck the palette creation form.
        - Accept UIImage as input and detect with SwiftVibrantium
        
# CASE STUDY -- A UI/UX Perspective
 TODO

# Main Challenges

*What is the problem we're trying to solve?*
This is the most important q from a product dev perspective. Never neglect this part.

*What is the best way to take user input in this context?*
- They take pics of their paints.
- There is a catalog in app consisting directly of the products of specific brands (W&N, VG, MM)

*How do we create the best data model for the palette detector?*
i.e. how do we make sure that it analyzes all possible hex codes that "Cadmium Red" can be?

*How do we optimize the image analyzer?*
so much shit to think about


# Personal Diary

## Backlog
- For missed connections, estimate the mixes of colour one would need to make that colour from the palette.
- Given an input of about 7 images, generate the least amount of colours needed to make a palette.
..

# POST MVP

## PREMIUM
- [ ] Multi select images, determine average palette, but also individual palette.
    - [ ] User can easily delete/re-add images and it's dynamic
- [ ] User can add palette colours with photos input (they take pics of their paints)
- [ ] Historical data of inputs and analyses

## ENHANCEMENTS
- [ ] IMPLEMENT AD MOB
- [ ] On UserPalette and PaletteCreation vertical center, to the right, there is a vertical menu of Circle() colour groups.
- [ ] Colour mapper can be better
- [ ] Select state rectangle matches colour of selected colour group
- [ ] SelectPaletteView - toast that indicates which colour has been added
- [ ] Sort by RGB

## LOW HANGING FRUIT
- [ ] Palette Creation - User can tap on Selected Colours to open a sheet of what colours they've selected so far.
- [ ] Make a widget that displays the last palette created.
- [ ] Alerts should have font (https://www.hackingwithswift.com/forums/swiftui/why-does-this-alert-code-not-show-colors/19662)

## QUESTIONS
- Should the imageview itself be tappable to open imagepicker menu?

------------------------------------------------------------------------------------------------------------------------
# TO PRODUCT MVP

### Wave 2 to MVP -- Beat the spaghetti code allegations.
- [ ] One big code cleanup

### Wave 3 to MVP -- MARKETING
- [ ] Create website
- [ ] Create screenshots
- [ ] Create demo video

### WAVE 5 -- THE DEPLOYMENT
- [ ] Deploy app.

### Wave 5.5 -- Post-deployment -- FINAL WAVE
- [ ] Create a fastlane file for deployment
- [ ] Create tickets for future steps.
- [ ] Write documentation for future devs.

And you should be done.

Suggestions:
- Should we add a floating bottom right button on UserPalette to toggle Edit view? Is long press not obvious enough?
------------------------------------------------------------------------------------------------------------------------

# Wave 2
## (November 1, 2024 -- ????)

That new new

### Wave 2.1
- [ ] Multi-select.
    - [ ] Group the colours in MinimumPalette like we do in colour selection
    - [ ] Top left button on each image to delete them from the list.
    - [ ] Show the most common colours at beginning.
...
- [ ] Palette of the Greats
    - [ ] Detail View
        - [x] Add AveragePalette to bottom of DetailView
        - [ ] Information on: birth date to death date
        - [ ] Add real avg. palette data
            - We should hard-code it... It's gonna be the same images all the time and we'd be doing the same calcs all the time..
...
- [ ] ColourComparisonView & Widget
    - [ ] Add Widget of last generated swatch
        How do we store that data?
        https://www.createwithswift.com/adding-a-widget-to-a-swiftui-app/
...
- [ ] An Attempt At Better User Input #1
    - [x] Merge the colour maps
    - [ ] On "Detected Colours", mark colours user already has
    - [ ] Add multi-select image option like Instagram.
    - [ ] On "Detected Colours"/"Add to Palette", allow user to add/delete colours.
    - [ ] Be able to detect misspellings//missing letters
...
- [ ] A better loading screen
    - The progression of an artwork being drawn and coloured.
        - Going from partially to fully coloured.
    - Ideally 2-3 of these.
        - Munch prelim
        - Matisse prelim

### Wave 2.2
- [ ] ???
- [ ] ???
- [ ] ???
- [ ] ???
- [ ] ???
- [ ] ??

### Wave 2.3
- [ ] ???
- [ ] ???
- [ ] ???
- [ ] ???
- [ ] ???
- [ ] ??


## Resources // R&D

## Palette of the greats
scrolling behaviour
https://stackoverflow.com/questions/78789315/how-to-infinitely-loop-and-move-image-in-swiftui-in-intervals
https://stackoverflow.com/questions/70630776/get-first-visible-index-from-lazyhstack-in-swiftui

### user input

### Catalog

Scrape this website for all colours
https://sensuallogic.com/artistcolordata

this too:
https://artistpigments.org/mediums/oil_pastel

Our colourMap will look like this:
```
[
"Black": [RGB1, RGB2, RGB3, RGB4],
"Burnt Umber": [RGB1, RGB2, RGB3, RGB4],
...
]
```

Notes:
- When we iterate through colours, we'll consider multiple RGB values for one.
  - Then later, we could narrow the input down to the brand maybe.
- Find a way to make colourMap store which store the RGB info is from, or make a separate colourMap for this. `brandMap`
- On text detection, try to detect the brand, and narrow


--------



Text recognition
https://medium.com/@jakir/text-recognition-or-ocr-using-vision-framework-ios-swiftui-b9c5df36ec32


Make a CoreML model to detect images? take a stab at it?

https://medium.com/@ssbrswm/how-to-create-a-coreml-model-with-the-createml-app-d9a84d626b58
https://developer.apple.com/documentation/coreml/getting-a-core-ml-model
https://apple.github.io/coremltools/docs-guides/source/introductory-quickstart.html

https://www.montmarte.com/collections/oil-pastels
- possibly can scrape, look at colours under "additional details" each page.

https://www.winsornewton.com/en-ca/collections/artists-oil?sort_by=title-ascending
https://www.winsornewton.com/en-ca/collections/cotman-watercolour
- load entire thing

# History

## November 7, 2024
- [x] BUGFIX: Some hex codes are over 255. Do it in Go. clean the catalog. not the sanitized data.
- [x] Re-design colour mapper to consumerist-facing
    - [x] Extract the colours from the product catalogs themselves, build mapper with that.
        - [x] From W&N, Mont Marte, etc.
- [x] An Attempt At Better User Input #2
    - [x] Create in-app "catalog", scraped data of INDIVIDUAL PAINTS
    - [x] Read from catalog.json, and parse
    - [x] Make VColour objects or something else out of those catalog items

## November 6, 2024
- [ ] Multi-select
    - [x] The individual palette breakdown for each image, make that a detail view for the images themselves

- [ ] Palette of the Greats
    - [x] More data
    - [x] https://www.tumblr.com/tagged/ettore%20tito

- [x] Better User Input #1 : Text Recognition and Matching
    - [x] Can we recognize text given an image?
    - [x] Can we extract the text we want?
    - [x] If we can detect an exact match of text on a line, we got it.

## November 5, 2024
PogS
    - [x] All assets filled.
    - [x] What if we enable auto scroll?
    - [x] List View
        - [x] Style List View Item
            - [x] Add portrait of each artist.

## November 4, 2024
    - [x] Add the Minimum Palette


------------------------------------------------------------------------------------------------------------------------
# Wave 1
### BULK
### history

### October 31, 2024

### Wave 1 to MVP (BULK!!)
- [x] Update image analysis view to have updated user palette so it can analyze colours properly (i tried)

### October 30, 2024
- [x] BUGFIX: Unknown detected colours on app start and analysis is first action.
    - Declare a shared instance of `ColourMapper` before any important view is loaded to populate `colourMap`.
- [x] Set up Localization
- [x] Localize at least 7 strings.
- [x] Revisit colour grouper to first group by names and then by rgb. 2 separate if statements.
- [x] Loading screen should have descriptive text on what is loading.
    - Instead of `Loading..`, make it `Creating Palette...`, `Generating Swatch...`
- [x] Revisit colour mapper so that it only fetches once on entire app run.
- [x] Clean up UserDefaults palette part 1.

### October 29, 2024
- [x] Onboarding view (https://www.youtube.com/watch?v=EZzTFbbiEls)
- [x] Onboarding flow
- [x] Add a general typeface
- [x] On `SaveSelectedColours` loading, hide top tab bar buttons on left and right, and hide the tab view.
- [x] Delete on UserPalette search does not delete item. Disable/hide search on Edit state?
- [x] UserPalette -> Top left tab bar button to Clear All with confirmation alert
- [x] When image analysis is processing, hide the bottom tab bar?
- [x] Disable `Analyze` button if `self.image` already has been Analyzed, just simply slide.
- [x] Fix word wrap on palette select items
- [x] ColourComparison - User can tap on image view to access image picker.

### October 28, 2024
- [x] Create app logo
- [x] Create App Launch screen
- [x] PaletteCreationView
    - [x] When selectedColours is not empty and user taps back button (to `Your Palette`), 
        have a confirmation "are u sure u wanna exit?"
- [x] Change styling of `Save Selected Colours`
- [x] `Save selected colours` button press -- "are you sure you want to save?" alert window
- [x] Loading screen after `Save selected colours`
..
- [x] Analyze View - placeholder imageview
- [x] Analyze View - Disable tab scrolling if no image input.
- [x] Analyze View - Button styling on Analyze View needs work.
..
- [x] Analyze View - Logic for "Detected Colours" if nothing from user palette.
    - [x] If nothing from user palette, make the entire thing full page
..
- [x] Pimped out loading views
..
- [x] Alert States
    - [x] "Save Selected Colours" with no selectedColours
    - [x] "Analyze" with no inputImage
...
- [x] On edit, keep the palette select items wiggling.
- [x] Analyze View - Asking for photo change text
- [x] Tab View -- change icons
...

### October 27, 2024
- [x] Fix colourName Text() overlap
- [x] Add select state on user palette creation.
    - [x] Select state rectangle corners rounded
- [x] SelectPaletteView - clear selection top right bar button
...
- [x] Dark mode vs. light mode, generate appropriate text.
- [x] Search functionality, get that shit done.
    - [x] on creation view
    - [x] on user palette view
- [x] UserPaletteView search states
    - [x] non-empty palette but search term is empty
    - [x] empty palette (don't view search at all?)
- [x] SelectPaletteView states
    - [x] on tap of colourItem already userOwned display alert.
- [x] On "Done" edit user palette state, animate the state change.


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



