//
//  KuenstlerViewModel.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-16.
//

import Foundation
import SwiftUI
import SwiftVibrantium

/**
 ViewModel responsible for taking image as input and producing a swatch as output
 */
class KuenstlerViewModel: ObservableObject {
    
    @State var colourMap: [VColour] = []
    
    init() {
        self.generateColourMapping()
    }
    
    func generateColourMapping(completion: (([VColour]) -> Void)? = nil) {
        // Check if the colourMap is already populated
        if !self.colourMap.isEmpty {
            completion?([])  // No need to regenerate
            return
        }
        
        let mapper = ColourMapper()
        
        DispatchQueue.main.async {
            mapper.createColourMapFromCSV { colourMap in
                self.colourMap = colourMap
                print("[--KuenstlerViewModel generateColourMapping() colourMap \(colourMap.count) items")
                
                // Call completion once the colour map is set
                completion?(self.colourMap)
            }
        }
        
    }
    
    func performAnalOnImage(artwork: Artwork, completion: @escaping (_ result: ([ColourPair])) -> Void) {
        
        var colourPairs: [ColourPair] = []
        print("Performing analysis on \(artwork.title)")
        DispatchQueue.main.async {
            Vibrant.from(artwork.image).getPalette() { palette in
                let p = palette
                let vibrant: Swatch? = p.Vibrant
                let darkVibrant: Swatch? = p.DarkVibrant
                let lightVibrant: Swatch? = p.LightVibrant
                let mutedVibrant: Swatch? = p.Muted
                let lightMuted: Swatch? = p.LightMuted
                let darkMuted: Swatch? = p.DarkMuted
                
                // Take input
                let inputs: [(String, Swatch?)] = [
                    ("Vibrant", vibrant),
                    ("Dark Vibrant", darkVibrant),
                    ("Light Vibrant", lightVibrant),
                    ("Muted Vibrant", mutedVibrant),
                    ("Light Muted", lightMuted),
                    ("Dark Muted", darkMuted)
                ]
                
                // Loop through each input
                for (colourType, swatchInput) in inputs {
                    if let swatchInput = swatchInput {
                        // Make an ActualColourInfo
                        let actualHex: String = swatchInput.hex
                        let actualUIColour: UIColor = swatchInput.uiColor
                        let actualRGBCode: RGBTuple = ColourConverter.hexToRGB(hex: actualHex)
                        
                        // ColourPair component 1
                        let actualColourInfo = ColourInfo(hexCode: actualHex, rgbCode: actualRGBCode, uiColour: actualUIColour)
                        
                        // Find nearest colour in the map
                        print("passing colourMap of \(self.colourMap.count) items to converter..")
                        let currentVColour: VColour = ColourConverter.findNearestColourInMap(withRgbValue: actualRGBCode, colourMap: self.colourMap)
                        let estimatedHexCode: String = currentVColour.hexCode
                        let estimatedUIColour: UIColor = currentVColour.uiColour
                        let estimatedRGBTuple: RGBTuple = currentVColour.rgbCode
                        
                        // ColourPair component 2
                        let estimatedColourInfo = ColourInfo(hexCode: estimatedHexCode, rgbCode: estimatedRGBTuple, uiColour: estimatedUIColour)
                        
                        // Create a ColourPair
                        let colourPair = ColourPair(name: currentVColour.name, type: colourType, actualColourInfo: actualColourInfo, estimatedColourInfo: estimatedColourInfo)
                        
                        // Add ColourPair to array
                        colourPairs.append(colourPair)
                    }
                }
                print("--KuenstlerViewModel analysis has been performed, colourPairs has \(colourPairs.count) elements. Completion will be called.")
                completion(colourPairs)
            }
        }
    }
}
