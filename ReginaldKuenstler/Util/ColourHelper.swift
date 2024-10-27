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
    
    // Convert hex to RGB tuple
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
    
    // Convert RGB to hex string
    static func rgbToHex(_ rgb: RGBTuple) -> String {
        return String(format: "#%02X%02X%02X", rgb.r, rgb.g, rgb.b)
    }

    // Calculate Euclidean distance between two RGB values
    static private func colourDistance(rgb1: RGBTuple, rgb2: RGBTuple) -> Double {
        let dr = rgb1.r - rgb2.r
        let dg = rgb1.g - rgb2.g
        let db = rgb1.b - rgb2.b
        return sqrt(Double(dr * dr + dg * dg + db * db))
    }

    // Find the nearest color in the provided color map
    static func findNearestColourInMap(withRgbValue inputRGBTuple: RGBTuple, colourMap: [VColour]) -> VColour {
        guard !colourMap.isEmpty else {
            print("--findNearestColourInMap: COLOUR MAP IS EMPTY. Returning default colour.")
            return VColour(name: "Unknown", hexCode: "#000000", rgbCode: (0, 0, 0), uiColour: UIColor.black)
        }
        
        var nearestColour = VColour()
        var minDistance: Double = Double.greatestFiniteMagnitude
        
        for col in colourMap {
            let distance = colourDistance(rgb1: inputRGBTuple, rgb2: col.rgbCode)
            if distance < minDistance {
                minDistance = distance
                nearestColour = col
            }
        }
        return nearestColour
    }
    
    // MARK: Colour Grouping
    
    static func findBestMixesForColours(targetColours: [VColour], userPalette: [VColour], learningRate: Double = 0.01, maxIterations: Int = 1000) -> [VColour] {
        var bestMixes: [(VColour, [VColour])] = []
        
        for targetColour in targetColours {
            // Attempt mixing two colors
            var bestMix: VColour?
            var bestMixDifference = Double.infinity
            var bestMixColors: [VColour] = []
            
            // Try mixing two palette colors
            for i in 0..<userPalette.count {
                for j in i+1..<userPalette.count {
                    let mix = ColourHelper.mixThreeColors(userPalette[i], userPalette[j], userPalette[0], weights: (0.5, 0.5, 0.0)) // Last color as dummy to focus on two
                    let difference = ColourHelper.deltaE(targetColour, mix)
                    
                    if difference < bestMixDifference {
                        bestMixDifference = difference
                        bestMix = mix
                        bestMixColors = [userPalette[i], userPalette[j]]
                    }
                }
            }
            
            // Try mixing three palette colors
            for i in 0..<userPalette.count {
                for j in i+1..<userPalette.count {
                    for k in j+1..<userPalette.count {
                        let mix = ColourHelper.mixThreeColors(userPalette[i], userPalette[j], userPalette[k], weights: (0.33, 0.33, 0.34))
                        let difference = ColourHelper.deltaE(targetColour, mix)
                        
                        if difference < bestMixDifference {
                            bestMixDifference = difference
                            bestMix = mix
                            bestMixColors = [userPalette[i], userPalette[j], userPalette[k]]
                        }
                    }
                }
            }
            
            if let bestMix = bestMix {
                bestMixes.append((bestMix, bestMixColors))
            }
        }
        
        let nearestColourMixes = bestMixes.map { $0.0 }
        
        return nearestColourMixes
    }


    
    static func groupColours(colours: [PaletteColour]) -> [String: [PaletteColour]] {
        var colourGroups: [String: [PaletteColour]] = ["Red": [], "Green": [], "Blue": [], "Yellow": [], "Brown": [], "Black": [], "White": [], "Gray": [], "Other": []]
        
        for colour in colours {
            let group = self.groupIndividualColour(hexColour: colour.hexCode, colourName: colour.colourName)
            colourGroups[group]?.append(colour)
        }
        // Create a new ordered dictionary with RGB categories first
        var orderedGroups: [String: [PaletteColour]] = [:]
        
        // Add primary categories first
        let primaryCategories = ["Red", "Green", "Blue"]
        for category in primaryCategories {
            if let colors = colourGroups[category], !colors.isEmpty {
                orderedGroups[category] = colors
            }
        }
        
        // Then add any remaining categories in alphabetical order
        let otherCategories = colourGroups.keys.filter { !primaryCategories.contains($0) }.sorted()
        for category in otherCategories {
            if let colors = colourGroups[category], !colors.isEmpty {
                orderedGroups[category] = colors
            }
        }
        return orderedGroups
    }
    
    static func groupColourSelectItems(colours: [PaletteColourSelectItem]) -> [String: [PaletteColourSelectItem]] {
        var colourGroups: [String: [PaletteColourSelectItem]] = ["Red": [], "Green": [], "Blue": [], "Yellow": [], "Black": [], "White": [], "Gray": [], "Other": []]
        
        for colourSelectItem in colours {
            let group = self.groupIndividualColour(hexColour: colourSelectItem.paletteColour.hexCode, colourName: colourSelectItem.paletteColour.colourName)
            colourGroups[group]?.append(colourSelectItem)
        }
        return colourGroups
    }
    
    // Group individual colour into predefined categories
    static func groupIndividualColour(hexColour: String, colourName: String) -> String {
        let rgb = self.hexToRGB(hex: hexColour)
        let (r, g, b) = (rgb.r, rgb.g, rgb.b)

        if (r > 200 && g < 100 && b < 100) || colourName.contains("Red") {
            return "Red"
        } else if (g > 200 && r < 100 && b < 100) || colourName.contains("Green") {
            return "Green"
        } else if (b > 200 && r < 100 && g < 100) || colourName.contains("Blue") {
            return "Blue"
        } else if (r > 200 && g > 200 && b < 100) || colourName.contains("Yellow") {
            return "Yellow"
        } else if (r > 200 && g > 100 && b < 100) || colourName.contains("Orange") {
            return "Orange"
        } else if (r > 200 && g < 100 && b > 200) || colourName.contains("Pink") {
            return "Pink"
        } else if (r < 100 && g < 100 && b > 200) || colourName.contains("Violet") {
            return "Violet"
        } else if (r < 50 && g < 50 && b < 50) || colourName.contains("Black") {
            return "Black"
        } else if (r > 200 && g > 200 && b > 200) || colourName.contains("White") {
            return "White"
        } else if abs(r - g) < 20 && abs(r - b) < 20 || colourName.contains("Gray") {
            return "Gray"
        } else if (r > 100 && g < 100 && b < 100 && r < 200) || colourName.contains("Brown") {
            return "Brown"
        } else {
            return "Other"
        }
    }
    
    // MARK: Colour Mixing
    
    static func deltaE(_ color1: VColour, _ color2: VColour) -> Double {
        let lab1 = convertToLAB(color1)
        let lab2 = convertToLAB(color2)
        
        let deltaL = lab1.L - lab2.L
        let deltaA = lab1.A - lab2.A
        let deltaB = lab1.B - lab2.B
        
        return sqrt(deltaL * deltaL + deltaA * deltaA + deltaB * deltaB)
    }

    static func mixThreeColors(_ color1: VColour, _ color2: VColour, _ color3: VColour, weights: (Double, Double, Double)) -> VColour {
        let totalWeight = weights.0 + weights.1 + weights.2
        let normalizedWeights = (
            weights.0 / totalWeight,
            weights.1 / totalWeight,
            weights.2 / totalWeight
        )
        
        let mixedRGB = (
            r: Int(Double(color1.rgbCode.r) * normalizedWeights.0 + Double(color2.rgbCode.r) * normalizedWeights.1 + Double(color3.rgbCode.r) * normalizedWeights.2),
            g: Int(Double(color1.rgbCode.g) * normalizedWeights.0 + Double(color2.rgbCode.g) * normalizedWeights.1 + Double(color3.rgbCode.g) * normalizedWeights.2),
            b: Int(Double(color1.rgbCode.b) * normalizedWeights.0 + Double(color2.rgbCode.b) * normalizedWeights.1 + Double(color3.rgbCode.b) * normalizedWeights.2)
        )
        
        var colourMixName = weights.2 > 0 ? "\(color1.name)\(color2.name)\(color3.name)" : "\(color1.name)\(color2.name)"
        
        return VColour(
            name: colourMixName,
            hexCode: ColourHelper.rgbToHex(mixedRGB),
            rgbCode: mixedRGB,
            uiColour: UIColor(
                red: CGFloat(mixedRGB.r) / 255.0,
                green: CGFloat(mixedRGB.g) / 255.0,
                blue: CGFloat(mixedRGB.b) / 255.0,
                alpha: 1.0
            )
        )
    }

    // Gradient descent to mix colors to match a target color
    static func gradientDescentMixing(targetColor: VColour, paletteColors: [VColour], learningRate: Double = 0.01, maxIterations: Int = 1000) -> (VColour, [Double]) {
        let numColors = paletteColors.count
        var weights = [Double](repeating: 1.0 / Double(numColors), count: numColors)
        
        func mixColorsWithWeights(weights: [Double]) -> VColour {
            var mixedR = 0.0
            var mixedG = 0.0
            var mixedB = 0.0
            
            for (i, color) in paletteColors.enumerated() {
                mixedR += Double(color.rgbCode.r) * weights[i]
                mixedG += Double(color.rgbCode.g) * weights[i]
                mixedB += Double(color.rgbCode.b) * weights[i]
            }
            
            let mixedRGB = (r: Int(mixedR), g: Int(mixedG), b: Int(mixedB))
            
            return VColour(
                name: "MixedColor",
                hexCode: ColourHelper.rgbToHex(mixedRGB),
                rgbCode: mixedRGB,
                uiColour: UIColor(
                    red: CGFloat(mixedR) / 255.0,
                    green: CGFloat(mixedG) / 255.0,
                    blue: CGFloat(mixedB) / 255.0,
                    alpha: 1.0
                )
            )
        }
        
        for _ in 0..<maxIterations {
            let currentMix = mixColorsWithWeights(weights: weights)
            let currentDelta = deltaE(currentMix, targetColor)
            
            var gradients = [Double](repeating: 0.0, count: numColors)
            
            for i in 0..<numColors {
                weights[i] += learningRate
                let updatedMix = mixColorsWithWeights(weights: weights)
                let updatedDelta = deltaE(updatedMix, targetColor)
                
                gradients[i] = updatedDelta - currentDelta
                weights[i] -= learningRate // Restore original weight
            }
            
            for i in 0..<numColors {
                weights[i] -= learningRate * gradients[i]
            }
        }
        
        let finalMix = mixColorsWithWeights(weights: weights)
        return (finalMix, weights)
    }
    
    // Convert VColour to LAB color space
    private static func convertToLAB(_ color: VColour) -> LABTuple {
        let rgb = color.rgbCode
        let (r, g, b) = (Double(rgb.r) / 255.0, Double(rgb.g) / 255.0, Double(rgb.b) / 255.0)
        
        // Conversion to XYZ space
        func f(_ t: Double) -> Double {
            return t > 0.04045 ? pow((t + 0.055) / 1.055, 2.4) : t / 12.92
        }
        let x = 0.4124564 * f(r) + 0.3575761 * f(g) + 0.1804375 * f(b)
        let y = 0.2126729 * f(r) + 0.7151522 * f(g) + 0.0721750 * f(b)
        let z = 0.0193339 * f(r) + 0.1191920 * f(g) + 0.9503041 * f(b)
        
        // Convert XYZ to LAB
        func labF(_ t: Double) -> Double {
            return t > 0.008856 ? pow(t, 1/3.0) : (903.3 * t + 16) / 116
        }
        
        let refX: Double = 0.95047
        let refY: Double = 1.00000
        let refZ: Double = 1.08883
        
        let L = 116 * labF(y / refY) - 16
        let A = 500 * (labF(x / refX) - labF(y / refY))
        let B = 200 * (labF(y / refY) - labF(z / refZ))
        
        return LABTuple(L: L, A: A, B: B)
    }
}

typealias LABTuple = (L: Double, A: Double, B: Double)

// MARK: Extension Color

extension Color {
    
    // MARK: Custom colours
    public static var blueSelectedState: Color {
        // 50, 125, 168
        return Color(UIColor(red: 50/255, green: 125/255, blue: 168/255, alpha: 0.3))
    }
    
    public static var whiteTextLightMode1: Color {
        return Color(UIColor(red: 232/255, green: 231/255, blue: 227/255, alpha: 1.0))
    }
    
    public static var goldInnerFrameImage: Color {
        return Color(UIColor(red: 218/255, green: 165/255, blue: 32/255, alpha: 1.0))
    }
    
    public static var brownOuterFrameImage: Color {
        return Color(UIColor(red: 111/255, green: 78/255, blue: 55/255, alpha: 1.0))
    }
}
