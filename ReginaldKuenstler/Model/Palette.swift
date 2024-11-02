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
struct PaletteColour: Identifiable, Equatable {
    static func == (lhs: PaletteColour, rhs: PaletteColour) -> Bool {
        (lhs.colourName == rhs.colourName) &&
        (lhs.hexCode == rhs.hexCode)
    }
    
    var id = UUID()
    
    var colourName: String
    
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
    
    mutating func toggleIsUserOwned() {
        self.isUserOwned.toggle()
    }
}

struct Palette {
    var title: String = ""
    var colours: [PaletteColour] = []
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
    static let mockPalette: [PaletteColour] = [
        PaletteColour(colourName: "Midnight Blue", hexCode: "#191970"),
        PaletteColour(colourName: "Sienna", hexCode: "#A0522D"),
        PaletteColour(colourName: "Cobalt Blue", hexCode: "#0047AB"),
        PaletteColour(colourName: "Cadmium Red", hexCode: "#D22B2B"),
        PaletteColour(colourName: "Cadmium Yellow", hexCode: "##FDDA0D")
        
    ]
}
