//
//  VColour.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation
import SwiftUI

struct VColour: Equatable {
    
    static func == (lhs: VColour, rhs: VColour) -> Bool {
        lhs.name == rhs.name &&
        lhs.hexCode == rhs.hexCode
    }
    
    var name: String = ""
    var hexCode: String = ""
    var rgbCode: RGBTuple = (r: 0, g: 0, b: 0)
    var uiColour: UIColor = UIColor.yellow
    
    init() {
        
    }
    
    init(name: String, hexCode: String, rgbCode: RGBTuple, uiColour: UIColor) {
        self.name = name
        self.hexCode = hexCode
        self.rgbCode = rgbCode
        self.uiColour = uiColour
    }
    
    init(name: String, hexCode: String) {
        self.name = name
        self.hexCode = hexCode
        self.rgbCode = ColourConverter.hexToRGB(hex: hexCode)
        self.uiColour = UIColor.init(hex: hexCode)
    }
}
