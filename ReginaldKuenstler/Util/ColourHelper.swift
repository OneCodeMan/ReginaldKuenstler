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
        var colourGroups: [String: [PaletteColour]] = ["Red": [], "Green": [], "Blue": [], "Yellow": [], "Brown": [], "Black": [], "White": [], "Gray": [], "Other": []]
        
        for colour in colours {
            let group = self.groupIndividualColour(hexColour: colour.hexCode, colourName: colour.colourName)
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
            let group = self.groupIndividualColour(hexColour: colourSelectItem.paletteColour.hexCode, colourName: colourSelectItem.paletteColour.colourName)
            colourGroups[group]?.append(colourSelectItem)
        }
        
        return colourGroups
    }
    
    // TODO: take rgb instead
    static func groupIndividualColour(hexColour: String, colourName: String) -> String {
        let rgb = self.hexToRGB(hex: hexColour)
        let (r, g, b) = (rgb.r, rgb.g, rgb.b)

        // Red
        if (r > 200 && g < 100 && b < 100) || (colourName.contains("Red")) {
            return "Red"
        }
        // Green
        else if (g > 200 && r < 100 && b < 100) || (colourName.contains("Green")) {
            return "Green"
        }
        // Blue
        else if (b > 200 && r < 100 && g < 100) || (colourName.contains("Blue")) {
            return "Blue"
        }
        // Yellow
        else if (r > 200 && g > 200 && b < 100) || (colourName.contains("Yellow")) {
            return "Yellow"
        }
        // Orange
        else if (r > 200 && g > 100 && b < 100) || (colourName.contains("Orange")) {
            return "Orange"
        }
        // Pink
        else if (r > 200 && g < 100 && b > 200) || (colourName.contains("Pink")) {
            return "Pink"
        }
        // Violet
        else if (r < 100 && g < 100 && b > 200) || (colourName.contains("Violet")) {
            return "Violet"
        }
        // Black
        else if (r < 50 && g < 50 && b < 50) || (colourName.contains("Black")) {
            return "Black"
        }
        // White
        else if (r > 200 && g > 200 && b > 200) || (colourName.contains("White")) {
            return "White"
        }
        // Gray
        else if (abs(r - g) < 20 && abs(r - b) < 20) || (colourName.contains("Gray")) {
            return "Gray"
        }
        // Purple
        else if (r < 100 && g < 100 && b > 200) || (colourName.contains("Purple")) {
            return "Purple"
        }
        // Brown
        else if (r > 100 && g < 100 && b < 100 && r < 200) || (g < 80 && r > 100 && b < 80) || (colourName.contains("Brown")) {
            return "Brown"
        }
        // Other
        else {
            return "Other"
        }
    }


    
}
