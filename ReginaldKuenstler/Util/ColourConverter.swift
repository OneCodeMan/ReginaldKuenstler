//
//  ColourConverter.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-16.
//

import Foundation
import SwiftUI

final class ColourConverter {
    
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
    
}
