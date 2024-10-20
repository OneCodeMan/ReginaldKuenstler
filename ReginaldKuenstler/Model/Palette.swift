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
struct PaletteColour {
    var colourName: String
    
    // used for display
    var hexCode: String
    var uiColor: UIColor
    
    // user info
    var isUserFavorite: Bool = false
    var isUserOwned: Bool = false // does user own it in a palette?
}

struct Palette {
    var title: String = ""
    var colours: [PaletteColour] = []
}

extension Palette {
    static let mockPalette = [
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
//        PaletteColour(colourName: "", hexCode: <#T##String#>, uiColor: <#T##UIColor#>, isUserFavorite: <#T##Bool#>, isUserOwned: <#T##Bool#>),
    ]
}
