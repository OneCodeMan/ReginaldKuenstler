#  DEVLOG

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

