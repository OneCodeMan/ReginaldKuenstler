# Pinselton

<img width="300" alt="appplogoo" src="https://github.com/user-attachments/assets/7804ba34-0fbf-422e-89f1-271141e02929">

**You have some paints, and you have something you want to paint... but you don't know which paints to use! Pinselton does.**

## Version 0.2
wip
- pimped out onboarding view
- multi-select images, average swatch calculation
- user can take pics of their paints as input
   - or they can input direct products from Winsor & Newton, Mont Marte, Van Gogh, etc
   - and app makes the user palette using that data
- the user can use a colour picker to point to where in the image to detect the colour
  - (meaning the generatedSwatch is editable after generation)
  - because what if there's a spot in the image not accounted for in swatch generation?
- "Palette of the Greats"
  - a list containing the AverageSwatch of famous artists based on their top 10-20 paintings.
  - Caravaggio, Monet, VG, Rembrandt, Matisse, Female Artist 1, Female Artist 2, Female Artist 3
  - AsyncImage to avoid copyright issues
    - This means internet would need to be on
    - error states for no internet connection needed
- A Widget view of last generated palette
  - just for fun

## Version 0.1

https://github.com/user-attachments/assets/bcab9f3d-f222-4154-bf38-72a2776c06b0

