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
    
    
    func performAnalOnImage(artwork: Artwork, completion: @escaping ([UIColor]) -> Void) {
        var infoString = ""
        var uiColours: [UIColor] = []
        print("performing anal on \(artwork.title)")
        Vibrant.from(artwork.image).getPalette() { palette in
            let p = palette
            let vibrant: String = p.Vibrant?.hex ?? ""
            let darkVibrant: String = p.DarkVibrant?.hex ?? ""
            let lightVibrant: String = p.LightVibrant?.hex ?? ""
            let mutedVibrant: String = p.Muted?.hex ?? ""
            let lightMuted: String = p.LightMuted?.hex ?? ""
            let darkMuted: String = p.DarkMuted?.hex ?? ""
            print("vibrant: \(vibrant);\n darkvibrant: \(darkVibrant);\n lightVibrant: \(lightVibrant); mutedVibrant: \(mutedVibrant); lightMuted: \(lightMuted); darkMuted: \(darkMuted)")
            
            // take input
            let inputs = [vibrant, darkVibrant, lightVibrant, mutedVibrant, lightMuted, darkMuted]
            var outputs: [VColour] = []
            
            let mapper = ColourMapper()
            let colourMap = mapper.createColourMapFromCSV()
            print("\n\n\n\n")
            
            // for every colour input
            for inputColour in inputs {
                // convert to rgb
                let rgbInputTuple = ColourConverter.hexToRGB(hex: inputColour)
                
                // calculate nearest distance, output
                let nearestColour = ColourConverter.findNearestColorFromRGBValue(rgbTuple: rgbInputTuple, colourMap: colourMap)
                outputs.append(nearestColour)
            }
            
            let inputOutputZip = zip(inputs, outputs)
            
            print("Analysis of \(artwork.title)")
            
            for (inputColour, outputColour) in inputOutputZip {
                let outputCode = outputColour.rgbCode
                let currentColour = UIColor(red: CGFloat(outputCode.r) / 255.0, green: CGFloat(outputCode.g) / 255.0, blue: CGFloat(outputCode.b) / 255.0, alpha: 1.0)
                uiColours.append(currentColour)
                
                let yap = "Vibrant took the input as \(inputColour), which corresponds to \(outputColour.name) (hex code: \(outputColour.hexCode))\nThe UIColor for \(outputColour.name) is: \(currentColour)\n\n"
                infoString += yap
                print(yap)
            }
            print("printing uiColours within callback: \(uiColours)")
            completion(uiColours)
        }
    }
}
