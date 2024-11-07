//
//  Palette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation
import SwiftUI

/**
 Information on what to display to the user.
  PaletteColours are made of VColours from the map.
 */
struct PaletteColour: Identifiable, Equatable, Hashable {
    static func == (lhs: PaletteColour, rhs: PaletteColour) -> Bool {
        (lhs.id == rhs.id) &&
        (lhs.colourName == rhs.colourName) &&
        (lhs.hexCode == rhs.hexCode)
    }
    
    var id = UUID()
    
    var colourName: String
    private var colourBrand: String?
    
    // used for display
    var hexCode: String
    var uiColour: UIColor = .yellow // TODO: create this out of init?
    var rgbCode: RGBTuple = RGBTuple(r: 0, g: 0, b: 0) // TODO: create a default value and reference that. DRY.
    
    // user info
    var isUserFavorite: Bool = false
    var isUserOwned: Bool // does user own it in a palette?
    
    /**
     Default initializer.
     */
    init(colourName: String, hexCode: String, isUserOwned: Bool = false) {
        self.colourName = colourName
        self.hexCode = hexCode
        self.uiColour = UIColor.init(hex: hexCode)
        self.rgbCode = ColourHelper.hexToRGB(hex: hexCode)
        self.isUserOwned = isUserOwned
    }
    
    /**
     Create a PaletteColour from a VColour
     */
    init(fromVColour vColour: VColour) {
        self.colourName = vColour.name
        self.hexCode = vColour.hexCode
        self.uiColour = vColour.uiColour
        self.rgbCode = vColour.rgbCode
        self.isUserOwned = false
    }
    
    init(fromCatalogColour catalogColour: CatalogColour, isUserOwned: Bool = false) {
        self.colourName = catalogColour.name
        self.colourBrand = catalogColour.brand
        
        if catalogColour.rgb.count == 3 {
            self.rgbCode = RGBTuple(r: catalogColour.rgb[0], g: catalogColour.rgb[1], b: catalogColour.rgb[2])
            self.hexCode = ColourHelper.rgbToHex(rgbCode)
            self.uiColour = UIColor.init(hex: hexCode)
            self.isUserOwned = isUserOwned
        } else {
            self.rgbCode = RGBTuple(r: 0, g: 0, b: 0)
            self.hexCode = ColourHelper.rgbToHex(rgbCode)
            self.uiColour = UIColor.init(hex: hexCode)
            self.isUserOwned = isUserOwned
        }
        
    }
    
    
    init() {
        self.colourName = "Midnight Blue (default init)"
        self.hexCode = "#191970" // midnight blue
        self.isUserOwned = false
    }
    
    mutating func toggleIsUserOwned() {
        self.isUserOwned.toggle()
    }
}

struct Palette: Hashable {
    var title: String = ""
    var colours: [PaletteColour] = []
    
    init() {
        self.title = "Initial Palette Title"
        self.colours = Palette.mockPalette.colours
    }
    
    init(title: String = "", colours: [PaletteColour]) {
        self.title = title
        self.colours = colours
    }
}


/**
 Has a list of artworks `artworks`,
 the `entirePalette` (all colours needed to make all artworks combined),
 the minimum # of colours `minimumPalette` needed to make those paintings (a set(entirePalette))
 */
// TODO: Later this should have "essentialPalette"
struct MultipleArtworksPalette {
    var artworks: [Artwork] = []
    var minimumPalette: [PaletteColour] = []
    var entirePalette: [PaletteColour] = []
    
    var essentialPalette: [PaletteColour] = [] // most frequent colours
    var collectionCounter: [(PaletteColour, Int)] = []
}


// MARK: MOCK DATA
extension Palette {
    static let mockPalette: Palette = Palette(title: "mock palette 1", colours: [
        PaletteColour(colourName: "Midnight Blue", hexCode: "#191970"),
        PaletteColour(colourName: "Sienna", hexCode: "#A0522D"),
        PaletteColour(colourName: "Cobalt Blue", hexCode: "#0047AB"),
        PaletteColour(colourName: "Cadmium Red", hexCode: "#D22B2B"),
        PaletteColour(colourName: "Cadmium Yellow", hexCode: "#FDDA0D"),
        PaletteColour(colourName: "Example Colour", hexCode: "#FDDA00"),
        PaletteColour(colourName: "Example Colour1", hexCode: "#BDDA0D"),
        PaletteColour(colourName: "Example Colour2", hexCode: "#0DDA0D"),
        PaletteColour(colourName: "Example Colour3", hexCode: "#FBBA0D")
    ])
}
