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
    
    @Published var relevantColoursFromUserPalette: [VColour] = []
    
    private var estimatedColours: [VColour] = []
    private var coloursFromUserPalette: [VColour] = []
    private var approximateUserMixes: [VColour] = []
    
    @Published var isLoading: Bool = false
    
    // private var userPaletteViewModel: UserPaletteViewModel
    
    init() {
        self.getColoursFromUserPalette()
    }
    
    @MainActor
    func performAnalOnImage(artwork: Artwork, completion: @escaping (_ result: [ColourPair], [VColour]) -> Void) async throws {
        let colourMap = ColourMapper.shared.colourMap
        print("colourMap status from KuenstlerViewModel.performAnal --- \(colourMap.count) items")
        self.isLoading = true
        var colourPairs: [ColourPair] = []
        self.relevantColoursFromUserPalette = []
        self.estimatedColours = []
        // print("Performing analysis on \(artwork.title)")
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
                        let actualRGBCode: RGBTuple = ColourHelper.hexToRGB(hex: actualHex)
                        
                        // ColourPair component 1
                        let actualColourInfo = ColourInfo(hexCode: actualHex, rgbCode: actualRGBCode, uiColour: actualUIColour)
                        
                        // Find nearest colour in the map
                        // print("passing colourMap of \(self.colourMap.count) items to converter..")
                        print("colourMap status, KuenstlerViewModel.performAnal, before we need it. --- \(ColourMapper.shared.colourMap.count) items")
                        let currentVColour: VColour = ColourHelper.findNearestColourInMap(withRgbValue: actualRGBCode, colourMap: colourMap)
                        let estimatedHexCode: String = currentVColour.hexCode
                        let estimatedUIColour: UIColor = currentVColour.uiColour
                        let estimatedRGBTuple: RGBTuple = currentVColour.rgbCode
                        
                        self.estimatedColours.append(currentVColour)
                        
                        // ColourPair component 2
                        let estimatedColourInfo = ColourInfo(hexCode: estimatedHexCode, rgbCode: estimatedRGBTuple, uiColour: estimatedUIColour)
                        
                        // Create a ColourPair
                        let colourPair = ColourPair(name: currentVColour.name, type: colourType, actualColourInfo: actualColourInfo, estimatedColourInfo: estimatedColourInfo)
                        
                        // Add ColourPair to array
                        colourPairs.append(colourPair)
                    }
                }
                // print("--KünstlerViewModel analysis has been performed, colourPairs has \(colourPairs.count) elements")
                // print(self.coloursFromUserPalette)
                // print(self.estimatedColours)
                let paletteIntersectionUserAndEstimate = self.determinePaletteIntersection(paletteOne: self.coloursFromUserPalette, paletteTwo: self.estimatedColours)
                
                let approximateColours: [VColour] = [] // ColourHelper.findBestMixesForColours(targetColours: self.estimatedColours, userPalette: self.coloursFromUserPalette)
                
                self.approximateUserMixes = approximateColours
                self.relevantColoursFromUserPalette = paletteIntersectionUserAndEstimate + approximateColours
                
//                print("--KünstlerViewModel, relevantColoursFromUserPalette: \(self.relevantColoursFromUserPalette.count) elements")
//                print("\n\(self.relevantColoursFromUserPalette.count) elements.\n\n")
                
                self.isLoading = false
                completion(colourPairs, self.relevantColoursFromUserPalette)
            }
        }
    }
    
    // MARK: User Palette
    private func getColoursFromUserPalette() {
        if UserDefaultsHelper.isKeyPresentInUserDefaults(key: UserPaletteConstants.userPalettesKey) {
            if let userPaletteFromUserDefaults = UserDefaults.standard.dictionary(forKey: UserPaletteConstants.userPalettesKey) as? [String: String]  {
                // convert UserPalette to list of VColours
                for (name, hexCode) in userPaletteFromUserDefaults {
                    let generatedVColour = VColour(name: name, hexCode: hexCode)
                    self.coloursFromUserPalette.append(generatedVColour)
                }
                
            }
        }
    }
    
    // takes two palettes and tells you where they overlap.
    // VColour for now, use Palette for later.
    private func determinePaletteIntersection(paletteOne: [VColour], paletteTwo: [VColour]) -> [VColour] {
        let interesectedPalette = paletteOne.filter { paletteTwo.contains($0) }
        return interesectedPalette
    }
    
    // TODO: DO THIS
    //    private func determineBestMixFromUserPalette() {
    //        let (bestMix, bestDeltaE) = ColourHelper.determineBestMixFromUserPalette(userPalette: self.coloursFromUserPalette, missingColor: missingColor)
    //    }
}
