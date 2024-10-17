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
class KuenstlerViewModel {
    
    @State var colourMap: [VColour] = []

    
    init() {
        self.generateColourMapping()
    }
    
    func generateColourMapping() {
        let mapper = ColourMapper()
        let colourMap = mapper.createColourMapFromCSV()
        self.colourMap = colourMap
        print("[--KuenstlerViewModel generateColourMapping() colourMap \(colourMap.count) items")
    }
    
    
    func performAnalOnImage(artwork: Artwork, completion: @escaping (_ result: ([ColourPair])) -> Void) {
        
        var colourPairs: [ColourPair] = []
        print("performing anal on \(artwork.title)")
        
        Vibrant.from(artwork.image).getPalette() { palette in
            let p = palette
            let vibrant: Swatch? = p.Vibrant
            let darkVibrant: Swatch? = p.DarkVibrant
            let lightVibrant: Swatch? = p.LightVibrant
            let mutedVibrant: Swatch? = p.Muted
            let lightMuted: Swatch? = p.LightMuted
            let darkMuted: Swatch? = p.DarkMuted
            
            // print("vibrant: \(vibrant);\n darkvibrant: \(darkVibrant);\n lightVibrant: \(lightVibrant); mutedVibrant: \(mutedVibrant); lightMuted: \(lightMuted); darkMuted: \(darkMuted)")
            
            // take input
            let inputs: [(String, Swatch?)] = [("Vibrant", vibrant), ("Dark Vibrant", darkVibrant), ("Light Vibrant", lightVibrant), ("Muted Vibrant", mutedVibrant), ("Light Muted", lightMuted), ("Dark Muted", darkMuted)]
            
            // loop through each input
            // for each input
            for (colourType, swatchInput) in inputs {
                if let swatchInput = swatchInput {
                    // make an ActualColourInfo
                    let actualHex: String = swatchInput.hex
                    let actualUIColour: UIColor = swatchInput.uiColor
                    let actualRGBCode: RGBTuple = ColourConverter.hexToRGB(hex: actualHex)

                    // ColourPair component 1
                    let actualColourInfo = ColourInfo(hexCode: actualHex, rgbCode: actualRGBCode, uiColour: actualUIColour)
                    
                    // convert info from there to get a mapping
                    // store mapping info to EstimatedColourInfo
                    let currentVColour: VColour = ColourConverter.findNearestColourInMap(withRgbValue: actualRGBCode, colourMap: self.colourMap)
                    let estimatedHexCode: String = currentVColour.hexCode
                    let estimatedUIColour: UIColor = currentVColour.uiColour
                    let estimatedRGBTuple: RGBTuple = currentVColour.rgbCode
                    
                    // ColourPair component 2
                    let estimatedColourInfo = ColourInfo(hexCode: estimatedHexCode, rgbCode: estimatedRGBTuple, uiColour: estimatedUIColour)
                    
                    // create a ColourPair
                    let colourPair = ColourPair(name: currentVColour.name, type: colourType, actualColourInfo: actualColourInfo, estimatedColourInfo: estimatedColourInfo)
                    
                    // add ColourPair to array
                    colourPairs.append(colourPair)
                }
            }
            print("--KuenstlerViewModel anal has been performed, colourPairs has \(colourPairs.count) elements. Completion will be called.")
            completion(colourPairs)
        }
    }
}
