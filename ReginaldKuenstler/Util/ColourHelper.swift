//
//  ColourConverter.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-16.
//

import Foundation
import SwiftUI

final class ColourHelper {
    
    // MARK: Colour Distance/Estimation
    
    // https://medium.com/@muzammalshahzad494/converting-hexadecimal-color-code-to-rgb-values-in-swift-3600d46bcbc9
    /*
     usage:
     if let rgb = hexToRGB(hex: "#FF0000") {
     print("Red: \(rgb.red), Green: \(rgb.green), Blue: \(rgb.blue)")
     } else {
     print("Invalid hexadecimal color code.")
     }
     */
    static func hexToRGB(hex: String) -> RGBTuple {
        var hexSanitized = hex.trimmingCharacters(in: .whitespacesAndNewlines)
        if hexSanitized.hasPrefix("#") {
            hexSanitized.removeFirst()
        }
        
        var rgb: UInt64 = 0
        Scanner(string: hexSanitized).scanHexInt64(&rgb)
        
        return RGBTuple(
            r: Int((rgb >> 16) & 0xFF),
            g: Int((rgb >> 8) & 0xFF),
            b: Int(rgb & 0xFF)
        )
    }
    
    static private func colourDistance(rgb1: (r: Int, g: Int, b: Int), rgb2: (r: Int, g: Int, b: Int)) -> Double {
        // print("--ColourConverter Calculating distance between \(rgb1) and \(rgb2)")
        let dr = rgb1.r - rgb2.r
        let dg = rgb1.g - rgb2.g
        let db = rgb1.b - rgb2.b
        return sqrt(Double(dr * dr + dg * dg + db * db))
    }
    
    static func findNearestColourInMap(withRgbValue inputRGBTuple: RGBTuple, colourMap: [VColour]) -> VColour {
        guard !colourMap.isEmpty else {
            print("--findNearestColourInMap: COLOUR MAP IS EMPTY. Returning default colour.")
            return VColour(name: "Unknown", hexCode: "#000000", rgbCode: (0, 0, 0), uiColour: UIColor.black)
        }
        var nearestColour: VColour = VColour()
        var minDistance: Double = Double.greatestFiniteMagnitude
        
        for col in colourMap {
            let currentColourRGBCode = col.rgbCode
            
            let distance = colourDistance(rgb1: inputRGBTuple, rgb2: currentColourRGBCode)
            if distance < minDistance {
                minDistance = distance
                nearestColour = col
            }
            
        }
       // print("--ColourConverter nearestColourInMap for rgb\(inputRGBTuple) is: \(nearestColour.name) \(nearestColour.rgbCode)\n")
        return nearestColour
    }
    
    // MARK: Colour Grouping
    
    // Group colors based on dominant color component
    // This is how we'd sort the colours
    static func groupColours(colours: [PaletteColour]) -> [String: [PaletteColour]] {
        var colourGroups: [String: [PaletteColour]] = ["Red": [], "Green": [], "Blue": [], "Yellow": [], "Black": [], "White": [], "Gray": [], "Other": []]
        
        for colour in colours {
            let group = self.groupIndividualColour(hexColour: colour.hexCode)
            colourGroups[group]?.append(colour)
        }
        
//        print("[--ColourHelper, colourGroups:")
//        print(colourGroups)
        
        return colourGroups
    }
    
    // Group colors based on dominant color component
    // This is how we'd sort the colours
    static func groupColourSelectItems(colours: [PaletteColourSelectItem]) -> [String: [PaletteColourSelectItem]] {
        var colourGroups: [String: [PaletteColourSelectItem]] = ["Red": [], "Green": [], "Blue": [], "Yellow": [], "Black": [], "White": [], "Gray": [], "Other": []]
        
        for colourSelectItem in colours {
            let group = self.groupIndividualColour(hexColour: colourSelectItem.paletteColour.hexCode)
            colourGroups[group]?.append(colourSelectItem)
        }
        
        return colourGroups
    }
    
    // TODO: take an RGB instead, pass in colour's rgb not hex.
    static func groupIndividualColour(hexColour: String) -> String {
        let rgb = self.hexToRGB(hex: hexColour)
        let (r, g, b) = (rgb.r, rgb.g, rgb.b)
        
        if r > 200 && g < 100 && b < 100 {
            return "Red"
        } else if g > 200 && r < 100 && b < 100 {
            return "Green"
        } else if b > 200 && r < 100 && g < 100 {
            return "Blue"
        } else if r > 200 && g > 200 && b < 100 {
            return "Yellow"
        } else if r < 50 && g < 50 && b < 50 {
            return "Black"
        } else if r > 200 && g > 200 && b > 200 {
            return "White"
        } else if abs(r - g) < 20 && abs(r - b) < 20 {
            return "Gray"
        } else {
            return "Other"
        }
    }
    
}
