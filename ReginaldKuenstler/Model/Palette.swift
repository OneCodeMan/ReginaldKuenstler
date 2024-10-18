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
    var hexCode: String
    var uiColor: UIColor
}

struct Palette {
    var title: String
    var colours: [PaletteColour] = []
}
