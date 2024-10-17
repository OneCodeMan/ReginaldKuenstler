//
//  ColourPair.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation
import SwiftUI

typealias RGBTuple = (r: Int, g: Int, b: Int)

// MARK: ColourPair
struct ColourPair {
    let name: String // Indigo, Viridian
    let type: String // Vibrant, Muted, etc
    let actualColourInfo: ColourInfo
    let estimatedColourInfo: ColourInfo
}

// MARK: ColourInfo
struct ColourInfo {
    let hexCode: String
    let rgbCode: RGBTuple
    let uiColour: UIColor
}
