//
//  VColour.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation
import SwiftUI

struct V2Colour: Equatable {
    
    static func == (lhs: V2Colour, rhs: V2Colour) -> Bool {
        lhs.name == rhs.name &&
        lhs.hexCode == rhs.hexCode &&
        lhs.brand == rhs.brand
    }
    
    var brand: String = ""
    
    var name: String = ""
    var hexCode: String = ""
    var rgbCode: RGBTuple = RGBTuple(r: 0, g: 0, b: 0)
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
        self.rgbCode = ColourHelper.hexToRGB(hex: hexCode)
        self.uiColour = UIColor.init(hex: hexCode)
    }
}


struct VColour: Equatable, Hashable {
    
    static func == (lhs: VColour, rhs: VColour) -> Bool {
        lhs.name == rhs.name &&
        lhs.hexCode == rhs.hexCode
    }
    
    var name: String = ""
    var hexCode: String = ""
    var rgbCode: RGBTuple = RGBTuple(r: 0, g: 0, b: 0)
    var uiColour: UIColor = UIColor.yellow
    
    init() {
        
    }
    
    init(name: String, rgbValue: [Int]) {
        self.name = name
        self.rgbCode = RGBTuple(r: rgbValue[0], g: rgbValue[1], b: rgbValue[2])
        self.hexCode = ColourHelper.rgbToHex(self.rgbCode)
        self.uiColour = UIColor.init(hex: self.hexCode)
//        print("\n\n\n\n")
//        print("name: \(name)")
//        print("rgbValue: \(rgbValue)")
//        print("hexCode: \(self.hexCode)")
//        print("\n\n\n")
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
        self.rgbCode = ColourHelper.hexToRGB(hex: hexCode)
        self.uiColour = UIColor.init(hex: hexCode)
    }
}
