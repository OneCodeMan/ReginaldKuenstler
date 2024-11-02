//
//  ColourPair.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation
import SwiftUI

// MARK: ColourPair
struct ColourPair: Hashable {
    static func == (lhs: ColourPair, rhs: ColourPair) -> Bool {
        lhs.name == rhs.name
    }
    
    let name: String // Indigo, Viridian
    let type: String // Vibrant, Muted, etc
    let actualColourInfo: ColourInfo
    let estimatedColourInfo: ColourInfo
}

// MARK: ColourInfo
struct ColourInfo: Hashable {
    
    static func == (lhs: ColourInfo, rhs: ColourInfo) -> Bool {
        lhs.hexCode == rhs.hexCode
    }
    let hexCode: String
    let rgbCode: RGBTuple
    let uiColour: UIColor
}

struct RGBTuple: Hashable {
    static func == (lhs: RGBTuple, rhs: RGBTuple) -> Bool {
        lhs.r == rhs.r &&
        lhs.g == rhs.g &&
        lhs.b == rhs.b
    }
    
    let r: Int
    let g: Int
    let b: Int
    
    init(r: Int, g: Int, b: Int) {
        self.r = r
        self.g = g
        self.b = b
    }
    
    init(_ rgbTuple: (r: Int, g: Int, b: Int)) {
        self.r = rgbTuple.r
        self.g = rgbTuple.g
        self.b = rgbTuple.b
    }
}
